import itertools

import numpy as np
import pytest

from quantum_lab import QuantumSimulator, gates, noise
from quantum_lab.circuit import Circuit
from quantum_lab.density import MAX_DENSITY_QUBITS, DensityMatrix, is_cptp
from quantum_lab.protocols import bell_circuit, ghz_circuit, teleportation_circuit
from quantum_lab.states import bloch_state, bloch_vector

from .helpers import TOL, random_state, random_unitary

PROBS = [0.0, 0.05, 0.3, 0.75, 1.0]


# ----------------------------------------------------------------- channels
@pytest.mark.parametrize("channel", noise.CHANNELS)
@pytest.mark.parametrize("p", PROBS)
def test_channels_are_trace_preserving(channel, p):
    kraus = noise.kraus_operators(channel, p)
    assert is_cptp(kraus)
    assert np.allclose(sum(k.conj().T @ k for k in kraus), np.eye(2), atol=TOL)


@pytest.mark.parametrize("p", PROBS)
def test_bit_flip_on_zero_state(p):
    rho = DensityMatrix(1)
    rho.apply_channel(noise.bit_flip_kraus(p), 0)
    assert rho.probabilities() == pytest.approx([1 - p, p], abs=TOL)
    assert bloch_vector(rho.matrix) == pytest.approx((0, 0, 1 - 2 * p), abs=TOL)


@pytest.mark.parametrize("p", PROBS)
def test_bit_flip_leaves_plus_state_invariant(p):
    rho = DensityMatrix(1)
    rho.apply(gates.HADAMARD, 0)
    rho.apply_channel(noise.bit_flip_kraus(p), 0)
    assert bloch_vector(rho.matrix) == pytest.approx((1, 0, 0), abs=TOL)
    assert rho.purity() == pytest.approx(1.0, abs=TOL)


@pytest.mark.parametrize("p", PROBS)
def test_phase_flip_shrinks_coherence_but_not_populations(p):
    rho = DensityMatrix(1)
    rho.apply(gates.HADAMARD, 0)
    rho.apply_channel(noise.phase_flip_kraus(p), 0)
    assert rho.probabilities() == pytest.approx([0.5, 0.5], abs=TOL)
    assert bloch_vector(rho.matrix) == pytest.approx((1 - 2 * p, 0, 0), abs=TOL)
    assert rho.purity() == pytest.approx((1 + (1 - 2 * p) ** 2) / 2, abs=TOL)


@pytest.mark.parametrize("p", PROBS)
def test_depolarizing_shrinks_bloch_vector_uniformly(p):
    theta, phi = 0.9, 2.2
    rho = DensityMatrix.from_statevector(bloch_state(theta, phi))
    before = bloch_vector(rho.matrix)
    rho.apply_channel(noise.depolarizing_kraus(p), 0)
    assert bloch_vector(rho.matrix) == pytest.approx((1 - 4 * p / 3) * before, abs=TOL)
    assert rho.trace() == pytest.approx(1.0, abs=TOL)


def test_depolarizing_three_quarters_is_maximally_mixed():
    rho = DensityMatrix.from_statevector(bloch_state(0.4, 1.0))
    rho.apply_channel(noise.depolarizing_kraus(0.75), 0)
    assert np.allclose(rho.matrix, np.eye(2) / 2, atol=TOL)
    assert rho.purity() == pytest.approx(0.5, abs=TOL)


@pytest.mark.parametrize("bad", [-0.1, 1.1, np.nan, np.inf])
def test_invalid_error_probability(bad):
    for channel in noise.CHANNELS:
        with pytest.raises(ValueError):
            noise.kraus_operators(channel, bad)
    with pytest.raises(ValueError):
        noise.simulate_density(bell_circuit(), noise.BIT_FLIP, bad)


def test_invalid_channel_and_probability_type():
    with pytest.raises(ValueError):
        noise.kraus_operators("amplitude_damping", 0.1)
    with pytest.raises(TypeError):
        noise.kraus_operators(noise.BIT_FLIP, "0.1")


# ----------------------------------------------------------- density matrix
@pytest.mark.parametrize("n", [1, 2, 3])
def test_noiseless_density_evolution_matches_state_vector(n):
    rng = np.random.default_rng(40 + n)
    sim, rho = QuantumSimulator(n), DensityMatrix(n)
    for _ in range(12):
        u = random_unitary(2, rng)
        q = int(rng.integers(n))
        sim.apply(u, [q])
        rho.apply(u, [q])
        if n > 1:
            c, t = (int(v) for v in rng.choice(n, size=2, replace=False))
            sim.cnot(c, t)
            rho.apply_controlled(gates.PAULI_X, [c], t)
    assert np.allclose(rho.matrix, np.outer(sim.state, sim.state.conj()), atol=1e-10)
    assert rho.probabilities() == pytest.approx(sim.get_probabilities(), abs=1e-10)
    assert rho.purity() == pytest.approx(1.0, abs=1e-10)
    assert rho.fidelity_with_pure(sim.state) == pytest.approx(1.0, abs=1e-10)
    for q in range(n):
        psi = sim.state.reshape((2,) * n)
        m = np.moveaxis(psi, q, 0).reshape(2, -1)
        assert np.allclose(rho.reduced(q), m @ m.conj().T, atol=1e-10)


def test_density_matrix_stays_physical_under_noise():
    rho = noise.simulate_density(ghz_circuit(3), noise.DEPOLARIZING, 0.2)
    m = rho.matrix
    assert np.allclose(m, m.conj().T, atol=TOL)
    assert rho.trace() == pytest.approx(1.0, abs=TOL)
    assert np.all(np.linalg.eigvalsh(m) > -1e-12)
    assert 1 / 8 <= rho.purity() < 1.0


def test_fidelity_properties():
    rng = np.random.default_rng(3)
    a, b = random_state(2, rng), random_state(2, rng)
    ra, rb = DensityMatrix.from_statevector(a), DensityMatrix.from_statevector(b)
    overlap = abs(np.vdot(a, b)) ** 2
    assert ra.fidelity(ra) == pytest.approx(1.0, abs=1e-7)
    assert ra.fidelity(rb) == pytest.approx(overlap, abs=1e-7)
    assert ra.fidelity(rb) == pytest.approx(rb.fidelity(ra), abs=1e-7)
    assert ra.fidelity_with_pure(b) == pytest.approx(overlap, abs=TOL)
    mixed = noise.simulate_density(bell_circuit(), noise.DEPOLARIZING, 0.1)
    ideal = noise.simulate_density(bell_circuit())
    pure = bell_circuit().run().simulator.state
    assert mixed.fidelity(ideal) == pytest.approx(mixed.fidelity_with_pure(pure), abs=1e-7)


def test_density_matrix_validation():
    with pytest.raises(ValueError):
        DensityMatrix(MAX_DENSITY_QUBITS + 1)
    rho = DensityMatrix(2)
    with pytest.raises(ValueError):
        rho.apply(2 * np.eye(2), 0)
    with pytest.raises(ValueError):
        rho.apply(gates.PAULI_X, 3)
    with pytest.raises(ValueError):
        rho.apply_channel([gates.PAULI_X, gates.PAULI_X], 0)  # not trace preserving
    with pytest.raises(ValueError):
        rho.project(0, 2)
    with pytest.raises(ValueError):
        DensityMatrix.from_statevector([1, 1])
    with pytest.raises(ValueError):
        rho.fidelity(DensityMatrix(1))


# ------------------------------------------------------- noisy circuit runs
@pytest.mark.parametrize("channel", noise.CHANNELS)
def test_zero_noise_equals_ideal(channel):
    circuit = ghz_circuit(3)
    ideal = circuit.run().simulator.state
    rho = noise.simulate_density(circuit, channel, 0.0)
    assert np.allclose(rho.matrix, np.outer(ideal, ideal.conj()), atol=1e-10)


def test_bell_state_under_bit_flip_matches_hand_calculation():
    # X after H leaves |+> alone; after the CNOT each qubit flips independently.
    p = 0.1
    rho = noise.simulate_density(bell_circuit(), noise.BIT_FLIP, p)
    odd = p * (1 - p)
    even = ((1 - p) ** 2 + p**2) / 2
    assert rho.probabilities() == pytest.approx([even, odd, odd, even], abs=TOL)


def test_bell_state_under_phase_flip_matches_hand_calculation():
    # Three Z-error locations; an odd number of flips turns Phi+ into Phi-.
    p = 0.1
    rho = noise.simulate_density(bell_circuit(), noise.PHASE_FLIP, p)
    ideal = bell_circuit().run().simulator.state
    assert rho.fidelity_with_pure(ideal) == pytest.approx((1 + (1 - 2 * p) ** 3) / 2, abs=TOL)
    assert rho.probabilities() == pytest.approx([0.5, 0, 0, 0.5], abs=TOL)


@pytest.mark.parametrize("channel", noise.CHANNELS)
def test_noisy_run_equals_exact_average_over_error_trajectories(channel):
    p = 0.15
    circuit = Circuit(2).gate("H", 0).cnot(0, 1).gate("T", 1)
    kraus = noise.kraus_operators(channel, p)
    locations = [q for op in circuit.ops for q in op.qubits]  # 1 + 2 + 1
    expected = np.zeros((4, 4), dtype=complex)
    for choice in itertools.product(range(len(kraus)), repeat=len(locations)):
        vec = np.zeros(4, dtype=complex)
        vec[0] = 1.0
        picks = iter(choice)
        for op in circuit.ops:
            u = gates.gate_matrix(op.name)
            if op.controls:
                vec = gates.cnot_matrix(op.controls[0], op.targets[0], 2) @ vec
            else:
                vec = gates.expand_gate(u, op.targets[0], 2) @ vec
            for q in op.qubits:  # unnormalised Kraus operator on that qubit
                k = kraus[next(picks)]
                full = np.kron(k, np.eye(2)) if q == 0 else np.kron(np.eye(2), k)
                vec = full @ vec
        expected += np.outer(vec, vec.conj())
    rho = noise.simulate_density(circuit, channel, p)
    assert np.allclose(rho.matrix, expected, atol=1e-10)


def test_more_noise_means_lower_fidelity_and_purity():
    ideal = bell_circuit().run().simulator.state
    for channel in noise.CHANNELS:
        fidelities, purities = [], []
        for p in (0.0, 0.02, 0.05, 0.1, 0.2):
            rho = noise.simulate_density(bell_circuit(), channel, p)
            fidelities.append(rho.fidelity_with_pure(ideal))
            purities.append(rho.purity())
        assert fidelities == sorted(fidelities, reverse=True)
        assert purities == sorted(purities, reverse=True)
        assert fidelities[0] == pytest.approx(1.0, abs=TOL)


def test_non_selective_measurement_dephases():
    rho = noise.simulate_density(Circuit(1).gate("H", 0).measure(0))
    assert np.allclose(rho.matrix, np.eye(2) / 2, atol=TOL)


def test_ideal_teleportation_ensemble_delivers_the_message():
    theta, phi = 1.3, 0.6
    rho = noise.simulate_density(teleportation_circuit(theta, phi))
    message = bloch_state(theta, phi)
    bob = rho.reduced(2)
    assert np.vdot(message, bob @ message).real == pytest.approx(1.0, abs=1e-10)
    noisy = noise.simulate_density(teleportation_circuit(theta, phi), noise.DEPOLARIZING, 0.05)
    bob_noisy = noisy.reduced(2)
    assert np.vdot(message, bob_noisy @ message).real < 0.99
    assert noisy.trace() == pytest.approx(1.0, abs=TOL)


def test_conditioned_gate_without_measurement_is_rejected():
    with pytest.raises(ValueError, match="has not been measured"):
        noise.simulate_density(Circuit(2).gate("X", 1, condition=0))
