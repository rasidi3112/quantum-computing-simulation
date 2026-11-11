import numpy as np
import pytest

from quantum_lab import QuantumSimulator, gates, measurement

from .helpers import TOL, basis, random_state

SQRT2 = np.sqrt(2)


def bell() -> QuantumSimulator:
    sim = QuantumSimulator(2)
    sim.apply(gates.HADAMARD, [0])
    sim.cnot(0, 1)
    return sim


# ------------------------------------------------------------ probabilities
def test_probabilities_follow_born_rule_and_sum_to_one():
    rng = np.random.default_rng(0)
    for n in (1, 2, 3, 4):
        state = random_state(n, rng)
        p = measurement.probabilities(state)
        assert np.all(p >= 0)
        assert np.allclose(p, (state * state.conj()).real)
        assert p.sum() == pytest.approx(1.0, abs=TOL)


def test_bell_state_measurement_probabilities():
    p = dict(zip(["00", "01", "10", "11"], bell().get_probabilities(), strict=True))
    assert p == pytest.approx({"00": 0.5, "01": 0.0, "10": 0.0, "11": 0.5}, abs=TOL)


def test_biased_single_qubit_probabilities():
    theta = 1.1
    sim = QuantumSimulator(1)
    sim.apply(gates.ry(theta), [0])
    assert sim.get_probabilities() == pytest.approx(
        [np.cos(theta / 2) ** 2, np.sin(theta / 2) ** 2], abs=TOL
    )


def test_marginal_probabilities():
    sim = QuantumSimulator(3)  # |1> (x) |+> (x) |0>
    sim.apply(gates.PAULI_X, [0])
    sim.apply(gates.HADAMARD, [1])
    assert sim.marginal_probabilities([0]) == pytest.approx([0, 1], abs=TOL)
    assert sim.marginal_probabilities([1]) == pytest.approx([0.5, 0.5], abs=TOL)
    assert sim.marginal_probabilities([2]) == pytest.approx([1, 0], abs=TOL)
    # order of the argument defines the bit order of the result
    assert sim.marginal_probabilities([0, 2]) == pytest.approx([0, 0, 1, 0], abs=TOL)
    assert sim.marginal_probabilities([2, 0]) == pytest.approx([0, 1, 0, 0], abs=TOL)
    assert sim.marginal_probabilities([0, 1, 2]) == pytest.approx(
        sim.get_probabilities(), abs=TOL
    )
    assert bell().marginal_probabilities([1]) == pytest.approx([0.5, 0.5], abs=TOL)


def test_marginal_matches_brute_force_on_random_state():
    rng = np.random.default_rng(9)
    state = random_state(4, rng)
    p = measurement.probabilities(state)
    for qubits in ([3, 1], [0, 2, 3], [2]):
        expected = np.zeros(2 ** len(qubits))
        for index, prob in enumerate(p):
            bits = format(index, "04b")
            expected[int("".join(bits[q] for q in qubits), 2)] += prob
        assert measurement.marginal_probabilities(state, qubits) == pytest.approx(
            expected, abs=TOL
        )


# ------------------------------------------------------------ shot sampling
def test_sampling_is_reproducible_with_a_seed():
    sim = bell()
    assert np.array_equal(sim.sample_counts(500, rng=42), sim.sample_counts(500, rng=42))
    assert np.array_equal(sim.measure(500, rng=42), sim.measure(500, rng=42))
    assert not np.array_equal(sim.measure(500, rng=42), sim.measure(500, rng=43))


def test_sampling_with_a_shared_generator_advances_it():
    sim = bell()
    rng = np.random.default_rng(1)
    first, second = sim.measure(200, rng=rng), sim.measure(200, rng=rng)
    assert not np.array_equal(first, second)


def test_sampling_does_not_change_the_state():
    sim = bell()
    before = sim.get_amplitudes()
    sim.measure(1000, rng=0)
    sim.sample_counts(1000, rng=0)
    assert np.array_equal(sim.state, before)


def test_bell_state_never_yields_01_or_10():
    counts = bell().sample_counts(20_000, rng=123)
    assert counts.sum() == 20_000
    assert counts[1] == 0 and counts[2] == 0
    # 5-sigma band around the binomial mean (sigma = sqrt(N/4) ~ 70.7)
    assert abs(counts[0] - 10_000) < 5 * np.sqrt(20_000 * 0.25)


def test_counts_converge_to_probabilities():
    sim = QuantumSimulator(3)
    sim.set_state(random_state(3, np.random.default_rng(4)))
    shots = 200_000
    p = sim.get_probabilities()
    freq = sim.sample_counts(shots, rng=2024) / shots
    sigma = np.sqrt(p * (1 - p) / shots)
    assert np.all(np.abs(freq - p) < 5 * sigma + 1e-9)


def test_measure_returns_indices_consistent_with_counts_shape():
    outcomes = bell().measure(300, rng=5)
    assert outcomes.shape == (300,)
    assert set(np.unique(outcomes)) <= {0, 3}


def test_deterministic_state_always_gives_the_same_outcome():
    sim = QuantumSimulator(2)
    sim.apply(gates.PAULI_X, [1])
    assert np.array_equal(sim.sample_counts(100, rng=0), [0, 100, 0, 0])


# ---------------------------------------------------- projective measurement
def test_measuring_a_basis_state_is_deterministic():
    sim = QuantumSimulator(2)
    sim.apply(gates.PAULI_X, [0])
    assert sim.measure_qubit(0, rng=0) == 1
    assert sim.measure_qubit(1, rng=0) == 0
    assert np.allclose(sim.state, basis("10"))


def test_collapse_of_superposition():
    for seed in range(20):
        sim = QuantumSimulator(1)
        sim.apply(gates.HADAMARD, [0])
        outcome = sim.measure_qubit(0, rng=seed)
        assert np.allclose(sim.state, basis(str(outcome)))
        assert sim.norm() == pytest.approx(1.0, abs=TOL)
        # measuring again must repeat the result (projective measurement)
        assert all(sim.measure_qubit(0, rng=s) == outcome for s in range(5))


def test_bell_state_collapse_correlates_both_qubits():
    seen = set()
    for seed in range(40):
        sim = bell()
        first = sim.measure_qubit(0, rng=seed)
        seen.add(first)
        assert np.allclose(sim.state, basis(f"{first}{first}"))
        assert sim.measure_qubit(1, rng=seed + 1000) == first
    assert seen == {0, 1}


def test_partial_collapse_keeps_remaining_superposition_normalised():
    # (|00> + |01> + |10>)/sqrt(3): measuring q0 = 0 leaves (|00> + |01>)/sqrt(2)
    sim = QuantumSimulator(2)
    sim.set_state(np.array([1, 1, 1, 0]) / np.sqrt(3))
    prob = sim.project(0, 0)
    assert prob == pytest.approx(2 / 3, abs=TOL)
    assert np.allclose(sim.state, np.array([1, 1, 0, 0]) / SQRT2, atol=TOL)
    assert sim.norm() == pytest.approx(1.0, abs=TOL)

    sim.set_state(np.array([1, 1, 1, 0]) / np.sqrt(3))
    assert sim.project(0, 1) == pytest.approx(1 / 3, abs=TOL)
    assert np.allclose(sim.state, basis("10"))


def test_collapse_preserves_relative_phases():
    state = np.array([0.5, 0.5j, -0.5, 0.5], dtype=complex)
    collapsed, prob = measurement.project_qubit(state, 1, 1)
    assert prob == pytest.approx(0.5, abs=TOL)
    assert np.allclose(collapsed, np.array([0, 1j, 0, 1]) / SQRT2, atol=TOL)
    assert np.allclose(state, [0.5, 0.5j, -0.5, 0.5])  # input untouched


def test_projection_on_random_state_matches_projector_algebra():
    rng = np.random.default_rng(31)
    n = 3
    for qubit in range(n):
        for outcome in (0, 1):
            state = random_state(n, rng)
            projector = gates.expand_gate(np.diag([1 - outcome, outcome]), qubit, n)
            unnormalised = projector @ state
            prob = np.vdot(unnormalised, unnormalised).real
            collapsed, p = measurement.project_qubit(state, qubit, outcome)
            assert p == pytest.approx(prob, abs=TOL)
            assert np.allclose(collapsed, unnormalised / np.sqrt(prob), atol=TOL)
            assert np.linalg.norm(collapsed) == pytest.approx(1.0, abs=TOL)


def test_single_qubit_measurement_statistics_follow_born_rule():
    theta = 2 * np.arcsin(np.sqrt(0.3))  # P(1) = 0.3
    rng = np.random.default_rng(77)
    trials, ones = 20_000, 0
    template = QuantumSimulator(1)
    template.apply(gates.ry(theta), [0])
    for _ in range(trials):
        ones += template.copy().measure_qubit(0, rng=rng)
    assert abs(ones / trials - 0.3) < 5 * np.sqrt(0.3 * 0.7 / trials)


def test_measure_all_collapses_to_a_basis_state():
    for seed in range(10):
        sim = QuantumSimulator(3)
        for q in range(3):
            sim.apply(gates.HADAMARD, [q])
        index = sim.measure_all(rng=seed)
        assert 0 <= index < 8
        assert np.allclose(sim.state, basis(format(index, "03b")))
        assert sim.measure_all(rng=seed + 1) == index


def test_projective_measurement_is_reproducible_with_a_seed():
    def trajectory(seed):
        rng = np.random.default_rng(seed)
        sim = QuantumSimulator(3)
        out = []
        for q in range(3):
            sim.apply(gates.HADAMARD, [q])
            out.append(sim.measure_qubit(q, rng=rng))
        return out

    assert trajectory(5) == trajectory(5)
    assert len({tuple(trajectory(s)) for s in range(30)}) > 1


# ------------------------------------------------------------ invalid input
def test_projecting_onto_an_impossible_outcome_raises():
    sim = QuantumSimulator(1)
    with pytest.raises(ValueError, match="zero probability"):
        sim.project(0, 1)
    assert np.allclose(sim.state, basis("0"))


@pytest.mark.parametrize(
    "call",
    [
        lambda s: s.measure(0),
        lambda s: s.measure(-5),
        lambda s: s.sample_counts(0),
        lambda s: s.measure_qubit(2),
        lambda s: s.project(0, 2),
        lambda s: s.project(5, 0),
        lambda s: s.marginal_probabilities([]),
        lambda s: s.marginal_probabilities([0, 0]),
        lambda s: s.measure(10, rng=-1),
    ],
)
def test_invalid_measurement_arguments(call):
    with pytest.raises(ValueError):
        call(bell())


@pytest.mark.parametrize(
    "call",
    [
        lambda s: s.measure(10.5),
        lambda s: s.measure("10"),
        lambda s: s.measure(10, rng="seed"),
        lambda s: s.measure(10, rng=1.5),
    ],
)
def test_invalid_measurement_argument_types(call):
    with pytest.raises(TypeError):
        call(bell())


@pytest.mark.parametrize(
    "probs", [[0.5, 0.6], [0.2, 0.2], [1.5, -0.5], [np.nan, 1.0], []]
)
def test_sampler_rejects_invalid_distributions(probs):
    with pytest.raises(ValueError):
        measurement.sample_counts(probs, 10, rng=0)


def test_sampler_tolerates_rounding_error_in_probabilities():
    p = np.array([0.5, 0.5]) * (1 + 3e-12)
    assert measurement.sample_counts(p, 10, rng=0).sum() == 10


def test_state_length_must_be_a_power_of_two():
    with pytest.raises(ValueError):
        measurement.marginal_probabilities(np.ones(3) / np.sqrt(3), [0])
