<h1 align="center">Mini Quantum Lab 2.0</h1>

<p align="center">
  <b>Interaktywny, przetestowany symulator obliczeń kwantowych do nauki</b><br>
  Python · NumPy · Streamlit · Plotly · 15 języków interfejsu
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="README_ar.md">العربية</a> ·
  <a href="README_de.md">Deutsch</a> ·
  <a href="README_es.md">Español</a> ·
  <a href="README_fr.md">Français</a> ·
  <a href="README_hi.md">हिन्दी</a> ·
  <a href="README_id.md">Bahasa Indonesia</a> ·
  <a href="README_it.md">Italiano</a> ·
  <a href="README_ja.md">日本語</a> ·
  <a href="README_ko.md">한국어</a> ·
  <a href="README_ms.md">Bahasa Melayu</a> ·
  <b>Polski</b> ·
  <a href="README_pt.md">Português</a> ·
  <a href="README_ru.md">Русский</a> ·
  <a href="README_tr.md">Türkçe</a> ·
  <a href="README_vi.md">Tiếng Việt</a> ·
  <a href="README_zh.md">中文</a>
</p>

---

## Przegląd

Mini Quantum Lab to edukacyjna aplikacja internetowa do poznawania podstaw obliczeń kwantowych: budowania małych obwodów bramka po bramce, obserwowania wektora stanu, oglądania każdego kubitu na sferze Blocha, wykonywania pomiarów, dodawania szumu oraz uruchamiania kilku podręcznikowych protokołów i algorytmów.

Wersja 2.0 zachowuje wygląd i sposób pracy pierwotnego projektu, a wymienia to, co pod spodem: osobny pakiet symulacyjny z testami jednostkowymi, jedną udokumentowaną konwencję kolejności kubitów, fizycznie spójny pomiar i nowe wizualizacje. Audyt, który był powodem zmian, znajduje się w [`docs/AUDIT.md`](docs/AUDIT.md).

> Projekt jest inspirowany stylem wizualnym narzędzi takich jak IBM Quantum Composer i Qiskit. Jest niezależnym projektem edukacyjnym i **nie jest powiązany z IBM ani przez IBM wspierany**, podobnie jak przez żadną inną organizację zajmującą się obliczeniami kwantowymi. Symuluje idealne i zaszumione kubity na komputerze klasycznym; nie łączy się ze sprzętem kwantowym.

## Funkcje

| Obszar | Co można zrobić |
|---|---|
| **Laboratorium** | 1–6 kubitów; bramki I, X, Y, Z, H, S, T na dowolnym kubicie; CNOT między dowolnymi dwoma kubitami; diagram obwodu na żywo, tabela stanu i historia bramek |
| **Wizualizacja stanu** | Rozkład prawdopodobieństwa, części rzeczywiste i urojone amplitud oraz faza każdej amplitudy, z etykietami stanów bazowych |
| **Sfera Blocha** | Interaktywna sfera 3D dla każdego kubitu, rysowana na podstawie jego *stanu zredukowanego*, z długością wektora i czystością, dzięki czemu można odróżnić stany czyste od mieszanych |
| **Pomiar** | Próbkowanie strzałami (100–10 000 strzałów) z ziarnem oraz pomiar rzutowy jednego lub wszystkich kubitów z kolapsem stanu |
| **Splątanie** | Generator czterech stanów Bella z entropią i demonstracją kolapsu; trójkubitowa teleportacja kwantowa dowolnego stanu jednego kubitu |
| **Szum** | Kanały bit-flip, phase-flip i depolaryzujący stosowane po każdej bramce, symulowane dokładnie za pomocą macierzy gęstości |
| **Algorytmy** | Wyszukiwanie Grovera (2–5 kubitów) i Deutsch–Jozsa (1–4 kubity wejściowe) z objaśnieniami i obwodami |
| **Języki** | English, Indonesian, Spanish, Mandarin Chinese, Arabic, French, Japanese, Korean, German, Portuguese, Russian, Hindi, Turkish, Italian, Vietnamese |

## Zrzuty ekranu

| Laboratorium: obwód, prawdopodobieństwa, amplitudy | Sfery Blocha (Q0 i Q1 splątane, Q2 czysty) |
|---|---|
| <img src="assets/screenshot_lab.png" alt="Lab" width="420"/> | <img src="assets/screenshot_bloch.png" alt="Bloch" width="420"/> |

| Próbkowanie strzałami i pomiar rzutowy | Teleportacja kwantowa |
|---|---|
| <img src="assets/screenshot_measurement.png" alt="Measurement" width="420"/> | <img src="assets/screenshot_teleportation.png" alt="Teleportation" width="420"/> |

| Szum: idealny i zdepolaryzowany stan Bella | Grover i Deutsch–Jozsa |
|---|---|
| <img src="assets/screenshot_noise.png" alt="Noise" width="420"/> | <img src="assets/screenshot_algorithms.png" alt="Algorithms" width="420"/> |

## Instalacja

Wymaga Pythona 3.11 lub nowszego (testowano na 3.11 i 3.13).

```bash
git clone https://github.com/rasidi3112/quantum-computing-simulation.git
cd quantum-computing-simulation
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

Następnie otwórz <http://localhost:8501>.

Zależności uruchomieniowe to `numpy`, `streamlit` i `plotly`. Sam pakiet symulacyjny (`quantum_lab`, bez `visualization`) wymaga tylko NumPy.

## Użytkowanie

1. Wybierz **liczbę kubitów** na pasku bocznym (zmiana rozpoczyna nowy, pusty obwód).
2. Wybierz bramkę i kubit docelowy, po czym naciśnij **Apply Gate**; przy dwóch lub więcej kubitach wybierz kubit sterujący i docelowy i naciśnij **Apply CNOT**.
3. Odczytaj wynik na kartach:
   - **Lab**: diagram obwodu, prawdopodobieństwa, amplitudy, fazy, tabela stanu;
   - **Bloch Sphere**: jedna sfera na kubit;
   - **Measurement**: *Run Measurement* próbkuje strzały bez zmiany stanu; *Measure Qubit* / *Measure All Qubits* powodują jego kolaps;
   - **Entanglement**, **Noise**, **Algorithms**: samodzielne demonstracje. *Load into Lab* kopiuje obwód Bella do laboratorium.
4. **Reset System** wraca do |0…0⟩ i uruchamia generator losowy od nowa z ziarna.

Wykresy są interaktywne (najechanie, powiększanie, obracanie). Przycisk aparatu na pasku narzędzi wykresu zapisuje PNG; przyciski *Save …* pobierają samodzielny interaktywny plik HTML.

### Przykładowe obwody

| Cel | Kroki | Oczekiwany wynik |
|---|---|---|
| Superpozycja | 1 qubit: H → Q0 | P(0) = P(1) = 0.5; wektor Blocha na +x |
| Stan Bella \|Φ+⟩ | 2 qubits: H → Q0, CNOT Q0 → Q1 | (\|00⟩ + \|11⟩)/√2; P(00) = P(11) = 0.5, P(01) = P(10) = 0; oba wektory Blocha mają długość 0 |
| H·Z·H = X | 1 qubit: H, Z, H → Q0 | \|1⟩ |
| Stan GHZ | 3 qubits: H → Q0, CNOT Q0 → Q1, CNOT Q1 → Q2 | (\|000⟩ + \|111⟩)/√2 |
| Kolaps | Stan Bella, potem *Measure Qubit* Q0 | \|00⟩ / \|11⟩; Q1 jest już określony |

```
q0: ──[H]──●──
           │
q1: ───────⊕──
```

### Używanie symulatora z Pythona

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

## Konwencje matematyki kwantowej

**Stan.** Rejestr *n* kubitów to zespolony wektor 2ⁿ amplitud αᵢ z Σ|αᵢ|² = 1, inicjalizowany w |0…0⟩.

**Kolejność kubitów: big-endian, wszędzie.** Kubit 0 to *skrajny lewy* bit etykiety bazowej i *górny* przewód diagramu:

```
|q0 q1 … q(n-1)⟩      index = Σ_k q_k · 2^(n-1-k)      |ψ⟩ = |q0⟩ ⊗ |q1⟩ ⊗ … ⊗ |q(n-1)⟩
```

Zatem dla dwóch kubitów X na Q0 zamienia |00⟩ w |10⟩ (indeks 2). Macierz działająca na listę kubitów `[a, b]` traktuje `a` jako najbardziej znaczący bit; w szczególności `gates.CNOT` to macierz dla `[control, target]`. To konwencja podręcznikowa (Nielsen & Chuang). **Qiskit stosuje kolejność odwrotną, little-endian**; przy porównywaniu odwróć ciągi bitów.

**Ewolucja.** Każdy operator jest sprawdzany pod kątem unitarności (U†U = I, tolerancja 10⁻¹⁰) przed zastosowaniem, a stan nigdy nie jest ponownie normalizowany podczas ewolucji unitarnej. Testy potwierdzają, że po 3000 bramek norma różni się od 1 o mniej niż 10⁻¹⁰.

**Pomiar (baza obliczeniowa):**

- *Próbkowanie strzałami* losuje wyniki z P(i) = |αᵢ|². Modeluje ponowne przygotowanie tego samego stanu dla każdego strzału; stan się nie zmienia.
- *Pomiar rzutowy* kubitu *k* losuje m ∈ {0, 1} z P(m) = Σ_{i: bit k = m} |αᵢ|², a następnie zastępuje stan przez P_m|ψ⟩ / √P(m). Pomiar wszystkich kubitów pozostawia stan bazowy.
- *Losowość.* Całkowite ziarno daje powtarzalne wyniki (`numpy.random.default_rng`). W aplikacji próbkowanie strzałami używa ziarna bezpośrednio (to samo ziarno i stan → ten sam histogram), a pomiary rzutowe korzystają z jednego generatora uruchamianego ponownie przy resecie, zmianie ziarna i zmianie rozmiaru rejestru.

**Wektor Blocha.** Dla kubitu *k* zredukowana macierz gęstości ρ_k = Tr_{others} |ψ⟩⟨ψ| daje r = (Tr ρ_kX, Tr ρ_kY, Tr ρ_kZ), gdzie ρ_k = (I + r·σ)/2. |r| = 1 dla czystego kubitu, |r| < 1, gdy jest splątany z innymi kubitami lub podlega szumowi, a czystość wynosi Tr ρ_k² = (1 + |r|²)/2. Splątany rejestr nie ma jednego wektora Blocha, więc żaden nie jest rysowany.

**Szum.** Po każdej bramce wybrany kanał działa na każdy kubit, którego ta bramka dotknęła (prawdopodobieństwo błędu *p* na zastosowanie):

| Kanał | Odwzorowanie |
|---|---|
| Bit flip | ρ → (1 − p)ρ + p XρX |
| Phase flip | ρ → (1 − p)ρ + p ZρZ |
| Depolaryzujący | ρ → (1 − p)ρ + (p/3)(XρX + YρY + ZρZ) |

Przy tej parametryzacji kanał depolaryzujący skaluje wektor Blocha o 1 − 4p/3 (p = 3/4 to stan maksymalnie mieszany). Bezczynne kubity i pomiary są bezszumowe. Macierz gęstości jest ewoluowana dokładnie; pomiary wewnątrz zaszumionego obwodu są uśredniane po wynikach.

**Wierność.** ⟨ψ|ρ|ψ⟩ względem czystego stanu odniesienia oraz ogólnie wierność Uhlmanna (Tr √(√ρ σ √ρ))².

## Obsługiwane bramki kwantowe

| Bramka | Macierz | Działanie |
|---|---|---|
| Identity (I) | [[1, 0], [0, 1]] | pozostawia kubit bez zmian |
| Pauli-X | [[0, 1], [1, 0]] | odwrócenie bitu \|0⟩ ↔ \|1⟩ |
| Pauli-Y | [[0, −i], [i, 0]] | Y\|0⟩ = i\|1⟩, Y\|1⟩ = −i\|0⟩ |
| Pauli-Z | [[1, 0], [0, −1]] | odwrócenie fazy \|1⟩ → −\|1⟩ |
| Hadamard (H) | [[1, 1], [1, −1]]/√2 | \|0⟩ → \|+⟩, \|1⟩ → \|−⟩ |
| S | diag(1, i) | faza π/2 |
| T | diag(1, e^{iπ/4}) | faza π/4 |
| CNOT | \|0⟩⟨0\| ⊗ I + \|1⟩⟨1\| ⊗ X | odwraca kubit docelowy, gdy sterujący jest w stanie |1⟩ |

API Pythona udostępnia ponadto `rx`, `ry`, `rz`, `phase`, dowolne operacje unitarne na dowolnej liście kubitów oraz wielokrotnie sterowane bramki jednokubitowe; korzystają z nich obwody teleportacji i Grovera, ale nie ma ich jeszcze na pasku bocznym.

## Algorytmy i protokoły

- **Stany Bella.** Bramki X wybierają wejście, potem H i CNOT.
- **Teleportacja.** Q0 niesie cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩, a Q1–Q2 dzielą parę Bella. Alicja stosuje CNOT i H oraz mierzy Q0 i Q1; Bob stosuje X, jeśli m₁ = 1, oraz Z, jeśli m₀ = 1. Wyświetlana wierność jest obliczana z zasymulowanego stanu i wynosi 1 we wszystkich czterech gałęziach.
- **Grover.** Wyrocznia = X na zerowych bitach oznaczonego elementu, wielokrotnie sterowane Z, ponownie X; dyfuzja = Hⁿ Xⁿ (MCZ) Xⁿ Hⁿ. Zasymulowane prawdopodobieństwo sukcesu zgadza się z sin²((2k+1)θ), sin θ = 1/√N.
- **Deutsch–Jozsa.** Wyrocznia U_f|x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩ jest budowana z tablicy prawdy funkcji f. Aplikacja oferuje funkcje stałe, parzystości wybranych bitów i losowe funkcje zrównoważone.

## Architektura

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

Zależności biegną w jednym kierunku: `main.py` → `quantum_lab` i `translations`; wewnątrz pakietu `visualization` jest jedynym modułem importującym Plotly i żaden nie importuje Streamlit, więc rdzeń można używać i testować osobno.

## Testy

```bash
pip install -r requirements-dev.txt
pytest
pytest --ignore=tests/test_app.py
ruff check .
python benchmarks/bench_gates.py
```

`pytest` trwa około 1,5 minuty (głównie testy interfejsu bez przeglądarki); z `--ignore=tests/test_app.py` testowany jest tylko rdzeń, w kilka sekund.

| Plik | Zakres |
|---|---|
| `test_gates.py` | unitarność każdej bramki, tożsamości algebraiczne, rozwinięcie Kroneckera, macierze CNOT |
| `test_simulator.py` | normalizacja, zachowanie bramek Pauliego i Hadamarda, H dwukrotnie, tablice prawdy CNOT, stany Bella i GHZ, porównanie z macierzami gęstymi, błędne dane wejściowe |
| `test_measurement.py` | reguła Borna, rozkłady brzegowe, próbkowanie z ziarnem, statystyka, kolaps i renormalizacja |
| `test_states.py` | ślad częściowy, wektory Blocha, czystość, entropia splątania |
| `test_circuit.py` | budowa i wykonanie obwodów, bramki warunkowe, układ diagramu |
| `test_noise.py` | kanały zachowują ślad, wyniki analityczne, pełna suma po trajektoriach błędów |
| `test_protocols.py` | cztery stany Bella, teleportacja we wszystkich czterech gałęziach |
| `test_algorithms.py` | Grover względem wzoru zamkniętego, Deutsch–Jozsa dla każdej funkcji zrównoważonej o 2 i 3 wejściach |
| `test_visualization.py` | wykresy zawierają poprawne dane |
| `test_translations.py` | 15 języków, identyczne klucze i symbole zastępcze, istnieje każdy klucz używany przez interfejs |
| `test_app.py` | aplikacja Streamlit od początku do końca (headless), w każdym języku |

Porównania numeryczne używają tolerancji (10⁻¹² dla amplitud, pasma 5σ dla statystyk próbkowania) zamiast dokładnej równości zmiennoprzecinkowej.

Zweryfikowane kombinacje: Python 3.11 + NumPy 1.26.4 / Streamlit 1.50.0 / Plotly 5.24.0; Python 3.13 + NumPy 2.5.4 / Streamlit 1.67.0 / Plotly 7.1.0.

## Wydajność i ograniczenia

| Wielkość | Wektor stanu | Macierz gęstości |
|---|---|---|
| Pamięć | 16 · 2ⁿ bytes | 16 · 4ⁿ bytes |
| Jedna bramka k-kubitowa | O(2ⁿ · 2ᵏ) | O(4ⁿ · 2ᵏ) |
| Twardy limit w kodzie | `MAX_QUBITS = 20` (16 MiB) | `MAX_DENSITY_QUBITS = 10` (16 MiB) |
| Limit w interfejsie | 6 qubits | 6 qubits |

Wersja 1.0 budowała gęstą macierz 2ⁿ × 2ⁿ dla każdej bramki; 2.0 kontraktuje bramkę z tensorem stanu. Zmierzono za pomocą `benchmarks/bench_gates.py` (jedna bramka Hadamarda, najlepszy z kilku przebiegów, jedna maszyna; traktować orientacyjnie):

| Qubits | Macierz gęsta (1.0) | Kontrakcja (2.0) | Stosunek |
|---|---|---|---|
| 3 | 35 µs | 40 µs | 0.9× |
| 6 | 100 µs | 43 µs | 2× |
| 8 | 553 µs | 44 µs | 13× |
| 10 | 7.6 ms | 49 µs | 155× |
| 12 | 184 ms | 57 µs | ≈ 3200× |

Przy dawnym limicie trzech kubitów nie ma przyspieszenia (walidacja danych kosztuje kilka mikrosekund); korzyść polega na tym, że większe rejestry stały się praktyczne. Koszt symulacji nadal podwaja się z każdym kubitem. To narzędzie dydaktyczne dla małych rejestrów, a nie symulator ogólnego przeznaczenia.

## Znane ograniczenia

- Interfejs oferuje 1–6 kubitów; bramki na pasku bocznym to I, X, Y, Z, H, S, T i CNOT. Bramki obrotu istnieją tylko w API Pythona.
- Pomiar odbywa się wyłącznie w bazie obliczeniowej (Z).
- Szum to jednokubitowy szum Pauliego po bramkach. Nie ma tłumienia amplitudy, błędu odczytu, szumu bezczynności ani szumu skorelowanego.
- Grover szuka jednego oznaczonego elementu; wyrocznia Deutsch–Jozsa jest stosowana jako jeden blok unitarny, a nie rozkładana na bramki elementarne.
- Do obwodu można tylko dodawać (brak cofania, edycji oraz przeciągania i upuszczania).
- Diagram obwodu to tekst o stałej szerokości; bardzo długie obwody przewijają się w poziomie.
- Język arabski jest przetłumaczony, ale układ strony nie jest odbijany z prawej do lewej.
- 80 tekstów dodanych w 2.0 przetłumaczono bez weryfikacji przez rodzimych użytkowników języka; poprawki są mile widziane.
- Brak połączenia z rzeczywistym sprzętem kwantowym i usługami chmurowymi.

## Zmiany względem 1.0, które mogą Cię dotyczyć

- **Wyniki CNOT są inne, ponieważ stare były błędne.** Wersja 1.0 mieszała dwie kolejności kubitów, więc obwody łączące bramki jednokubitowe z CNOT dawały niepoprawne stany (zob. `docs/AUDIT.md`, ustalenie Q1).
- `QuantumSimulator` przeniesiono z `main.py` do `quantum_lab`. Metody z 1.0 (`apply_gate`, `get_probabilities`, `get_amplitudes`, `measure`, `reset`, `_expand_gate`, `_create_cnot_matrix`) zostały zachowane. Błędne dane zgłaszają teraz `ValueError`/`TypeError`, zamiast być po cichu akceptowane, `state` jest tylko do odczytu, a macierze nieunitarne są odrzucane.
- Histogram pomiaru pojawia się po naciśnięciu *Run Measurement*, zamiast być generowany przy każdej interakcji.
- Wykresy tworzy Plotly zamiast Matplotlib. Przyciski *Save …* pobierają teraz interaktywny HTML; eksport PNG jest na pasku narzędzi każdego wykresu.
- Z `requirements.txt` usunięto `matplotlib` i nieużywany `qiskit`; dodano `plotly`.

## Wdrożenie w Streamlit Community Cloud

1. Wypchnij repozytorium (lub swój fork) na GitHub.
2. Zaloguj się na <https://share.streamlit.io> przez GitHub i utwórz nową aplikację.
3. Wybierz repozytorium i gałąź oraz ustaw main file path na `main.py`.
4. W advanced settings wybierz Pythona 3.11 lub nowszego, a następnie wdróż.

Zależności są instalowane z `requirements.txt`; nie są potrzebne sekrety ani zmienne środowiskowe. Kroki te spisano na podstawie doświadczenia z platformą i podczas przygotowywania tego wydania nie udało się ich porównać z aktualną dokumentacją. Jeśli ekrany wyglądają inaczej, skorzystaj z <https://docs.streamlit.io/deploy/streamlit-community-cloud>.

Konfiguracja `.devcontainer` uruchamia Streamlit z wyłączoną ochroną CORS i XSRF, czego wymaga przekierowanie portów w GitHub Codespaces. Nie używaj tych opcji we wdrożeniu publicznym.

## Plan rozwoju

- Bramki obrotu (Rx, Ry, Rz) i kolejne bramki dwukubitowe (CZ, SWAP) na pasku bocznym
- Cofanie i edycja obwodu; zapisywanie i wczytywanie obwodów
- Pomiar w innych bazach; wartości oczekiwane obserwabli Pauliego
- Kanały tłumienia amplitudy i błędu odczytu
- Eksport obwodów do OpenQASM
- Weryfikacja tłumaczeń przez rodzimych użytkowników języka; układ od prawej do lewej

## Licencja i autorstwo

Wydano na [licencji MIT](LICENSE), Copyright (c) 2025 rasidi3112. Plik licencji pozostaje bez zmian.

Mini Quantum Lab stworzył [Rasidi](https://github.com/rasidi3112), autor pierwotnej aplikacji, interfejsu i tłumaczeń. Wersja 2.0 (rdzeń symulacji, testy, wizualizacje i dodane funkcje) opiera się na tej pracy.
