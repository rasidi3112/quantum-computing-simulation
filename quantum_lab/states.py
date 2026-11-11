from __future__ import annotations

from collections.abc import Sequence

import numpy as np

from .gates import PAULI_X, PAULI_Y, PAULI_Z, validate_qubits
from .measurement import num_qubits_of


def basis_labels(num_qubits: int) -> list[str]:
    return [format(i, f"0{num_qubits}b") for i in range(2**num_qubits)]


def reduced_density_matrix(state: np.ndarray, qubits: Sequence[int] | int) -> np.ndarray:
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
    rho = np.asarray(rho, dtype=complex)
    if rho.shape != (2, 2):
        raise ValueError(f"expected a 2x2 density matrix, got shape {rho.shape}")
    return np.array(
        [np.trace(rho @ pauli).real for pauli in (PAULI_X, PAULI_Y, PAULI_Z)]
    )


def qubit_bloch_vector(state: np.ndarray, qubit: int) -> np.ndarray:
    return bloch_vector(reduced_density_matrix(state, [qubit]))


def bloch_state(theta: float, phi: float) -> np.ndarray:
    return np.array(
        [np.cos(theta / 2), np.exp(1j * phi) * np.sin(theta / 2)], dtype=complex
    )


def purity(rho: np.ndarray) -> float:
    rho = np.asarray(rho)
    return float(np.sum(np.abs(rho) ** 2))


def entanglement_entropy(state: np.ndarray, qubits: Sequence[int] | int) -> float:
    eigenvalues = np.linalg.eigvalsh(reduced_density_matrix(state, qubits))
    eigenvalues = eigenvalues[eigenvalues > 1e-15]
    return float(max(0.0, -np.sum(eigenvalues * np.log2(eigenvalues))))
