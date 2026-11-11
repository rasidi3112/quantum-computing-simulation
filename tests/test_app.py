"""End-to-end checks of the Streamlit interface with ``streamlit.testing``."""

from pathlib import Path

import numpy as np
import pytest
from streamlit.testing.v1 import AppTest

from translations import AVAILABLE_LANGUAGES, get_text

APP = str(Path(__file__).resolve().parent.parent / "main.py")
SQRT2 = np.sqrt(2)


def fresh() -> AppTest:
    at = AppTest.from_file(APP, default_timeout=120).run()
    assert not at.exception
    return at


def select(at, label):
    """Selectbox with the given (English) label; the last one wins (sidebar)."""
    matches = [box for box in at.selectbox if box.label == label]
    assert matches, f"no selectbox labelled {label!r}"
    return matches[-1]


def click(at, key):
    at.button(key=key).click().run()
    assert not at.exception
    return at


def set_qubits(at, n):
    at.selectbox(key="num_qubits").select(n).run()
    assert not at.exception
    return at


def apply_gate(at, gate_id, target):
    select(at, "Select Gate:").select(gate_id).run()
    select(at, "Target Qubit:").select(target).run()
    return click(at, "btn_apply_gate")


def apply_cnot(at, control, target):
    select(at, "Control:").select(control).run()
    select(at, "Target:").select(target).run()
    return click(at, "btn_apply_cnot")


def state(at):
    return np.array(at.session_state["simulator"].state)


def shows(elements, text):
    """True if an alert shows ``text`` (Streamlit moves a leading emoji to the icon)."""
    return any(el.value.strip() and el.value.strip() in text for el in elements)


def test_initial_page():
    at = fresh()
    assert [tab.label for tab in at.tabs] == [
        "🧪 Lab", "🌐 Bloch Sphere", "📏 Measurement", "🔗 Entanglement", "🌫️ Noise",
        "🧠 Algorithms",
    ]
    assert np.allclose(state(at), [1, 0])
    assert not at.error and not at.warning
    assert any("q0: ──" in block.value for block in at.code)


def test_bell_state_through_the_sidebar():
    at = set_qubits(fresh(), 2)
    apply_gate(at, "H", 0)
    apply_cnot(at, 0, 1)
    assert np.allclose(state(at), np.array([1, 0, 0, 1]) / SQRT2)
    diagram = at.session_state["circuit"].draw()
    assert "[H]" in diagram and "●" in diagram and "⊕" in diagram
    assert any(block.value == diagram for block in at.code)
    text = " ".join(m.value for m in at.markdown)
    assert "**|00⟩**: 0.7071 (P=0.5000)" in text and "**|11⟩**: 0.7071 (P=0.5000)" in text
    assert "1. Hadamard (H) → Q0" in text and "2. CNOT: Q0 → Q1" in text
    assert any("CNOT" in s.value for s in at.sidebar.success)


def test_reversed_cnot_and_every_gate_button():
    at = set_qubits(fresh(), 2)
    apply_gate(at, "X", 1)
    apply_cnot(at, 1, 0)
    assert np.allclose(state(at), [0, 0, 0, 1])
    for gate_id in ("H", "X", "Y", "Z", "S", "T", "I"):
        apply_gate(at, gate_id, 0)
    assert np.linalg.norm(state(at)) == pytest.approx(1.0, abs=1e-12)
    assert len(at.session_state["circuit"]) == 9


def test_reset_shows_its_message_and_clears_everything():
    at = apply_gate(fresh(), "H", 0)
    click(at, "btn_reset")
    assert np.allclose(state(at), [1, 0])
    assert len(at.session_state["circuit"]) == 0
    assert len(at.sidebar.warning) == 1
    assert shows(at.sidebar.warning, get_text("English", "reset_warning"))
    at.run()  # the message is one-shot
    assert not at.sidebar.warning


def test_changing_the_register_size_rebuilds_the_lab():
    at = apply_gate(fresh(), "X", 0)
    set_qubits(at, 4)
    assert at.session_state["simulator"].num_qubits == 4
    assert np.allclose(state(at), np.eye(16)[0])
    assert len(at.session_state["circuit"]) == 0
    set_qubits(at, 6)
    for q in range(6):
        apply_gate(at, "H", q)
    assert np.allclose(state(at), np.full(64, 1 / 8))
    assert any("16" in c.value and "64" in c.value for c in at.caption)  # truncation note
    set_qubits(at, 1)
    assert np.allclose(state(at), [1, 0])


def test_shot_sampling_is_seeded_stable_across_reruns_and_does_not_collapse():
    at = set_qubits(fresh(), 2)
    apply_gate(at, "H", 0)
    apply_cnot(at, 0, 1)
    assert any(i.value == get_text("English", "no_shots_yet") for i in at.info)
    click(at, "btn_run_shots")
    first = at.session_state["shots_result"]["counts"].copy()
    assert first.sum() == 1000 and first[1] == 0 and first[2] == 0
    assert np.allclose(state(at), np.array([1, 0, 0, 1]) / SQRT2)  # no collapse
    at.checkbox[0].check().run()  # unrelated interaction must not resample
    assert np.array_equal(at.session_state["shots_result"]["counts"], first)
    click(at, "btn_run_shots")  # same seed, same state -> same counts
    assert np.array_equal(at.session_state["shots_result"]["counts"], first)
    at.number_input(key="seed").set_value(43).run()
    click(at, "btn_run_shots")
    assert not np.array_equal(at.session_state["shots_result"]["counts"], first)
    apply_gate(at, "X", 0)  # state changed -> stale histogram is hidden again
    assert any(i.value == get_text("English", "no_shots_yet") for i in at.info)


def test_projective_measurement_collapses_and_is_recorded():
    at = set_qubits(fresh(), 2)
    apply_gate(at, "H", 0)
    apply_cnot(at, 0, 1)
    click(at, "btn_measure_qubit")
    psi = state(at)
    outcome = int(np.argmax(np.abs(psi)) == 3)
    assert np.allclose(np.abs(psi), np.eye(4)[3 * outcome])
    last = at.session_state["circuit"].ops[-1]
    assert last.kind == "measure" and last.outcome == outcome
    assert f"[M={outcome}]" in at.session_state["circuit"].draw()
    assert any(f"Q0 = {outcome}" in s.value for s in at.success)


def test_projective_measurement_sequence_is_reproducible_after_reset():
    def outcomes():
        at = set_qubits(fresh(), 3)
        results = []
        for _ in range(4):
            for q in range(3):
                apply_gate(at, "H", q)
            click(at, "btn_measure_all")
            results.append(int(np.argmax(np.abs(state(at)))))
        return results

    assert outcomes() == outcomes()


def test_measure_all_collapses_to_a_basis_state():
    at = set_qubits(fresh(), 3)
    for q in range(3):
        apply_gate(at, "H", q)
    click(at, "btn_measure_all")
    psi = state(at)
    assert sorted(np.abs(psi))[-1] == pytest.approx(1.0) and np.count_nonzero(psi) == 1
    assert sum(op.kind == "measure" for op in at.session_state["circuit"].ops) == 3


def test_load_bell_state_into_the_lab():
    at = fresh()
    select(at, "Bell state:").select("Ψ-").run()
    click(at, "btn_load_bell")
    assert at.session_state["num_qubits"] == 2
    assert at.selectbox(key="num_qubits").value == 2
    assert abs(np.vdot(np.array([0, 1, -1, 0]) / SQRT2, state(at))) == pytest.approx(1.0)
    assert len(at.session_state["circuit"]) == 4
    assert shows(at.success, get_text("English", "loaded_into_lab"))


def test_teleportation_panel_reports_unit_fidelity():
    at = fresh()
    metrics = {m.label: m.value for m in at.metric}
    assert metrics["Fidelity"] == "1.000000"
    assert any("Alice measured" in s.value for s in at.success)


def test_noise_panel():
    at = fresh()
    assert any(i.value == get_text("English", "noise_empty_circuit") for i in at.info)
    select(at, "Circuit:").select("bell").run()
    assert not at.exception
    values = [m.value for m in at.metric if m.label == "Fidelity"]
    assert "1.000000" in values  # teleportation
    noisy = [float(v) for v in values if v != "1.000000"]
    assert noisy and 0.5 < noisy[0] < 1.0
    select(at, "Noise channel:").select("depolarizing").run()
    select(at, "Circuit:").select("ghz").run()
    assert not at.exception
    # lab circuit containing a measurement
    apply_gate(at, "H", 0)
    click(at, "btn_measure_qubit")
    select(at, "Circuit:").select("lab").run()
    assert not at.exception
    assert any(c.value == get_text("English", "noise_measure_note") for c in at.caption)


def test_algorithm_panels():
    at = fresh()
    metrics = {m.label: m.value for m in at.metric}
    assert metrics["Success probability · Simulated"] == metrics["Success probability · Theory"]
    assert float(metrics["Success probability · Simulated"]) == pytest.approx(0.9453, abs=1e-4)
    assert metrics["P(input register = 0…0)"] == "0.0000"
    assert shows(at.success, get_text("English", "dj_verdict_balanced"))
    select(at, "Function f(x):").select("const1").run()
    assert {m.label: m.value for m in at.metric}["P(input register = 0…0)"] == "1.0000"
    assert shows(at.success, get_text("English", "dj_verdict_constant"))
    select(at, "Function f(x):").select("random").run()
    assert {m.label: m.value for m in at.metric}["P(input register = 0…0)"] == "0.0000"
    for n in (2, 4, 5):
        at.selectbox(key="grover_n").select(n).run()
        assert not at.exception
    at.selectbox(key="dj_n").select(1).run()
    assert not at.exception


@pytest.mark.parametrize("lang", AVAILABLE_LANGUAGES)
def test_every_language_renders_without_errors(lang):
    at = fresh()
    at.selectbox(key="language").select(lang).run()
    assert not at.exception
    assert at.title[0].value == get_text(lang, "main_title").strip()
    assert [tab.label for tab in at.tabs][0] == get_text(lang, "tab_lab")
    set_qubits(at, 2)
    click(at, "btn_apply_gate")
    click(at, "btn_apply_cnot")
    click(at, "btn_run_shots")
    click(at, "btn_measure_qubit")
    assert not at.error
    # state survives the language switch and nothing is left untranslated
    assert at.session_state["simulator"].num_qubits == 2
    assert any(get_text(lang, "projective_header") == h.value for h in at.subheader)
