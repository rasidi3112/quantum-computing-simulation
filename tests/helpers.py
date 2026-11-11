import numpy as np

#: Tolerance for comparing amplitudes and probabilities.
TOL = 1e-12


def random_state(num_qubits: int, rng: np.random.Generator) -> np.ndarray:
    dim = 2**num_qubits
    vec = rng.normal(size=dim) + 1j * rng.normal(size=dim)
    return vec / np.linalg.norm(vec)


def random_unitary(dim: int, rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def basis(label: str) -> np.ndarray:
    vec = np.zeros(2 ** len(label), dtype=complex)
    vec[int(label, 2)] = 1.0
    return vec
