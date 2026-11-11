"""Mini Quantum Lab — Streamlit interface.

Run with ``streamlit run main.py``.  All physics lives in the ``quantum_lab``
package; this file only wires widgets, session state and translations to it.

Session state
-------------
``language``       current language name (bound to the language selector)
``num_qubits``     size of the lab register (bound to its selector)
``simulator``      ``QuantumSimulator`` holding the lab state
``circuit``        ``Circuit`` with every gate and measurement applied so far
``seed`` / ``rng`` user seed and the generator used for projective outcomes
``shots_result``   last shot-sampling result, tagged with ``state_version``
``state_version``  bumped whenever the lab state changes
``flash``          one-shot messages produced by button callbacks
"""

import numpy as np
import streamlit as st

from quantum_lab import QuantumSimulator, algorithms, noise, protocols, states
from quantum_lab import visualization as viz
from quantum_lab.circuit import GATE, MEASURE, Circuit
from quantum_lab.gates import GATES
from quantum_lab.measurement import make_rng
from translations import AVAILABLE_LANGUAGES, TRANSLATIONS, get_gate_description, get_text

#: Largest register offered in the interface (64 basis states stay readable).
MAX_UI_QUBITS = 6
#: Number of amplitudes listed in the "current state" panel.
MAX_STATE_ROWS = 16
MAX_SEED = 2**31 - 1
DEFAULT_SEED = 42

NOISE_FORMULAS = {
    noise.BIT_FLIP: "ρ → (1 − p)·ρ + p·XρX",
    noise.PHASE_FLIP: "ρ → (1 − p)·ρ + p·ZρZ",
    noise.DEPOLARIZING: "ρ → (1 − p)·ρ + (p/3)·(XρX + YρY + ZρZ)",
}

# Initialise the language before the page config so the tab title is translated.
if "language" not in st.session_state:
    st.session_state.language = "English"

st.set_page_config(
    page_title=get_text(st.session_state.language, "page_title"),
    page_icon="⚛️",
    layout="wide",
)

ss = st.session_state


def t(key, **kwargs):
    """Translate ``key`` into the current language."""
    return get_text(ss.language, key, **kwargs)


# ------------------------------------------------------------------ helpers
def format_amplitude(amp):
    """Compact text for a complex amplitude (same style as version 1.0)."""
    real, imag = float(np.real(amp)), float(np.imag(amp))
    if abs(imag) < 1e-10:
        return f"{real:.4f}"
    if abs(real) < 1e-10:
        return f"{imag:.4f}i"
    return f"({real:.3f}{imag:+.3f}i)"


def ket_string(state, max_terms=4):
    """Short ket expansion such as ``0.7071|00⟩ + 0.7071|11⟩``."""
    labels = states.basis_labels(int(np.log2(len(state))))
    terms = [
        f"{format_amplitude(amp)}|{label}⟩"
        for label, amp in zip(labels, state, strict=True)
        if abs(amp) > 1e-10
    ]
    text = " + ".join(terms[:max_terms])
    return text + (" + …" if len(terms) > max_terms else "")


def palette():
    """Chart colours matching the active Streamlit theme."""
    try:
        return viz.palette_for(st.context.theme.type)
    except Exception:  # theme information is unavailable on old versions
        return viz.LIGHT


def show_chart(fig, key, filename="quantum_lab_chart"):
    st.plotly_chart(
        fig,
        key=key,
        config={
            "displaylogo": False,
            "toImageButtonOptions": {"format": "png", "scale": 2, "filename": filename},
        },
    )


def figures_to_html(title, figures):
    """Standalone interactive HTML page containing the given figures."""
    parts = [
        fig.to_html(full_html=False, include_plotlyjs="cdn" if i == 0 else False)
        for i, fig in enumerate(figures)
    ]
    return (
        "<!doctype html><html><head><meta charset='utf-8'>"
        f"<title>{title}</title></head><body>{''.join(parts)}</body></html>"
    )


def flash(slot, kind, text):
    ss.flash.append((slot, kind, text))


def show_flash(slot, container=st):
    for entry_slot, kind, text in ss.flash:
        if entry_slot == slot:
            getattr(container, kind)(text)


def bump():
    """Mark the lab state as changed (invalidates stored shot results)."""
    ss.state_version += 1


def rebuild_lab():
    """Fresh |0…0⟩ register of the selected size and a re-seeded generator."""
    ss.simulator = QuantumSimulator(ss.num_qubits)
    ss.circuit = Circuit(ss.num_qubits)
    ss.rng = make_rng(int(ss.seed))
    ss.shots_result = None
    bump()


def init_state():
    ss.setdefault("num_qubits", 1)
    ss.setdefault("seed", DEFAULT_SEED)
    ss.setdefault("state_version", 0)
    ss.setdefault("shots_result", None)
    ss.setdefault("flash", [])
    if "simulator" not in ss or ss.simulator.num_qubits != ss.num_qubits:
        rebuild_lab()


# ---------------------------------------------------------------- callbacks
# Callbacks run before the script body, so every element of the page is drawn
# from the already-updated state.
def cb_apply_gate(gate_id, target):
    try:
        ss.simulator.apply(GATES[gate_id].matrix, [target])
        ss.circuit.gate(gate_id, target)
    except (ValueError, TypeError) as exc:
        flash("gate", "error", t("error_operation", message=exc))
        return
    bump()
    flash("gate", "success",
          t("gate_applied_success", gate_name=GATES[gate_id].name, target=target))


def cb_apply_cnot(control, target):
    try:
        ss.simulator.cnot(control, target)
        ss.circuit.cnot(control, target)
    except (ValueError, TypeError) as exc:
        flash("cnot", "error", t("error_operation", message=exc))
        return
    bump()
    flash("cnot", "success", t("cnot_applied_success", control=control, target=target))


def cb_reset():
    rebuild_lab()
    flash("reset", "warning", t("reset_warning"))


def cb_seed_changed():
    ss.rng = make_rng(int(ss.seed))


def cb_run_shots(shots):
    try:
        counts = ss.simulator.sample_counts(int(shots), rng=int(ss.seed))
    except (ValueError, TypeError) as exc:
        flash("shots", "error", t("error_operation", message=exc))
        return
    ss.shots_result = {"counts": counts, "shots": int(shots), "version": ss.state_version}


def cb_measure_qubit(qubit):
    try:
        outcome = ss.simulator.measure_qubit(qubit, ss.rng)
        ss.circuit.measure(qubit, outcome=outcome)
    except (ValueError, TypeError) as exc:
        flash("measure", "error", t("error_operation", message=exc))
        return
    bump()
    flash("measure", "success", t("measure_result", result=f"Q{qubit} = {outcome}"))


def cb_measure_all():
    index = ss.simulator.measure_all(ss.rng)
    bits = format(index, f"0{ss.num_qubits}b")
    for qubit, bit in enumerate(bits):
        ss.circuit.measure(qubit, outcome=int(bit))
    bump()
    flash("measure", "success", t("measure_result", result=f"|{bits}⟩"))


def cb_load_circuit(circuit):
    """Replace the lab with ``circuit`` (used by the demonstration tabs)."""
    ss.num_qubits = circuit.num_qubits
    rebuild_lab()
    result = circuit.run(rng=ss.rng)
    ss.simulator, ss.circuit = result.simulator, result.circuit
    flash("main", "success", t("loaded_into_lab"))


# ------------------------------------------------------------------ sidebar
def render_sidebar():
    lang = ss.language
    st.sidebar.header(t("language_label"))
    st.sidebar.selectbox(
        t("language_label"),
        options=AVAILABLE_LANGUAGES,
        key="language",
        format_func=lambda name: f"{TRANSLATIONS[name]['flag']} {name}",
        label_visibility="collapsed",
    )
    st.sidebar.markdown("---")

    st.sidebar.header(t("sidebar_settings"))
    st.sidebar.selectbox(
        t("num_qubits_label"),
        options=list(range(1, MAX_UI_QUBITS + 1)),
        key="num_qubits",
        help=t("num_qubits_help", max_qubits=MAX_UI_QUBITS),
        on_change=rebuild_lab,
    )
    num_qubits = ss.num_qubits

    st.sidebar.markdown("---")
    st.sidebar.subheader(t("add_gate_header"))
    gate_id = st.sidebar.selectbox(
        t("select_gate"),
        options=list(GATES),
        format_func=lambda g: GATES[g].name,
        help=t("select_gate_help"),
    )
    target = st.sidebar.selectbox(
        t("target_qubit"),
        options=list(range(num_qubits)),
        format_func=lambda q: f"Q{q}",
        help=t("target_qubit_help"),
    )
    spec = GATES[gate_id]
    st.sidebar.info(f"{spec.emoji} **{spec.name}**\n\n{get_gate_description(lang, spec.name)}")
    st.sidebar.button(t("apply_gate_btn"), key="btn_apply_gate", width="stretch",
                      on_click=cb_apply_gate, args=(gate_id, target))
    show_flash("gate", st.sidebar)

    st.sidebar.markdown("---")
    if num_qubits > 1:
        st.sidebar.subheader(t("cnot_header"))
        col1, col2 = st.sidebar.columns(2)
        control = col1.selectbox(
            t("control_label"), options=list(range(num_qubits)), format_func=lambda q: f"Q{q}"
        )
        cnot_target = col2.selectbox(
            t("target_label"),
            options=[q for q in range(num_qubits) if q != control],
            format_func=lambda q: f"Q{q}",
        )
        st.sidebar.info(t("cnot_info"))
        st.sidebar.button(t("apply_cnot_btn"), key="btn_apply_cnot", width="stretch",
                          on_click=cb_apply_cnot, args=(control, cnot_target))
        show_flash("cnot", st.sidebar)
        st.sidebar.markdown("---")

    st.sidebar.button(t("reset_btn"), key="btn_reset", width="stretch", type="secondary",
                      on_click=cb_reset)
    show_flash("reset", st.sidebar)
    return spec


# ---------------------------------------------------------------------- lab
def display_matrix(matrix, title):
    """Text rendering of a gate matrix."""
    st.markdown(f"### 🔢 {t('matrix_title')} {title}")
    lines = []
    for row in matrix:
        cells = []
        for value in row:
            real, imag = float(np.real(value)), float(np.imag(value))
            if abs(imag) < 1e-10:
                cells.append(f" {real:7.4f}      ")
            elif abs(real) < 1e-10:
                cells.append(f" {imag:7.4f}i     ")
            else:
                cells.append(f" {real:.3f}{imag:+.3f}i ")
        lines.append("[" + "".join(cells) + "]")
    st.code("\n".join(lines), language=None)


def history_line(op):
    if op.kind == MEASURE:
        return f"📏 Q{op.targets[0]} = {op.outcome}"
    if op.kind == GATE and op.controls:
        return f"CNOT: Q{op.controls[0]} → Q{op.targets[0]}"
    return f"{GATES[op.name].name} → Q{op.targets[0]}"


def render_lab(selected_gate):
    sim, circuit, pal = ss.simulator, ss.circuit, palette()
    labels = states.basis_labels(sim.num_qubits)
    amplitudes, probabilities = sim.get_amplitudes(), sim.get_probabilities()

    st.markdown(t("circuit_diagram_header"))
    st.code(circuit.draw(), language=None)
    st.caption(t("convention_note"))

    col_left, col_right = st.columns([2, 1])
    with col_left:
        st.subheader(t("state_vector_header"))
        fig_prob = viz.probability_figure(
            probabilities, labels, title=t("probability_dist_title"),
            x_title=t("basis_state_label"), y_title=t("probability_label"), palette=pal,
        )
        fig_amp = viz.amplitude_figure(
            amplitudes, labels, title=t("amplitude_title"), x_title=t("basis_state_label"),
            y_title=t("amplitude_label"), real_label=t("real_label"),
            imag_label=t("imaginary_label"), palette=pal,
        )
        fig_phase = viz.phase_figure(
            amplitudes, labels, title=t("phase_title"), x_title=t("basis_state_label"),
            palette=pal,
        )
        show_chart(fig_prob, "lab_prob", "quantum_state_vector")
        show_chart(fig_amp, "lab_amp", "quantum_amplitudes")
        show_chart(fig_phase, "lab_phase", "quantum_phase")
        st.download_button(
            label=t("save_state_vector_btn"),
            data=figures_to_html(t("state_vector_header"), [fig_prob, fig_amp, fig_phase]),
            file_name="quantum_state_vector.html",
            mime="text/html",
        )
        st.caption(t("download_hint"))

    with col_right:
        st.subheader(t("state_info_header"))
        st.markdown(t("current_state"))
        nonzero = [i for i in np.argsort(-probabilities, kind="stable")
                   if abs(amplitudes[i]) > 1e-10]
        shown = sorted(nonzero[:MAX_STATE_ROWS])
        st.markdown(
            "\n\n".join(
                f"**|{labels[i]}⟩**: {format_amplitude(amplitudes[i])} "
                f"(P={probabilities[i]:.4f})"
                for i in shown
            )
        )
        if len(nonzero) > len(shown):
            st.caption(t("state_truncated", shown=len(shown), total=len(nonzero)))

        st.markdown("---")
        st.markdown(t("circuit_history"))
        if len(circuit):
            st.markdown("\n".join(f"{i}. {history_line(op)}"
                                  for i, op in enumerate(circuit, 1)))
        else:
            st.info(t("no_gates_applied"))

        st.markdown("---")
        if st.checkbox(t("show_matrix")):
            display_matrix(selected_gate.matrix, selected_gate.name)


# -------------------------------------------------------------------- Bloch
def render_bloch_cell(vector, title, key):
    """One sphere with its length, purity and pure/mixed status."""
    length = float(np.linalg.norm(vector))
    show_chart(viz.bloch_figure(vector, title=title, palette=palette()), key, "bloch_sphere")
    col1, col2 = st.columns(2)
    col1.metric(t("bloch_length"), f"{length:.3f}")
    col2.metric(t("purity_label"), f"{(1 + length**2) / 2:.3f}")
    if length > 1 - 1e-6:
        st.caption(f"🟢 {t('state_pure')}")
    else:
        st.caption(f"🟠 {t('state_mixed')}")


def render_bloch():
    sim = ss.simulator
    st.markdown(t("bloch_intro"))
    vectors = [states.qubit_bloch_vector(sim.state, q) for q in range(sim.num_qubits)]
    for start in range(0, len(vectors), 3):
        columns = st.columns(3)
        for column, qubit in zip(columns, range(start, min(start + 3, len(vectors))),
                                 strict=False):
            with column:
                render_bloch_cell(vectors[qubit], f"Q{qubit}", f"bloch_{qubit}")


# -------------------------------------------------------------- measurement
def render_measurement():
    sim, pal = ss.simulator, palette()
    labels = states.basis_labels(sim.num_qubits)

    st.subheader(t("measurement_header"))
    st.markdown(t("sampling_info"))
    col1, col2 = st.columns(2)
    shots = col1.slider(t("shots_label"), min_value=100, max_value=10000, value=1000, step=100)
    col2.number_input(t("seed_label"), min_value=0, max_value=MAX_SEED, step=1, key="seed",
                      help=t("seed_help"), on_change=cb_seed_changed)
    st.button(t("run_shots_btn"), key="btn_run_shots", type="primary", on_click=cb_run_shots,
              args=(shots,))
    show_flash("shots")

    result = ss.shots_result
    if result is not None and result["version"] == ss.state_version:
        fig = viz.histogram_figure(
            result["counts"], sim.get_probabilities() * result["shots"], labels,
            title=t("histogram_title", shots=result["shots"]),
            x_title=t("measurement_result_label"),
            y_title=t("frequency_label", shots=result["shots"]),
            measured_label=t("measured_label"), expected_label=t("expected_label"), palette=pal,
        )
        show_chart(fig, "shots_hist", "quantum_measurement")
        st.download_button(
            label=t("save_measurement_btn"),
            data=figures_to_html(t("measurement_header"), [fig]),
            file_name="quantum_measurement.html",
            mime="text/html",
        )
    else:
        st.info(t("no_shots_yet"))

    st.markdown("---")
    st.subheader(t("projective_header"))
    st.markdown(t("projective_info"))
    qubit = st.selectbox(t("measure_qubit_label"), options=list(range(sim.num_qubits)),
                         format_func=lambda q: f"Q{q}")
    col1, col2 = st.columns(2)
    col1.button(t("measure_qubit_btn"), key="btn_measure_qubit", width="stretch",
                on_click=cb_measure_qubit, args=(qubit,))
    col2.button(t("measure_all_btn"), key="btn_measure_all", width="stretch",
                on_click=cb_measure_all)
    show_flash("measure")
    st.code(ss.circuit.draw(), language=None)
    st.markdown(f"{t('current_state')}\n\n`{ket_string(sim.state)}`")


# ---------------------------------------------------------------- protocols
def render_bell():
    pal = palette()
    st.subheader(t("bell_header"))
    kind = st.selectbox(t("bell_select"), options=list(protocols.BELL_STATES),
                        format_func=lambda k: f"|{k}⟩")
    circuit = protocols.bell_circuit(kind)
    sim = circuit.run().simulator
    st.code(circuit.draw(), language=None)

    col_left, col_right = st.columns([2, 1])
    with col_left:
        show_chart(
            viz.probability_figure(
                sim.get_probabilities(), states.basis_labels(2),
                title=t("probability_dist_title"), x_title=t("basis_state_label"),
                y_title=t("probability_label"), palette=pal,
            ),
            "bell_prob", "bell_state",
        )
    with col_right:
        st.markdown(f"{t('current_state')}\n\n`|{kind}⟩ = {ket_string(sim.state)}`")
        st.metric(t("entropy_label"), f"{states.entanglement_entropy(sim.state, [0]):.3f}")
        lengths = [np.linalg.norm(states.qubit_bloch_vector(sim.state, q)) for q in (0, 1)]
        st.metric(t("bloch_length"), " · ".join(f"Q{q}: {r:.3f}" for q, r in enumerate(lengths)))

    st.info(t("bell_explain"))
    for outcome in (0, 1):
        branch = sim.copy()
        prob = branch.project(0, outcome)
        st.markdown("- " + t("collapse_if", outcome=outcome, prob=f"{prob:.2f}",
                             state=f"`{ket_string(branch.state)}`"))
    st.button(t("load_into_lab_btn"), key="btn_load_bell", on_click=cb_load_circuit,
              args=(circuit,))


def render_teleportation():
    st.subheader(t("teleport_header"))
    st.markdown(t("teleport_explain"))
    col1, col2, col3 = st.columns(3)
    theta = col1.slider("θ / π", min_value=0.0, max_value=1.0, value=0.35, step=0.01) * np.pi
    phi = col2.slider("φ / π", min_value=0.0, max_value=2.0, value=0.60, step=0.01) * np.pi
    seed = col3.number_input(t("seed_label"), min_value=0, max_value=MAX_SEED, value=7, step=1,
                             key="teleport_seed", help=t("seed_help"))
    st.caption("|ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)·sin(θ/2)|1⟩")

    result = protocols.run_teleportation(theta, phi, rng=int(seed))
    st.code(result.run.circuit.draw(), language=None)
    m0, m1 = result.outcomes
    correction = ", ".join(g for g, bit in (("X", m1), ("Z", m0)) if bit) or t("no_correction")
    st.success(t("teleport_outcomes", m0=m0, m1=m1, correction=correction))

    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        show_chart(viz.bloch_figure(result.message_bloch, title=t("teleport_message_title"),
                                    palette=palette()), "teleport_message", "teleport_message")
    with col2:
        show_chart(viz.bloch_figure(result.bob_bloch, title=t("teleport_bob_title"),
                                    palette=palette()), "teleport_bob", "teleport_bob")
    with col3:
        st.metric(t("fidelity_label"), f"{result.fidelity:.6f}")
        st.metric(t("bloch_length"), f"{np.linalg.norm(result.bob_bloch):.3f}")


# -------------------------------------------------------------------- noise
def render_noise():
    pal = palette()
    st.markdown(t("noise_intro"))
    sources = {
        "lab": t("noise_source_lab"),
        "bell": "Bell |Φ+⟩",
        "ghz": "GHZ (Q0, Q1, Q2)",
    }
    col1, col2, col3 = st.columns(3)
    source = col1.selectbox(t("noise_source_label"), options=list(sources),
                            format_func=sources.get)
    channel_names = {name: t(f"channel_{name}") for name in noise.CHANNELS}
    channel = col2.selectbox(t("noise_channel_label"), options=list(channel_names),
                             format_func=channel_names.get)
    p = col3.slider(t("noise_prob_label"), min_value=0.0, max_value=0.5, value=0.05, step=0.01)
    st.caption(NOISE_FORMULAS[channel])

    if source == "lab":
        circuit = ss.circuit
        if len(circuit) == 0:
            st.info(t("noise_empty_circuit"))
            return
    elif source == "bell":
        circuit = protocols.bell_circuit()
    else:
        circuit = protocols.ghz_circuit(3)

    ideal = noise.simulate_density(circuit)
    noisy = noise.simulate_density(circuit, channel, float(p))

    with st.expander(t("show_circuit")):
        st.code(circuit.draw(), language=None)
    if any(op.kind == MEASURE for op in circuit):
        st.caption(t("noise_measure_note"))

    col_left, col_right = st.columns([2, 1])
    with col_left:
        show_chart(
            viz.comparison_figure(
                ideal.probabilities(), noisy.probabilities(),
                states.basis_labels(circuit.num_qubits), title=t("noise_chart_title"),
                x_title=t("basis_state_label"), y_title=t("probability_label"),
                first_label=t("ideal_label"), second_label=t("noisy_label"), palette=pal,
            ),
            "noise_compare", "noise_comparison",
        )
        col1, col2 = st.columns(2)
        col1.metric(t("fidelity_label"), f"{noisy.fidelity(ideal):.4f}")
        col2.metric(t("purity_label"), f"{noisy.purity():.4f}")
    with col_right:
        qubit = st.radio("Qubit", options=list(range(circuit.num_qubits)),
                         format_func=lambda q: f"Q{q}", horizontal=True,
                         label_visibility="collapsed", key=f"noise_qubit_{circuit.num_qubits}")
        render_bloch_cell(states.bloch_vector(noisy.reduced(qubit)),
                          f"Q{qubit} · {t('noisy_label')}", "noise_bloch")


# --------------------------------------------------------------- algorithms
@st.cache_data(show_spinner=False)
def grover_curve(num_qubits, marked, max_iterations):
    return algorithms.grover_success_probabilities(num_qubits, marked, max_iterations)


def render_grover():
    pal = palette()
    st.subheader(t("grover_header"))
    st.markdown(t("grover_explain"))
    col1, col2, col3 = st.columns(3)
    n = col1.selectbox(t("num_qubits_label"), options=[2, 3, 4, 5], index=1, key="grover_n")
    labels = states.basis_labels(n)
    marked = col2.selectbox(t("grover_marked_label"), options=list(range(2**n)),
                            index=2**n - 3, format_func=lambda i: f"|{labels[i]}⟩",
                            key=f"grover_marked_{n}")
    k_opt = algorithms.grover_optimal_iterations(n)
    k_max = 2 * k_opt + 2
    k = col3.slider(t("grover_iterations_label"), min_value=0, max_value=k_max, value=k_opt,
                    key=f"grover_k_{n}")
    st.caption(t("grover_optimal", k=k_opt))

    circuit = algorithms.grover_circuit(n, marked, k)
    probabilities = circuit.run().simulator.get_probabilities()
    curve = grover_curve(n, marked, k_max)
    col1, col2 = st.columns(2)
    col1.metric(f"{t('grover_success_label')} · {t('simulated_label')}",
                f"{probabilities[marked]:.4f}")
    col2.metric(f"{t('grover_success_label')} · {t('theory_label')}",
                f"{algorithms.grover_theoretical_probability(n, k):.4f}")

    col1, col2 = st.columns(2)
    with col1:
        show_chart(
            viz.probability_figure(
                probabilities, labels, title=t("probability_dist_title"),
                x_title=t("basis_state_label"), y_title=t("probability_label"),
                palette=pal, highlight=marked,
            ),
            "grover_prob", "grover_probabilities",
        )
    with col2:
        xs = np.linspace(0, k_max, 200)
        theta = algorithms.grover_angle(n)
        show_chart(
            viz.curve_figure(
                list(range(k_max + 1)), curve, xs, np.sin((2 * xs + 1) * theta) ** 2,
                title=t("grover_curve_title"), x_title=t("grover_iterations_label"),
                y_title=t("grover_success_label"), simulated_label=t("simulated_label"),
                theory_label=t("theory_label"), palette=pal, marker_x=k,
            ),
            "grover_curve", "grover_curve",
        )
    with st.expander(t("show_circuit")):
        st.code(circuit.draw(), language=None)


def render_deutsch_jozsa():
    pal = palette()
    st.subheader(t("dj_header"))
    st.markdown(t("dj_explain"))
    kinds = {
        "const0": f"{t('dj_constant')}: f(x) = 0",
        "const1": f"{t('dj_constant')}: f(x) = 1",
        "parity": t("dj_balanced_parity"),
        "random": t("dj_balanced_random"),
    }
    col1, col2, col3 = st.columns(3)
    n = col1.selectbox(t("dj_inputs_label"), options=[1, 2, 3, 4], index=2, key="dj_n")
    kind = col2.selectbox(t("dj_oracle_label"), options=list(kinds), index=2,
                          format_func=kinds.get)
    labels = states.basis_labels(n)

    if kind == "parity":
        mask = col3.selectbox(
            t("dj_mask_label"), options=list(range(1, 2**n)), index=2**n - 2,
            format_func=lambda m: " ⊕ ".join(
                f"x{q}" for q in range(n) if (m >> (n - 1 - q)) & 1),
            key=f"dj_mask_{n}",
        )
        table = algorithms.parity_oracle(n, mask)
    elif kind == "random":
        seed = col3.number_input(t("seed_label"), min_value=0, max_value=MAX_SEED, value=1,
                                 step=1, key="dj_seed", help=t("seed_help"))
        table = algorithms.random_balanced_oracle(n, rng=int(seed))
    else:
        table = algorithms.constant_oracle(n, int(kind == "const1"))

    st.caption("f(x):  " + "   ".join(f"{labels[x]}→{f}" for x, f in enumerate(table)))
    result = algorithms.run_deutsch_jozsa(table)

    col_left, col_right = st.columns([2, 1])
    with col_left:
        show_chart(
            viz.probability_figure(
                result.input_probabilities, labels, title=t("probability_dist_title"),
                x_title=t("basis_state_label"), y_title=t("probability_label"), palette=pal,
            ),
            "dj_prob", "deutsch_jozsa",
        )
    with col_right:
        st.metric(t("dj_prob_zero"), f"{result.prob_all_zero:.4f}")
        if result.verdict == algorithms.CONSTANT:
            st.success(t("dj_verdict_constant"))
        else:
            st.success(t("dj_verdict_balanced"))
        st.caption(t("dj_queries", classical=result.classical_queries_worst_case))
    with st.expander(t("show_circuit")):
        st.code(result.circuit.draw(), language=None)


# --------------------------------------------------------------------- page
def main():
    init_state()
    selected_gate = render_sidebar()

    st.title(t("main_title"))
    show_flash("main")
    st.markdown("---")
    with st.expander(t("intro_header"), expanded=False):
        st.markdown(t("intro_title"))
        st.markdown(t("intro_content"))
    st.markdown("---")

    tabs = st.tabs([t("tab_lab"), t("tab_bloch"), t("tab_measure"), t("tab_protocols"),
                    t("tab_noise"), t("tab_algorithms")])
    with tabs[0]:
        render_lab(selected_gate)
    with tabs[1]:
        render_bloch()
    with tabs[2]:
        render_measurement()
    with tabs[3]:
        render_bell()
        st.markdown("---")
        render_teleportation()
    with tabs[4]:
        render_noise()
    with tabs[5]:
        render_grover()
        st.markdown("---")
        render_deutsch_jozsa()

    st.markdown("---")
    st.markdown(
        f"""
    <div style='text-align: center; color: #7f8c8d; font-size: 12px;'>
        <p>{t("footer")}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    ss.flash = []


if __name__ == "__main__":
    main()
