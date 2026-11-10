"""State-vector simulator: state handling, gate behaviour, qubit ordering."""

import numpy as np
import pytest

from quantum_lab import MAX_QUBITS, QuantumSimulator, gates

from .helpers import TOL, basis, random_state, random_unitary

SQRT2 = np.sqrt(2)


def run(n, *ops, start=None):
    """Apply ``(gate_id, target)`` or ``("CNOT", control, target)`` tuples."""
    sim = QuantumSimulator(n)
    if start is not None:
        sim.set_state(start)
    for op in ops:
        if op[0] == "CNOT":
            sim.cnot(op[1], op[2])
        else:
            sim.apply(gates.gate_matrix(op[0]), [op[1]])
    return sim


# ------------------------------------------------------------- state & norm
@pytest.mark.parametrize("n", [1, 2, 3, 5])
def test_initial_state_is_all_zeros_and_normalised(n):
    sim = QuantumSimulator(n)
    assert sim.dim == 2**n
    assert sim.state.dtype == np.complex128
    assert np.allclose(sim.state, basis("0" * n))
    assert sim.norm() == pytest.approx(1.0, abs=TOL)
    assert sim.get_probabilities().sum() == pytest.approx(1.0, abs=TOL)


def test_normalisation_is_preserved_by_every_gate():
    rng = np.random.default_rng(1)
    sim = QuantumSimulator(3)
    sim.set_state(random_state(3, rng))
    for gate_id in gates.GATES:
        for q in range(3):
            sim.apply(gates.gate_matrix(gate_id), [q])
            assert sim.get_probabilities().sum() == pytest.approx(1.0, abs=TOL)
    for c, t in [(0, 1), (1, 2), (2, 0)]:
        sim.cnot(c, t)
        assert sim.get_probabilities().sum() == pytest.approx(1.0, abs=TOL)


def test_no_numerical_drift_over_a_long_circuit():
    # 3000 random gates without any renormalisation step.
    rng = np.random.default_rng(7)
    sim = QuantumSimulator(4)
    ids = list(gates.GATES)
    for _ in range(3000):
        if rng.random() < 0.25:
            c, t = rng.choice(4, size=2, replace=False)
            sim.cnot(int(c), int(t))
        else:
            sim.apply(gates.gate_matrix(ids[rng.integers(len(ids))]), [int(rng.integers(4))])
    assert sim.norm() == pytest.approx(1.0, abs=1e-10)


def test_reset_and_copy():
    sim = run(2, ("H", 0), ("CNOT", 0, 1))
    clone = sim.copy()
    sim.reset()
    assert np.allclose(sim.state, basis("00"))
    assert np.allclose(clone.state, (basis("00") + basis("11")) / SQRT2)


def test_state_is_read_only_and_amplitudes_are_copies():
    sim = QuantumSimulator(1)
    with pytest.raises(ValueError):
        sim.state[0] = 0
    amplitudes = sim.get_amplitudes()
    amplitudes[0] = 0
    assert np.allclose(sim.state, basis("0"))


def test_set_state_validation():
    sim = QuantumSimulator(2)
    sim.set_state([0, 1, 0, 0])
    assert np.allclose(sim.state, basis("01"))
    sim.state = np.array([0, 0, 0, 1j])
    assert np.allclose(sim.state, 1j * basis("11"))
    sim.set_state([3, 0, 4, 0], normalize=True)
    assert np.allclose(sim.state, [0.6, 0, 0.8, 0])
    with pytest.raises(ValueError):
        sim.set_state([1, 0])  # wrong length
    with pytest.raises(ValueError):
        sim.set_state([1, 1, 0, 0])  # not normalised
    with pytest.raises(ValueError):
        sim.set_state([0, 0, 0, 0], normalize=True)
    with pytest.raises(ValueError):
        sim.set_state([np.nan, 0, 0, 0])


# ------------------------------------------------------ single-qubit gates
def test_pauli_x_flips_basis_states():
    assert np.allclose(run(1, ("X", 0)).state, basis("1"))
    assert np.allclose(run(1, ("X", 0), ("X", 0)).state, basis("0"))


def test_pauli_y_behaviour():
    assert np.allclose(run(1, ("Y", 0)).state, 1j * basis("1"))  # Y|0> = i|1>
    assert np.allclose(run(1, ("X", 0), ("Y", 0)).state, -1j * basis("0"))  # Y|1> = -i|0>


def test_pauli_z_behaviour():
    assert np.allclose(run(1, ("Z", 0)).state, basis("0"))  # Z|0> = |0>
    assert np.allclose(run(1, ("X", 0), ("Z", 0)).state, -basis("1"))  # Z|1> = -|1>
    # Z|+> = |->
    assert np.allclose(run(1, ("H", 0), ("Z", 0)).state, np.array([1, -1]) / SQRT2)


def test_hadamard_creates_equal_superposition():
    plus = run(1, ("H", 0))
    assert np.allclose(plus.state, np.array([1, 1]) / SQRT2)
    assert np.allclose(plus.get_probabilities(), [0.5, 0.5], atol=TOL)
    minus = run(1, ("X", 0), ("H", 0))
    assert np.allclose(minus.state, np.array([1, -1]) / SQRT2)


def test_hadamard_twice_is_identity():
    rng = np.random.default_rng(3)
    for n in (1, 2, 3):
        start = random_state(n, rng)
        for q in range(n):
            assert np.allclose(run(n, ("H", q), ("H", q), start=start).state, start, atol=TOL)


def test_phase_gates():
    assert np.allclose(run(1, ("X", 0), ("S", 0)).state, 1j * basis("1"))
    assert np.allclose(
        run(1, ("X", 0), ("T", 0)).state, np.exp(1j * np.pi / 4) * basis("1")
    )
    # H Z H = X  (experiment 3 of the original usage notes)
    assert np.allclose(run(1, ("H", 0), ("Z", 0), ("H", 0)).state, basis("1"))


def test_identity_leaves_state_unchanged():
    start = random_state(2, np.random.default_rng(5))
    assert np.allclose(run(2, ("I", 0), ("I", 1), start=start).state, start)


# -------------------------------------------------- ordering & multi-qubit
def test_qubit_zero_is_the_leftmost_bit():
    assert np.allclose(run(2, ("X", 0)).state, basis("10"))
    assert np.allclose(run(2, ("X", 1)).state, basis("01"))
    assert np.allclose(run(3, ("X", 0)).state, basis("100"))
    assert np.allclose(run(3, ("X", 2)).state, basis("001"))
    assert np.allclose(run(3, ("X", 0), ("X", 2)).state, basis("101"))


@pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
def test_single_qubit_gate_matches_dense_expansion(n):
    rng = np.random.default_rng(100 + n)
    for target in range(n):
        u = random_unitary(2, rng)
        start = random_state(n, rng)
        sim = QuantumSimulator(n)
        sim.set_state(start)
        sim.apply(u, [target])
        assert np.allclose(sim.state, gates.expand_gate(u, target, n) @ start, atol=TOL)
        assert np.allclose(sim.state, sim._expand_gate(u, target) @ start, atol=TOL)


def test_two_qubit_gate_on_arbitrary_qubits_matches_kron():
    rng = np.random.default_rng(11)
    u = random_unitary(4, rng)
    start = random_state(3, rng)
    eye = np.eye(2)
    # adjacent pairs can be written directly as Kronecker products
    for qubits, dense in [([0, 1], np.kron(u, eye)), ([1, 2], np.kron(eye, u))]:
        sim = QuantumSimulator(3)
        sim.set_state(start)
        sim.apply(u, qubits)
        assert np.allclose(sim.state, dense @ start, atol=TOL)
    # reversed qubit list == conjugating the matrix with SWAP
    swap = np.eye(4)[[0, 2, 1, 3]]
    a, b = QuantumSimulator(3), QuantumSimulator(3)
    a.set_state(start)
    b.set_state(start)
    a.apply(u, [1, 0])
    b.apply(swap @ u @ swap, [0, 1])
    assert np.allclose(a.state, b.state, atol=TOL)


def test_product_state_is_kron_of_single_qubit_states():
    plus = np.array([1, 1]) / SQRT2
    one = np.array([0, 1])
    sim = run(3, ("H", 0), ("X", 1))
    assert np.allclose(sim.state, np.kron(np.kron(plus, one), [1, 0]))


# --------------------------------------------------------------------- CNOT
@pytest.mark.parametrize(
    "start, expected",
    [("00", "00"), ("01", "01"), ("10", "11"), ("11", "10")],
)
def test_cnot_truth_table_control0_target1(start, expected):
    sim = QuantumSimulator(2)
    sim.set_state(basis(start))
    sim.cnot(0, 1)
    assert np.allclose(sim.state, basis(expected))


@pytest.mark.parametrize(
    "start, expected",
    [("00", "00"), ("01", "11"), ("10", "10"), ("11", "01")],
)
def test_cnot_truth_table_control1_target0(start, expected):
    sim = QuantumSimulator(2)
    sim.set_state(basis(start))
    sim.cnot(1, 0)
    assert np.allclose(sim.state, basis(expected))


def test_cnot_on_non_adjacent_qubits():
    assert np.allclose(run(3, ("X", 0), ("CNOT", 0, 2)).state, basis("101"))
    assert np.allclose(run(3, ("X", 2), ("CNOT", 2, 0)).state, basis("101"))
    assert np.allclose(run(3, ("X", 1), ("CNOT", 0, 2)).state, basis("010"))


@pytest.mark.parametrize("n", [2, 3, 4])
def test_cnot_matches_dense_matrix_for_every_pair(n):
    rng = np.random.default_rng(200 + n)
    for control in range(n):
        for target in range(n):
            if control == target:
                continue
            start = random_state(n, rng)
            sim = QuantumSimulator(n)
            sim.set_state(start)
            sim.cnot(control, target)
            assert np.allclose(sim.state, gates.cnot_matrix(control, target, n) @ start)
            assert np.allclose(sim.state, sim._create_cnot_matrix(control, target) @ start)


def test_controlled_gate_with_several_controls():
    rng = np.random.default_rng(21)
    u = random_unitary(2, rng)
    start = random_state(4, rng)
    for controls, target in [([0, 1], 3), ([3, 1], 0), ([0, 2, 3], 1)]:
        sim = QuantumSimulator(4)
        sim.set_state(start)
        sim.apply_controlled(u, controls, target)
        ref = QuantumSimulator(4)
        ref.set_state(start)
        ref.apply(gates.controlled_matrix(u, len(controls)), [*controls, target])
        assert np.allclose(sim.state, ref.state, atol=TOL)
    toffoli = QuantumSimulator(3)
    toffoli.set_state(basis("110"))
    toffoli.apply_controlled(gates.PAULI_X, [0, 1], 2)
    assert np.allclose(toffoli.state, basis("111"))


# --------------------------------------------------------------- Bell state
def test_bell_state_generation():
    sim = run(2, ("H", 0), ("CNOT", 0, 1))
    expected = (basis("00") + basis("11")) / SQRT2
    assert np.allclose(sim.state, expected, atol=TOL)
    p = dict(zip(["00", "01", "10", "11"], sim.get_probabilities()))
    assert p["00"] == pytest.approx(0.5, abs=TOL)
    assert p["11"] == pytest.approx(0.5, abs=TOL)
    assert p["01"] == pytest.approx(0.0, abs=TOL)
    assert p["10"] == pytest.approx(0.0, abs=TOL)


def test_bell_state_via_legacy_apply_gate_api():
    # Exactly the calls made by Mini Quantum Lab 1.0's user interface.
    sim = QuantumSimulator(2)
    sim.apply_gate(gates.HADAMARD, 0)
    sim.apply_gate(gates.IDENTITY, 1, 0)
    assert np.allclose(sim.state, (basis("00") + basis("11")) / SQRT2, atol=TOL)


def test_ghz_state():
    sim = run(3, ("H", 0), ("CNOT", 0, 1), ("CNOT", 1, 2))
    assert np.allclose(sim.state, (basis("000") + basis("111")) / SQRT2, atol=TOL)


# ------------------------------------------------------------ invalid input
@pytest.mark.parametrize("n", [0, -1, MAX_QUBITS + 1])
def test_invalid_register_size(n):
    with pytest.raises(ValueError):
        QuantumSimulator(n)


@pytest.mark.parametrize("n", [1.5, "2", None, True])
def test_non_integer_register_size(n):
    with pytest.raises(TypeError):
        QuantumSimulator(n)


@pytest.mark.parametrize(
    "call",
    [
        lambda s: s.apply(gates.PAULI_X, [2]),
        lambda s: s.apply(gates.PAULI_X, [-1]),
        lambda s: s.apply(gates.PAULI_X, []),
        lambda s: s.apply(gates.PAULI_X, [0, 1]),  # 2 qubits need a 4x4 matrix
        lambda s: s.apply(gates.CNOT, [0]),
        lambda s: s.apply(gates.CNOT, [0, 0]),
        lambda s: s.apply(2 * gates.IDENTITY, [0]),  # not unitary
        lambda s: s.apply(np.array([[1, 1], [1, 1]]), [0]),
        lambda s: s.cnot(0, 0),
        lambda s: s.cnot(0, 2),
        lambda s: s.apply_controlled(gates.CNOT, [0], 1),
        lambda s: s.apply_controlled(np.zeros((2, 2)), [0], 1),
        lambda s: s.apply_gate(gates.IDENTITY, 0, 0),
    ],
)
def test_invalid_operations_raise_and_leave_state_untouched(call):
    sim = QuantumSimulator(2)
    sim.apply(gates.HADAMARD, [0])
    before = sim.get_amplitudes()
    with pytest.raises(ValueError):
        call(sim)
    assert np.allclose(sim.state, before)


def test_non_integer_qubit_raises_type_error():
    with pytest.raises(TypeError):
        QuantumSimulator(2).apply(gates.PAULI_X, [0.0])
