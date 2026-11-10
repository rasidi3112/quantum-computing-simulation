"""Reduced states, Bloch vectors, purity and entanglement entropy."""

import numpy as np
import pytest

from quantum_lab import QuantumSimulator, gates, states

from .helpers import TOL, basis, random_state

SQRT2 = np.sqrt(2)


def test_basis_labels_are_big_endian_bit_strings():
    assert states.basis_labels(1) == ["0", "1"]
    assert states.basis_labels(2) == ["00", "01", "10", "11"]
    assert states.basis_labels(3)[5] == "101"


@pytest.mark.parametrize(
    "ops, expected",
    [
        ([], (0, 0, 1)),  # |0>
        (["X"], (0, 0, -1)),  # |1>
        (["H"], (1, 0, 0)),  # |+>
        (["X", "H"], (-1, 0, 0)),  # |->
        (["H", "S"], (0, 1, 0)),  # |+i>
        (["H", "S", "Z"], (0, -1, 0)),  # |-i>
        (["H", "T"], (1 / SQRT2, 1 / SQRT2, 0)),
    ],
)
def test_bloch_vector_of_cardinal_states(ops, expected):
    sim = QuantumSimulator(1)
    for gate_id in ops:
        sim.apply(gates.gate_matrix(gate_id), [0])
    assert states.qubit_bloch_vector(sim.state, 0) == pytest.approx(expected, abs=TOL)


def test_bloch_state_matches_spherical_coordinates():
    theta, phi = 1.2, -0.7
    r = states.bloch_vector(np.outer(states.bloch_state(theta, phi),
                                     states.bloch_state(theta, phi).conj()))
    expected = [np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)]
    assert r == pytest.approx(expected, abs=TOL)
    assert np.linalg.norm(r) == pytest.approx(1.0, abs=TOL)


def test_product_state_qubits_have_unit_bloch_vectors():
    sim = QuantumSimulator(3)  # |1> |+> |0>
    sim.apply(gates.PAULI_X, [0])
    sim.apply(gates.HADAMARD, [1])
    assert states.qubit_bloch_vector(sim.state, 0) == pytest.approx((0, 0, -1), abs=TOL)
    assert states.qubit_bloch_vector(sim.state, 1) == pytest.approx((1, 0, 0), abs=TOL)
    assert states.qubit_bloch_vector(sim.state, 2) == pytest.approx((0, 0, 1), abs=TOL)


def test_entangled_qubits_have_zero_bloch_vector_and_mixed_reduced_state():
    bell = (basis("00") + basis("11")) / SQRT2
    for q in (0, 1):
        rho = states.reduced_density_matrix(bell, [q])
        assert np.allclose(rho, np.eye(2) / 2, atol=TOL)
        assert states.bloch_vector(rho) == pytest.approx((0, 0, 0), abs=TOL)
        assert states.purity(rho) == pytest.approx(0.5, abs=TOL)
        assert states.entanglement_entropy(bell, [q]) == pytest.approx(1.0, abs=1e-9)


def test_partially_entangled_state():
    # cos(a)|00> + sin(a)|11>: <Z> = cos(2a), entropy = H2(cos^2 a)
    a = 0.4
    state = np.cos(a) * basis("00") + np.sin(a) * basis("11")
    r = states.qubit_bloch_vector(state, 0)
    assert r == pytest.approx((0, 0, np.cos(2 * a)), abs=TOL)
    p = np.cos(a) ** 2
    entropy = -p * np.log2(p) - (1 - p) * np.log2(1 - p)
    assert states.entanglement_entropy(state, [0]) == pytest.approx(entropy, abs=1e-9)


def test_reduced_density_matrix_properties_on_random_states():
    rng = np.random.default_rng(8)
    state = random_state(4, rng)
    for qubits in ([0], [3], [1, 2], [2, 0], [0, 1, 3]):
        rho = states.reduced_density_matrix(state, qubits)
        assert rho.shape == (2 ** len(qubits),) * 2
        assert np.allclose(rho, rho.conj().T, atol=TOL)
        assert np.trace(rho).real == pytest.approx(1.0, abs=TOL)
        assert np.all(np.linalg.eigvalsh(rho) > -1e-12)
    # tracing nothing out gives the projector
    full = states.reduced_density_matrix(state, [0, 1, 2, 3])
    assert np.allclose(full, np.outer(state, state.conj()), atol=TOL)
    # complementary subsystems of a pure state have equal entropy
    assert states.entanglement_entropy(state, [0, 2]) == pytest.approx(
        states.entanglement_entropy(state, [1, 3]), abs=1e-9
    )


def test_reduced_density_matrix_respects_argument_order():
    state = basis("10")
    assert np.allclose(np.diag(states.reduced_density_matrix(state, [0, 1])).real, [0, 0, 1, 0])
    assert np.allclose(np.diag(states.reduced_density_matrix(state, [1, 0])).real, [0, 1, 0, 0])


def test_product_state_has_zero_entropy():
    sim = QuantumSimulator(2)
    sim.apply(gates.HADAMARD, [0])
    sim.apply(gates.T_GATE, [0])
    assert states.entanglement_entropy(sim.state, [0]) == pytest.approx(0.0, abs=1e-9)


def test_invalid_arguments():
    with pytest.raises(ValueError):
        states.bloch_vector(np.eye(4))
    with pytest.raises(ValueError):
        states.reduced_density_matrix(basis("00"), [])
    with pytest.raises(ValueError):
        states.reduced_density_matrix(basis("00"), [2])
