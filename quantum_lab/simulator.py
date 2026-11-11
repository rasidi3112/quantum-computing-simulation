"""State-vector quantum simulator.

Qubit ordering is big-endian (qubit 0 = leftmost bit); see
:mod:`quantum_lab.gates` for the full statement of the convention.

Cost model
----------
The state of ``n`` qubits is a vector of ``2**n`` complex128 amplitudes, i.e.
``16 * 2**n`` bytes.  A ``k``-qubit gate is applied by tensor contraction in
``O(2**n * 2**k)`` time without ever building a ``2**n x 2**n`` matrix.
``MAX_QUBITS`` bounds the allocation.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence

import numpy as np

from . import gates, measurement

#: Hard upper bound on the register size (2**20 amplitudes = 16 MiB).
MAX_QUBITS = 20


def _validate_num_qubits(num_qubits: int, limit: int) -> int:
    if isinstance(num_qubits, (bool, np.bool_)) or not isinstance(
        num_qubits, (int, np.integer)
    ):
        raise TypeError(f"num_qubits must be an integer, got {num_qubits!r}")
    if num_qubits < 1:
        raise ValueError("num_qubits must be at least 1")
    if num_qubits > limit:
        raise ValueError(
            f"num_qubits={num_qubits} exceeds the supported maximum of {limit}"
        )
    return int(num_qubits)


def apply_matrix(
    tensor: np.ndarray, matrix: np.ndarray, axes: Sequence[int]
) -> np.ndarray:
    """Contract a ``2^k x 2^k`` matrix with ``k`` axes of a rank-n qubit tensor.

    ``axes[0]`` is the most significant qubit of the matrix index.  Returns a
    new tensor with the same axis order as ``tensor``.
    """
    k = len(axes)
    op = np.asarray(matrix, dtype=complex).reshape((2,) * (2 * k))
    out = np.tensordot(op, tensor, axes=(list(range(k, 2 * k)), list(axes)))
    return np.moveaxis(out, list(range(k)), list(axes))


class QuantumSimulator:
    """Ideal (noise-free) simulator for a register of ``num_qubits`` qubits.

    The register starts in ``|0...0>``.  Unitary evolution never renormalises
    the state: every operator is checked for unitarity instead, so the norm is
    preserved by construction.  Only projective measurement renormalises.
    """

    def __init__(self, num_qubits: int):
        self.num_qubits = _validate_num_qubits(num_qubits, MAX_QUBITS)
        self.dim = 2**self.num_qubits
        self._state = np.zeros(self.dim, dtype=complex)
        self._state[0] = 1.0

    # ------------------------------------------------------------------ state
    @property
    def state(self) -> np.ndarray:
        """Read-only view of the amplitudes (index = big-endian basis label)."""
        view = self._state.view()
        view.setflags(write=False)
        return view

    @state.setter
    def state(self, value: np.ndarray) -> None:
        self.set_state(value)

    def set_state(self, amplitudes: Iterable[complex], normalize: bool = False) -> None:
        """Replace the state vector.

        The vector must have ``2**num_qubits`` finite entries and unit norm;
        pass ``normalize=True`` to rescale a non-zero vector instead.
        """
        vec = np.array(amplitudes, dtype=complex).reshape(-1)
        if vec.shape != (self.dim,):
            raise ValueError(
                f"state must have {self.dim} amplitudes, got {vec.shape[0]}"
            )
        if not np.all(np.isfinite(vec)):
            raise ValueError("state amplitudes must be finite")
        norm = float(np.linalg.norm(vec))
        if normalize:
            if norm < gates.ATOL:
                raise ValueError("cannot normalise the zero vector")
            vec = vec / norm
        elif abs(norm - 1.0) > 1e-8:
            raise ValueError(f"state must be normalised (norm = {norm:.6g})")
        self._state = vec

    def reset(self) -> None:
        """Return to ``|0...0>``."""
        self._state = np.zeros(self.dim, dtype=complex)
        self._state[0] = 1.0

    def copy(self) -> QuantumSimulator:
        other = QuantumSimulator(self.num_qubits)
        other._state = self._state.copy()
        return other

    def norm(self) -> float:
        """Euclidean norm of the state (1 up to floating-point rounding)."""
        return float(np.linalg.norm(self._state))

    def get_amplitudes(self) -> np.ndarray:
        """Copy of the complex amplitudes."""
        return self._state.copy()

    def get_probabilities(self) -> np.ndarray:
        """Born-rule probabilities ``|alpha_i|^2`` for every basis state."""
        return measurement.probabilities(self._state)

    def marginal_probabilities(self, qubits: Sequence[int]) -> np.ndarray:
        """Joint distribution of the listed qubits (first listed = leftmost bit)."""
        return measurement.marginal_probabilities(self._state, qubits)

    # ------------------------------------------------------------------ gates
    def apply(self, matrix: np.ndarray, qubits: Sequence[int] | int) -> None:
        """Apply a ``k``-qubit unitary to the listed qubits.

        ``qubits[0]`` is the most significant qubit of the matrix index.
        Raises ``ValueError`` if the matrix is not unitary or has the wrong
        shape, or if a qubit index is invalid.
        """
        if isinstance(qubits, (int, np.integer)):
            qubits = [qubits]
        qubits = gates.validate_qubits(qubits, self.num_qubits)
        if not qubits:
            raise ValueError("at least one qubit is required")
        m = np.asarray(matrix, dtype=complex)
        size = 2 ** len(qubits)
        if m.shape != (size, size):
            raise ValueError(
                f"a {len(qubits)}-qubit gate needs a {size}x{size} matrix, "
                f"got shape {m.shape}"
            )
        if not gates.is_unitary(m):
            raise ValueError("gate matrix is not unitary (U^dagger U != I)")
        tensor = self._state.reshape((2,) * self.num_qubits)
        self._state = np.ascontiguousarray(apply_matrix(tensor, m, qubits)).reshape(-1)

    def apply_controlled(
        self, matrix: np.ndarray, controls: Sequence[int] | int, target: int
    ) -> None:
        """Apply a single-qubit unitary to ``target`` iff all ``controls`` are 1."""
        if isinstance(controls, (int, np.integer)):
            controls = [controls]
        controls = tuple(controls)
        qubits = gates.validate_qubits([*controls, target], self.num_qubits)
        target = qubits[-1]
        m = np.asarray(matrix, dtype=complex)
        if m.shape != (2, 2):
            raise ValueError(f"expected a 2x2 gate, got shape {m.shape}")
        if not gates.is_unitary(m):
            raise ValueError("gate matrix is not unitary (U^dagger U != I)")
        if not controls:
            self.apply(m, [target])
            return
        tensor = self._state.reshape((2,) * self.num_qubits).copy()
        index: list[slice | int] = [slice(None)] * self.num_qubits
        for c in qubits[:-1]:
            index[c] = 1
        # Axis of the target inside the sub-tensor where all controls are 1.
        axis = target - sum(1 for c in qubits[:-1] if c < target)
        block = tensor[tuple(index)]
        tensor[tuple(index)] = apply_matrix(block, m, [axis])
        self._state = tensor.reshape(-1)

    def cnot(self, control: int, target: int) -> None:
        """Controlled-NOT: flip ``target`` iff ``control`` is ``|1>``."""
        self.apply_controlled(gates.PAULI_X, [control], target)

    def apply_gate(
        self,
        gate_matrix: np.ndarray,
        target_qubit: int,
        control_qubit: int | None = None,
    ) -> None:
        """Mini Quantum Lab 1.0 entry point, kept for backward compatibility.

        Without ``control_qubit`` this is :meth:`apply` on one qubit.  With a
        ``control_qubit`` it applies a CNOT and ignores ``gate_matrix`` — that
        is what 1.0 did.  New code should call :meth:`apply`, :meth:`cnot` or
        :meth:`apply_controlled`.
        """
        if control_qubit is not None:
            self.cnot(control_qubit, target_qubit)
        else:
            self.apply(gate_matrix, [target_qubit])

    # Reference implementations (dense matrices), kept under their 1.0 names.
    def _expand_gate(self, gate: np.ndarray, target: int) -> np.ndarray:
        return gates.expand_gate(gate, target, self.num_qubits)

    def _create_cnot_matrix(self, control: int, target: int) -> np.ndarray:
        return gates.cnot_matrix(control, target, self.num_qubits)

    # ------------------------------------------------------------ measurement
    def measure(self, shots: int = 1000, rng=None) -> np.ndarray:
        """Sample ``shots`` basis-state indices from the Born distribution.

        This models *repeated preparation and measurement* of identical copies
        of the state; the simulator's state is **not** changed.  ``rng`` may be
        ``None``, an integer seed or a ``numpy.random.Generator``.
        """
        return measurement.sample_outcomes(self.get_probabilities(), shots, rng)

    def sample_counts(self, shots: int = 1000, rng=None) -> np.ndarray:
        """Like :meth:`measure` but returns the count of every basis state."""
        return measurement.sample_counts(self.get_probabilities(), shots, rng)

    def project(self, qubit: int, outcome: int) -> float:
        """Collapse ``qubit`` onto ``outcome`` (post-selection).

        Returns the probability that outcome had before the collapse.
        """
        self._state, prob = measurement.project_qubit(self._state, qubit, outcome)
        return prob

    def measure_qubit(self, qubit: int, rng=None) -> int:
        """Projective measurement of one qubit: sample, collapse, renormalise."""
        self._state, outcome = measurement.measure_qubit(self._state, qubit, rng)
        return outcome

    def measure_all(self, rng=None) -> int:
        """Projective measurement of every qubit; returns the basis index."""
        self._state, outcome = measurement.measure_all(self._state, rng)
        return outcome
