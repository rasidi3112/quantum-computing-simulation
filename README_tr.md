<h1 align="center">Mini Quantum Lab 2.0</h1>

<p align="center">
  <b>Öğrenmek için etkileşimli ve test edilmiş bir kuantum hesaplama simülatörü</b><br>
  Python · NumPy · Streamlit · Plotly · 15 arayüz dili
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
  <a href="README_pl.md">Polski</a> ·
  <a href="README_pt.md">Português</a> ·
  <a href="README_ru.md">Русский</a> ·
  <b>Türkçe</b> ·
  <a href="README_vi.md">Tiếng Việt</a> ·
  <a href="README_zh.md">中文</a>
</p>

---

## Genel bakış

Mini Quantum Lab, kuantum hesaplamanın temellerini keşfetmek için hazırlanmış eğitsel bir web uygulamasıdır: küçük devreleri kapı kapı kurabilir, durum vektörünü izleyebilir, her kübiti Bloch küresinde görebilir, ölçüm yapabilir, gürültü ekleyebilir ve birkaç ders kitabı protokolü ile algoritmasını çalıştırabilirsiniz.

Sürüm 2.0, özgün projenin görünümünü ve iş akışını korur, altındaki yapıyı ise yeniler: birim testleri olan ayrı bir simülasyon paketi, belgelenmiş tek bir kübit sıralama kuralı, fiziksel olarak tutarlı ölçüm ve yeni görselleştirmeler. Değişikliklere yol açan denetim [`docs/AUDIT.md`](docs/AUDIT.md) dosyasındadır.

> Bu proje, IBM Quantum Composer ve Qiskit gibi araçların görsel tarzından esinlenmiştir. Bağımsız bir eğitim projesidir ve **IBM ile bağlantılı değildir, IBM tarafından da desteklenmemektedir**; başka bir kuantum hesaplama kuruluşuyla da ilişkisi yoktur. İdeal ve gürültülü kübitleri klasik bir bilgisayarda simüle eder; kuantum donanımına bağlanmaz.

## Özellikler

| Alan | Neler yapabilirsiniz |
|---|---|
| **Laboratuvar** | 1–6 kübit; herhangi bir kübitte I, X, Y, Z, H, S, T kapıları; herhangi iki kübit arasında CNOT; canlı devre şeması, durum tablosu ve kapı geçmişi |
| **Durum görselleştirme** | Olasılık dağılımı, genliklerin gerçel/sanal kısımları ve her genliğin fazı, taban durumu etiketleriyle |
| **Bloch küresi** | Her kübit için, kübitin *indirgenmiş durumundan* çizilen etkileşimli 3B küre; vektör uzunluğu ve saflık sayesinde saf ve karışık durumlar ayırt edilir |
| **Ölçüm** | Tohumlu atış örneklemesi (100–10 000 atış) ve bir ya da tüm kübitlerin durum çökmeli izdüşümsel ölçümü |
| **Dolanıklık** | Entropi ve çökme gösterimiyle dört Bell durumu üreteci; herhangi bir tek kübit durumunun üç kübitli kuantum ışınlaması |
| **Gürültü** | Her kapıdan sonra uygulanan bit çevirme, faz çevirme ve depolarizasyon kanalları; yoğunluk matrisiyle tam olarak simüle edilir |
| **Algoritmalar** | Açıklamalar ve devrelerle Grover araması (2–5 kübit) ve Deutsch–Jozsa (1–4 girdi kübiti) |
| **Diller** | English, Indonesian, Spanish, Mandarin Chinese, Arabic, French, Japanese, Korean, German, Portuguese, Russian, Hindi, Turkish, Italian, Vietnamese |

## Ekran görüntüleri

| Laboratuvar: devre, olasılıklar, genlikler | Bloch küreleri (Q0 ve Q1 dolanık, Q2 saf) |
|---|---|
| <img src="assets/screenshot_lab.png" alt="Lab" width="420"/> | <img src="assets/screenshot_bloch.png" alt="Bloch" width="420"/> |

| Atış örneklemesi ve izdüşümsel ölçüm | Kuantum ışınlama |
|---|---|
| <img src="assets/screenshot_measurement.png" alt="Measurement" width="420"/> | <img src="assets/screenshot_teleportation.png" alt="Teleportation" width="420"/> |

| Gürültü: ideal ve depolarize Bell durumu | Grover ve Deutsch–Jozsa |
|---|---|
| <img src="assets/screenshot_noise.png" alt="Noise" width="420"/> | <img src="assets/screenshot_algorithms.png" alt="Algorithms" width="420"/> |

## Kurulum

Python 3.11 veya daha yenisini gerektirir (3.11 ve 3.13 ile test edildi).

```bash
git clone https://github.com/rasidi3112/quantum-computing-simulation.git
cd quantum-computing-simulation
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

Ardından şu adresi açın: <http://localhost:8501>.

Çalışma zamanı bağımlılıkları `numpy`, `streamlit` ve `plotly` paketleridir. Simülasyon paketinin kendisi (`quantum_lab`, `visualization` hariç) yalnızca NumPy gerektirir.

## Kullanım

1. Kenar çubuğundan **kübit sayısını** seçin (değiştirmek yeni ve boş bir devre başlatır).
2. Bir kapı ve hedef kübit seçip **Apply Gate** düğmesine basın; iki veya daha fazla kübitte kontrol ve hedefi seçip **Apply CNOT** düğmesine basın.
3. Sonucu sekmelerden okuyun:
   - **Lab**: devre şeması, olasılıklar, genlikler, fazlar, durum tablosu;
   - **Bloch Sphere**: her kübit için bir küre;
   - **Measurement**: *Run Measurement* duruma dokunmadan atış örnekler; *Measure Qubit* / *Measure All Qubits* durumu çökertir;
   - **Entanglement**, **Noise**, **Algorithms**: kendi başına çalışan gösterimler. *Load into Lab* bir Bell devresini laboratuvara kopyalar.
4. **Reset System** |0…0⟩ durumuna döner ve rastgele sayı üretecini tohumdan yeniden başlatır.

Grafikler etkileşimlidir (üzerine gelme, yakınlaştırma, döndürme). Grafiğin araç çubuğundaki kamera düğmesi PNG kaydeder; *Save …* düğmeleri bağımsız, etkileşimli bir HTML dosyası indirir.

### Örnek devreler

| Amaç | Adımlar | Beklenen sonuç |
|---|---|---|
| Süperpozisyon | 1 qubit: H → Q0 | P(0) = P(1) = 0.5; Bloch vektörü +x yönünde |
| Bell durumu \|Φ+⟩ | 2 qubits: H → Q0, CNOT Q0 → Q1 | (\|00⟩ + \|11⟩)/√2; P(00) = P(11) = 0.5, P(01) = P(10) = 0; her iki Bloch vektörünün uzunluğu 0 |
| H·Z·H = X | 1 qubit: H, Z, H → Q0 | \|1⟩ |
| GHZ durumu | 3 qubits: H → Q0, CNOT Q0 → Q1, CNOT Q1 → Q2 | (\|000⟩ + \|111⟩)/√2 |
| Çökme | Bell durumu, ardından *Measure Qubit* Q0 | \|00⟩ / \|11⟩; Q1 artık belirlenmiştir |

```
q0: ──[H]──●──
           │
q1: ───────⊕──
```

### Simülatörü Python'dan kullanma

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

## Kuantum matematiği kuralları

**Durum.** *n* kübitlik bir yazmaç, Σ|αᵢ|² = 1 koşulunu sağlayan 2ⁿ genlikten (αᵢ) oluşan karmaşık bir vektördür ve |0…0⟩ ile başlatılır.

**Kübit sırası: big-endian, her yerde.** Kübit 0, taban etiketinin *en soldaki* biti ve şemanın *en üstteki* telidir:

```
|q0 q1 … q(n-1)⟩      index = Σ_k q_k · 2^(n-1-k)      |ψ⟩ = |q0⟩ ⊗ |q1⟩ ⊗ … ⊗ |q(n-1)⟩
```

Dolayısıyla iki kübitte Q0 üzerindeki X, |00⟩ durumunu |10⟩ durumuna (indis 2) çevirir. `[a, b]` kübit listesine etki eden bir matris `a` kübitini en anlamlı bit olarak ele alır; özellikle `gates.CNOT`, `[control, target]` için matristir. Bu, ders kitabı kuralıdır (Nielsen & Chuang). **Qiskit bunun tersini, little-endian sırayı kullanır**; karşılaştırırken bit dizilerini ters çevirin.

**Evrim.** Her işleç uygulanmadan önce üniterlik açısından denetlenir (U†U = I, tolerans 10⁻¹⁰) ve durum üniter evrim sırasında hiçbir zaman yeniden normalize edilmez. Testler, 3000 kapıdan sonra normun 1'den en çok 10⁻¹⁰ saptığını doğrular.

**Ölçüm (hesaplama tabanı):**

- *Atış örneklemesi* sonuçları P(i) = |αᵢ|² dağılımından çeker. Her atış için aynı durumun yeniden hazırlanmasını modeller; durum değişmez.
- *k* kübitinin *izdüşümsel ölçümü* P(m) = Σ_{i: bit k = m} |αᵢ|² olasılığıyla m ∈ {0, 1} çeker, ardından durumu P_m|ψ⟩ / √P(m) ile değiştirir. Tüm kübitlerin ölçülmesi bir taban durumu bırakır.
- *Rastgelelik.* Tam sayı bir tohum yinelenebilir sonuçlar verir (`numpy.random.default_rng`). Uygulamada atış örneklemesi tohumu doğrudan kullanır (aynı tohum ve durum → aynı histogram); izdüşümsel ölçümler ise sıfırlamada, tohum değiştiğinde ve yazmaç boyutu değiştiğinde yeniden başlatılan tek bir üreteci tüketir.

**Bloch vektörü.** *k* kübiti için indirgenmiş yoğunluk matrisi ρ_k = Tr_{others} |ψ⟩⟨ψ|, ρ_k = (I + r·σ)/2 olmak üzere r = (Tr ρ_kX, Tr ρ_kY, Tr ρ_kZ) vektörünü verir. Saf bir kübit için |r| = 1, başka kübitlerle dolanık ya da gürültüden etkilenmiş kübit için |r| < 1 olur; saflık Tr ρ_k² = (1 + |r|²)/2 değerindedir. Dolanık bir yazmacın tek bir Bloch vektörü yoktur, bu yüzden çizilmez.

**Gürültü.** Her kapıdan sonra seçilen kanal, o kapının dokunduğu her kübite etki eder (uygulama başına hata olasılığı *p*):

| Kanal | Dönüşüm |
|---|---|
| Bit çevirme | ρ → (1 − p)ρ + p XρX |
| Faz çevirme | ρ → (1 − p)ρ + p ZρZ |
| Depolarizasyon | ρ → (1 − p)ρ + (p/3)(XρX + YρY + ZρZ) |

Bu parametrelendirmeyle depolarizasyon kanalı Bloch vektörünü 1 − 4p/3 oranında ölçekler (p = 3/4 en üst düzeyde karışık durumdur). Boşta bekleyen kübitler ve ölçümler gürültüsüzdür. Yoğunluk matrisi tam olarak evrilir; gürültülü bir devre içindeki ölçümlerin sonuçları üzerinden ortalama alınır.

**Sadakat (fidelity).** Saf bir referansa göre ⟨ψ|ρ|ψ⟩ ve genel durumda Uhlmann sadakati (Tr √(√ρ σ √ρ))².

## Desteklenen kuantum kapıları

| Kapı | Matris | Etki |
|---|---|---|
| Identity (I) | [[1, 0], [0, 1]] | kübiti değiştirmez |
| Pauli-X | [[0, 1], [1, 0]] | bit çevirme \|0⟩ ↔ \|1⟩ |
| Pauli-Y | [[0, −i], [i, 0]] | Y\|0⟩ = i\|1⟩, Y\|1⟩ = −i\|0⟩ |
| Pauli-Z | [[1, 0], [0, −1]] | faz çevirme \|1⟩ → −\|1⟩ |
| Hadamard (H) | [[1, 1], [1, −1]]/√2 | \|0⟩ → \|+⟩, \|1⟩ → \|−⟩ |
| S | diag(1, i) | faz π/2 |
| T | diag(1, e^{iπ/4}) | faz π/4 |
| CNOT | \|0⟩⟨0\| ⊗ I + \|1⟩⟨1\| ⊗ X | kontrol |1⟩ ise hedefi çevirir |

Python API'si ayrıca `rx`, `ry`, `rz`, `phase`, herhangi bir kübit listesi üzerinde keyfi üniterler ve çok kontrollü tek kübit kapıları sunar; bunlar ışınlama ve Grover devrelerinde kullanılır ancak henüz kenar çubuğunda yer almaz.

## Algoritmalar ve protokoller

- **Bell durumları.** X kapıları girdiyi seçer, ardından H ve CNOT uygulanır.
- **Işınlama.** Q0, cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩ durumunu taşır; Q1–Q2 bir Bell çiftini paylaşır. Alice CNOT ve H uygular, Q0 ile Q1'i ölçer; Bob m₁ = 1 ise X, m₀ = 1 ise Z uygular. Gösterilen sadakat simüle edilen durumdan hesaplanır ve dört dalın tümünde 1'dir.
- **Grover.** Kâhin = işaretli öğenin sıfır bitlerinde X, çok kontrollü Z, yeniden X; difüzyon = Hⁿ Xⁿ (MCZ) Xⁿ Hⁿ. Simüle edilen başarı olasılığı sin²((2k+1)θ), sin θ = 1/√N ile örtüşür.
- **Deutsch–Jozsa.** U_f|x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩ kâhini f fonksiyonunun doğruluk tablosundan kurulur. Uygulama sabit fonksiyonlar, seçilen bitlerin pariteleri ve rastgele dengeli fonksiyonlar sunar.

## Mimari

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

Bağımlılıklar tek yönlüdür: `main.py` → `quantum_lab` ve `translations`; paketin içinde Plotly'yi içe aktaran tek modül `visualization` modülüdür ve hiçbir modül Streamlit'i içe aktarmaz, böylece çekirdek tek başına kullanılabilir ve test edilebilir.

## Testler

```bash
pip install -r requirements-dev.txt
pytest
pytest --ignore=tests/test_app.py
ruff check .
python benchmarks/bench_gates.py
```

`pytest` yaklaşık 1,5 dakika sürer (çoğu tarayıcısız arayüz testleridir); `--ignore=tests/test_app.py` ile yalnızca çekirdek birkaç saniyede test edilir.

| Dosya | Kapsam |
|---|---|
| `test_gates.py` | her kapının üniterliği, cebirsel özdeşlikler, Kronecker açılımı, CNOT matrisleri |
| `test_simulator.py` | normalizasyon, Pauli/Hadamard davranışı, iki kez H, CNOT doğruluk tabloları, Bell ve GHZ durumları, yoğun matrislerle karşılaştırma, geçersiz girdi |
| `test_measurement.py` | Born kuralı, marjinal dağılımlar, tohumlu örnekleme, istatistik, çökme ve yeniden normalizasyon |
| `test_states.py` | kısmi iz, Bloch vektörleri, saflık, dolanıklık entropisi |
| `test_circuit.py` | devre kurma ve çalıştırma, koşullu kapılar, şema yerleşimi |
| `test_noise.py` | kanallar izi korur, analitik sonuçlar, hata yörüngeleri üzerinden tam toplam |
| `test_protocols.py` | dört Bell durumu, dört dalın tümünde ışınlama |
| `test_algorithms.py` | kapalı formüle karşı Grover, 2 ve 3 girdili her dengeli fonksiyon için Deutsch–Jozsa |
| `test_visualization.py` | şekiller doğru veriyi içerir |
| `test_translations.py` | 15 dil, aynı anahtarlar ve yer tutucular, arayüzün kullandığı her anahtar mevcut |
| `test_app.py` | Streamlit uygulaması uçtan uca (tarayıcısız), her dilde |

Sayısal karşılaştırmalar, tam kayan nokta eşitliği yerine toleranslar kullanır (genlikler için 10⁻¹², örnekleme istatistikleri için 5σ bantları).

Doğrulanan birleşimler: Python 3.11 + NumPy 1.26.4 / Streamlit 1.50.0 / Plotly 5.24.0; Python 3.13 + NumPy 2.5.4 / Streamlit 1.67.0 / Plotly 7.1.0.

## Başarım ve sınırlar

| Büyüklük | Durum vektörü | Yoğunluk matrisi |
|---|---|---|
| Bellek | 16 · 2ⁿ bytes | 16 · 4ⁿ bytes |
| k kübitlik bir kapı | O(2ⁿ · 2ᵏ) | O(4ⁿ · 2ᵏ) |
| Koddaki kesin sınır | `MAX_QUBITS = 20` (16 MiB) | `MAX_DENSITY_QUBITS = 10` (16 MiB) |
| Arayüzdeki sınır | 6 qubits | 6 qubits |

Sürüm 1.0 her kapı için yoğun bir 2ⁿ × 2ⁿ matris kuruyordu; 2.0 kapıyı durum tensörüyle daraltır. `benchmarks/bench_gates.py` ile ölçülmüştür (tek Hadamard, birkaç çalıştırmanın en iyisi, tek makine; yaklaşık değer olarak değerlendirin):

| Qubits | Yoğun matris (1.0) | Daraltma (2.0) | Oran |
|---|---|---|---|
| 3 | 35 µs | 40 µs | 0.9× |
| 6 | 100 µs | 43 µs | 2× |
| 8 | 553 µs | 44 µs | 13× |
| 10 | 7.6 ms | 49 µs | 155× |
| 12 | 184 ms | 57 µs | ≈ 3200× |

Eski üç kübit sınırında hızlanma yoktur (girdi doğrulaması birkaç mikrosaniye tutar); kazanç, daha büyük yazmaçların kullanılabilir hâle gelmesidir. Simülasyon maliyeti yine de her kübitte ikiye katlanır. Bu, küçük yazmaçlar için bir öğretim aracıdır, genel amaçlı bir simülatör değildir.

## Bilinen sınırlamalar

- Arayüz 1–6 kübit sunar; kenar çubuğundaki kapılar I, X, Y, Z, H, S, T ve CNOT'tur. Dönme kapıları yalnızca Python API'sinde bulunur.
- Ölçüm yalnızca hesaplama (Z) tabanında yapılır.
- Gürültü, kapılardan sonraki tek kübitli Pauli gürültüsüdür. Genlik sönümü, okuma hatası, bekleme gürültüsü ve ilintili gürültü yoktur.
- Grover tek bir işaretli öğe arar; Deutsch–Jozsa kâhini temel kapılara ayrıştırılmak yerine tek bir üniter kutu olarak uygulanır.
- Devreye yalnızca ekleme yapılabilir (geri alma, düzenleme, sürükle bırak yoktur).
- Devre şeması eş aralıklı metindir; çok uzun devreler yatay kayar.
- Arapça çevrilmiştir ancak sayfa düzeni sağdan sola yansıtılmaz.
- 2.0'da eklenen 80 metin, ana dili konuşurlarının incelemesi olmadan çevrilmiştir; düzeltmeler memnuniyetle karşılanır.
- Gerçek kuantum donanımına veya bulut altyapılarına bağlantı yoktur.

## 1.0'dan bu yana sizi etkileyebilecek değişiklikler

- **CNOT sonuçları farklıdır çünkü eskileri yanlıştı.** 1.0 iki kübit sıralamasını karıştırıyordu; bu yüzden tek kübit kapılarını CNOT ile birleştiren devreler hatalı durumlar veriyordu (bkz. `docs/AUDIT.md`, bulgu Q1).
- `QuantumSimulator`, `main.py` dosyasından `quantum_lab` paketine taşındı. 1.0'daki yöntemleri (`apply_gate`, `get_probabilities`, `get_amplitudes`, `measure`, `reset`, `_expand_gate`, `_create_cnot_matrix`) korunmuştur. Geçersiz girdi artık sessizce kabul edilmek yerine `ValueError`/`TypeError` üretir, `state` salt okunurdur ve üniter olmayan matrisler reddedilir.
- Ölçüm histogramı her etkileşimde yeniden üretilmek yerine *Run Measurement* düğmesine basıldıktan sonra görünür.
- Grafikler Matplotlib yerine Plotly ile çizilir. *Save …* düğmeleri artık etkileşimli HTML indirir; PNG dışa aktarma her grafiğin araç çubuğundadır.
- `matplotlib` ve kullanılmayan `qiskit`, `requirements.txt` dosyasından çıkarıldı; `plotly` eklendi.

## Streamlit Community Cloud'da yayımlama

1. Depoyu (veya kendi çatalınızı) GitHub'a gönderin.
2. <https://share.streamlit.io> adresinde GitHub ile oturum açın ve yeni bir uygulama oluşturun.
3. Depoyu ve dalı seçin, main file path alanını `main.py` olarak ayarlayın.
4. Advanced settings bölümünde Python 3.11 veya daha yenisini seçin ve yayımlayın.

Bağımlılıklar `requirements.txt` dosyasından kurulur; gizli anahtar ya da ortam değişkeni gerekmez. Bu adımlar platformla ilgili deneyime dayanarak yazılmıştır ve bu sürüm hazırlanırken güncel belgelerle karşılaştırılamamıştır. Ekranlar farklıysa şu belgeleri izleyin: <https://docs.streamlit.io/deploy/streamlit-community-cloud>.

`.devcontainer` yapılandırması Streamlit'i CORS ve XSRF koruması kapalı olarak başlatır; GitHub Codespaces'in port yönlendirmesi bunu gerektirir. Bu seçenekleri herkese açık bir yayında kullanmayın.

## Yol haritası

- Kenar çubuğunda dönme kapıları (Rx, Ry, Rz) ve daha fazla iki kübit kapısı (CZ, SWAP)
- Geri alma ve devre düzenleme; devreleri kaydetme ve yükleme
- Başka tabanlarda ölçüm; Pauli gözlenebilirlerinin beklenen değerleri
- Genlik sönümü ve okuma hatası kanalları
- Devrelerin OpenQASM'e aktarılması
- Çevirilerin ana dili konuşurlarınca gözden geçirilmesi; sağdan sola düzen

## Lisans ve atıf

[MIT Lisansı](LICENSE) ile yayımlanmıştır, Copyright (c) 2025 rasidi3112. Lisans dosyası değiştirilmemiştir.

Mini Quantum Lab, özgün uygulamayı, arayüzü ve çevirileri yazan [Rasidi](https://github.com/rasidi3112) tarafından oluşturulmuştur. Sürüm 2.0 (simülasyon çekirdeği, testler, görselleştirmeler ve eklenen özellikler) bu çalışmanın üzerine kuruludur.
