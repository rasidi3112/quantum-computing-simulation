from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

import numpy as np

from .circuit import Circuit
from .measurement import make_rng

# ===================================================================== Grover
GROVER_MIN_QUBITS = 2


def _check_grover(num_qubits: int, marked: int) -> None:
    if num_qubits < GROVER_MIN_QUBITS:
        raise ValueError(f"Grover search needs at least {GROVER_MIN_QUBITS} qubits")
    if isinstance(marked, (bool, np.bool_)) or not isinstance(marked, (int, np.integer)):
        raise TypeError("marked state must be an integer basis index")
    if not 0 <= marked < 2**num_qubits:
        raise ValueError(f"marked state {marked} out of range for {num_qubits} qubits")


def grover_angle(num_qubits: int) -> float:
    return float(np.arcsin(1.0 / np.sqrt(2**num_qubits)))


def grover_optimal_iterations(num_qubits: int) -> int:
    return int(np.floor(np.pi / (4 * grover_angle(num_qubits))))


def grover_theoretical_probability(num_qubits: int, iterations: int) -> float:
    return float(np.sin((2 * iterations + 1) * grover_angle(num_qubits)) ** 2)


def _phase_flip_all_ones(circuit: Circuit) -> None:
    n = circuit.num_qubits
    circuit.gate("Z", n - 1, controls=list(range(n - 1)))


def grover_circuit(num_qubits: int, marked: int, iterations: int) -> Circuit:
    _check_grover(num_qubits, marked)
    if iterations < 0:
        raise ValueError("iterations must be non-negative")
    bits = format(marked, f"0{num_qubits}b")
    zeros = [q for q, bit in enumerate(bits) if bit == "0"]
    circuit = Circuit(num_qubits)
    for q in range(num_qubits):
        circuit.gate("H", q)
    for _ in range(iterations):
        for q in zeros:
            circuit.gate("X", q)
        _phase_flip_all_ones(circuit)
        for q in zeros:
            circuit.gate("X", q)
        for name in ("H", "X"):
            for q in range(num_qubits):
                circuit.gate(name, q)
        _phase_flip_all_ones(circuit)
        for name in ("X", "H"):
            for q in range(num_qubits):
                circuit.gate(name, q)
    return circuit


def grover_success_probabilities(num_qubits: int, marked: int, max_iterations: int) -> list[float]:
    _check_grover(num_qubits, marked)
    return [
        float(grover_circuit(num_qubits, marked, k).run().simulator.get_probabilities()[marked])
        for k in range(max_iterations + 1)
    ]


# ============================================================= Deutsch-Jozsa
CONSTANT, BALANCED, NEITHER = "constant", "balanced", "neither"


def _check_table(truth_table: Sequence[int]) -> tuple[np.ndarray, int]:
    table = np.asarray(truth_table)
    size = table.shape[0] if table.ndim == 1 else 0
    n = int(size).bit_length() - 1
    if size < 2 or 2**n != size:
        raise ValueError("truth table length must be 2**n with n >= 1")
    if not np.all((table == 0) | (table == 1)):
        raise ValueError("truth table entries must be 0 or 1")
    return table.astype(int), n


def classify_function(truth_table: Sequence[int]) -> str:
    table, _ = _check_table(truth_table)
    ones = int(table.sum())
    if ones in (0, table.size):
        return CONSTANT
    if 2 * ones == table.size:
        return BALANCED
    return NEITHER


def constant_oracle(num_inputs: int, value: int) -> list[int]:
    if value not in (0, 1):
        raise ValueError("value must be 0 or 1")
    if num_inputs < 1:
        raise ValueError("num_inputs must be at least 1")
    return [int(value)] * 2**num_inputs


def parity_oracle(num_inputs: int, mask: int, flip: bool = False) -> list[int]:
    if num_inputs < 1:
        raise ValueError("num_inputs must be at least 1")
    if not 0 < mask < 2**num_inputs:
        raise ValueError("mask must be a non-zero n-bit integer")
    return [(bin(x & mask).count("1") + int(flip)) % 2 for x in range(2**num_inputs)]


def random_balanced_oracle(num_inputs: int, rng=None) -> list[int]:
    if num_inputs < 1:
        raise ValueError("num_inputs must be at least 1")
    size = 2**num_inputs
    table = np.zeros(size, dtype=int)
    table[make_rng(rng).choice(size, size=size // 2, replace=False)] = 1
    return table.tolist()


def oracle_matrix(truth_table: Sequence[int]) -> np.ndarray:
    table, n = _check_table(truth_table)
    dim = 2 ** (n + 1)
    matrix = np.zeros((dim, dim), dtype=complex)
    for x in range(2**n):
        for y in (0, 1):
            matrix[(x << 1) | (y ^ int(table[x])), (x << 1) | y] = 1.0
    return matrix


def deutsch_jozsa_circuit(truth_table: Sequence[int]) -> Circuit:
    _, n = _check_table(truth_table)
    circuit = Circuit(n + 1).gate("X", n)
    for q in range(n + 1):
        circuit.gate("H", q)
    circuit.unitary("Uf", list(range(n + 1)), oracle_matrix(truth_table))
    for q in range(n):
        circuit.gate("H", q)
    return circuit


@dataclass
class DeutschJozsaResult:
    num_inputs: int
    function_type: str  #: ground truth from the truth table
    input_probabilities: np.ndarray  #: distribution of the input register
    prob_all_zero: float  #: P(input register = 0...0)
    verdict: str  #: what the algorithm concludes from a measurement
    circuit: Circuit
    classical_queries_worst_case: int  #: 2^(n-1) + 1 for a deterministic answer


def run_deutsch_jozsa(truth_table: Sequence[int]) -> DeutschJozsaResult:
    table, n = _check_table(truth_table)
    circuit = deutsch_jozsa_circuit(table)
    sim = circuit.run().simulator
    marginal = sim.marginal_probabilities(list(range(n)))
    prob_zero = float(marginal[0])
    return DeutschJozsaResult(
        num_inputs=n,
        function_type=classify_function(table),
        input_probabilities=marginal,
        prob_all_zero=prob_zero,
        verdict=CONSTANT if prob_zero > 0.5 else BALANCED,
        circuit=circuit,
        classical_queries_worst_case=2 ** (n - 1) + 1,
    )
