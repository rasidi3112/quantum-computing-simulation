<h1 align="center">Mini Quantum Lab 2.0</h1>

<p align="center">
  <b>Simulator komputasi kuantum interaktif dan teruji untuk belajar</b><br>
  Python · NumPy · Streamlit · Plotly · 15 bahasa antarmuka
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="README_ar.md">العربية</a> ·
  <a href="README_de.md">Deutsch</a> ·
  <a href="README_es.md">Español</a> ·
  <a href="README_fr.md">Français</a> ·
  <a href="README_hi.md">हिन्दी</a> ·
  <b>Bahasa Indonesia</b> ·
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

## Ringkasan

Mini Quantum Lab adalah aplikasi web edukatif untuk menjelajahi dasar-dasar komputasi kuantum: menyusun sirkuit kecil gate demi gate, mengamati state vector, melihat setiap qubit pada Bloch sphere, melakukan pengukuran, menambahkan noise, serta menjalankan beberapa protokol dan algoritma buku teks.

Versi 2.0 mempertahankan tampilan dan alur kerja proyek asli, tetapi mengganti bagian dalamnya: paket simulasi terpisah yang diuji unit, satu konvensi urutan qubit yang terdokumentasi, pengukuran yang konsisten secara fisika, dan visualisasi baru. Audit yang melatarbelakangi perubahan ini ada di [`docs/AUDIT.md`](docs/AUDIT.md).

> Proyek ini terinspirasi gaya visual alat seperti IBM Quantum Composer dan Qiskit. Ini adalah proyek edukasi independen dan **tidak berafiliasi dengan maupun didukung oleh IBM** atau organisasi komputasi kuantum lain. Proyek ini mensimulasikan qubit ideal dan ber-noise pada komputer klasik dan tidak terhubung ke perangkat keras kuantum.

## Fitur

| Area | Yang dapat dilakukan |
|---|---|
| **Lab** | 1–6 qubit; gate I, X, Y, Z, H, S, T pada qubit mana pun; CNOT antara dua qubit mana pun; diagram sirkuit langsung, tabel state, dan riwayat gate |
| **Visualisasi state** | Distribusi probabilitas, amplitudo real/imajiner, dan fase setiap amplitudo, lengkap dengan label basis state |
| **Bloch sphere** | Bola 3D interaktif per qubit yang digambar dari *reduced state* qubit, dengan panjang vektor dan kemurnian sehingga state murni dan campuran dapat dibedakan |
| **Pengukuran** | Sampling shot (100–10 000 shot) dengan seed, serta pengukuran proyektif satu atau semua qubit dengan collapse state |
| **Entanglement** | Generator empat Bell state dengan entropi dan demonstrasi collapse; teleportasi kuantum tiga qubit untuk sembarang state satu qubit |
| **Noise** | Kanal bit-flip, phase-flip, dan depolarisasi yang diterapkan setelah setiap gate, disimulasikan secara eksak dengan density matrix |
| **Algoritma** | Pencarian Grover (2–5 qubit) dan Deutsch–Jozsa (1–4 qubit input) dengan penjelasan dan sirkuit |
| **Bahasa** | English, Indonesian, Spanish, Mandarin Chinese, Arabic, French, Japanese, Korean, German, Portuguese, Russian, Hindi, Turkish, Italian, Vietnamese |

## Tangkapan layar

| Lab: sirkuit, probabilitas, amplitudo | Bloch sphere (Q0 dan Q1 ter-entangle, Q2 murni) |
|---|---|
| <img src="assets/screenshot_lab.png" alt="Lab" width="420"/> | <img src="assets/screenshot_bloch.png" alt="Bloch" width="420"/> |

| Sampling shot dan pengukuran proyektif | Teleportasi kuantum |
|---|---|
| <img src="assets/screenshot_measurement.png" alt="Measurement" width="420"/> | <img src="assets/screenshot_teleportation.png" alt="Teleportation" width="420"/> |

| Noise: Bell state ideal vs. terdepolarisasi | Grover dan Deutsch–Jozsa |
|---|---|
| <img src="assets/screenshot_noise.png" alt="Noise" width="420"/> | <img src="assets/screenshot_algorithms.png" alt="Algorithms" width="420"/> |

## Instalasi

Membutuhkan Python 3.11 atau lebih baru (diuji pada 3.11 dan 3.13).

```bash
git clone https://github.com/rasidi3112/quantum-computing-simulation.git
cd quantum-computing-simulation
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

Lalu buka <http://localhost:8501>.

Dependensi runtime adalah `numpy`, `streamlit`, dan `plotly`. Paket simulasinya sendiri (`quantum_lab`, tanpa `visualization`) hanya membutuhkan NumPy.

## Penggunaan

1. Pilih **jumlah qubit** di sidebar (mengubahnya memulai sirkuit baru yang kosong).
2. Pilih gate dan qubit target lalu tekan **Apply Gate**; untuk dua qubit atau lebih, pilih control dan target lalu tekan **Apply CNOT**.
3. Baca hasilnya di tab:
   - **Lab**: diagram sirkuit, probabilitas, amplitudo, fase, tabel state;
   - **Bloch Sphere**: satu bola per qubit;
   - **Measurement**: *Run Measurement* mengambil sampel shot tanpa mengubah state; *Measure Qubit* / *Measure All Qubits* membuatnya collapse;
   - **Entanglement**, **Noise**, **Algorithms**: demonstrasi mandiri. *Load into Lab* menyalin sirkuit Bell ke lab.
4. **Reset System** mengembalikan ke |0…0⟩ dan memulai ulang generator acak dari seed.

Grafik bersifat interaktif (hover, zoom, putar). Tombol kamera pada toolbar grafik menyimpan PNG; tombol *Save …* mengunduh berkas HTML interaktif mandiri.

### Contoh sirkuit

| Tujuan | Langkah | Hasil yang diharapkan |
|---|---|---|
| Superposisi | 1 qubit: H → Q0 | P(0) = P(1) = 0.5; vektor Bloch pada +x |
| Bell state \|Φ+⟩ | 2 qubits: H → Q0, CNOT Q0 → Q1 | (\|00⟩ + \|11⟩)/√2; P(00) = P(11) = 0.5, P(01) = P(10) = 0; kedua vektor Bloch berpanjang 0 |
| H·Z·H = X | 1 qubit: H, Z, H → Q0 | \|1⟩ |
| State GHZ | 3 qubits: H → Q0, CNOT Q0 → Q1, CNOT Q1 → Q2 | (\|000⟩ + \|111⟩)/√2 |
| Collapse | Bell state, lalu *Measure Qubit* Q0 | \|00⟩ / \|11⟩; Q1 kini sudah tertentu |

```
q0: ──[H]──●──
           │
q1: ───────⊕──
```

### Menggunakan simulator dari Python

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

## Konvensi matematika kuantum

**State.** Register *n* qubit adalah vektor kompleks berisi 2ⁿ amplitudo αᵢ dengan Σ|αᵢ|² = 1, diinisialisasi ke |0…0⟩.

**Urutan qubit: big-endian, dipakai di mana-mana.** Qubit 0 adalah bit *paling kiri* pada label basis dan kawat *paling atas* pada diagram:

```
|q0 q1 … q(n-1)⟩      index = Σ_k q_k · 2^(n-1-k)      |ψ⟩ = |q0⟩ ⊗ |q1⟩ ⊗ … ⊗ |q(n-1)⟩
```

Jadi pada dua qubit, X pada Q0 mengubah |00⟩ menjadi |10⟩ (indeks 2). Matriks yang bekerja pada daftar qubit `[a, b]` memperlakukan `a` sebagai bit paling signifikan; khususnya `gates.CNOT` adalah matriks untuk `[control, target]`. Ini konvensi buku teks (Nielsen & Chuang). **Qiskit memakai urutan sebaliknya, little-endian**; balik string bitnya saat membandingkan.

**Evolusi.** Setiap operator diperiksa unitaritasnya (U†U = I, toleransi 10⁻¹⁰) sebelum diterapkan, dan state tidak pernah dinormalisasi ulang selama evolusi uniter. Tes memastikan norma tetap dalam 10⁻¹⁰ dari 1 setelah 3000 gate.

**Pengukuran (basis komputasi):**

- *Sampling shot* mengambil hasil dari P(i) = |αᵢ|². Ini memodelkan penyiapan ulang state yang sama untuk setiap shot; state tidak berubah.
- *Pengukuran proyektif* pada qubit *k* mengambil m ∈ {0, 1} dengan P(m) = Σ_{i: bit k = m} |αᵢ|², lalu mengganti state dengan P_m|ψ⟩ / √P(m). Mengukur semua qubit menyisakan satu basis state.
- *Keacakan.* Seed bilangan bulat memberi hasil yang dapat diulang (`numpy.random.default_rng`). Di aplikasi, sampling shot memakai seed secara langsung (seed dan state sama → histogram sama), sedangkan pengukuran proyektif memakai satu generator yang dimulai ulang saat reset, saat seed berubah, dan saat ukuran register berubah.

**Vektor Bloch.** Untuk qubit *k*, reduced density matrix ρ_k = Tr_{others} |ψ⟩⟨ψ| memberikan r = (Tr ρ_kX, Tr ρ_kY, Tr ρ_kZ) dengan ρ_k = (I + r·σ)/2. |r| = 1 untuk qubit murni, |r| < 1 bila qubit ter-entangle dengan qubit lain atau terkena noise, dan kemurnian Tr ρ_k² = (1 + |r|²)/2. Register yang ter-entangle tidak punya satu vektor Bloch, jadi tidak digambar.

**Noise.** Setelah setiap gate, kanal yang dipilih bekerja pada tiap qubit yang dikenai gate itu (probabilitas galat *p* per penerapan):

| Kanal | Pemetaan |
|---|---|
| Bit flip | ρ → (1 − p)ρ + p XρX |
| Phase flip | ρ → (1 − p)ρ + p ZρZ |
| Depolarisasi | ρ → (1 − p)ρ + (p/3)(XρX + YρY + ZρZ) |

Dengan parametrisasi ini kanal depolarisasi menskalakan vektor Bloch sebesar 1 − 4p/3 (p = 3/4 adalah state campuran maksimal). Qubit yang diam dan pengukuran bebas noise. Density matrix dievolusikan secara eksak; pengukuran di dalam sirkuit ber-noise dirata-ratakan atas semua hasilnya.

**Fidelitas.** ⟨ψ|ρ|ψ⟩ terhadap referensi murni, dan fidelitas Uhlmann (Tr √(√ρ σ √ρ))² secara umum.

## Gate kuantum yang didukung

| Gate | Matriks | Aksi |
|---|---|---|
| Identity (I) | [[1, 0], [0, 1]] | membiarkan qubit tidak berubah |
| Pauli-X | [[0, 1], [1, 0]] | bit flip \|0⟩ ↔ \|1⟩ |
| Pauli-Y | [[0, −i], [i, 0]] | Y\|0⟩ = i\|1⟩, Y\|1⟩ = −i\|0⟩ |
| Pauli-Z | [[1, 0], [0, −1]] | phase flip \|1⟩ → −\|1⟩ |
| Hadamard (H) | [[1, 1], [1, −1]]/√2 | \|0⟩ → \|+⟩, \|1⟩ → \|−⟩ |
| S | diag(1, i) | fase π/2 |
| T | diag(1, e^{iπ/4}) | fase π/4 |
| CNOT | \|0⟩⟨0\| ⊗ I + \|1⟩⟨1\| ⊗ X | membalik target jika control bernilai |1⟩ |

API Python juga menyediakan `rx`, `ry`, `rz`, `phase`, uniter sembarang pada daftar qubit mana pun, dan gate satu qubit multi-control; semuanya dipakai oleh sirkuit teleportasi dan Grover tetapi belum ada di sidebar.

## Algoritma dan protokol

- **Bell state.** Gate X memilih input, lalu H dan CNOT.
- **Teleportasi.** Q0 membawa cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩, Q1–Q2 berbagi pasangan Bell. Alice menerapkan CNOT dan H lalu mengukur Q0, Q1; Bob menerapkan X jika m₁ = 1 dan Z jika m₀ = 1. Fidelitas yang ditampilkan dihitung dari state hasil simulasi dan bernilai 1 di keempat cabang.
- **Grover.** Oracle = X pada bit nol dari item bertanda, Z multi-control, lalu X lagi; difusi = Hⁿ Xⁿ (MCZ) Xⁿ Hⁿ. Probabilitas sukses hasil simulasi cocok dengan sin²((2k+1)θ), sin θ = 1/√N.
- **Deutsch–Jozsa.** Oracle U_f|x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩ dibangun dari tabel kebenaran f. Aplikasi menyediakan fungsi konstan, paritas bit terpilih, dan fungsi seimbang acak.

## Arsitektur

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

Dependensi mengarah satu arah: `main.py` → `quantum_lab` dan `translations`; di dalam paket, `visualization` adalah satu-satunya modul yang mengimpor Plotly dan tidak ada yang mengimpor Streamlit, sehingga inti simulasi dapat dipakai dan diuji secara terpisah.

## Pengujian

```bash
pip install -r requirements-dev.txt
pytest
pytest --ignore=tests/test_app.py
ruff check .
python benchmarks/bench_gates.py
```

`pytest` memakan sekitar 1,5 menit (sebagian besar untuk tes UI tanpa browser); dengan `--ignore=tests/test_app.py` hanya inti yang diuji, dalam beberapa detik.

| Berkas | Cakupan |
|---|---|
| `test_gates.py` | unitaritas setiap gate, identitas aljabar, ekspansi Kronecker, matriks CNOT |
| `test_simulator.py` | normalisasi, perilaku Pauli/Hadamard, H dua kali, tabel kebenaran CNOT, state Bell dan GHZ, perbandingan dengan matriks padat, input tidak valid |
| `test_measurement.py` | aturan Born, marginal, sampling ber-seed, statistik, collapse dan renormalisasi |
| `test_states.py` | partial trace, vektor Bloch, kemurnian, entropi entanglement |
| `test_circuit.py` | penyusunan dan eksekusi sirkuit, gate terkondisi, tata letak diagram |
| `test_noise.py` | kanal mempertahankan trace, hasil analitik, penjumlahan menyeluruh atas lintasan galat |
| `test_protocols.py` | empat Bell state, teleportasi di keempat cabang |
| `test_algorithms.py` | Grover terhadap bentuk tertutup, Deutsch–Jozsa untuk setiap fungsi seimbang pada 2 dan 3 input |
| `test_visualization.py` | figur memuat data yang benar |
| `test_translations.py` | 15 bahasa, kunci dan placeholder identik, setiap kunci yang dipakai UI tersedia |
| `test_app.py` | aplikasi Streamlit dari ujung ke ujung (headless), di setiap bahasa |

Perbandingan numerik memakai toleransi (10⁻¹² untuk amplitudo, pita 5σ untuk statistik sampling), bukan kesetaraan floating-point eksak.

Kombinasi yang terverifikasi: Python 3.11 + NumPy 1.26.4 / Streamlit 1.50.0 / Plotly 5.24.0; Python 3.13 + NumPy 2.5.4 / Streamlit 1.67.0 / Plotly 7.1.0.

## Performa dan batasan

| Besaran | State vector | Density matrix |
|---|---|---|
| Memori | 16 · 2ⁿ bytes | 16 · 4ⁿ bytes |
| Satu gate k-qubit | O(2ⁿ · 2ᵏ) | O(4ⁿ · 2ᵏ) |
| Batas keras di kode | `MAX_QUBITS = 20` (16 MiB) | `MAX_DENSITY_QUBITS = 10` (16 MiB) |
| Batas di antarmuka | 6 qubits | 6 qubits |

Versi 1.0 membangun matriks padat 2ⁿ × 2ⁿ untuk setiap gate; versi 2.0 mengontraksikan gate dengan tensor state. Diukur dengan `benchmarks/bench_gates.py` (satu Hadamard, terbaik dari beberapa kali jalan, satu mesin; anggap indikatif):

| Qubits | Matriks padat (1.0) | Kontraksi (2.0) | Rasio |
|---|---|---|---|
| 3 | 35 µs | 40 µs | 0.9× |
| 6 | 100 µs | 43 µs | 2× |
| 8 | 553 µs | 44 µs | 13× |
| 10 | 7.6 ms | 49 µs | 155× |
| 12 | 184 ms | 57 µs | ≈ 3200× |

Pada batas lama tiga qubit tidak ada percepatan (validasi input memakan beberapa mikrodetik); manfaatnya adalah register yang lebih besar menjadi praktis. Biaya simulasi tetap berlipat dua untuk setiap tambahan qubit. Ini alat belajar untuk register kecil, bukan simulator serbaguna.

## Keterbatasan yang diketahui

- Antarmuka menyediakan 1–6 qubit; gate di sidebar adalah I, X, Y, Z, H, S, T, dan CNOT. Gate rotasi hanya ada di API Python.
- Pengukuran hanya pada basis komputasi (Z).
- Noise berupa noise Pauli satu qubit setelah gate. Tidak ada amplitude damping, galat pembacaan, noise saat diam, maupun noise berkorelasi.
- Grover mencari satu item bertanda; oracle Deutsch–Jozsa diterapkan sebagai satu kotak uniter, tidak diuraikan menjadi gate elementer.
- Sirkuit hanya bisa ditambah (tanpa undo, tanpa penyuntingan, tanpa drag and drop).
- Diagram sirkuit berupa teks monospace; sirkuit yang sangat panjang bergulir secara horizontal.
- Bahasa Arab diterjemahkan tetapi tata letak halaman tidak dicerminkan kanan-ke-kiri.
- 80 string yang ditambahkan di 2.0 diterjemahkan tanpa tinjauan penutur asli; koreksi dipersilakan.
- Tidak ada koneksi ke perangkat keras kuantum nyata atau back end cloud.

## Perubahan dari 1.0 yang mungkin memengaruhi Anda

- **Hasil CNOT berbeda karena yang lama keliru.** Versi 1.0 mencampur dua urutan qubit, sehingga sirkuit yang menggabungkan gate satu qubit dengan CNOT memberi state yang salah (lihat `docs/AUDIT.md`, temuan Q1).
- `QuantumSimulator` pindah dari `main.py` ke `quantum_lab`. Metode 1.0 (`apply_gate`, `get_probabilities`, `get_amplitudes`, `measure`, `reset`, `_expand_gate`, `_create_cnot_matrix`) dipertahankan. Input tidak valid kini memunculkan `ValueError`/`TypeError` alih-alih diterima diam-diam, `state` hanya-baca, dan matriks non-uniter ditolak.
- Histogram pengukuran muncul setelah menekan *Run Measurement*, tidak lagi dibuat ulang pada setiap interaksi.
- Grafik memakai Plotly, bukan Matplotlib. Tombol *Save …* kini mengunduh HTML interaktif; ekspor PNG ada di toolbar tiap grafik.
- `matplotlib` dan `qiskit` yang tidak terpakai dihapus dari `requirements.txt`; `plotly` ditambahkan.

## Deploy ke Streamlit Community Cloud

1. Push repositori (atau fork Anda) ke GitHub.
2. Masuk ke <https://share.streamlit.io> dengan GitHub dan buat app baru.
3. Pilih repositori dan branch, lalu isi main file path dengan `main.py`.
4. Di advanced settings pilih Python 3.11 atau lebih baru, lalu deploy.

Dependensi dipasang dari `requirements.txt`; tidak perlu secret atau variabel lingkungan. Langkah ini ditulis berdasarkan pengalaman dengan platform tersebut dan belum dapat dicek terhadap dokumentasi terkininya saat rilis ini disiapkan. Jika tampilannya berbeda, ikuti <https://docs.streamlit.io/deploy/streamlit-community-cloud>.

Konfigurasi `.devcontainer` menjalankan Streamlit dengan proteksi CORS dan XSRF dinonaktifkan, yang dibutuhkan port forwarding GitHub Codespaces. Jangan gunakan flag tersebut untuk deployment publik.

## Peta jalan

- Gate rotasi (Rx, Ry, Rz) dan gate dua qubit lain (CZ, SWAP) di sidebar
- Undo dan penyuntingan sirkuit; simpan dan muat sirkuit
- Pengukuran pada basis lain; nilai ekspektasi observabel Pauli
- Kanal amplitude damping dan galat pembacaan
- Ekspor sirkuit ke OpenQASM
- Tinjauan terjemahan oleh penutur asli; tata letak kanan-ke-kiri

## Lisensi dan atribusi

Dirilis di bawah [Lisensi MIT](LICENSE), Copyright (c) 2025 rasidi3112. Berkas lisensi tidak diubah.

Mini Quantum Lab dibuat oleh [Rasidi](https://github.com/rasidi3112), yang menulis aplikasi, antarmuka, dan terjemahan aslinya. Versi 2.0 (inti simulasi, tes, visualisasi, dan fitur tambahan) dibangun di atas karya tersebut.
