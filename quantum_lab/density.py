"""Density-matrix representation for mixed states (needed for noise).

A register of ``n`` qubits is a ``2^n x 2^n`` complex matrix, i.e.
``16 * 4**n`` bytes — quadratically more than a state vector, hence the much
lower ``MAX_DENSITY_QUBITS``.  Indices are big-endian like everywhere else.
"""

from __future__ import annotations

from collections.abc import Sequence

import numpy as np

from . import gates
from .simulator import _validate_num_qubits, apply_matrix

#: 4**10 complex128 entries = 16 MiB.
MAX_DENSITY_QUBITS = 10


def is_cptp(kraus_ops: Sequence[np.ndarray], atol: float = gates.ATOL) -> bool:
    """True if ``sum_k K_k^dagger K_k = I`` (trace-preserving Kraus set)."""
    ops = [np.asarray(k, dtype=complex) for k in kraus_ops]
    if not ops or any(k.ndim != 2 or k.shape != ops[0].shape for k in ops):
        return False
    total = sum(k.conj().T @ k for k in ops)
    return bool(np.allclose(total, np.eye(ops[0].shape[1]), atol=atol, rtol=0))


def _psd_sqrt(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * np.sqrt(np.clip(values, 0.0, None))) @ vectors.conj().T


class DensityMatrix:
    """Mixed state ``rho`` of ``num_qubits`` qubits, initially ``|0..0><0..0|``."""

    def __init__(self, num_qubits: int):
        self.num_qubits = _validate_num_qubits(num_qubits, MAX_DENSITY_QUBITS)
        self.dim = 2**self.num_qubits
        self._rho = np.zeros((self.dim, self.dim), dtype=complex)
        self._rho[0, 0] = 1.0

    @classmethod
    def from_statevector(cls, state: np.ndarray) -> DensityMatrix:
        vec = np.asarray(state, dtype=complex).reshape(-1)
        n = int(vec.shape[0]).bit_length() - 1
        out = cls(n)
        if vec.shape[0] != out.dim:
            raise ValueError("state length is not a power of two")
        if abs(np.linalg.norm(vec) - 1.0) > 1e-8:
            raise ValueError("state must be normalised")
        out._rho = np.outer(vec, vec.conj())
        return out

    @classmethod
    def from_matrix(cls, rho: np.ndarray, num_qubits: int) -> DensityMatrix:
        """Wrap an existing matrix (used for ensemble sums); shape-checked only."""
        out = cls(num_qubits)
        rho = np.array(rho, dtype=complex)
        if rho.shape != (out.dim, out.dim):
            raise ValueError(f"expected a {out.dim}x{out.dim} matrix")
        out._rho = rho
        return out

    @property
    def matrix(self) -> np.ndarray:
        """Copy of ``rho``."""
        return self._rho.copy()

    def copy(self) -> DensityMatrix:
        return DensityMatrix.from_matrix(self._rho, self.num_qubits)

    # ------------------------------------------------------------ evolution
    def _tensor(self) -> np.ndarray:
        return self._rho.reshape((2,) * (2 * self.num_qubits))

    def _sandwich(self, tensor: np.ndarray, op: np.ndarray, qubits) -> np.ndarray:
        """``op . rho . op^dagger`` on the listed qubits (no validation)."""
        n = self.num_qubits
        out = apply_matrix(tensor, op, list(qubits))
        return apply_matrix(out, op.conj(), [n + q for q in qubits])

    def apply(self, matrix: np.ndarray, qubits: Sequence[int] | int) -> None:
        """Unitary evolution ``rho -> U rho U^dagger`` on the listed qubits."""
        if isinstance(qubits, (int, np.integer)):
            qubits = [qubits]
        qubits = gates.validate_qubits(qubits, self.num_qubits)
        m = np.asarray(matrix, dtype=complex)
        size = 2 ** len(qubits)
        if not qubits or m.shape != (size, size):
            raise ValueError(f"a {len(qubits)}-qubit gate needs a {size}x{size} matrix")
        if not gates.is_unitary(m):
            raise ValueError("gate matrix is not unitary (U^dagger U != I)")
        self._rho = self._sandwich(self._tensor(), m, qubits).reshape(self.dim, self.dim)

    def apply_controlled(self, matrix: np.ndarray, controls: Sequence[int], target: int) -> None:
        """Single-qubit unitary on ``target`` controlled by ``controls``."""
        controls = tuple(controls)
        m = np.asarray(matrix, dtype=complex)
        if m.shape != (2, 2):
            raise ValueError(f"expected a 2x2 gate, got shape {m.shape}")
        self.apply(gates.controlled_matrix(m, len(controls)), [*controls, target])

    def apply_channel(self, kraus_ops: Sequence[np.ndarray], qubit: int) -> None:
        """Single-qubit quantum channel ``rho -> sum_k K_k rho K_k^dagger``."""
        (qubit,) = gates.validate_qubits([qubit], self.num_qubits)
        ops = [np.asarray(k, dtype=complex) for k in kraus_ops]
        if any(k.shape != (2, 2) for k in ops) or not is_cptp(ops):
            raise ValueError("Kraus operators must be 2x2 and satisfy sum K^dagger K = I")
        tensor = self._tensor()
        total = sum(self._sandwich(tensor, k, [qubit]) for k in ops)
        self._rho = total.reshape(self.dim, self.dim)

    def project(self, qubit: int, outcome: int) -> float:
        """Unnormalised projection ``P rho P``; returns its trace (the probability).

        The matrix is deliberately left unnormalised so that branches of an
        ensemble can be summed with the correct weights.
        """
        (qubit,) = gates.validate_qubits([qubit], self.num_qubits)
        if outcome not in (0, 1):
            raise ValueError("measurement outcome must be 0 or 1")
        projector = np.diag([1.0 - outcome, float(outcome)]).astype(complex)
        self._rho = self._sandwich(self._tensor(), projector, [qubit]).reshape(
            self.dim, self.dim
        )
        return self.trace()

    # ------------------------------------------------------------- analysis
    def trace(self) -> float:
        return float(np.trace(self._rho).real)

    def probabilities(self) -> np.ndarray:
        """Diagonal of ``rho``: computational-basis measurement probabilities."""
        return np.clip(np.diag(self._rho).real, 0.0, None)

    def purity(self) -> float:
        """``Tr(rho^2)`` in ``[1/2^n, 1]``; 1 only for a pure state."""
        return float(np.sum(np.abs(self._rho) ** 2))

    def reduced(self, qubit: int) -> np.ndarray:
        """2x2 reduced density matrix of one qubit (partial trace over the rest)."""
        (qubit,) = gates.validate_qubits([qubit], self.num_qubits)
        n = self.num_qubits
        tensor = np.moveaxis(self._tensor(), [qubit, n + qubit], [0, 1])
        rest = 2 ** (n - 1)
        return np.trace(tensor.reshape(2, 2, rest, rest), axis1=2, axis2=3)

    def fidelity_with_pure(self, state: np.ndarray) -> float:
        """``<psi| rho |psi>``."""
        vec = np.asarray(state, dtype=complex).reshape(-1)
        return float(np.vdot(vec, self._rho @ vec).real)

    def fidelity(self, other: DensityMatrix) -> float:
        """Uhlmann fidelity ``(Tr sqrt(sqrt(rho) sigma sqrt(rho)))^2`` in [0, 1]."""
        if other.num_qubits != self.num_qubits:
            raise ValueError("density matrices must have the same number of qubits")
        root = _psd_sqrt(self._rho)
        inner = root @ other._rho @ root
        values = np.clip(np.linalg.eigvalsh((inner + inner.conj().T) / 2), 0.0, None)
        return float(min(1.0, np.sum(np.sqrt(values)) ** 2))
