<h1 align="center">Mini Quantum Lab 2.0</h1>

<p align="center">
  <b>Simulator pengkomputeran kuantum interaktif dan teruji untuk pembelajaran</b><br>
  Python · NumPy · Streamlit · Plotly · 15 bahasa antara muka
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
  <b>Bahasa Melayu</b> ·
  <a href="README_pl.md">Polski</a> ·
  <a href="README_pt.md">Português</a> ·
  <a href="README_ru.md">Русский</a> ·
  <a href="README_tr.md">Türkçe</a> ·
  <a href="README_vi.md">Tiếng Việt</a> ·
  <a href="README_zh.md">中文</a>
</p>

---

## Gambaran keseluruhan

Mini Quantum Lab ialah aplikasi web pendidikan untuk meneroka asas pengkomputeran kuantum: membina litar kecil get demi get, memerhati vektor keadaan, melihat setiap qubit pada sfera Bloch, membuat pengukuran, menambah hingar, serta menjalankan beberapa protokol dan algoritma buku teks.

Versi 2.0 mengekalkan rupa dan aliran kerja projek asal tetapi menggantikan bahagian dalamannya: pakej simulasi berasingan yang diuji unit, satu konvensyen susunan qubit yang didokumenkan, pengukuran yang konsisten secara fizik, dan visualisasi baharu. Audit yang mendorong perubahan ini terdapat dalam [`docs/AUDIT.md`](docs/AUDIT.md).

> Projek ini diilhamkan oleh gaya visual alat seperti IBM Quantum Composer dan Qiskit. Ia projek pendidikan bebas dan **tidak bergabung dengan atau disokong oleh IBM** atau mana-mana organisasi pengkomputeran kuantum lain. Ia mensimulasikan qubit ideal dan berhingar pada komputer klasik dan tidak bersambung ke perkakasan kuantum.

## Ciri-ciri

| Bahagian | Apa yang boleh dilakukan |
|---|---|
| **Makmal** | 1–6 qubit; get I, X, Y, Z, H, S, T pada mana-mana qubit; CNOT antara mana-mana dua qubit; gambar rajah litar langsung, jadual keadaan dan sejarah get |
| **Visualisasi keadaan** | Taburan kebarangkalian, amplitud nyata/khayalan dan fasa setiap amplitud, dengan label keadaan asas |
| **Sfera Bloch** | Sfera 3D interaktif bagi setiap qubit, dilukis daripada *keadaan terturun* qubit, dengan panjang vektor dan ketulenan supaya keadaan tulen dan campuran dapat dibezakan |
| **Pengukuran** | Pensampelan tembakan (100–10 000 tembakan) dengan benih, dan pengukuran unjuran bagi satu atau semua qubit dengan keruntuhan keadaan |
| **Keterbelitan** | Penjana empat keadaan Bell dengan entropi dan demonstrasi keruntuhan; teleportasi kuantum tiga qubit bagi sebarang keadaan satu qubit |
| **Hingar** | Saluran bit-flip, phase-flip dan penyahkutuban yang dikenakan selepas setiap get, disimulasikan secara tepat dengan matriks ketumpatan |
| **Algoritma** | Carian Grover (2–5 qubit) dan Deutsch–Jozsa (1–4 qubit input) dengan penerangan dan litar |
| **Bahasa** | English, Indonesian, Spanish, Mandarin Chinese, Arabic, French, Japanese, Korean, German, Portuguese, Russian, Hindi, Turkish, Italian, Vietnamese |

## Tangkapan skrin

| Makmal: litar, kebarangkalian, amplitud | Sfera Bloch (Q0 dan Q1 terbelit, Q2 tulen) |
|---|---|
| <img src="assets/screenshot_lab.png" alt="Lab" width="420"/> | <img src="assets/screenshot_bloch.png" alt="Bloch" width="420"/> |

| Pensampelan tembakan dan pengukuran unjuran | Teleportasi kuantum |
|---|---|
| <img src="assets/screenshot_measurement.png" alt="Measurement" width="420"/> | <img src="assets/screenshot_teleportation.png" alt="Teleportation" width="420"/> |

| Hingar: keadaan Bell ideal lwn. ternyahkutub | Grover dan Deutsch–Jozsa |
|---|---|
| <img src="assets/screenshot_noise.png" alt="Noise" width="420"/> | <img src="assets/screenshot_algorithms.png" alt="Algorithms" width="420"/> |

## Pemasangan

Memerlukan Python 3.11 atau lebih baharu (diuji pada 3.11 dan 3.13).

```bash
git clone https://github.com/rasidi3112/quantum-computing-simulation.git
cd quantum-computing-simulation
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

Kemudian buka <http://localhost:8501>.

Kebergantungan masa jalan ialah `numpy`, `streamlit` dan `plotly`. Pakej simulasi itu sendiri (`quantum_lab`, tanpa `visualization`) hanya memerlukan NumPy.

## Penggunaan

1. Pilih **bilangan qubit** di bar sisi (menukarnya memulakan litar baharu yang kosong).
2. Pilih get dan qubit sasaran lalu tekan **Apply Gate**; untuk dua qubit atau lebih, pilih kawalan dan sasaran lalu tekan **Apply CNOT**.
3. Baca hasilnya dalam tab:
   - **Lab**: gambar rajah litar, kebarangkalian, amplitud, fasa, jadual keadaan;
   - **Bloch Sphere**: satu sfera bagi setiap qubit;
   - **Measurement**: *Run Measurement* mengambil sampel tembakan tanpa mengubah keadaan; *Measure Qubit* / *Measure All Qubits* meruntuhkannya;
   - **Entanglement**, **Noise**, **Algorithms**: demonstrasi kendiri. *Load into Lab* menyalin litar Bell ke makmal.
4. **Reset System** kembali ke |0…0⟩ dan memulakan semula penjana rawak daripada benih.

Carta adalah interaktif (hover, zum, putar). Butang kamera pada bar alat carta menyimpan PNG; butang *Save …* memuat turun fail HTML interaktif kendiri.

### Contoh litar

| Matlamat | Langkah | Hasil yang dijangka |
|---|---|---|
| Superposisi | 1 qubit: H → Q0 | P(0) = P(1) = 0.5; vektor Bloch pada +x |
| Keadaan Bell \|Φ+⟩ | 2 qubits: H → Q0, CNOT Q0 → Q1 | (\|00⟩ + \|11⟩)/√2; P(00) = P(11) = 0.5, P(01) = P(10) = 0; kedua-dua vektor Bloch berpanjang 0 |
| H·Z·H = X | 1 qubit: H, Z, H → Q0 | \|1⟩ |
| Keadaan GHZ | 3 qubits: H → Q0, CNOT Q0 → Q1, CNOT Q1 → Q2 | (\|000⟩ + \|111⟩)/√2 |
| Keruntuhan | Keadaan Bell, kemudian *Measure Qubit* Q0 | \|00⟩ / \|11⟩; Q1 kini sudah ditentukan |

```
q0: ──[H]──●──
           │
q1: ───────⊕──
```

### Menggunakan simulator daripada Python

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

## Konvensyen matematik kuantum

**Keadaan.** Daftar *n* qubit ialah vektor kompleks dengan 2ⁿ amplitud αᵢ dengan Σ|αᵢ|² = 1, dimulakan pada |0…0⟩.

**Susunan qubit: big-endian, digunakan di semua tempat.** Qubit 0 ialah bit *paling kiri* pada label asas dan wayar *paling atas* pada gambar rajah:

```
|q0 q1 … q(n-1)⟩      index = Σ_k q_k · 2^(n-1-k)      |ψ⟩ = |q0⟩ ⊗ |q1⟩ ⊗ … ⊗ |q(n-1)⟩
```

Jadi dengan dua qubit, X pada Q0 menukar |00⟩ kepada |10⟩ (indeks 2). Matriks yang bertindak pada senarai qubit `[a, b]` menganggap `a` sebagai bit paling bererti; khususnya `gates.CNOT` ialah matriks bagi `[control, target]`. Ini konvensyen buku teks (Nielsen & Chuang). **Qiskit menggunakan susunan bertentangan, little-endian**; terbalikkan rentetan bit semasa membandingkan.

**Evolusi.** Setiap operator disemak keunitarannya (U†U = I, toleransi 10⁻¹⁰) sebelum digunakan, dan keadaan tidak pernah dinormalkan semula semasa evolusi unitari. Ujian mengesahkan norma kekal dalam 10⁻¹⁰ daripada 1 selepas 3000 get.

**Pengukuran (asas pengiraan):**

- *Pensampelan tembakan* mengambil hasil daripada P(i) = |αᵢ|². Ia memodelkan penyediaan semula keadaan yang sama bagi setiap tembakan; keadaan tidak berubah.
- *Pengukuran unjuran* bagi qubit *k* mengambil m ∈ {0, 1} dengan P(m) = Σ_{i: bit k = m} |αᵢ|², kemudian menggantikan keadaan dengan P_m|ψ⟩ / √P(m). Mengukur semua qubit meninggalkan satu keadaan asas.
- *Kerawakan.* Benih integer memberi hasil yang boleh diulang (`numpy.random.default_rng`). Dalam aplikasi, pensampelan tembakan menggunakan benih secara terus (benih dan keadaan sama → histogram sama), manakala pengukuran unjuran menggunakan satu penjana yang dimulakan semula apabila reset, apabila benih berubah dan apabila saiz daftar berubah.

**Vektor Bloch.** Bagi qubit *k*, matriks ketumpatan terturun ρ_k = Tr_{others} |ψ⟩⟨ψ| memberikan r = (Tr ρ_kX, Tr ρ_kY, Tr ρ_kZ) dengan ρ_k = (I + r·σ)/2. |r| = 1 bagi qubit tulen, |r| < 1 apabila ia terbelit dengan qubit lain atau terkesan oleh hingar, dan ketulenan Tr ρ_k² = (1 + |r|²)/2. Daftar yang terbelit tidak mempunyai satu vektor Bloch, maka tiada yang dilukis.

**Hingar.** Selepas setiap get, saluran yang dipilih bertindak pada setiap qubit yang disentuh get itu (kebarangkalian ralat *p* bagi setiap penggunaan):

| Saluran | Pemetaan |
|---|---|
| Bit flip | ρ → (1 − p)ρ + p XρX |
| Phase flip | ρ → (1 − p)ρ + p ZρZ |
| Penyahkutuban | ρ → (1 − p)ρ + (p/3)(XρX + YρY + ZρZ) |

Dengan parameter ini saluran penyahkutuban menskalakan vektor Bloch sebanyak 1 − 4p/3 (p = 3/4 ialah keadaan campuran maksimum). Qubit melahu dan pengukuran bebas hingar. Matriks ketumpatan dievolusikan secara tepat; pengukuran dalam litar berhingar dipuratakan ke atas semua hasilnya.

**Kesetiaan.** ⟨ψ|ρ|ψ⟩ terhadap rujukan tulen, dan kesetiaan Uhlmann (Tr √(√ρ σ √ρ))² secara umum.

## Get kuantum yang disokong

| Get | Matriks | Tindakan |
|---|---|---|
| Identity (I) | [[1, 0], [0, 1]] | membiarkan qubit tidak berubah |
| Pauli-X | [[0, 1], [1, 0]] | bit flip \|0⟩ ↔ \|1⟩ |
| Pauli-Y | [[0, −i], [i, 0]] | Y\|0⟩ = i\|1⟩, Y\|1⟩ = −i\|0⟩ |
| Pauli-Z | [[1, 0], [0, −1]] | phase flip \|1⟩ → −\|1⟩ |
| Hadamard (H) | [[1, 1], [1, −1]]/√2 | \|0⟩ → \|+⟩, \|1⟩ → \|−⟩ |
| S | diag(1, i) | fasa π/2 |
| T | diag(1, e^{iπ/4}) | fasa π/4 |
| CNOT | \|0⟩⟨0\| ⊗ I + \|1⟩⟨1\| ⊗ X | membalikkan sasaran jika kawalan ialah |1⟩ |

API Python turut menyediakan `rx`, `ry`, `rz`, `phase`, unitari sebarang pada mana-mana senarai qubit, dan get satu qubit berbilang kawalan; semuanya digunakan oleh litar teleportasi dan Grover tetapi belum ada di bar sisi.

## Algoritma dan protokol

- **Keadaan Bell.** Get X memilih input, kemudian H dan CNOT.
- **Teleportasi.** Q0 membawa cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩, Q1–Q2 berkongsi pasangan Bell. Alice mengenakan CNOT dan H lalu mengukur Q0, Q1; Bob mengenakan X jika m₁ = 1 dan Z jika m₀ = 1. Kesetiaan yang dipaparkan dikira daripada keadaan simulasi dan bernilai 1 dalam keempat-empat cabang.
- **Grover.** Oracle = X pada bit sifar item bertanda, Z berbilang kawalan, kemudian X sekali lagi; resapan = Hⁿ Xⁿ (MCZ) Xⁿ Hⁿ. Kebarangkalian kejayaan simulasi sepadan dengan sin²((2k+1)θ), sin θ = 1/√N.
- **Deutsch–Jozsa.** Oracle U_f|x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩ dibina daripada jadual kebenaran f. Aplikasi menawarkan fungsi malar, pariti bit terpilih dan fungsi seimbang rawak.

## Seni bina

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

Kebergantungan menghala satu arah: `main.py` → `quantum_lab` dan `translations`; di dalam pakej, `visualization` ialah satu-satunya modul yang mengimport Plotly dan tiada yang mengimport Streamlit, jadi teras boleh digunakan dan diuji secara berasingan.

## Pengujian

```bash
pip install -r requirements-dev.txt
pytest
pytest --ignore=tests/test_app.py
ruff check .
python benchmarks/bench_gates.py
```

`pytest` mengambil kira-kira 1.5 minit (kebanyakannya ujian UI tanpa pelayar); dengan `--ignore=tests/test_app.py` hanya teras diuji, dalam beberapa saat.

| Fail | Liputan |
|---|---|
| `test_gates.py` | keunitaran setiap get, identiti algebra, pengembangan Kronecker, matriks CNOT |
| `test_simulator.py` | penormalan, kelakuan Pauli/Hadamard, H dua kali, jadual kebenaran CNOT, keadaan Bell dan GHZ, perbandingan dengan matriks padat, input tidak sah |
| `test_measurement.py` | peraturan Born, marginal, pensampelan berbenih, statistik, keruntuhan dan penormalan semula |
| `test_states.py` | surih separa, vektor Bloch, ketulenan, entropi keterbelitan |
| `test_circuit.py` | pembinaan dan pelaksanaan litar, get bersyarat, susun atur gambar rajah |
| `test_noise.py` | saluran mengekalkan surih, hasil analitik, hasil tambah menyeluruh ke atas trajektori ralat |
| `test_protocols.py` | empat keadaan Bell, teleportasi dalam keempat-empat cabang |
| `test_algorithms.py` | Grover berbanding bentuk tertutup, Deutsch–Jozsa bagi setiap fungsi seimbang pada 2 dan 3 input |
| `test_visualization.py` | rajah mengandungi data yang betul |
| `test_translations.py` | 15 bahasa, kunci dan pemegang tempat yang serupa, setiap kunci yang digunakan UI wujud |
| `test_app.py` | aplikasi Streamlit dari hujung ke hujung (headless), dalam setiap bahasa |

Perbandingan berangka menggunakan toleransi (10⁻¹² bagi amplitud, jalur 5σ bagi statistik pensampelan) dan bukannya kesamaan titik apung yang tepat.

Gabungan yang disahkan: Python 3.11 + NumPy 1.26.4 / Streamlit 1.50.0 / Plotly 5.24.0; Python 3.13 + NumPy 2.5.4 / Streamlit 1.67.0 / Plotly 7.1.0.

## Prestasi dan had

| Kuantiti | Vektor keadaan | Matriks ketumpatan |
|---|---|---|
| Memori | 16 · 2ⁿ bytes | 16 · 4ⁿ bytes |
| Satu get k-qubit | O(2ⁿ · 2ᵏ) | O(4ⁿ · 2ᵏ) |
| Had keras dalam kod | `MAX_QUBITS = 20` (16 MiB) | `MAX_DENSITY_QUBITS = 10` (16 MiB) |
| Had dalam antara muka | 6 qubits | 6 qubits |

Versi 1.0 membina matriks padat 2ⁿ × 2ⁿ bagi setiap get; versi 2.0 mengecutkan get dengan tensor keadaan. Diukur dengan `benchmarks/bench_gates.py` (satu Hadamard, terbaik daripada beberapa larian, satu mesin; anggap sebagai petunjuk):

| Qubits | Matriks padat (1.0) | Pengecutan (2.0) | Nisbah |
|---|---|---|---|
| 3 | 35 µs | 40 µs | 0.9× |
| 6 | 100 µs | 43 µs | 2× |
| 8 | 553 µs | 44 µs | 13× |
| 10 | 7.6 ms | 49 µs | 155× |
| 12 | 184 ms | 57 µs | ≈ 3200× |

Pada had lama tiga qubit tiada pecutan (pengesahan input mengambil beberapa mikrosaat); manfaatnya ialah daftar yang lebih besar menjadi praktikal. Kos simulasi tetap berganda bagi setiap qubit tambahan. Ini alat pengajaran untuk daftar kecil, bukan simulator serba guna.

## Had yang diketahui

- Antara muka menawarkan 1–6 qubit; get di bar sisi ialah I, X, Y, Z, H, S, T dan CNOT. Get putaran hanya wujud dalam API Python.
- Pengukuran hanya pada asas pengiraan (Z).
- Hingar ialah hingar Pauli satu qubit selepas get. Tiada redaman amplitud, ralat bacaan, hingar semasa melahu atau hingar berkorelasi.
- Grover mencari satu item bertanda; oracle Deutsch–Jozsa dikenakan sebagai satu kotak unitari dan tidak diuraikan kepada get asas.
- Litar hanya boleh ditambah (tiada undo, tiada penyuntingan, tiada seret dan lepas).
- Gambar rajah litar ialah teks monospace; litar yang sangat panjang menatal secara mendatar.
- Bahasa Arab diterjemahkan tetapi susun atur halaman tidak dicerminkan kanan-ke-kiri.
- 80 rentetan yang ditambah dalam 2.0 diterjemahkan tanpa semakan penutur asli; pembetulan dialu-alukan.
- Tiada sambungan ke perkakasan kuantum sebenar atau back end awan.

## Perubahan daripada 1.0 yang mungkin menjejaskan anda

- **Hasil CNOT berbeza kerana yang lama salah.** Versi 1.0 mencampurkan dua susunan qubit, jadi litar yang menggabungkan get satu qubit dengan CNOT memberi keadaan yang salah (lihat `docs/AUDIT.md`, penemuan Q1).
- `QuantumSimulator` berpindah dari `main.py` ke `quantum_lab`. Kaedah 1.0 (`apply_gate`, `get_probabilities`, `get_amplitudes`, `measure`, `reset`, `_expand_gate`, `_create_cnot_matrix`) dikekalkan. Input tidak sah kini menimbulkan `ValueError`/`TypeError` dan tidak lagi diterima secara senyap, `state` baca sahaja, dan matriks bukan unitari ditolak.
- Histogram pengukuran muncul selepas menekan *Run Measurement*, tidak lagi dijana semula pada setiap interaksi.
- Plot menggunakan Plotly, bukan Matplotlib. Butang *Save …* kini memuat turun HTML interaktif; eksport PNG ada pada bar alat setiap carta.
- `matplotlib` dan `qiskit` yang tidak digunakan dibuang daripada `requirements.txt`; `plotly` ditambah.

## Penggunaan di Streamlit Community Cloud

1. Tolak repositori (atau fork anda) ke GitHub.
2. Log masuk di <https://share.streamlit.io> dengan GitHub dan cipta app baharu.
3. Pilih repositori dan cabang, dan tetapkan main file path kepada `main.py`.
4. Dalam advanced settings pilih Python 3.11 atau lebih baharu, kemudian deploy.

Kebergantungan dipasang daripada `requirements.txt`; tiada rahsia atau pemboleh ubah persekitaran diperlukan. Langkah ini ditulis berdasarkan pengalaman dengan platform tersebut dan tidak dapat disemak dengan dokumentasi semasanya ketika keluaran ini disediakan. Jika skrinnya berbeza, ikuti <https://docs.streamlit.io/deploy/streamlit-community-cloud>.

Konfigurasi `.devcontainer` memulakan Streamlit dengan perlindungan CORS dan XSRF dilumpuhkan, yang diperlukan oleh pemajuan port GitHub Codespaces. Jangan gunakan bendera itu untuk penggunaan awam.

## Hala tuju

- Get putaran (Rx, Ry, Rz) dan lebih banyak get dua qubit (CZ, SWAP) di bar sisi
- Undo dan penyuntingan litar; simpan dan muat litar
- Pengukuran pada asas lain; nilai jangkaan bagi pemerhati Pauli
- Saluran redaman amplitud dan ralat bacaan
- Eksport litar ke OpenQASM
- Semakan terjemahan oleh penutur asli; susun atur kanan-ke-kiri

## Lesen dan atribusi

Dikeluarkan di bawah [Lesen MIT](LICENSE), Copyright (c) 2025 rasidi3112. Fail lesen tidak diubah.

Mini Quantum Lab dicipta oleh [Rasidi](https://github.com/rasidi3112), yang menulis aplikasi, antara muka dan terjemahan asal. Versi 2.0 (teras simulasi, ujian, visualisasi dan ciri tambahan) dibina di atas karya itu.
