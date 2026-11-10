"""Grover search and Deutsch-Jozsa."""

import itertools

import numpy as np
import pytest

from quantum_lab import algorithms as alg
from quantum_lab import gates

from .helpers import TOL


# ------------------------------------------------------------------- Grover
@pytest.mark.parametrize("n", [2, 3, 4])
def test_grover_matches_closed_form_for_every_marked_state(n):
    for marked in range(2**n):
        simulated = alg.grover_success_probabilities(n, marked, 4)
        theory = [alg.grover_theoretical_probability(n, k) for k in range(5)]
        assert simulated == pytest.approx(theory, abs=1e-10)


def test_grover_two_qubits_is_exact_after_one_iteration():
    for marked in range(4):
        probs = alg.grover_circuit(2, marked, 1).run().simulator.get_probabilities()
        expected = np.zeros(4)
        expected[marked] = 1.0
        assert probs == pytest.approx(expected, abs=TOL)


@pytest.mark.parametrize("n, k_opt", [(2, 1), (3, 2), (4, 3), (5, 4), (6, 6)])
def test_grover_optimal_iteration_count(n, k_opt):
    assert alg.grover_optimal_iterations(n) == k_opt
    best = alg.grover_theoretical_probability(n, k_opt)
    assert best >= alg.grover_theoretical_probability(n, k_opt - 1)
    assert best >= alg.grover_theoretical_probability(n, k_opt + 1)
    assert best > 0.9


def test_grover_amplifies_only_the_marked_state():
    n, marked = 4, 0b1010
    probs = alg.grover_circuit(n, marked, alg.grover_optimal_iterations(n)).run() \
        .simulator.get_probabilities()
    assert int(np.argmax(probs)) == marked
    assert probs[marked] == pytest.approx(0.9613189697265625, abs=1e-10)
    others = np.delete(probs, marked)
    assert np.allclose(others, others[0], atol=TOL)  # unmarked states stay uniform
    assert probs.sum() == pytest.approx(1.0, abs=TOL)


def test_grover_oracle_and_diffusion_operators():
    # One iteration, read as a matrix, must equal -(2|s><s| - I)(I - 2|w><w|).
    n, marked = 3, 5
    dim = 2**n
    zero_iter, one_iter = (alg.grover_circuit(n, marked, k) for k in (0, 1))
    iteration_ops = one_iter.ops[len(zero_iter.ops):]
    unitary = np.eye(dim, dtype=complex)
    for op in iteration_ops:
        m = gates.gate_matrix(op.name)
        if op.controls:
            full = np.eye(dim, dtype=complex)
            full[dim - 1, dim - 1] = -1  # MCZ in any qubit order
        else:
            full = gates.expand_gate(m, op.targets[0], n)
        unitary = full @ unitary
    s = np.full(dim, 1 / np.sqrt(dim))
    w = np.zeros(dim)
    w[marked] = 1
    oracle = np.eye(dim) - 2 * np.outer(w, w)
    diffusion = 2 * np.outer(s, s) - np.eye(dim)
    assert np.allclose(unitary, -diffusion @ oracle, atol=1e-10)


def test_grover_over_rotation_reduces_success():
    probs = alg.grover_success_probabilities(3, 6, 4)
    assert probs[2] > probs[3] > probs[4]


@pytest.mark.parametrize(
    "call",
    [
        lambda: alg.grover_circuit(1, 0, 1),
        lambda: alg.grover_circuit(2, 4, 1),
        lambda: alg.grover_circuit(2, -1, 1),
        lambda: alg.grover_circuit(2, 0, -1),
        lambda: alg.grover_success_probabilities(1, 0, 2),
    ],
)
def test_grover_invalid_arguments(call):
    with pytest.raises(ValueError):
        call()


def test_grover_marked_must_be_an_integer():
    with pytest.raises(TypeError):
        alg.grover_circuit(2, "11", 1)


# ------------------------------------------------------------ Deutsch-Jozsa
@pytest.mark.parametrize("n", [1, 2, 3, 4])
@pytest.mark.parametrize("value", [0, 1])
def test_constant_functions_give_all_zeros(n, value):
    result = alg.run_deutsch_jozsa(alg.constant_oracle(n, value))
    assert result.function_type == alg.CONSTANT
    assert result.prob_all_zero == pytest.approx(1.0, abs=TOL)
    assert result.verdict == alg.CONSTANT


@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_parity_functions_never_give_all_zeros(n):
    for mask in range(1, 2**n):
        for flip in (False, True):
            table = alg.parity_oracle(n, mask, flip)
            result = alg.run_deutsch_jozsa(table)
            assert result.function_type == alg.BALANCED
            assert result.prob_all_zero == pytest.approx(0.0, abs=TOL)
            assert result.verdict == alg.BALANCED
            # Bernstein-Vazirani: the register reads the mask itself
            assert result.input_probabilities[mask] == pytest.approx(1.0, abs=TOL)


def test_every_balanced_function_on_two_and_three_inputs():
    for n in (2, 3):
        size = 2**n
        for ones in itertools.combinations(range(size), size // 2):
            table = [1 if x in ones else 0 for x in range(size)]
            result = alg.run_deutsch_jozsa(table)
            assert result.prob_all_zero == pytest.approx(0.0, abs=TOL)
            assert result.verdict == alg.BALANCED


def test_random_balanced_oracle_is_balanced_and_seeded():
    for n in (1, 2, 3, 4, 5):
        table = alg.random_balanced_oracle(n, rng=n)
        assert alg.classify_function(table) == alg.BALANCED
        assert table == alg.random_balanced_oracle(n, rng=n)
        assert alg.run_deutsch_jozsa(table).verdict == alg.BALANCED
    assert len({tuple(alg.random_balanced_oracle(3, rng=s)) for s in range(20)}) > 1


def test_promise_violation_gives_intermediate_probability():
    table = [0, 0, 0, 1]  # neither constant nor balanced
    result = alg.run_deutsch_jozsa(table)
    assert result.function_type == alg.NEITHER
    expected = abs(sum((-1) ** f for f in table) / 4) ** 2
    assert result.prob_all_zero == pytest.approx(expected, abs=TOL)
    assert 0 < result.prob_all_zero < 1


def test_oracle_matrix_is_a_unitary_permutation_implementing_f():
    table = alg.random_balanced_oracle(3, rng=5)
    u = alg.oracle_matrix(table)
    assert gates.is_unitary(u)
    assert np.allclose(u @ u, np.eye(16))  # XOR twice = identity
    for x in range(8):
        for y in (0, 1):
            column = u[:, (x << 1) | y]
            assert column[(x << 1) | (y ^ table[x])] == 1


def test_classical_query_count_and_circuit_shape():
    result = alg.run_deutsch_jozsa(alg.constant_oracle(3, 0))
    assert result.num_inputs == 3
    assert result.classical_queries_worst_case == 5
    assert result.circuit.num_qubits == 4
    assert sum(op.name == "Uf" for op in result.circuit.ops) == 1  # a single query
    assert result.input_probabilities.sum() == pytest.approx(1.0, abs=TOL)


def test_classify_function():
    assert alg.classify_function([0, 0]) == alg.CONSTANT
    assert alg.classify_function([1, 1, 1, 1]) == alg.CONSTANT
    assert alg.classify_function([0, 1, 1, 0]) == alg.BALANCED
    assert alg.classify_function([0, 1, 1, 1]) == alg.NEITHER


@pytest.mark.parametrize(
    "call",
    [
        lambda: alg.run_deutsch_jozsa([0, 1, 0]),
        lambda: alg.run_deutsch_jozsa([0]),
        lambda: alg.run_deutsch_jozsa([0, 2]),
        lambda: alg.constant_oracle(2, 3),
        lambda: alg.constant_oracle(0, 0),
        lambda: alg.parity_oracle(2, 0),
        lambda: alg.parity_oracle(2, 4),
        lambda: alg.random_balanced_oracle(0),
    ],
)
def test_deutsch_jozsa_invalid_arguments(call):
    with pytest.raises(ValueError):
        call()
