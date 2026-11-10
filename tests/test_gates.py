"""Gate matrices: definitions, unitarity and dense expansions."""

import numpy as np
import pytest

from quantum_lab import gates

from .helpers import TOL, random_unitary

FIXED = {
    "I": gates.IDENTITY,
    "X": gates.PAULI_X,
    "Y": gates.PAULI_Y,
    "Z": gates.PAULI_Z,
    "H": gates.HADAMARD,
    "S": gates.S_GATE,
    "T": gates.T_GATE,
    "CNOT": gates.CNOT,
}


@pytest.mark.parametrize("name", FIXED)
def test_fixed_gates_are_unitary(name):
    u = FIXED[name]
    assert np.allclose(u.conj().T @ u, np.eye(u.shape[0]), atol=TOL)
    assert gates.is_unitary(u)


@pytest.mark.parametrize("factory", [gates.rx, gates.ry, gates.rz, gates.phase])
@pytest.mark.parametrize("angle", [0.0, 0.3, np.pi / 2, np.pi, -2.1, 7.0])
def test_parametric_gates_are_unitary(factory, angle):
    assert gates.is_unitary(factory(angle))


def test_registry_gates_are_unitary_and_complete():
    assert set(gates.GATES) == {"I", "X", "Y", "Z", "H", "S", "T"}
    for spec in gates.GATES.values():
        assert spec.matrix.shape == (2, 2)
        assert gates.is_unitary(spec.matrix)


def test_gate_definitions():
    assert np.allclose(gates.PAULI_X, [[0, 1], [1, 0]])
    assert np.allclose(gates.PAULI_Y, [[0, -1j], [1j, 0]])
    assert np.allclose(gates.PAULI_Z, [[1, 0], [0, -1]])
    assert np.allclose(gates.HADAMARD, np.array([[1, 1], [1, -1]]) / np.sqrt(2))
    assert np.allclose(gates.S_GATE, np.diag([1, 1j]))
    assert np.allclose(gates.T_GATE, np.diag([1, np.exp(1j * np.pi / 4)]))


def test_algebraic_identities():
    x, y, z, h, s, t = (FIXED[k] for k in "XYZHST")
    eye = np.eye(2)
    for pauli in (x, y, z, h):
        assert np.allclose(pauli @ pauli, eye, atol=TOL)  # involutions
    assert np.allclose(s @ s, z, atol=TOL)
    assert np.allclose(t @ t, s, atol=TOL)
    assert np.allclose(x @ y, 1j * z, atol=TOL)
    assert np.allclose(h @ z @ h, x, atol=TOL)
    assert np.allclose(h @ x @ h, z, atol=TOL)
    assert np.allclose(-1j * x @ y @ z, eye, atol=TOL)


def test_rotations_match_paulis_up_to_global_phase():
    assert np.allclose(gates.rx(np.pi), -1j * gates.PAULI_X, atol=TOL)
    assert np.allclose(gates.ry(np.pi), -1j * gates.PAULI_Y, atol=TOL)
    assert np.allclose(gates.rz(np.pi), -1j * gates.PAULI_Z, atol=TOL)
    assert np.allclose(gates.phase(np.pi / 2), gates.S_GATE, atol=TOL)
    assert np.allclose(gates.phase(np.pi / 4), gates.T_GATE, atol=TOL)


def test_is_unitary_rejects_bad_matrices():
    assert not gates.is_unitary(2 * gates.IDENTITY)
    assert not gates.is_unitary(np.array([[1, 1], [0, 1]]))
    assert not gates.is_unitary(np.ones((2, 3)))
    assert not gates.is_unitary(np.array([[np.nan, 0], [0, 1]]))
    assert not gates.is_unitary(np.zeros(4))


def test_fixed_matrices_are_read_only():
    with pytest.raises(ValueError):
        gates.PAULI_X[0, 0] = 1


def test_gate_matrix_lookup():
    assert np.allclose(gates.gate_matrix("H"), gates.HADAMARD)
    assert np.allclose(gates.gate_matrix("RY", [0.4]), gates.ry(0.4))
    with pytest.raises(ValueError):
        gates.gate_matrix("H", [0.1])
    with pytest.raises(ValueError):
        gates.gate_matrix("RX")
    with pytest.raises(ValueError):
        gates.gate_matrix("RX", [np.inf])
    with pytest.raises(ValueError):
        gates.gate_matrix("NOPE")


# ------------------------------------------------------------ dense expansion
def test_expand_gate_is_kron_in_big_endian_order():
    x, eye = gates.PAULI_X, gates.IDENTITY
    assert np.allclose(gates.expand_gate(x, 0, 2), np.kron(x, eye))
    assert np.allclose(gates.expand_gate(x, 1, 2), np.kron(eye, x))
    assert np.allclose(gates.expand_gate(x, 1, 3), np.kron(np.kron(eye, x), eye))
    assert np.allclose(gates.expand_gate(x, 0, 1), x)


@pytest.mark.parametrize("n", [1, 2, 3, 4])
def test_expanded_gates_are_unitary(n):
    rng = np.random.default_rng(n)
    for target in range(n):
        assert gates.is_unitary(gates.expand_gate(random_unitary(2, rng), target, n))


def test_two_qubit_cnot_matrices():
    assert np.allclose(gates.cnot_matrix(0, 1, 2), gates.CNOT)
    reversed_cnot = [[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]]
    assert np.allclose(gates.cnot_matrix(1, 0, 2), reversed_cnot)


@pytest.mark.parametrize("n", [2, 3, 4])
def test_cnot_matrix_truth_table_every_pair(n):
    for control in range(n):
        for target in range(n):
            if control == target:
                continue
            m = gates.cnot_matrix(control, target, n)
            assert gates.is_unitary(m)
            assert np.allclose(m @ m, np.eye(2**n))  # self-inverse
            for index in range(2**n):
                bits = [int(b) for b in format(index, f"0{n}b")]
                bits[target] ^= bits[control]
                expected = int("".join(map(str, bits)), 2)
                assert m[expected, index] == 1


def test_cnot_equals_projector_decomposition():
    # CNOT = |0><0| (x) I + |1><1| (x) X, embedded with expand_gate (big-endian).
    p0, p1 = np.diag([1, 0]).astype(complex), np.diag([0, 1]).astype(complex)
    for control, target, n in [(0, 1, 2), (1, 0, 2), (0, 2, 3), (2, 0, 3), (1, 3, 4)]:
        def embed(op, qubit, n=n):
            mats = [op if q == qubit else gates.IDENTITY for q in range(n)]
            out = np.eye(1)
            for m in mats:
                out = np.kron(out, m)
            return out

        expected = embed(p0, control) + embed(p1, control) @ embed(gates.PAULI_X, target)
        assert np.allclose(gates.cnot_matrix(control, target, n), expected)


def test_controlled_matrix():
    assert np.allclose(gates.controlled_matrix(gates.PAULI_X), gates.CNOT)
    toffoli = gates.controlled_matrix(gates.PAULI_X, 2)
    assert toffoli.shape == (8, 8)
    expected = np.eye(8)
    expected[[6, 7]] = expected[[7, 6]]
    assert np.allclose(toffoli, expected)
    assert np.allclose(gates.controlled_matrix(gates.HADAMARD, 0), gates.HADAMARD)


@pytest.mark.parametrize(
    "call",
    [
        lambda: gates.expand_gate(gates.PAULI_X, 2, 2),
        lambda: gates.expand_gate(gates.PAULI_X, -1, 2),
        lambda: gates.expand_gate(gates.CNOT, 0, 2),
        lambda: gates.cnot_matrix(0, 0, 2),
        lambda: gates.cnot_matrix(0, 3, 3),
        lambda: gates.validate_qubits([0, 0], 2),
        lambda: gates.controlled_matrix(gates.PAULI_X, -1),
    ],
)
def test_invalid_arguments_raise_value_error(call):
    with pytest.raises(ValueError):
        call()


@pytest.mark.parametrize("bad", [1.0, "0", None, True])
def test_non_integer_qubit_index_raises_type_error(bad):
    with pytest.raises(TypeError):
        gates.validate_qubits([bad], 2)
