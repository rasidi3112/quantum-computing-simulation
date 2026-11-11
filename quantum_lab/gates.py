"""Quantum gate definitions and matrix helpers.

Qubit-ordering convention (used by the whole package)
-----------------------------------------------------
**Big-endian / textbook order**: qubit 0 is the *leftmost* (most significant)
bit of a basis label.  For ``n`` qubits

    |q0 q1 ... q(n-1)>   has basis index   sum_k  q_k * 2**(n-1-k)

so a product state is ``|q0> (x) |q1> (x) ... (x) |q(n-1)>`` in ``numpy.kron``
order and, after ``state.reshape((2,) * n)``, tensor axis ``k`` is qubit ``k``.
This matches Nielsen & Chuang and the labels shown in the user interface.
(Qiskit uses the opposite, little-endian order.)

Multi-qubit gate matrices follow the same rule: for a matrix acting on the
qubit list ``[a, b]`` the *first* listed qubit is the most significant bit of
the matrix index.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from dataclasses import dataclass

import numpy as np

#: Absolute tolerance used for unitarity / normalisation checks.
ATOL = 1e-10

IDENTITY = np.eye(2, dtype=complex)
PAULI_X = np.array([[0, 1], [1, 0]], dtype=complex)
PAULI_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
PAULI_Z = np.array([[1, 0], [0, -1]], dtype=complex)
HADAMARD = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
S_GATE = np.array([[1, 0], [0, 1j]], dtype=complex)
T_GATE = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=complex)

#: Two-qubit CNOT on the qubit list ``[control, target]`` (big-endian).
CNOT = np.array(
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], dtype=complex
)

for _m in (IDENTITY, PAULI_X, PAULI_Y, PAULI_Z, HADAMARD, S_GATE, T_GATE, CNOT):
    _m.setflags(write=False)
del _m


def rx(theta: float) -> np.ndarray:
    """Rotation about the X axis: ``exp(-i * theta/2 * X)``."""
    c, s = np.cos(theta / 2), np.sin(theta / 2)
    return np.array([[c, -1j * s], [-1j * s, c]], dtype=complex)


def ry(theta: float) -> np.ndarray:
    """Rotation about the Y axis: ``exp(-i * theta/2 * Y)``."""
    c, s = np.cos(theta / 2), np.sin(theta / 2)
    return np.array([[c, -s], [s, c]], dtype=complex)


def rz(theta: float) -> np.ndarray:
    """Rotation about the Z axis: ``exp(-i * theta/2 * Z)``."""
    return np.array(
        [[np.exp(-1j * theta / 2), 0], [0, np.exp(1j * theta / 2)]], dtype=complex
    )


def phase(lam: float) -> np.ndarray:
    """Phase gate ``diag(1, e^{i*lam})``; ``S = phase(pi/2)``, ``T = phase(pi/4)``."""
    return np.array([[1, 0], [0, np.exp(1j * lam)]], dtype=complex)


@dataclass(frozen=True)
class GateSpec:
    """Static description of a named single-qubit gate."""

    gate_id: str  #: short identifier used in circuits and diagrams, e.g. ``"H"``
    name: str  #: display name (kept identical to Mini Quantum Lab 1.0)
    matrix: np.ndarray
    emoji: str


#: Fixed single-qubit gates offered by the lab, keyed by short identifier.
GATES: dict[str, GateSpec] = {
    spec.gate_id: spec
    for spec in (
        GateSpec("H", "Hadamard (H)", HADAMARD, "🌊"),
        GateSpec("X", "Pauli-X", PAULI_X, "🔄"),
        GateSpec("Y", "Pauli-Y", PAULI_Y, "🔃"),
        GateSpec("Z", "Pauli-Z", PAULI_Z, "⚡"),
        GateSpec("S", "S Gate", S_GATE, "📐"),
        GateSpec("T", "T Gate", T_GATE, "🎯"),
        GateSpec("I", "Identity (I)", IDENTITY, "⏸️"),
    )
}

_PARAMETRIC = {"RX": rx, "RY": ry, "RZ": rz, "P": phase}


def gate_matrix(gate_id: str, params: Sequence[float] = ()) -> np.ndarray:
    """Return the 2x2 matrix of a named gate (``"H"``, ``"X"``, ``"RY"`` ...).

    Parametric gates (``RX``, ``RY``, ``RZ``, ``P``) take exactly one angle in
    radians; fixed gates take none.
    """
    if gate_id in GATES:
        if len(params) != 0:
            raise ValueError(f"gate {gate_id!r} takes no parameters")
        return GATES[gate_id].matrix
    if gate_id in _PARAMETRIC:
        if len(params) != 1:
            raise ValueError(f"gate {gate_id!r} takes exactly one angle")
        angle = float(params[0])
        if not np.isfinite(angle):
            raise ValueError("gate angle must be finite")
        return _PARAMETRIC[gate_id](angle)
    raise ValueError(f"unknown gate {gate_id!r}")


def is_unitary(matrix: np.ndarray, atol: float = ATOL) -> bool:
    """Return True if ``matrix`` is square and satisfies ``U^dagger U = I``."""
    m = np.asarray(matrix)
    if m.ndim != 2 or m.shape[0] != m.shape[1]:
        return False
    if not np.all(np.isfinite(m)):
        return False
    return bool(np.allclose(m.conj().T @ m, np.eye(m.shape[0]), atol=atol, rtol=0))


def validate_qubits(qubits: Iterable[int], num_qubits: int) -> tuple[int, ...]:
    """Check that ``qubits`` are distinct integer indices in ``[0, num_qubits)``."""
    out = []
    for q in qubits:
        if isinstance(q, (bool, np.bool_)) or not isinstance(q, (int, np.integer)):
            raise TypeError(f"qubit index must be an integer, got {q!r}")
        q = int(q)
        if not 0 <= q < num_qubits:
            raise ValueError(
                f"qubit index {q} out of range for a {num_qubits}-qubit system"
            )
        out.append(q)
    if len(set(out)) != len(out):
        raise ValueError(f"qubit indices must be distinct, got {out}")
    return tuple(out)


def controlled_matrix(matrix: np.ndarray, num_controls: int = 1) -> np.ndarray:
    """Matrix of a controlled gate on the qubit list ``[*controls, *targets]``.

    The result is the identity except for the bottom-right block, where all
    control qubits are ``|1>``.
    """
    if num_controls < 0:
        raise ValueError("num_controls must be non-negative")
    m = np.asarray(matrix, dtype=complex)
    dim = m.shape[0] * 2**num_controls
    out = np.eye(dim, dtype=complex)
    out[dim - m.shape[0] :, dim - m.shape[0] :] = m
    return out


def expand_gate(gate: np.ndarray, target: int, num_qubits: int) -> np.ndarray:
    """Full ``2^n x 2^n`` matrix of a single-qubit gate acting on ``target``.

    ``I (x) ... (x) gate (x) ... (x) I`` with ``gate`` at tensor position
    ``target`` (big-endian).  Costs ``O(4^n)`` memory: it exists for teaching
    and for cross-checking the simulator, which never builds this matrix.
    """
    (target,) = validate_qubits([target], num_qubits)
    g = np.asarray(gate, dtype=complex)
    if g.shape != (2, 2):
        raise ValueError(f"expected a 2x2 gate, got shape {g.shape}")
    result = np.eye(1, dtype=complex)
    for q in range(num_qubits):
        result = np.kron(result, g if q == target else IDENTITY)
    return result


def cnot_matrix(control: int, target: int, num_qubits: int) -> np.ndarray:
    """Full ``2^n x 2^n`` CNOT permutation matrix (big-endian, see module doc).

    Basis state ``|... c ... t ...>`` is mapped to ``|... c ... t XOR c ...>``.
    """
    control, target = validate_qubits([control, target], num_qubits)
    dim = 2**num_qubits
    control_mask = 1 << (num_qubits - 1 - control)
    target_mask = 1 << (num_qubits - 1 - target)
    matrix = np.zeros((dim, dim), dtype=complex)
    for column in range(dim):
        row = column ^ target_mask if column & control_mask else column
        matrix[row, column] = 1.0
    return matrix
