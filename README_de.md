<h1 align="center">Mini Quantum Lab 2.0</h1>

<p align="center">
  <b>Ein interaktiver, getesteter Quantencomputer-Simulator zum Lernen</b><br>
  Python · NumPy · Streamlit · Plotly · 15 Oberflächensprachen
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="README_ar.md">العربية</a> ·
  <b>Deutsch</b> ·
  <a href="README_es.md">Español</a> ·
  <a href="README_fr.md">Français</a> ·
  <a href="README_hi.md">हिन्दी</a> ·
  <a href="README_id.md">Bahasa Indonesia</a> ·
  <a href="README_it.md">Italiano</a> ·
  <a href="README_ja.md">日本語</a> ·
  <a href="README_ko.md">한국어</a> ·
  <a href="README_ms.md">Bahasa Melayu</a> ·
  <a href="README_pl.md">Polski</a> ·
  <a href="README_pt.md">Português</a> ·
  <a href="README_ru.md">Русский</a> ·
  <a href="README_tr.md">Türkçe</a> ·
  <a href="README_vi.md">Tiếng Việt</a> ·
  <a href="README_zh.md">中文</a>
</p>

---

## Überblick

Mini Quantum Lab ist eine Lern-Webanwendung zum Erkunden der Grundlagen des Quantencomputings: kleine Schaltkreise Gatter für Gatter aufbauen, den Zustandsvektor beobachten, jedes Qubit auf einer Bloch-Kugel betrachten, messen, Rauschen hinzufügen und einige Lehrbuchprotokolle und -algorithmen ausführen.

Version 2.0 behält Aussehen und Arbeitsablauf des ursprünglichen Projekts bei und ersetzt, was darunter liegt: ein eigenes, mit Unit-Tests abgesichertes Simulationspaket mit einer einzigen dokumentierten Qubit-Reihenfolge, physikalisch konsistenter Messung und neuen Visualisierungen. Das Audit, das die Änderungen veranlasst hat, steht in [`docs/AUDIT.md`](docs/AUDIT.md).

> Dieses Projekt orientiert sich am visuellen Stil von Werkzeugen wie IBM Quantum Composer und Qiskit. Es ist ein unabhängiges Lernprojekt und **steht in keiner Verbindung zu IBM und wird nicht von IBM unterstützt**, ebenso wenig von anderen Quantencomputing-Organisationen. Es simuliert ideale und verrauschte Qubits auf einem klassischen Computer und verbindet sich nicht mit Quantenhardware.

## Funktionen

| Bereich | Was Sie tun können |
|---|---|
| **Labor** | 1–6 Qubits; Gatter I, X, Y, Z, H, S, T auf jedem Qubit; CNOT zwischen zwei beliebigen Qubits; Live-Schaltkreisdiagramm, Zustandstabelle und Gatterverlauf |
| **Zustandsvisualisierung** | Wahrscheinlichkeitsverteilung, Real-/Imaginärteile der Amplituden und die Phase jeder Amplitude, mit Beschriftung der Basiszustände |
| **Bloch-Kugel** | Interaktive 3D-Kugel pro Qubit, gezeichnet aus dem *reduzierten Zustand* des Qubits, mit Vektorlänge und Reinheit, damit reine und gemischte Zustände unterscheidbar sind |
| **Messung** | Shot-Sampling (100–10 000 Schüsse) mit Seed sowie projektive Messung eines oder aller Qubits mit Zustandskollaps |
| **Verschränkung** | Generator für die vier Bell-Zustände mit Entropie und Kollaps-Demonstration; Drei-Qubit-Quantenteleportation eines beliebigen Ein-Qubit-Zustands |
| **Rauschen** | Bit-Flip-, Phasen-Flip- und depolarisierender Kanal nach jedem Gatter, exakt mit einer Dichtematrix simuliert |
| **Algorithmen** | Grover-Suche (2–5 Qubits) und Deutsch-Jozsa (1–4 Eingabe-Qubits) mit Erklärungen und Schaltkreisen |
| **Sprachen** | English, Indonesian, Spanish, Mandarin Chinese, Arabic, French, Japanese, Korean, German, Portuguese, Russian, Hindi, Turkish, Italian, Vietnamese |

## Screenshots

| Labor: Schaltkreis, Wahrscheinlichkeiten, Amplituden | Bloch-Kugeln (Q0 und Q1 verschränkt, Q2 rein) |
|---|---|
| <img src="assets/screenshot_lab.png" alt="Lab" width="420"/> | <img src="assets/screenshot_bloch.png" alt="Bloch" width="420"/> |

| Shot-Sampling und projektive Messung | Quantenteleportation |
|---|---|
| <img src="assets/screenshot_measurement.png" alt="Measurement" width="420"/> | <img src="assets/screenshot_teleportation.png" alt="Teleportation" width="420"/> |

| Rauschen: idealer und depolarisierter Bell-Zustand | Grover und Deutsch-Jozsa |
|---|---|
| <img src="assets/screenshot_noise.png" alt="Noise" width="420"/> | <img src="assets/screenshot_algorithms.png" alt="Algorithms" width="420"/> |

## Installation

Erfordert Python 3.11 oder neuer (getestet mit 3.11 und 3.13).

```bash
git clone https://github.com/rasidi3112/quantum-computing-simulation.git
cd quantum-computing-simulation
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

Öffnen Sie dann <http://localhost:8501>.

Laufzeitabhängigkeiten sind `numpy`, `streamlit` und `plotly`. Das Simulationspaket selbst (`quantum_lab`, ohne `visualization`) benötigt nur NumPy.

## Verwendung

1. Wählen Sie in der Seitenleiste die **Anzahl der Qubits** (eine Änderung beginnt einen neuen, leeren Schaltkreis).
2. Wählen Sie ein Gatter und ein Ziel-Qubit und drücken Sie **Apply Gate**; bei zwei oder mehr Qubits wählen Sie Steuerung und Ziel und drücken **Apply CNOT**.
3. Lesen Sie das Ergebnis in den Tabs ab:
   - **Lab**: Schaltkreisdiagramm, Wahrscheinlichkeiten, Amplituden, Phasen, Zustandstabelle;
   - **Bloch Sphere**: eine Kugel pro Qubit;
   - **Measurement**: *Run Measurement* zieht Stichproben, ohne den Zustand zu verändern; *Measure Qubit* / *Measure All Qubits* lassen ihn kollabieren;
   - **Entanglement**, **Noise**, **Algorithms**: eigenständige Demonstrationen. *Load into Lab* kopiert einen Bell-Schaltkreis ins Labor.
4. **Reset System** kehrt zu |0…0⟩ zurück und startet den Zufallsgenerator neu aus dem Seed.

Die Diagramme sind interaktiv (Hover, Zoom, Drehen). Die Kamera-Schaltfläche in der Werkzeugleiste eines Diagramms speichert ein PNG; die Schaltflächen *Save …* laden eine eigenständige interaktive HTML-Datei herunter.

### Beispielschaltkreise

| Ziel | Schritte | Erwartetes Ergebnis |
|---|---|---|
| Superposition | 1 qubit: H → Q0 | P(0) = P(1) = 0.5; Bloch-Vektor auf +x |
| Bell-Zustand \|Φ+⟩ | 2 qubits: H → Q0, CNOT Q0 → Q1 | (\|00⟩ + \|11⟩)/√2; P(00) = P(11) = 0.5, P(01) = P(10) = 0; beide Bloch-Vektoren haben die Länge 0 |
| H·Z·H = X | 1 qubit: H, Z, H → Q0 | \|1⟩ |
| GHZ-Zustand | 3 qubits: H → Q0, CNOT Q0 → Q1, CNOT Q1 → Q2 | (\|000⟩ + \|111⟩)/√2 |
| Kollaps | Bell-Zustand, dann *Measure Qubit* Q0 | \|00⟩ / \|11⟩; Q1 ist nun festgelegt |

```
q0: ──[H]──●──
           │
q1: ───────⊕──
```

### Den Simulator aus Python verwenden

```python
import numpy as np
from quantum_lab import Circuit, QuantumSimulator, gates

sim = QuantumSimulator(2)
sim.apply(gates.HADAMARD, [0])
sim.cnot(0, 1)
print(np.round(sim.state, 4))             # [0.7071 0 0 0.7071]
print(sim.sample_counts(1000, rng=42))    # [487 0 0 513] = counts of 00, 01, 10, 11
print(sim.measure_qubit(0, rng=7), sim.state)   # 0 [1 0 0 0]: collapsed to |00>

circuit = Circuit(2).gate("H", 0).cnot(0, 1).measure(0).measure(1)
print(circuit.draw())
print(circuit.run(rng=1).outcomes)        # {0: 0, 1: 0}; the two bits always agree
```

## Quantenmathematische Konventionen

**Zustand.** Ein Register aus *n* Qubits ist ein komplexer Vektor mit 2ⁿ Amplituden αᵢ und Σ|αᵢ|² = 1, initialisiert auf |0…0⟩.

**Qubit-Reihenfolge: Big-Endian, überall.** Qubit 0 ist das *linke* Bit einer Basisbeschriftung und die *oberste* Leitung eines Diagramms:

```
|q0 q1 … q(n-1)⟩      index = Σ_k q_k · 2^(n-1-k)      |ψ⟩ = |q0⟩ ⊗ |q1⟩ ⊗ … ⊗ |q(n-1)⟩
```

Bei zwei Qubits macht X auf Q0 also aus |00⟩ den Zustand |10⟩ (Index 2). Eine Matrix, die auf die Qubit-Liste `[a, b]` wirkt, behandelt `a` als höchstwertiges Bit; insbesondere ist `gates.CNOT` die Matrix für `[control, target]`. Das ist die Lehrbuchkonvention (Nielsen & Chuang). **Qiskit verwendet die umgekehrte Little-Endian-Reihenfolge**; kehren Sie beim Vergleich die Bitfolgen um.

**Zeitentwicklung.** Jeder Operator wird vor der Anwendung auf Unitarität geprüft (U†U = I, Toleranz 10⁻¹⁰), und der Zustand wird während der unitären Entwicklung nie neu normiert. Tests bestätigen, dass die Norm nach 3000 Gattern um weniger als 10⁻¹⁰ von 1 abweicht.

**Messung (Rechenbasis):**

- *Shot-Sampling* zieht Ergebnisse aus P(i) = |αᵢ|². Es modelliert, dass derselbe Zustand für jeden Schuss neu präpariert wird; der Zustand bleibt unverändert.
- Die *projektive Messung* von Qubit *k* zieht m ∈ {0, 1} mit P(m) = Σ_{i: bit k = m} |αᵢ|² und ersetzt den Zustand durch P_m|ψ⟩ / √P(m). Werden alle Qubits gemessen, bleibt ein Basiszustand.
- *Zufall.* Ein ganzzahliger Seed liefert reproduzierbare Ergebnisse (`numpy.random.default_rng`). In der App verwendet das Shot-Sampling den Seed direkt (gleicher Seed und Zustand → gleiches Histogramm), während projektive Messungen einen Generator verbrauchen, der beim Zurücksetzen, bei Änderung des Seeds und bei Änderung der Registergröße neu gestartet wird.

**Bloch-Vektor.** Für Qubit *k* liefert die reduzierte Dichtematrix ρ_k = Tr_{others} |ψ⟩⟨ψ| den Vektor r = (Tr ρ_kX, Tr ρ_kY, Tr ρ_kZ) mit ρ_k = (I + r·σ)/2. |r| = 1 für ein reines Qubit, |r| < 1, wenn es mit anderen Qubits verschränkt oder von Rauschen betroffen ist, und die Reinheit ist Tr ρ_k² = (1 + |r|²)/2. Ein verschränktes Register hat keinen einzelnen Bloch-Vektor, daher wird keiner gezeichnet.

**Rauschen.** Nach jedem Gatter wirkt der gewählte Kanal auf jedes Qubit, das dieses Gatter berührt hat (Fehlerwahrscheinlichkeit *p* pro Anwendung):

| Kanal | Abbildung |
|---|---|
| Bit-Flip | ρ → (1 − p)ρ + p XρX |
| Phasen-Flip | ρ → (1 − p)ρ + p ZρZ |
| Depolarisierend | ρ → (1 − p)ρ + (p/3)(XρX + YρY + ZρZ) |

Mit dieser Parametrisierung skaliert der depolarisierende Kanal den Bloch-Vektor um 1 − 4p/3 (p = 3/4 ist der maximal gemischte Zustand). Untätige Qubits und Messungen sind rauschfrei. Die Dichtematrix wird exakt entwickelt; Messungen innerhalb eines verrauschten Schaltkreises werden über ihre Ergebnisse gemittelt.

**Fidelität.** ⟨ψ|ρ|ψ⟩ gegenüber einer reinen Referenz und allgemein die Uhlmann-Fidelität (Tr √(√ρ σ √ρ))².

## Unterstützte Quantengatter

| Gatter | Matrix | Wirkung |
|---|---|---|
| Identity (I) | [[1, 0], [0, 1]] | lässt das Qubit unverändert |
| Pauli-X | [[0, 1], [1, 0]] | Bit-Flip \|0⟩ ↔ \|1⟩ |
| Pauli-Y | [[0, −i], [i, 0]] | Y\|0⟩ = i\|1⟩, Y\|1⟩ = −i\|0⟩ |
| Pauli-Z | [[1, 0], [0, −1]] | Phasen-Flip \|1⟩ → −\|1⟩ |
| Hadamard (H) | [[1, 1], [1, −1]]/√2 | \|0⟩ → \|+⟩, \|1⟩ → \|−⟩ |
| S | diag(1, i) | Phase π/2 |
| T | diag(1, e^{iπ/4}) | Phase π/4 |
| CNOT | \|0⟩⟨0\| ⊗ I + \|1⟩⟨1\| ⊗ X | kippt das Ziel, wenn die Steuerung |1⟩ ist |

Die Python-API bietet zusätzlich `rx`, `ry`, `rz`, `phase`, beliebige Unitäre auf jeder Qubit-Liste und mehrfach gesteuerte Ein-Qubit-Gatter; sie werden von den Teleportations- und Grover-Schaltkreisen verwendet, stehen aber noch nicht in der Seitenleiste.

## Algorithmen und Protokolle

- **Bell-Zustände.** X-Gatter wählen die Eingabe, danach H und CNOT.
- **Teleportation.** Q0 trägt cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩, Q1–Q2 teilen ein Bell-Paar. Alice wendet CNOT und H an und misst Q0 und Q1; Bob wendet X an, falls m₁ = 1, und Z, falls m₀ = 1. Die angezeigte Fidelität wird aus dem simulierten Zustand berechnet und beträgt in allen vier Zweigen 1.
- **Grover.** Orakel = X auf den Null-Bits des markierten Elements, mehrfach gesteuertes Z, erneut X; Diffusion = Hⁿ Xⁿ (MCZ) Xⁿ Hⁿ. Die simulierte Erfolgswahrscheinlichkeit stimmt mit sin²((2k+1)θ), sin θ = 1/√N, überein.
- **Deutsch–Jozsa.** Das Orakel U_f|x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩ wird aus der Wahrheitstabelle von f gebaut. Die App bietet konstante Funktionen, Paritäten ausgewählter Bits und zufällige balancierte Funktionen.

## Architektur

```
quantum-computing-simulation/
├── main.py                  Streamlit interface (widgets, session state, layout)
├── translations.py          original 54 keys × 15 languages + lookup helpers
├── translations_extra.py    80 keys added in 2.0 × 15 languages
├── quantum_lab/             simulation core, no Streamlit imports
│   ├── gates.py             gate matrices, unitarity check, dense reference expansions
│   ├── simulator.py         QuantumSimulator (state vector)
│   ├── measurement.py       probabilities, shot sampling, projective collapse
│   ├── states.py            reduced density matrices, Bloch vectors, entropy
│   ├── circuit.py           Circuit / Operation, execution, text diagram
│   ├── density.py           DensityMatrix (mixed states)
│   ├── noise.py             Kraus channels, noisy circuit simulation
│   ├── protocols.py         Bell, GHZ, teleportation
│   ├── algorithms.py        Grover, Deutsch–Jozsa
│   └── visualization.py     Plotly figures
├── tests/                   pytest suite (500 tests)
├── benchmarks/bench_gates.py
├── docs/AUDIT.md            audit of version 1.0
├── assets/                  screenshots
├── requirements.txt         runtime dependencies
└── requirements-dev.txt     + pytest, ruff
```

Abhängigkeiten zeigen in eine Richtung: `main.py` → `quantum_lab` und `translations`; innerhalb des Pakets ist `visualization` das einzige Modul, das Plotly importiert, und keines importiert Streamlit, sodass der Kern für sich verwendet und getestet werden kann.

## Tests

```bash
pip install -r requirements-dev.txt
pytest
pytest --ignore=tests/test_app.py
ruff check .
python benchmarks/bench_gates.py
```

`pytest` dauert etwa 1,5 Minuten (überwiegend die browserlosen UI-Tests); mit `--ignore=tests/test_app.py` wird nur der Kern getestet, in wenigen Sekunden.

| Datei | Deckt ab |
|---|---|
| `test_gates.py` | Unitarität jedes Gatters, algebraische Identitäten, Kronecker-Erweiterung, CNOT-Matrizen |
| `test_simulator.py` | Normierung, Pauli-/Hadamard-Verhalten, H zweimal, CNOT-Wahrheitstabellen, Bell- und GHZ-Zustände, Vergleich mit dichten Matrizen, ungültige Eingaben |
| `test_measurement.py` | Born-Regel, Randverteilungen, Sampling mit Seed, Statistik, Kollaps und Renormierung |
| `test_states.py` | Partialspur, Bloch-Vektoren, Reinheit, Verschränkungsentropie |
| `test_circuit.py` | Aufbau und Ausführung von Schaltkreisen, bedingte Gatter, Diagrammlayout |
| `test_noise.py` | Kanäle sind spurerhaltend, analytische Ergebnisse, vollständige Summe über Fehlertrajektorien |
| `test_protocols.py` | vier Bell-Zustände, Teleportation in allen vier Zweigen |
| `test_algorithms.py` | Grover gegen die geschlossene Formel, Deutsch-Jozsa für jede balancierte Funktion mit 2 und 3 Eingaben |
| `test_visualization.py` | Abbildungen enthalten die richtigen Daten |
| `test_translations.py` | 15 Sprachen, identische Schlüssel und Platzhalter, jeder von der Oberfläche verwendete Schlüssel existiert |
| `test_app.py` | die Streamlit-App von Anfang bis Ende (headless), in jeder Sprache |

Numerische Vergleiche verwenden Toleranzen (10⁻¹² für Amplituden, 5σ-Bänder für Sampling-Statistiken) statt exakter Gleitkommagleichheit.

Geprüfte Kombinationen: Python 3.11 + NumPy 1.26.4 / Streamlit 1.50.0 / Plotly 5.24.0; Python 3.13 + NumPy 2.5.4 / Streamlit 1.67.0 / Plotly 7.1.0.

## Leistung und Grenzen

| Größe | Zustandsvektor | Dichtematrix |
|---|---|---|
| Speicher | 16 · 2ⁿ bytes | 16 · 4ⁿ bytes |
| Ein k-Qubit-Gatter | O(2ⁿ · 2ᵏ) | O(4ⁿ · 2ᵏ) |
| Harte Grenze im Code | `MAX_QUBITS = 20` (16 MiB) | `MAX_DENSITY_QUBITS = 10` (16 MiB) |
| Grenze in der Oberfläche | 6 qubits | 6 qubits |

Version 1.0 baute für jedes Gatter eine dichte 2ⁿ × 2ⁿ-Matrix; 2.0 kontrahiert das Gatter mit dem Zustandstensor. Gemessen mit `benchmarks/bench_gates.py` (ein Hadamard, bester von mehreren Läufen, eine einzelne Maschine; als Richtwert zu verstehen):

| Qubits | Dichte Matrix (1.0) | Kontraktion (2.0) | Verhältnis |
|---|---|---|---|
| 3 | 35 µs | 40 µs | 0.9× |
| 6 | 100 µs | 43 µs | 2× |
| 8 | 553 µs | 44 µs | 13× |
| 10 | 7.6 ms | 49 µs | 155× |
| 12 | 184 ms | 57 µs | ≈ 3200× |

An der alten Grenze von drei Qubits gibt es keine Beschleunigung (die Eingabeprüfung kostet einige Mikrosekunden); der Nutzen liegt darin, dass größere Register praktikabel wurden. Der Simulationsaufwand verdoppelt sich weiterhin mit jedem Qubit. Dies ist ein Lehrwerkzeug für kleine Register, kein Allzwecksimulator.

## Bekannte Einschränkungen

- Die Oberfläche bietet 1–6 Qubits; die Gatter in der Seitenleiste sind I, X, Y, Z, H, S, T und CNOT. Rotationsgatter gibt es nur in der Python-API.
- Gemessen wird nur in der Rechenbasis (Z).
- Das Rauschen ist Ein-Qubit-Pauli-Rauschen nach Gattern. Es gibt keine Amplitudendämpfung, keinen Auslesefehler, kein Leerlaufrauschen und kein korreliertes Rauschen.
- Grover sucht ein einzelnes markiertes Element; das Deutsch-Jozsa-Orakel wird als eine unitäre Box angewendet und nicht in elementare Gatter zerlegt.
- Der Schaltkreis lässt sich nur erweitern (kein Rückgängig, keine Bearbeitung, kein Drag-and-drop).
- Das Schaltkreisdiagramm ist Text in fester Zeichenbreite; sehr lange Schaltkreise scrollen horizontal.
- Arabisch ist übersetzt, aber das Seitenlayout wird nicht von rechts nach links gespiegelt.
- Die 80 in 2.0 hinzugefügten Zeichenketten wurden ohne Prüfung durch Muttersprachler übersetzt; Korrekturen sind willkommen.
- Keine Verbindung zu echter Quantenhardware oder Cloud-Backends.

## Änderungen gegenüber 1.0, die Sie betreffen können

- **CNOT-Ergebnisse weichen ab, weil die alten falsch waren.** Version 1.0 vermischte zwei Qubit-Reihenfolgen, sodass Schaltkreise aus Ein-Qubit-Gattern und CNOT falsche Zustände lieferten (siehe `docs/AUDIT.md`, Befund Q1).
- `QuantumSimulator` ist von `main.py` nach `quantum_lab` umgezogen. Die Methoden aus 1.0 (`apply_gate`, `get_probabilities`, `get_amplitudes`, `measure`, `reset`, `_expand_gate`, `_create_cnot_matrix`) bleiben erhalten. Ungültige Eingaben lösen jetzt `ValueError`/`TypeError` aus, statt stillschweigend akzeptiert zu werden, `state` ist schreibgeschützt und nicht unitäre Matrizen werden abgelehnt.
- Das Messhistogramm erscheint nach dem Drücken von *Run Measurement* und wird nicht mehr bei jeder Interaktion neu erzeugt.
- Die Diagramme stammen von Plotly statt Matplotlib. Die Schaltflächen *Save …* laden jetzt interaktives HTML herunter; der PNG-Export befindet sich in der Werkzeugleiste jedes Diagramms.
- `matplotlib` und das ungenutzte `qiskit` wurden aus `requirements.txt` entfernt; `plotly` wurde hinzugefügt.

## Bereitstellung auf Streamlit Community Cloud

1. Pushen Sie das Repository (oder Ihren Fork) zu GitHub.
2. Melden Sie sich mit GitHub bei <https://share.streamlit.io> an und erstellen Sie eine neue App.
3. Wählen Sie Repository und Branch und setzen Sie main file path auf `main.py`.
4. Wählen Sie in den advanced settings Python 3.11 oder neuer und stellen Sie dann bereit.

Abhängigkeiten werden aus `requirements.txt` installiert; Secrets oder Umgebungsvariablen sind nicht nötig. Diese Schritte wurden aus Erfahrung mit der Plattform geschrieben und konnten bei der Vorbereitung dieser Version nicht mit der aktuellen Dokumentation abgeglichen werden. Falls die Bildschirme abweichen, folgen Sie <https://docs.streamlit.io/deploy/streamlit-community-cloud>.

Die `.devcontainer`-Konfiguration startet Streamlit mit deaktiviertem CORS- und XSRF-Schutz, was die Portweiterleitung von GitHub Codespaces erfordert. Verwenden Sie diese Optionen nicht für eine öffentliche Bereitstellung.

## Roadmap

- Rotationsgatter (Rx, Ry, Rz) und weitere Zwei-Qubit-Gatter (CZ, SWAP) in der Seitenleiste
- Rückgängig und Schaltkreisbearbeitung; Schaltkreise speichern und laden
- Messung in anderen Basen; Erwartungswerte von Pauli-Observablen
- Kanäle für Amplitudendämpfung und Auslesefehler
- Export von Schaltkreisen nach OpenQASM
- Prüfung der Übersetzungen durch Muttersprachler; Layout von rechts nach links

## Lizenz und Urheberschaft

Veröffentlicht unter der [MIT-Lizenz](LICENSE), Copyright (c) 2025 rasidi3112. Die Lizenzdatei ist unverändert.

Mini Quantum Lab wurde von [Rasidi](https://github.com/rasidi3112) geschaffen, der die ursprüngliche Anwendung, Oberfläche und Übersetzungen geschrieben hat. Version 2.0 (Simulationskern, Tests, Visualisierungen und die neuen Funktionen) baut auf dieser Arbeit auf.
