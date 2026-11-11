# Mini Quantum Lab — Codebase Audit (v1.0 baseline)

**Scope:** every tracked file at commit `d30f36a` — `main.py` (469 lines),
`translations.py` (1189 lines), `requirements.txt`, `README.md`,
`contoh-penggunaan.txt`, `.gitignore`, `.devcontainer/devcontainer.json`, `assets/`.
There were no tests, no CI configuration and no deployment files besides the
dev-container.

**Method:** static reading of all source files, plus executing the original
`QuantumSimulator` class in isolation and the original app headlessly
(`streamlit.testing.v1.AppTest`). Every finding below marked **Reproduced** was
observed by running the original code; findings marked **By inspection** follow
directly from the cited lines. Line numbers refer to the v1.0 files.

Severity: **Critical** = wrong physics shown to the user · **High** = wrong or
misleading behaviour · **Medium** = robustness / maintainability · **Low** = cosmetic.

---

## 1. Summary

| ID | Severity | Area | Finding | Status |
|----|----------|------|---------|--------|
| Q1 | Critical | Qubit ordering | Single-qubit gates are big-endian, CNOT is little-endian | Reproduced |
| Q2 | High | State evolution | Re-normalisation after every gate hides non-unitary operators | Reproduced |
| Q3 | High | CNOT | `control == target` builds a non-unitary matrix | Reproduced |
| Q4 | Medium | Validation | Out-of-range target qubit is silently ignored | Reproduced |
| Q5 | Medium | Encapsulation | `get_amplitudes()` returns the live internal array | Reproduced |
| M1 | High | Measurement | Histogram is re-sampled on every Streamlit rerun; no seed | By inspection |
| M2 | High | Measurement | No projective measurement / collapse exists | By inspection |
| M3 | Low | Measurement | Probabilities are passed to the sampler without tolerance handling | By inspection |
| U1 | Medium | UI / i18n | Matplotlib cannot render emoji, CJK, Arabic or Devanagari labels | Reproduced |
| U2 | Low | UI | "System reset" warning is never visible | By inspection |
| U3 | Low | UI | Gate order is only a text list; no circuit diagram | By inspection |
| U4 | Low | UI | README promises "phase" but phase is not plotted | By inspection |
| U5 | Low | UI | Bar colour encodes the same value as bar height | By inspection |
| S1 | Medium | Session state | Circuit is stored twice (`gate_history` is dead code) | By inspection |
| S2 | Low | Session state | Language switch needs an extra forced rerun | By inspection |
| P1 | Medium | Performance | Every gate allocates a dense 2ⁿ×2ⁿ matrix | By inspection |
| D1 | Medium | Dependencies | `qiskit` is required but never imported; nothing is pinned | Reproduced |
| D2 | Low | Docs | README structure lists a file that does not exist | Reproduced |
| D3 | Low | Repo hygiene | Stray placeholder `assets/simulation`; odd `.gitignore` line | Reproduced |
| C1 | Low | Configuration | Dev-container disables CORS and XSRF protection | By inspection |
| T1 | Medium | Testing | No automated tests of any kind | Reproduced |
| I1 | Low | i18n | Help text hard-codes "1-3 qubits" in all 15 languages | Reproduced |

Checked and found **correct** (no change needed): all gate matrices (§2.6), the
15 language tables (54 keys each, no missing or extra keys), state
initialisation to |0…0⟩, the tensor-product expansion of single-qubit gates
taken on its own, and `get_probabilities()`.

One suspicion was **not** confirmed and is therefore not listed as a bug: the
Matplotlib figures are never closed explicitly in `main.py`, but after repeated
headless reruns `plt.get_fignums()` stayed at 0, so no figure leak was observed.

---

## 2. Quantum-mechanical findings

### Q1 — Mixed endianness between `_expand_gate` and `_create_cnot_matrix` (Critical)

`_expand_gate` (lines 50-66) builds `G₀ ⊗ G₁ ⊗ … ⊗ Gₙ₋₁` with `np.kron`, which
makes **qubit 0 the most significant bit** of the basis index (big-endian).
The plot labels (`bin(i)[2:].zfill(n)`, lines 161, 203, 422) agree with this:
the leftmost character is qubit 0.

`_create_cnot_matrix` (lines 68-86) extracts bits with `(i >> k) & 1`, which
makes **qubit 0 the least significant bit** (little-endian).

The two conventions are mixed in the same state vector, so any circuit that
combines a single-qubit gate with a CNOT is wrong. Reproduction with the
original class:

| Circuit (as labelled in the UI) | Original output | Correct output |
|---|---|---|
| H(Q0), CNOT(control Q0 → target Q1) | (\|00⟩ + \|10⟩)/√2 — a product state | (\|00⟩ + \|11⟩)/√2 |
| X(Q0), CNOT(Q0 → Q1) | \|10⟩ (target not flipped) | \|11⟩ |
| X(Q1), CNOT(Q0 → Q1) | \|11⟩ (flipped although control is \|0⟩) | \|01⟩ |
| 3 qubits: X(Q0), CNOT(Q0 → Q2) | \|100⟩ | \|101⟩ |

Consequence: "Eksperimen 2" in `contoh-penggunaan.txt` (the Bell state) — the
project's own flagship example — does not produce an entangled state.

**Fix:** adopt one convention everywhere (big-endian, see
`README.md` → *Quantum mathematical conventions*), reimplement CNOT with it and
lock it down with tests.

### Q2 — Normalisation after each gate masks errors (High)

`apply_gate` ends with `self.state /= np.linalg.norm(self.state)` (line 48).
A unitary never changes the norm, so this line can only have an effect when the
operator is *not* unitary — in which case it silently converts a bug into a
plausible-looking state. Reproduced: applying `2·I` is accepted and the state
norm stays 1.0.

**Fix:** validate that operators are unitary (`U†U = I`) before applying them
and never renormalise during unitary evolution. Renormalisation is physically
meaningful only after a projective measurement.

### Q3 — CNOT with `control == target` is non-unitary (High)

For `control == target` the loop in `_create_cnot_matrix` writes two rows with
a 1 in the same column. Together with Q2, `|00⟩` turns into
`(|00⟩ + |01⟩)/√2` — a superposition manufactured by the bug. The UI prevents
this combination, the class does not.

**Fix:** reject `control == target` with a `ValueError`.

### Q4 — Out-of-range qubit index is silently ignored (Medium)

`_expand_gate` only compares `i == target`; with `target = 5` on a 2-qubit
system it returns the identity and reports success.

**Fix:** validate every qubit index and raise `ValueError`.

### Q5 — `get_amplitudes()` exposes internal state (Medium)

It returns `self.state` itself; mutating the returned array corrupts the
simulator (reproduced: writing 0 into it yields the zero vector).

**Fix:** return a copy / read-only view.

### 2.6 Gate matrices (verified correct)

`I, X, Y, Z, H, S, T` on lines 104-116 match the standard definitions and
satisfy `U†U = I` to machine precision. The logical CNOT truth table is
correct *within its own (little-endian) convention*; the defect is the
inconsistency described in Q1.

---

## 3. Measurement findings

### M1 — Measurement is re-sampled on every rerun, not reproducible (High)

`plot_measurement_histogram` calls `simulator.measure(shots)` (line 202) on
every script execution. Streamlit re-executes the script for any widget
interaction, so ticking "Show Gate Matrix" or changing the language produces a
different histogram for the same state. `np.random.choice` uses the global
unseeded generator, so results can never be reproduced.

**Fix:** explicit "run measurement" action, configurable seed
(`numpy.random.default_rng`), results kept in session state.

### M2 — No projective measurement (High)

The introduction text explains collapse, but the simulator cannot perform one:
`measure()` only draws samples from `|αᵢ|²` and leaves the state untouched.
Repeated sampling of identically prepared states and a single projective
measurement of one system are different operations and both are needed.

**Fix:** add `measure_qubit` / `measure_all` (collapse + renormalise) alongside
shot sampling, and label the difference in the UI.

### M3 — Sampler receives raw probabilities (Low)

`np.random.choice(p=probs)` raises `ValueError` when `sum(p)` deviates from 1
beyond its tolerance. With the per-gate renormalisation removed (Q2) this must
be handled deliberately.

**Fix:** check `|Σp − 1|` against a tolerance and normalise the probability
vector before sampling.

---

## 4. UI / UX findings

- **U1 (Reproduced).** Plot titles contain emoji (`📊`, `🌊`) and, in 10 of 15
  languages, non-Latin text. Matplotlib's default font has none of these
  glyphs; headless runs emit `Glyph … missing from font(s) DejaVu Sans` for
  every such character and the plots show empty boxes. The saved PNGs have the
  same defect.
- **U2.** `st.sidebar.warning(...)` is followed immediately by `st.rerun()`
  (lines 370-371), so the message is discarded before it is displayed.
- **U3.** The circuit is a numbered text list; control/target structure and
  parallelism are not visible.
- **U4.** The README describes "amplitude and phase", but only real and
  imaginary parts are drawn.
- **U5.** Bars are coloured with a colour map of their own height
  (`viridis`/`plasma`), which encodes the same number twice and makes the
  largest bar the palest.
- The gate names `"S Gate"`, `"T Gate"` and the `Q{n}` qubit labels are fixed
  English strings; they are technical proper names and are kept.

## 5. Session-state findings

- **S1.** `QuantumSimulator.gate_history` is initialised and reset but never
  written; the real history lives in `st.session_state.circuit` as preformatted
  strings, which cannot be replayed, drawn or analysed.
- **S2.** The language selector has no widget key; the page title is computed
  before the selector runs, so a second forced `st.rerun()` is required.
- Changing the number of qubits discards the circuit without notice.

## 6. Performance findings

- **P1.** Each gate builds a dense `2ⁿ × 2ⁿ` complex matrix (`16·4ⁿ` bytes)
  and multiplies it with the state: `O(4ⁿ)` time and memory per gate, where
  `O(2ⁿ)` suffices by contracting the 2×2 gate with one tensor axis. Harmless
  at n ≤ 3, but it is the reason the limit could not be raised.
- Nothing is cached; both figures are rebuilt and PNG-encoded at 150 dpi on
  every rerun whether or not the user downloads them.

## 7. Dependencies, configuration, security

- **D1.** `requirements.txt` lists `qiskit`, which is not imported anywhere
  (`grep` finds no usage). It adds a large install (and its transitive
  dependencies) to every deployment for no benefit. No versions are pinned.
- **D2.** README "Project Structure" lists `assets/quantum_gate_simulation.png`;
  the real file is `assets/quantum_measurement.png`. `translations.py` is not
  listed.
- **D3.** `assets/simulation` is a 4-byte placeholder containing `img`.
  `.gitignore` has a line consisting of a single space.
- **C1.** The dev-container starts Streamlit with
  `--server.enableCORS false --server.enableXsrfProtection false`. This is the
  stock GitHub Codespaces template (required by its port-forwarding proxy) and
  is acceptable **only** for that environment; it must not be copied into a
  public deployment. No secrets, tokens or credentials were found in the
  repository or its history of tracked files.
- No user input reaches `eval`, the filesystem or the network.
  `unsafe_allow_html=True` is used once for the footer with a static,
  repository-controlled string.

## 8. Testing

- **T1.** There is no test suite, so none of the defects above could have been
  caught automatically.

## 9. Internationalisation

- All 15 languages define exactly the same 54 keys — verified programmatically.
- **I1.** `num_qubits_help` hard-codes the range "1-3" in every language, so the
  limit cannot change without editing 15 strings.

---

## 10. Remediation plan

| Order | Action | Addresses |
|---|---|---|
| 1 | One documented qubit convention; tensor-contraction gate application; input and unitarity validation; no hidden renormalisation | Q1–Q5, P1 |
| 2 | `pytest` suite for states, gates, expansion and CNOT | T1 |
| 3 | Measurement engine: seeded shot sampling, projective measurement with collapse | M1–M3 |
| 4 | Structured circuit model and text circuit diagram | S1, U3 |
| 5 | Plotly visualisation (browser fonts fix the glyph problem), Bloch sphere, phase plot | U1, U4, U5 |
| 6 | Bell/teleportation demos, noise channels, Grover and Deutsch–Jozsa | new features |
| 7 | Streamlit interface on top of the modules, translations for all 15 languages | S2, U2, I1 |
| 8 | Dependencies, README, repository hygiene | D1–D3 |

---

## 11. Resolution status in version 2.0

Added after the work was completed. "Test" names the test module that guards
the fix; all 500 tests pass (see the README for the verified environments).

| ID | Status | How | Test |
|----|--------|-----|------|
| Q1 | Fixed | Big-endian ordering in every module; CNOT reimplemented | `test_simulator.py`, `test_gates.py` |
| Q2 | Fixed | Unitarity is validated; no renormalisation during unitary evolution | `test_simulator.py` |
| Q3 | Fixed | `control == target` raises `ValueError` | `test_simulator.py` |
| Q4 | Fixed | Qubit indices are validated | `test_gates.py`, `test_simulator.py` |
| Q5 | Fixed | `get_amplitudes()` returns a copy; `state` is a read-only view | `test_simulator.py` |
| M1 | Fixed | Sampling on demand, seeded, stored in session state | `test_measurement.py`, `test_app.py` |
| M2 | Fixed | `measure_qubit`, `measure_all`, `project` with collapse | `test_measurement.py`, `test_app.py` |
| M3 | Fixed | Probability vector is checked and normalised before sampling | `test_measurement.py` |
| U1 | Fixed | Plotly charts; text is rendered by the browser | checked visually in Japanese and Arabic |
| U2 | Fixed | One-shot messages drawn after the callback | `test_app.py` |
| U3 | Fixed | Text circuit diagram | `test_circuit.py` |
| U4 | Fixed | Phase plot | `test_visualization.py` |
| U5 | Fixed | One colour per series; emphasis only where the chart is about one bar | `test_visualization.py` |
| S1 | Fixed | One structured `Circuit` in session state | `test_app.py` |
| S2 | Fixed | Language selector bound to session state by key | `test_app.py` |
| P1 | Fixed | Tensor contraction, O(2ⁿ) per gate | `benchmarks/bench_gates.py` |
| D1 | Fixed | `qiskit` and `matplotlib` removed, `plotly` added, lower bounds tested | — |
| D2 | Fixed | README rewritten | — |
| D3 | Fixed | Placeholder removed, `.gitignore` cleaned | — |
| C1 | Documented | Dev-container flags left as they are (Codespaces needs them); warning added to the README | — |
| T1 | Fixed | pytest suite | — |
| I1 | Fixed | Range is a `{max_qubits}` placeholder | `test_translations.py` |

Found while doing the work, not in the original audit:

- **U6 (Low, reproduced).** The language selector was created with an empty
  label, for which Streamlit logs an accessibility warning on every run
  ("`label` got an empty value"). It now has a label that is hidden visually.
- The headless test harness calls a select box's `format_func` outside the
  script thread, so label functions must not read session state. One did
  during development and was changed to a plain dictionary lookup.
