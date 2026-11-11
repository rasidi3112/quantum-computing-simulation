<h1 align="center">Mini Quantum Lab 2.0</h1>

<p align="center">
  <b>Un simulatore di calcolo quantistico interattivo e testato per imparare</b><br>
  Python · NumPy · Streamlit · Plotly · 15 lingue dell'interfaccia
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="README_ar.md">العربية</a> ·
  <a href="README_de.md">Deutsch</a> ·
  <a href="README_es.md">Español</a> ·
  <a href="README_fr.md">Français</a> ·
  <a href="README_hi.md">हिन्दी</a> ·
  <a href="README_id.md">Bahasa Indonesia</a> ·
  <b>Italiano</b> ·
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

## Panoramica

Mini Quantum Lab è un'applicazione web didattica per esplorare le basi del calcolo quantistico: costruire piccoli circuiti porta dopo porta, osservare il vettore di stato, guardare ogni qubit su una sfera di Bloch, misurare, aggiungere rumore ed eseguire alcuni protocolli e algoritmi da manuale.

La versione 2.0 mantiene l'aspetto e il flusso di lavoro del progetto originale e sostituisce ciò che sta sotto: un pacchetto di simulazione separato con test unitari, un'unica convenzione documentata per l'ordine dei qubit, una misurazione fisicamente coerente e nuove visualizzazioni. L'audit che ha motivato le modifiche si trova in [`docs/AUDIT.md`](docs/AUDIT.md).

> Questo progetto si ispira allo stile visivo di strumenti come IBM Quantum Composer e Qiskit. È un progetto didattico indipendente e **non è affiliato né approvato da IBM** o da altre organizzazioni di calcolo quantistico. Simula qubit ideali e rumorosi su un computer classico; non si collega a hardware quantistico.

## Funzionalità

| Area | Cosa si può fare |
|---|---|
| **Laboratorio** | 1–6 qubit; porte I, X, Y, Z, H, S, T su qualsiasi qubit; CNOT tra due qubit qualsiasi; diagramma del circuito in tempo reale, tabella di stato e cronologia delle porte |
| **Visualizzazione dello stato** | Distribuzione di probabilità, ampiezze reali/immaginarie e fase di ogni ampiezza, con le etichette degli stati di base |
| **Sfera di Bloch** | Sfera 3D interattiva per qubit, disegnata dallo *stato ridotto* del qubit, con lunghezza del vettore e purezza per distinguere stati puri e misti |
| **Misurazione** | Campionamento a colpi (100–10 000 colpi) con seme, e misurazione proiettiva di uno o di tutti i qubit con collasso dello stato |
| **Entanglement** | Generatore dei quattro stati di Bell con entropia e dimostrazione del collasso; teletrasporto quantistico a tre qubit di qualsiasi stato a un qubit |
| **Rumore** | Canali di inversione di bit, inversione di fase e depolarizzante applicati dopo ogni porta, simulati esattamente con una matrice densità |
| **Algoritmi** | Ricerca di Grover (2–5 qubit) e Deutsch–Jozsa (1–4 qubit di ingresso) con spiegazioni e circuiti |
| **Lingue** | English, Indonesian, Spanish, Mandarin Chinese, Arabic, French, Japanese, Korean, German, Portuguese, Russian, Hindi, Turkish, Italian, Vietnamese |

## Schermate

| Laboratorio: circuito, probabilità, ampiezze | Sfere di Bloch (Q0 e Q1 entangled, Q2 puro) |
|---|---|
| <img src="assets/screenshot_lab.png" alt="Lab" width="420"/> | <img src="assets/screenshot_bloch.png" alt="Bloch" width="420"/> |

| Campionamento a colpi e misurazione proiettiva | Teletrasporto quantistico |
|---|---|
| <img src="assets/screenshot_measurement.png" alt="Measurement" width="420"/> | <img src="assets/screenshot_teleportation.png" alt="Teleportation" width="420"/> |

| Rumore: stato di Bell ideale e depolarizzato | Grover e Deutsch–Jozsa |
|---|---|
| <img src="assets/screenshot_noise.png" alt="Noise" width="420"/> | <img src="assets/screenshot_algorithms.png" alt="Algorithms" width="420"/> |

## Installazione

Richiede Python 3.11 o successivo (testato su 3.11 e 3.13).

```bash
git clone https://github.com/rasidi3112/quantum-computing-simulation.git
cd quantum-computing-simulation
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

Poi apri <http://localhost:8501>.

Le dipendenze di esecuzione sono `numpy`, `streamlit` e `plotly`. Il pacchetto di simulazione in sé (`quantum_lab`, senza `visualization`) richiede solo NumPy.

## Utilizzo

1. Scegli il **numero di qubit** nella barra laterale (cambiarlo avvia un nuovo circuito vuoto).
2. Scegli una porta e un qubit bersaglio e premi **Apply Gate**; con due o più qubit, scegli controllo e bersaglio e premi **Apply CNOT**.
3. Leggi il risultato nelle schede:
   - **Lab**: diagramma del circuito, probabilità, ampiezze, fasi, tabella di stato;
   - **Bloch Sphere**: una sfera per qubit;
   - **Measurement**: *Run Measurement* campiona i colpi senza toccare lo stato; *Measure Qubit* / *Measure All Qubits* lo fanno collassare;
   - **Entanglement**, **Noise**, **Algorithms**: dimostrazioni autonome. *Load into Lab* copia un circuito di Bell nel laboratorio.
4. **Reset System** torna a |0…0⟩ e riavvia il generatore casuale dal seme.

I grafici sono interattivi (passaggio del mouse, zoom, rotazione). Il pulsante della fotocamera nella barra degli strumenti di un grafico salva un PNG; i pulsanti *Save …* scaricano un file HTML interattivo autonomo.

### Circuiti di esempio

| Obiettivo | Passi | Risultato atteso |
|---|---|---|
| Sovrapposizione | 1 qubit: H → Q0 | P(0) = P(1) = 0.5; vettore di Bloch su +x |
| Stato di Bell \|Φ+⟩ | 2 qubits: H → Q0, CNOT Q0 → Q1 | (\|00⟩ + \|11⟩)/√2; P(00) = P(11) = 0.5, P(01) = P(10) = 0; entrambi i vettori di Bloch hanno lunghezza 0 |
| H·Z·H = X | 1 qubit: H, Z, H → Q0 | \|1⟩ |
| Stato GHZ | 3 qubits: H → Q0, CNOT Q0 → Q1, CNOT Q1 → Q2 | (\|000⟩ + \|111⟩)/√2 |
| Collasso | Stato di Bell, poi *Measure Qubit* Q0 | \|00⟩ / \|11⟩; Q1 è ora determinato |

```
q0: ──[H]──●──
           │
q1: ───────⊕──
```

### Usare il simulatore da Python

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

## Convenzioni matematiche quantistiche

**Stato.** Un registro di *n* qubit è un vettore complesso di 2ⁿ ampiezze αᵢ con Σ|αᵢ|² = 1, inizializzato a |0…0⟩.

**Ordine dei qubit: big-endian, ovunque.** Il qubit 0 è il bit *più a sinistra* di un'etichetta di base e il filo *in alto* di un diagramma:

```
|q0 q1 … q(n-1)⟩      index = Σ_k q_k · 2^(n-1-k)      |ψ⟩ = |q0⟩ ⊗ |q1⟩ ⊗ … ⊗ |q(n-1)⟩
```

Quindi, con due qubit, X su Q0 trasforma |00⟩ in |10⟩ (indice 2). Una matrice che agisce sulla lista di qubit `[a, b]` tratta `a` come il suo bit più significativo; in particolare `gates.CNOT` è la matrice per `[control, target]`. È la convenzione dei manuali (Nielsen & Chuang). **Qiskit usa l'ordine opposto, little-endian**; inverti le stringhe di bit quando confronti.

**Evoluzione.** L'unitarietà di ogni operatore viene verificata (U†U = I, tolleranza 10⁻¹⁰) prima dell'applicazione, e lo stato non viene mai rinormalizzato durante l'evoluzione unitaria. I test confermano che la norma resta entro 10⁻¹⁰ da 1 dopo 3000 porte.

**Misurazione (base computazionale):**

- Il *campionamento a colpi* estrae risultati da P(i) = |αᵢ|². Modella la nuova preparazione dello stesso stato a ogni colpo; lo stato non cambia.
- La *misurazione proiettiva* del qubit *k* estrae m ∈ {0, 1} con P(m) = Σ_{i: bit k = m} |αᵢ|², poi sostituisce lo stato con P_m|ψ⟩ / √P(m). Misurare tutti i qubit lascia uno stato di base.
- *Casualità.* Un seme intero dà risultati riproducibili (`numpy.random.default_rng`). Nell'app il campionamento a colpi usa direttamente il seme (stesso seme e stato → stesso istogramma), mentre le misurazioni proiettive consumano un generatore che viene riavviato al reset, al cambio del seme e al cambio della dimensione del registro.

**Vettore di Bloch.** Per il qubit *k* la matrice densità ridotta ρ_k = Tr_{others} |ψ⟩⟨ψ| dà r = (Tr ρ_kX, Tr ρ_kY, Tr ρ_kZ) con ρ_k = (I + r·σ)/2. |r| = 1 per un qubit puro, |r| < 1 quando è entangled con altri qubit o soggetto a rumore, e la purezza è Tr ρ_k² = (1 + |r|²)/2. Un registro entangled non ha un unico vettore di Bloch, quindi non ne viene disegnato nessuno.

**Rumore.** Dopo ogni porta il canale selezionato agisce su ogni qubit toccato da quella porta (probabilità di errore *p* per applicazione):

| Canale | Mappa |
|---|---|
| Inversione di bit | ρ → (1 − p)ρ + p XρX |
| Inversione di fase | ρ → (1 − p)ρ + p ZρZ |
| Depolarizzante | ρ → (1 − p)ρ + (p/3)(XρX + YρY + ZρZ) |

Con questa parametrizzazione il canale depolarizzante scala il vettore di Bloch di 1 − 4p/3 (p = 3/4 è lo stato massimamente misto). I qubit inattivi e le misurazioni sono privi di rumore. La matrice densità viene evoluta esattamente; le misurazioni all'interno di un circuito rumoroso sono mediate sui loro risultati.

**Fedeltà.** ⟨ψ|ρ|ψ⟩ rispetto a un riferimento puro, e la fedeltà di Uhlmann (Tr √(√ρ σ √ρ))² in generale.

## Porte quantistiche supportate

| Porta | Matrice | Azione |
|---|---|---|
| Identity (I) | [[1, 0], [0, 1]] | lascia il qubit invariato |
| Pauli-X | [[0, 1], [1, 0]] | inversione di bit \|0⟩ ↔ \|1⟩ |
| Pauli-Y | [[0, −i], [i, 0]] | Y\|0⟩ = i\|1⟩, Y\|1⟩ = −i\|0⟩ |
| Pauli-Z | [[1, 0], [0, −1]] | inversione di fase \|1⟩ → −\|1⟩ |
| Hadamard (H) | [[1, 1], [1, −1]]/√2 | \|0⟩ → \|+⟩, \|1⟩ → \|−⟩ |
| S | diag(1, i) | fase π/2 |
| T | diag(1, e^{iπ/4}) | fase π/4 |
| CNOT | \|0⟩⟨0\| ⊗ I + \|1⟩⟨1\| ⊗ X | inverte il bersaglio se il controllo è |1⟩ |

L'API Python offre inoltre `rx`, `ry`, `rz`, `phase`, unitarie arbitrarie su qualsiasi lista di qubit e porte a un qubit con più controlli; sono usate dai circuiti di teletrasporto e di Grover ma non sono ancora nella barra laterale.

## Algoritmi e protocolli

- **Stati di Bell.** Le porte X selezionano l'ingresso, poi H e CNOT.
- **Teletrasporto.** Q0 porta cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩, Q1–Q2 condividono una coppia di Bell. Alice applica CNOT e H e misura Q0 e Q1; Bob applica X se m₁ = 1 e Z se m₀ = 1. La fedeltà mostrata è calcolata dallo stato simulato e vale 1 in tutti e quattro i rami.
- **Grover.** Oracolo = X sui bit zero dell'elemento marcato, Z multi-controllata, di nuovo X; diffusione = Hⁿ Xⁿ (MCZ) Xⁿ Hⁿ. La probabilità di successo simulata coincide con sin²((2k+1)θ), sin θ = 1/√N.
- **Deutsch–Jozsa.** L'oracolo U_f|x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩ è costruito dalla tabella di verità di f. L'app offre funzioni costanti, parità di bit selezionati e funzioni bilanciate casuali.

## Architettura

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

Le dipendenze vanno in una sola direzione: `main.py` → `quantum_lab` e `translations`; all'interno del pacchetto, `visualization` è l'unico modulo che importa Plotly e nessuno importa Streamlit, quindi il nucleo può essere usato e testato da solo.

## Test

```bash
pip install -r requirements-dev.txt
pytest
pytest --ignore=tests/test_app.py
ruff check .
python benchmarks/bench_gates.py
```

`pytest` richiede circa 1,5 minuti (per lo più i test dell'interfaccia senza browser); con `--ignore=tests/test_app.py` viene testato solo il nucleo, in pochi secondi.

| File | Copre |
|---|---|
| `test_gates.py` | unitarietà di ogni porta, identità algebriche, espansione di Kronecker, matrici CNOT |
| `test_simulator.py` | normalizzazione, comportamento di Pauli/Hadamard, H due volte, tabelle di verità del CNOT, stati di Bell e GHZ, confronto con matrici dense, input non validi |
| `test_measurement.py` | regola di Born, marginali, campionamento con seme, statistiche, collasso e rinormalizzazione |
| `test_states.py` | traccia parziale, vettori di Bloch, purezza, entropia di entanglement |
| `test_circuit.py` | costruzione ed esecuzione dei circuiti, porte condizionate, disposizione del diagramma |
| `test_noise.py` | i canali conservano la traccia, risultati analitici, somma esaustiva sulle traiettorie di errore |
| `test_protocols.py` | i quattro stati di Bell, teletrasporto in tutti e quattro i rami |
| `test_algorithms.py` | Grover rispetto alla formula chiusa, Deutsch–Jozsa per ogni funzione bilanciata a 2 e 3 ingressi |
| `test_visualization.py` | le figure contengono i dati corretti |
| `test_translations.py` | 15 lingue, chiavi e segnaposto identici, ogni chiave usata dall'interfaccia esiste |
| `test_app.py` | l'app Streamlit da un capo all'altro (headless), in ogni lingua |

I confronti numerici usano tolleranze (10⁻¹² per le ampiezze, bande a 5σ per le statistiche di campionamento) anziché l'uguaglianza esatta in virgola mobile.

Combinazioni verificate: Python 3.11 + NumPy 1.26.4 / Streamlit 1.50.0 / Plotly 5.24.0; Python 3.13 + NumPy 2.5.4 / Streamlit 1.67.0 / Plotly 7.1.0.

## Prestazioni e limiti

| Grandezza | Vettore di stato | Matrice densità |
|---|---|---|
| Memoria | 16 · 2ⁿ bytes | 16 · 4ⁿ bytes |
| Una porta a k qubit | O(2ⁿ · 2ᵏ) | O(4ⁿ · 2ᵏ) |
| Limite rigido nel codice | `MAX_QUBITS = 20` (16 MiB) | `MAX_DENSITY_QUBITS = 10` (16 MiB) |
| Limite nell'interfaccia | 6 qubits | 6 qubits |

La versione 1.0 costruiva una matrice densa 2ⁿ × 2ⁿ per ogni porta; la 2.0 contrae la porta con il tensore di stato. Misurato con `benchmarks/bench_gates.py` (una Hadamard, migliore di più esecuzioni, una sola macchina; da considerare indicativo):

| Qubits | Matrice densa (1.0) | Contrazione (2.0) | Rapporto |
|---|---|---|---|
| 3 | 35 µs | 40 µs | 0.9× |
| 6 | 100 µs | 43 µs | 2× |
| 8 | 553 µs | 44 µs | 13× |
| 10 | 7.6 ms | 49 µs | 155× |
| 12 | 184 ms | 57 µs | ≈ 3200× |

Al vecchio limite di tre qubit non c'è accelerazione (la validazione dell'input costa qualche microsecondo); il vantaggio è che registri più grandi sono diventati praticabili. Il costo della simulazione raddoppia comunque a ogni qubit. È uno strumento didattico per piccoli registri, non un simulatore di uso generale.

## Limitazioni note

- L'interfaccia offre 1–6 qubit; le porte nella barra laterale sono I, X, Y, Z, H, S, T e CNOT. Le porte di rotazione esistono solo nell'API Python.
- La misurazione avviene solo nella base computazionale (Z).
- Il rumore è rumore di Pauli a un qubit dopo le porte. Non ci sono smorzamento di ampiezza, errore di lettura, rumore a riposo né rumore correlato.
- Grover cerca un solo elemento marcato; l'oracolo di Deutsch–Jozsa è applicato come un'unica scatola unitaria anziché scomposto in porte elementari.
- Il circuito è solo in aggiunta (niente annulla, niente modifica, niente trascinamento).
- Il diagramma del circuito è testo a spaziatura fissa; i circuiti molto lunghi scorrono in orizzontale.
- L'arabo è tradotto ma il layout della pagina non è speculare da destra a sinistra.
- Le 80 stringhe aggiunte nella 2.0 sono state tradotte senza revisione di madrelingua; le correzioni sono benvenute.
- Nessun collegamento a hardware quantistico reale o a back end cloud.

## Modifiche rispetto alla 1.0 che potrebbero riguardarti

- **I risultati del CNOT sono diversi perché quelli vecchi erano errati.** La 1.0 mescolava due ordinamenti dei qubit, quindi i circuiti che combinavano porte a un qubit con CNOT davano stati sbagliati (vedi `docs/AUDIT.md`, rilievo Q1).
- `QuantumSimulator` è stato spostato da `main.py` a `quantum_lab`. I suoi metodi della 1.0 (`apply_gate`, `get_probabilities`, `get_amplitudes`, `measure`, `reset`, `_expand_gate`, `_create_cnot_matrix`) sono mantenuti. Gli input non validi ora sollevano `ValueError`/`TypeError` invece di essere accettati in silenzio, `state` è di sola lettura e le matrici non unitarie vengono rifiutate.
- L'istogramma di misurazione compare dopo aver premuto *Run Measurement* invece di essere rigenerato a ogni interazione.
- I grafici sono Plotly anziché Matplotlib. I pulsanti *Save …* ora scaricano HTML interattivo; l'esportazione PNG è nella barra degli strumenti di ogni grafico.
- `matplotlib` e `qiskit` (inutilizzato) sono stati rimossi da `requirements.txt`; è stato aggiunto `plotly`.

## Distribuzione su Streamlit Community Cloud

1. Carica il repository (o il tuo fork) su GitHub.
2. Accedi a <https://share.streamlit.io> con GitHub e crea una nuova app.
3. Seleziona repository e branch e imposta main file path su `main.py`.
4. In advanced settings scegli Python 3.11 o successivo, poi esegui il deploy.

Le dipendenze vengono installate da `requirements.txt`; non servono segreti né variabili d'ambiente. Questi passi sono stati scritti in base all'esperienza con la piattaforma e non è stato possibile confrontarli con la documentazione attuale durante la preparazione di questa versione. Se le schermate sono diverse, segui <https://docs.streamlit.io/deploy/streamlit-community-cloud>.

La configurazione `.devcontainer` avvia Streamlit con le protezioni CORS e XSRF disattivate, come richiede l'inoltro delle porte di GitHub Codespaces. Non riutilizzare queste opzioni in una distribuzione pubblica.

## Piano di sviluppo

- Porte di rotazione (Rx, Ry, Rz) e altre porte a due qubit (CZ, SWAP) nella barra laterale
- Annulla e modifica del circuito; salvataggio e caricamento dei circuiti
- Misurazione in altre basi; valori di aspettazione di osservabili di Pauli
- Canali di smorzamento di ampiezza e di errore di lettura
- Esportazione dei circuiti in OpenQASM
- Revisione delle traduzioni da parte di madrelingua; layout da destra a sinistra

## Licenza e attribuzione

Rilasciato sotto [Licenza MIT](LICENSE), Copyright (c) 2025 rasidi3112. Il file di licenza è invariato.

Mini Quantum Lab è stato creato da [Rasidi](https://github.com/rasidi3112), autore dell'applicazione, dell'interfaccia e delle traduzioni originali. La versione 2.0 (nucleo di simulazione, test, visualizzazioni e funzionalità aggiunte) si basa su quel lavoro.
