import numpy as np
import pytest

from quantum_lab import gates
from quantum_lab.circuit import GATE, MEASURE, Circuit, Operation

from .helpers import TOL, basis

SQRT2 = np.sqrt(2)


def test_run_matches_direct_simulation():
    result = Circuit(2).gate("H", 0).cnot(0, 1).run()
    assert np.allclose(result.simulator.state, (basis("00") + basis("11")) / SQRT2, atol=TOL)
    assert result.outcomes == {}


def test_parametric_and_controlled_gates():
    sim = Circuit(1).gate("RY", 0, params=[np.pi]).run().simulator
    assert np.allclose(np.abs(sim.state), [0, 1], atol=TOL)
    sim = Circuit(3).gate("X", 0).gate("X", 1).gate("X", 2, controls=[0, 1]).run().simulator
    assert np.allclose(sim.state, basis("111"))


def test_unitary_box():
    swap = np.eye(4)[[0, 2, 1, 3]]
    sim = Circuit(2).gate("X", 0).unitary("SWAP", [0, 1], swap).run().simulator
    assert np.allclose(sim.state, basis("01"))


def test_measurement_outcomes_are_recorded_and_seeded():
    circuit = Circuit(2).gate("H", 0).cnot(0, 1).measure(0).measure(1)
    a, b = circuit.run(rng=11), circuit.run(rng=11)
    assert a.outcomes == b.outcomes
    assert a.outcomes[0] == a.outcomes[1]  # Bell correlations
    recorded = [op.outcome for op in a.circuit.ops if op.kind == MEASURE]
    assert recorded == [a.outcomes[0], a.outcomes[1]]
    # the template circuit itself is not modified
    assert all(op.outcome is None for op in circuit.ops if op.kind == MEASURE)
    assert {circuit.run(rng=s).outcomes[0] for s in range(30)} == {0, 1}


def test_forced_outcomes_post_select():
    circuit = Circuit(2).gate("H", 0).cnot(0, 1).measure(0)
    for bit in (0, 1):
        result = circuit.run(forced={0: bit})
        assert result.outcomes == {0: bit}
        assert np.allclose(result.simulator.state, basis(f"{bit}{bit}"))
    with pytest.raises(ValueError, match="zero probability"):
        Circuit(1).measure(0).run(forced={0: 1})


def test_classically_conditioned_gate():
    circuit = Circuit(2).gate("H", 0).measure(0).gate("X", 1, condition=0)
    for bit in (0, 1):
        sim = circuit.run(forced={0: bit}).simulator
        assert np.allclose(sim.state, basis(f"{bit}{bit}"))
    with pytest.raises(ValueError, match="has not been measured"):
        Circuit(2).gate("X", 1, condition=0).run()


def test_initial_state():
    sim = Circuit(1).gate("X", 0).run(initial_state=basis("1")).simulator
    assert np.allclose(sim.state, basis("0"))


@pytest.mark.parametrize(
    "build",
    [
        lambda c: c.gate("H", 2),
        lambda c: c.gate("NOPE", 0),
        lambda c: c.gate("H", 0, params=[1.0]),
        lambda c: c.gate("RX", 0),
        lambda c: c.cnot(0, 0),
        lambda c: c.gate("X", 0, condition=7),
        lambda c: c.measure(5),
        lambda c: c.measure(0, outcome=2),
        lambda c: c.unitary("U", [0, 1], np.eye(2)),
        lambda c: c.unitary("U", [0], 2 * np.eye(2)),
        lambda c: c.append(Operation("mystery", "?", (0,))),
        lambda c: c.append(Operation(GATE, "H", (0, 1))),
    ],
)
def test_invalid_operations_are_rejected_at_build_time(build):
    circuit = Circuit(2)
    with pytest.raises(ValueError):
        build(circuit)
    assert len(circuit) == 0


def test_invalid_register_size():
    with pytest.raises(ValueError):
        Circuit(0)


# ------------------------------------------------------------------ diagram
def test_draw_bell_circuit():
    expected = "\n".join(
        [
            "q0: ──[H]──●──",
            "           │",
            "q1: ───────⊕──",
        ]
    )
    assert Circuit(2).gate("H", 0).cnot(0, 1).draw() == expected


def test_draw_empty_circuit_shows_bare_wires():
    assert Circuit(2).draw() == "q0: ──\n\nq1: ──"
    assert Circuit(1).draw() == "q0: ──"


def test_draw_keeps_gate_order_and_packs_parallel_gates():
    circuit = Circuit(2).gate("H", 0).gate("X", 1).cnot(0, 1).gate("Z", 0)
    lines = circuit.draw().split("\n")
    q0, q1 = lines[0], lines[2]
    assert q0.index("[H]") == q1.index("[X]")  # same column
    assert q0.index("[H]") < q0.index("●") < q0.index("[Z]")
    assert q1.index("[X]") < q1.index("⊕")
    assert q0.index("●") == q1.index("⊕") == lines[1].index("│")


def test_draw_reversed_cnot_and_crossing_wire():
    lines = Circuit(3).cnot(2, 0).draw().split("\n")
    assert "⊕" in lines[0] and "┼" in lines[2] and "●" in lines[4]
    column = lines[0].index("⊕")
    assert lines[2][column] == "┼" and lines[4][column] == "●"
    assert lines[1][column] == "│" and lines[3][column] == "│"


def test_draw_all_wires_have_equal_length():
    circuit = (
        Circuit(3).gate("RY", 0, params=[0.5]).gate("H", 1).cnot(1, 2).measure(0)
        .gate("Z", 2, condition=0).unitary("Uf", [0, 1, 2], np.eye(8))
    )
    wires = circuit.draw().split("\n")[::2]
    assert len({len(w) for w in wires}) == 1
    assert "[RY(0.16π)]" in wires[0] and "[M]" in wires[0] and "[Z^m0]" in wires[2]
    assert all("[Uf]" in w for w in wires)


def test_draw_shows_recorded_measurement_outcome():
    executed = Circuit(1).gate("X", 0).measure(0).run().circuit
    assert "[M=1]" in executed.draw()


def test_conditioned_gate_is_drawn_after_its_measurement():
    lines = Circuit(3).measure(0).gate("X", 2, condition=0).draw().split("\n")
    assert lines[4].index("[X^m0]") > lines[0].index("[M]")


def test_layers_respect_dependencies():
    circuit = Circuit(3).gate("H", 0).gate("H", 1).gate("H", 2).cnot(0, 2).gate("X", 1)
    layers = circuit.layers()
    assert [len(layer) for layer in layers] == [3, 1, 1]  # X(q1) cannot pass the CNOT span


def test_controlled_z_label_and_multi_control():
    lines = Circuit(3).gate("Z", 2, controls=[0, 1]).draw().split("\n")
    assert "●" in lines[0] and "●" in lines[2] and "[Z]" in lines[4]
    assert gates.is_unitary(gates.controlled_matrix(gates.PAULI_Z, 2))
