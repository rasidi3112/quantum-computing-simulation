import numpy as np
import pytest

from quantum_lab import protocols
from quantum_lab.states import bloch_state, entanglement_entropy, qubit_bloch_vector

from .helpers import TOL, basis

SQRT2 = np.sqrt(2)

EXPECTED_BELL = {
    "Φ+": (basis("00") + basis("11")) / SQRT2,
    "Φ-": (basis("00") - basis("11")) / SQRT2,
    "Ψ+": (basis("01") + basis("10")) / SQRT2,
    "Ψ-": (basis("01") - basis("10")) / SQRT2,
}


@pytest.mark.parametrize("kind", list(EXPECTED_BELL))
def test_bell_states(kind):
    sim = protocols.bell_circuit(kind).run().simulator
    # equal up to a global phase
    assert abs(np.vdot(EXPECTED_BELL[kind], sim.state)) == pytest.approx(1.0, abs=TOL)
    assert entanglement_entropy(sim.state, [0]) == pytest.approx(1.0, abs=1e-9)
    for q in (0, 1):
        assert qubit_bloch_vector(sim.state, q) == pytest.approx((0, 0, 0), abs=TOL)


def test_phi_plus_is_exact_and_has_required_probabilities():
    sim = protocols.bell_circuit("Φ+").run().simulator
    assert np.allclose(sim.state, EXPECTED_BELL["Φ+"], atol=TOL)
    p00, p01, p10, p11 = sim.get_probabilities()
    assert p00 == pytest.approx(0.5, abs=TOL)
    assert p11 == pytest.approx(0.5, abs=TOL)
    assert p01 == pytest.approx(0.0, abs=TOL)
    assert p10 == pytest.approx(0.0, abs=TOL)


def test_bell_states_are_mutually_orthogonal():
    vectors = [protocols.bell_circuit(k).run().simulator.state for k in EXPECTED_BELL]
    gram = np.abs(np.array([[np.vdot(a, b) for b in vectors] for a in vectors]))
    assert np.allclose(gram, np.eye(4), atol=TOL)


@pytest.mark.parametrize("kind, same", [("Φ+", True), ("Φ-", True), ("Ψ+", False), ("Ψ-", False)])
def test_bell_measurement_correlations(kind, same):
    for seed in range(15):
        circuit = protocols.bell_circuit(kind).measure(0).measure(1)
        outcomes = circuit.run(rng=seed).outcomes
        assert (outcomes[0] == outcomes[1]) is same


@pytest.mark.parametrize("n", [2, 3, 5])
def test_ghz_state(n):
    sim = protocols.ghz_circuit(n).run().simulator
    expected = (basis("0" * n) + basis("1" * n)) / SQRT2
    assert np.allclose(sim.state, expected, atol=TOL)


def test_invalid_protocol_arguments():
    with pytest.raises(ValueError):
        protocols.bell_circuit("Ω")
    with pytest.raises(ValueError):
        protocols.ghz_circuit(1)
    with pytest.raises(ValueError):
        protocols.run_teleportation(np.nan, 0.0)


# ------------------------------------------------------------ teleportation
ANGLES = [(0.0, 0.0), (np.pi, 0.0), (np.pi / 2, 0.0), (np.pi / 2, np.pi / 2),
          (1.1, 2.3), (2.7, -1.9), (0.3, 5.5)]


@pytest.mark.parametrize("theta, phi", ANGLES)
@pytest.mark.parametrize("m0, m1", [(0, 0), (0, 1), (1, 0), (1, 1)])
def test_teleportation_has_unit_fidelity_in_every_branch(theta, phi, m0, m1):
    result = protocols.run_teleportation(theta, phi, forced={0: m0, 1: m1})
    assert result.outcomes == (m0, m1)
    assert result.fidelity == pytest.approx(1.0, abs=1e-10)
    assert result.bob_bloch == pytest.approx(result.message_bloch, abs=1e-10)
    assert np.allclose(result.message, bloch_state(theta, phi))
    # Bob's qubit ends up pure (disentangled from Alice's measured qubits)
    assert np.linalg.norm(result.bob_bloch) == pytest.approx(1.0, abs=1e-10)


def test_each_teleportation_outcome_has_probability_one_quarter():
    circuit = protocols.teleportation_circuit(1.1, 2.3)
    counts = {}
    rng = np.random.default_rng(2)
    for _ in range(4000):
        outcomes = circuit.run(rng=rng).outcomes
        key = (outcomes[0], outcomes[1])
        counts[key] = counts.get(key, 0) + 1
    assert set(counts) == {(0, 0), (0, 1), (1, 0), (1, 1)}
    for value in counts.values():
        assert abs(value - 1000) < 5 * np.sqrt(4000 * 0.25 * 0.75)


def test_corrections_are_necessary():
    # Without the fix-up gates only the (0, 0) branch already holds the message.
    theta, phi = 1.1, 2.3
    message = bloch_state(theta, phi)
    for m0, m1 in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        result = protocols.run_teleportation(theta, phi, forced={0: m0, 1: m1})
        before = np.vdot(message, result.bob_before_correction @ message).real
        if (m0, m1) == (0, 0):
            assert before == pytest.approx(1.0, abs=1e-10)
        else:
            assert before < 0.9


def test_teleportation_is_reproducible_with_a_seed():
    a = protocols.run_teleportation(0.8, 1.0, rng=99)
    b = protocols.run_teleportation(0.8, 1.0, rng=99)
    assert a.outcomes == b.outcomes
    assert a.fidelity == pytest.approx(1.0, abs=1e-10)
    seen = {protocols.run_teleportation(0.8, 1.0, rng=s).outcomes for s in range(40)}
    assert len(seen) == 4


def test_bob_learns_nothing_before_the_classical_bits_arrive():
    # Averaged over Alice's outcomes, Bob's uncorrected qubit is maximally mixed.
    theta, phi = 1.1, 2.3
    average = np.zeros((2, 2), dtype=complex)
    for m0 in (0, 1):
        for m1 in (0, 1):
            result = protocols.run_teleportation(theta, phi, forced={0: m0, 1: m1})
            average += result.bob_before_correction / 4
    assert np.allclose(average, np.eye(2) / 2, atol=1e-10)
