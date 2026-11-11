from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .circuit import Circuit, RunResult
from .states import bloch_state, bloch_vector, reduced_density_matrix

#: Bell state name -> (x, y): prepare |x y>, then H on q0 and CNOT(q0 -> q1).
#: The result is (|0 y> + (-1)^x |1 not-y>) / sqrt(2).
BELL_STATES: dict[str, tuple[int, int]] = {
    "Φ+": (0, 0),  # (|00> + |11>)/sqrt(2)
    "Φ-": (1, 0),  # (|00> - |11>)/sqrt(2)
    "Ψ+": (0, 1),  # (|01> + |10>)/sqrt(2)
    "Ψ-": (1, 1),  # (|01> - |10>)/sqrt(2)
}


def bell_circuit(kind: str = "Φ+") -> Circuit:
    if kind not in BELL_STATES:
        raise ValueError(f"unknown Bell state {kind!r}; expected one of {list(BELL_STATES)}")
    x, y = BELL_STATES[kind]
    circuit = Circuit(2)
    if x:
        circuit.gate("X", 0)
    if y:
        circuit.gate("X", 1)
    return circuit.gate("H", 0).cnot(0, 1)


def ghz_circuit(num_qubits: int) -> Circuit:
    if num_qubits < 2:
        raise ValueError("a GHZ state needs at least 2 qubits")
    circuit = Circuit(num_qubits).gate("H", 0)
    for q in range(num_qubits - 1):
        circuit.cnot(q, q + 1)
    return circuit


def teleportation_circuit(theta: float, phi: float) -> Circuit:
    return (
        Circuit(3)
        .gate("RY", 0, params=[theta])
        .gate("P", 0, params=[phi])
        .gate("H", 1)
        .cnot(1, 2)
        .cnot(0, 1)
        .gate("H", 0)
        .measure(0)
        .measure(1)
        .gate("X", 2, condition=1)
        .gate("Z", 2, condition=0)
    )


@dataclass
class TeleportationResult:
    message: np.ndarray  #: the single-qubit state Alice wanted to send
    outcomes: tuple[int, int]  #: Alice's classical bits (m0, m1)
    bob_density: np.ndarray  #: Bob's 2x2 reduced density matrix after correction
    bob_before_correction: np.ndarray  #: Bob's reduced state before X/Z fixes
    fidelity: float  #: <message| bob_density |message>
    message_bloch: np.ndarray
    bob_bloch: np.ndarray
    run: RunResult


def run_teleportation(
    theta: float, phi: float, rng=None, forced: dict[int, int] | None = None
) -> TeleportationResult:
    if not (np.isfinite(theta) and np.isfinite(phi)):
        raise ValueError("theta and phi must be finite")
    message = bloch_state(theta, phi)
    circuit = teleportation_circuit(theta, phi)
    result = circuit.run(rng=rng, forced=forced)
    bob = reduced_density_matrix(result.simulator.state, [2])

    # Same run, stopped before Bob's corrections, with the same outcomes.
    uncorrected = Circuit(3, circuit.ops[:-2]).run(forced=result.outcomes)
    bob_before = reduced_density_matrix(uncorrected.simulator.state, [2])

    fidelity = float(np.vdot(message, bob @ message).real)
    return TeleportationResult(
        message=message,
        outcomes=(result.outcomes[0], result.outcomes[1]),
        bob_density=bob,
        bob_before_correction=bob_before,
        fidelity=fidelity,
        message_bloch=bloch_vector(np.outer(message, message.conj())),
        bob_bloch=bloch_vector(bob),
        run=result,
    )
