"""Analysis helpers for state vectors and density matrices.

All functions use the package's big-endian convention (qubit 0 = leftmost
bit); see :mod:`quantum_lab.gates`.
"""

from __future__ import annotations

from typing import Sequence

import numpy as np

from .gates import PAULI_X, PAULI_Y, PAULI_Z, validate_qubits
from .measurement import num_qubits_of


def basis_labels(num_qubits: int) -> list[str]:
    """Bit-string labels ``"00..0"`` .. ``"11..1"`` in basis-index order."""
    return [format(i, f"0{num_qubits}b") for i in range(2**num_qubits)]


def reduced_density_matrix(state: np.ndarray, qubits: Sequence[int] | int) -> np.ndarray:
    """Partial trace of ``|psi><psi|`` over every qubit *not* listed.

    Returns a ``2^k x 2^k`` density matrix whose index is ordered like the
    ``qubits`` argument (first listed = most significant).
    """
    n = num_qubits_of(state)
    if isinstance(qubits, (int, np.integer)):
        qubits = [qubits]
    qubits = validate_qubits(qubits, n)
    if not qubits:
        raise ValueError("at least one qubit is required")
    tensor = np.asarray(state, dtype=complex).reshape((2,) * n)
    tensor = np.moveaxis(tensor, list(qubits), list(range(len(qubits))))
    m = tensor.reshape(2 ** len(qubits), -1)
    return m @ m.conj().T


def bloch_vector(rho: np.ndarray) -> np.ndarray:
    """Bloch vector ``(<X>, <Y>, <Z>)`` of a single-qubit density matrix.

    ``rho = (I + r . sigma) / 2``.  ``|r| = 1`` for a pure state and
    ``|r| < 1`` for a mixed state (``r = 0``: maximally mixed).
    """
    rho = np.asarray(rho, dtype=complex)
    if rho.shape != (2, 2):
        raise ValueError(f"expected a 2x2 density matrix, got shape {rho.shape}")
    return np.array(
        [np.trace(rho @ pauli).real for pauli in (PAULI_X, PAULI_Y, PAULI_Z)]
    )


def qubit_bloch_vector(state: np.ndarray, qubit: int) -> np.ndarray:
    """Bloch vector of one qubit of a (possibly entangled) pure state.

    The vector describes the qubit's *reduced* state.  If the qubit is
    entangled with the rest of the register its length is below 1.
    """
    return bloch_vector(reduced_density_matrix(state, [qubit]))


def bloch_state(theta: float, phi: float) -> np.ndarray:
    """Pure state ``cos(theta/2)|0> + e^{i phi} sin(theta/2)|1>``."""
    return np.array(
        [np.cos(theta / 2), np.exp(1j * phi) * np.sin(theta / 2)], dtype=complex
    )


def purity(rho: np.ndarray) -> float:
    """``Tr(rho^2)``: 1 for a pure state, ``1/d`` for the maximally mixed state."""
    rho = np.asarray(rho)
    return float(np.sum(np.abs(rho) ** 2))


def entanglement_entropy(state: np.ndarray, qubits: Sequence[int] | int) -> float:
    """Von Neumann entropy (in bits) of the reduced state of ``qubits``.

    For a pure state this measures the entanglement between ``qubits`` and
    the remaining qubits: 0 for a product state, 1 for a Bell pair.
    """
    eigenvalues = np.linalg.eigvalsh(reduced_density_matrix(state, qubits))
    eigenvalues = eigenvalues[eigenvalues > 1e-15]
    return float(max(0.0, -np.sum(eigenvalues * np.log2(eigenvalues))))
