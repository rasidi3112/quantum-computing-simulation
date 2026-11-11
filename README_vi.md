<h1 align="center">Mini Quantum Lab 2.0</h1>

<p align="center">
  <b>Trình mô phỏng điện toán lượng tử tương tác, đã được kiểm thử, dùng để học tập</b><br>
  Python · NumPy · Streamlit · Plotly · 15 ngôn ngữ giao diện
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
  <a href="README_tr.md">Türkçe</a> ·
  <b>Tiếng Việt</b> ·
  <a href="README_zh.md">中文</a>
</p>

---

## Tổng quan

Mini Quantum Lab là một ứng dụng web giáo dục để khám phá những điều cơ bản của điện toán lượng tử: dựng các mạch nhỏ từng cổng một, quan sát vectơ trạng thái, xem từng qubit trên mặt cầu Bloch, thực hiện phép đo, thêm nhiễu và chạy một vài giao thức, thuật toán kinh điển.

Phiên bản 2.0 giữ nguyên giao diện và cách làm việc của dự án gốc nhưng thay phần bên dưới: một gói mô phỏng riêng có kiểm thử đơn vị, một quy ước thứ tự qubit duy nhất được ghi rõ, phép đo nhất quán về mặt vật lý và các hình trực quan mới. Bản đánh giá dẫn tới những thay đổi này nằm trong [`docs/AUDIT.md`](docs/AUDIT.md).

> Dự án lấy cảm hứng từ phong cách trực quan của các công cụ như IBM Quantum Composer và Qiskit. Đây là một dự án giáo dục độc lập, **không liên kết với IBM và không được IBM bảo trợ**, cũng như bất kỳ tổ chức điện toán lượng tử nào khác. Dự án mô phỏng các qubit lý tưởng và có nhiễu trên máy tính cổ điển, không kết nối với phần cứng lượng tử.

## Tính năng

| Phần | Bạn có thể làm gì |
|---|---|
| **Phòng thí nghiệm** | 1–6 qubit; các cổng I, X, Y, Z, H, S, T trên bất kỳ qubit nào; CNOT giữa hai qubit bất kỳ; sơ đồ mạch trực tiếp, bảng trạng thái và lịch sử cổng |
| **Trực quan hóa trạng thái** | Phân bố xác suất, phần thực/ảo của biên độ và pha của từng biên độ, kèm nhãn trạng thái cơ sở |
| **Mặt cầu Bloch** | Mặt cầu 3D tương tác cho từng qubit, vẽ từ *trạng thái rút gọn* của qubit, kèm độ dài vectơ và độ thuần để phân biệt trạng thái thuần và hỗn hợp |
| **Đo lường** | Lấy mẫu theo lần bắn (100–10 000 lần) có hạt giống, và phép đo chiếu trên một hoặc tất cả qubit với sự sụp đổ trạng thái |
| **Vướng víu** | Bộ tạo bốn trạng thái Bell kèm entropy và minh họa sụp đổ; viễn tải lượng tử ba qubit cho trạng thái một qubit bất kỳ |
| **Nhiễu** | Các kênh đảo bit, đảo pha và khử phân cực áp dụng sau mỗi cổng, được mô phỏng chính xác bằng ma trận mật độ |
| **Thuật toán** | Tìm kiếm Grover (2–5 qubit) và Deutsch–Jozsa (1–4 qubit đầu vào) kèm giải thích và mạch |
| **Ngôn ngữ** | English, Indonesian, Spanish, Mandarin Chinese, Arabic, French, Japanese, Korean, German, Portuguese, Russian, Hindi, Turkish, Italian, Vietnamese |

## Ảnh chụp màn hình

| Phòng thí nghiệm: mạch, xác suất, biên độ | Mặt cầu Bloch (Q0 và Q1 vướng víu, Q2 thuần) |
|---|---|
| <img src="assets/screenshot_lab.png" alt="Lab" width="420"/> | <img src="assets/screenshot_bloch.png" alt="Bloch" width="420"/> |

| Lấy mẫu theo lần bắn và phép đo chiếu | Viễn tải lượng tử |
|---|---|
| <img src="assets/screenshot_measurement.png" alt="Measurement" width="420"/> | <img src="assets/screenshot_teleportation.png" alt="Teleportation" width="420"/> |

| Nhiễu: trạng thái Bell lý tưởng và bị khử phân cực | Grover và Deutsch–Jozsa |
|---|---|
| <img src="assets/screenshot_noise.png" alt="Noise" width="420"/> | <img src="assets/screenshot_algorithms.png" alt="Algorithms" width="420"/> |

## Cài đặt

Yêu cầu Python 3.11 trở lên (đã kiểm thử trên 3.11 và 3.13).

```bash
git clone https://github.com/rasidi3112/quantum-computing-simulation.git
cd quantum-computing-simulation
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

Sau đó mở <http://localhost:8501>.

Các phụ thuộc khi chạy là `numpy`, `streamlit` và `plotly`. Bản thân gói mô phỏng (`quantum_lab`, không tính `visualization`) chỉ cần NumPy.

## Cách dùng

1. Chọn **số qubit** ở thanh bên (thay đổi sẽ bắt đầu một mạch mới, trống).
2. Chọn một cổng và qubit mục tiêu rồi nhấn **Apply Gate**; với hai qubit trở lên, chọn qubit điều khiển và mục tiêu rồi nhấn **Apply CNOT**.
3. Xem kết quả trong các thẻ:
   - **Lab**: sơ đồ mạch, xác suất, biên độ, pha, bảng trạng thái;
   - **Bloch Sphere**: mỗi qubit một mặt cầu;
   - **Measurement**: *Run Measurement* lấy mẫu mà không đụng tới trạng thái; *Measure Qubit* / *Measure All Qubits* làm trạng thái sụp đổ;
   - **Entanglement**, **Noise**, **Algorithms**: các phần minh họa độc lập. *Load into Lab* sao chép một mạch Bell vào phòng thí nghiệm.
4. **Reset System** trở về |0…0⟩ và khởi động lại bộ sinh số ngẫu nhiên từ hạt giống.

Biểu đồ có tính tương tác (rê chuột, thu phóng, xoay). Nút máy ảnh trên thanh công cụ của biểu đồ lưu ảnh PNG; các nút *Save …* tải về một tệp HTML tương tác độc lập.

### Mạch ví dụ

| Mục tiêu | Các bước | Kết quả mong đợi |
|---|---|---|
| Chồng chập | 1 qubit: H → Q0 | P(0) = P(1) = 0.5; vectơ Bloch nằm trên +x |
| Trạng thái Bell \|Φ+⟩ | 2 qubits: H → Q0, CNOT Q0 → Q1 | (\|00⟩ + \|11⟩)/√2; P(00) = P(11) = 0.5, P(01) = P(10) = 0; cả hai vectơ Bloch có độ dài 0 |
| H·Z·H = X | 1 qubit: H, Z, H → Q0 | \|1⟩ |
| Trạng thái GHZ | 3 qubits: H → Q0, CNOT Q0 → Q1, CNOT Q1 → Q2 | (\|000⟩ + \|111⟩)/√2 |
| Sụp đổ | Trạng thái Bell, rồi *Measure Qubit* Q0 | \|00⟩ / \|11⟩; Q1 lúc này đã xác định |

```
q0: ──[H]──●──
           │
q1: ───────⊕──
```

### Dùng trình mô phỏng từ Python

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

## Quy ước toán học lượng tử

**Trạng thái.** Thanh ghi *n* qubit là một vectơ phức gồm 2ⁿ biên độ αᵢ với Σ|αᵢ|² = 1, khởi tạo ở |0…0⟩.

**Thứ tự qubit: big-endian, dùng ở mọi nơi.** Qubit 0 là bit *ngoài cùng bên trái* của nhãn cơ sở và là dây *trên cùng* của sơ đồ:

```
|q0 q1 … q(n-1)⟩      index = Σ_k q_k · 2^(n-1-k)      |ψ⟩ = |q0⟩ ⊗ |q1⟩ ⊗ … ⊗ |q(n-1)⟩
```

Vì vậy với hai qubit, X trên Q0 biến |00⟩ thành |10⟩ (chỉ số 2). Ma trận tác dụng lên danh sách qubit `[a, b]` coi `a` là bit có trọng số cao nhất; cụ thể `gates.CNOT` là ma trận cho `[control, target]`. Đây là quy ước trong sách giáo khoa (Nielsen & Chuang). **Qiskit dùng thứ tự ngược lại, little-endian**; hãy đảo chuỗi bit khi so sánh.

**Tiến hóa.** Mọi toán tử đều được kiểm tra tính unita (U†U = I, dung sai 10⁻¹⁰) trước khi áp dụng, và trạng thái không bao giờ được chuẩn hóa lại trong quá trình tiến hóa unita. Các bài kiểm thử xác nhận chuẩn lệch khỏi 1 không quá 10⁻¹⁰ sau 3000 cổng.

**Phép đo (cơ sở tính toán):**

- *Lấy mẫu theo lần bắn* rút kết quả từ P(i) = |αᵢ|². Nó mô hình hóa việc chuẩn bị lại cùng một trạng thái cho mỗi lần bắn; trạng thái không đổi.
- *Phép đo chiếu* trên qubit *k* rút m ∈ {0, 1} với P(m) = Σ_{i: bit k = m} |αᵢ|², rồi thay trạng thái bằng P_m|ψ⟩ / √P(m). Đo tất cả qubit để lại một trạng thái cơ sở.
- *Tính ngẫu nhiên.* Hạt giống nguyên cho kết quả lặp lại được (`numpy.random.default_rng`). Trong ứng dụng, lấy mẫu theo lần bắn dùng trực tiếp hạt giống (cùng hạt giống và trạng thái → cùng biểu đồ tần suất), còn các phép đo chiếu dùng chung một bộ sinh được khởi động lại khi đặt lại, khi đổi hạt giống và khi đổi kích thước thanh ghi.

**Vectơ Bloch.** Với qubit *k*, ma trận mật độ rút gọn ρ_k = Tr_{others} |ψ⟩⟨ψ| cho r = (Tr ρ_kX, Tr ρ_kY, Tr ρ_kZ) với ρ_k = (I + r·σ)/2. |r| = 1 với qubit thuần, |r| < 1 khi nó vướng víu với qubit khác hoặc chịu nhiễu, và độ thuần là Tr ρ_k² = (1 + |r|²)/2. Một thanh ghi vướng víu không có một vectơ Bloch duy nhất nên không vectơ nào được vẽ.

**Nhiễu.** Sau mỗi cổng, kênh được chọn tác dụng lên từng qubit mà cổng đó chạm tới (xác suất lỗi *p* cho mỗi lần áp dụng):

| Kênh | Ánh xạ |
|---|---|
| Đảo bit | ρ → (1 − p)ρ + p XρX |
| Đảo pha | ρ → (1 − p)ρ + p ZρZ |
| Khử phân cực | ρ → (1 − p)ρ + (p/3)(XρX + YρY + ZρZ) |

Với cách tham số hóa này, kênh khử phân cực co vectơ Bloch theo hệ số 1 − 4p/3 (p = 3/4 là trạng thái hỗn hợp cực đại). Qubit đang chờ và phép đo không có nhiễu. Ma trận mật độ được tiến hóa chính xác; các phép đo bên trong mạch có nhiễu được lấy trung bình trên các kết quả.

**Độ trung thực.** ⟨ψ|ρ|ψ⟩ so với một trạng thái thuần tham chiếu, và độ trung thực Uhlmann (Tr √(√ρ σ √ρ))² trong trường hợp tổng quát.

## Các cổng lượng tử được hỗ trợ

| Cổng | Ma trận | Tác dụng |
|---|---|---|
| Identity (I) | [[1, 0], [0, 1]] | giữ nguyên qubit |
| Pauli-X | [[0, 1], [1, 0]] | đảo bit \|0⟩ ↔ \|1⟩ |
| Pauli-Y | [[0, −i], [i, 0]] | Y\|0⟩ = i\|1⟩, Y\|1⟩ = −i\|0⟩ |
| Pauli-Z | [[1, 0], [0, −1]] | đảo pha \|1⟩ → −\|1⟩ |
| Hadamard (H) | [[1, 1], [1, −1]]/√2 | \|0⟩ → \|+⟩, \|1⟩ → \|−⟩ |
| S | diag(1, i) | pha π/2 |
| T | diag(1, e^{iπ/4}) | pha π/4 |
| CNOT | \|0⟩⟨0\| ⊗ I + \|1⟩⟨1\| ⊗ X | đảo qubit mục tiêu nếu qubit điều khiển là |1⟩ |

API Python còn cung cấp `rx`, `ry`, `rz`, `phase`, các phép unita tùy ý trên bất kỳ danh sách qubit nào và các cổng một qubit nhiều điều khiển; chúng được dùng trong mạch viễn tải và Grover nhưng chưa có ở thanh bên.

## Thuật toán và giao thức

- **Trạng thái Bell.** Các cổng X chọn đầu vào, sau đó là H và CNOT.
- **Viễn tải.** Q0 mang cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩, Q1–Q2 chia sẻ một cặp Bell. Alice áp dụng CNOT và H rồi đo Q0, Q1; Bob áp dụng X nếu m₁ = 1 và Z nếu m₀ = 1. Độ trung thực hiển thị được tính từ trạng thái mô phỏng và bằng 1 ở cả bốn nhánh.
- **Grover.** Oracle = X trên các bit 0 của phần tử được đánh dấu, Z nhiều điều khiển, rồi X lần nữa; khuếch tán = Hⁿ Xⁿ (MCZ) Xⁿ Hⁿ. Xác suất thành công mô phỏng khớp với sin²((2k+1)θ), sin θ = 1/√N.
- **Deutsch–Jozsa.** Oracle U_f|x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩ được dựng từ bảng chân trị của f. Ứng dụng cung cấp hàm hằng, tính chẵn lẻ của các bit được chọn và hàm cân bằng ngẫu nhiên.

## Kiến trúc

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

Phụ thuộc chỉ đi một chiều: `main.py` → `quantum_lab` và `translations`; trong gói, `visualization` là mô-đun duy nhất nhập Plotly và không mô-đun nào nhập Streamlit, nên phần lõi có thể được dùng và kiểm thử riêng.

## Kiểm thử

```bash
pip install -r requirements-dev.txt
pytest
pytest --ignore=tests/test_app.py
ruff check .
python benchmarks/bench_gates.py
```

`pytest` mất khoảng 1,5 phút (phần lớn là kiểm thử giao diện không cần trình duyệt); với `--ignore=tests/test_app.py` chỉ phần lõi được kiểm thử, trong vài giây.

| Tệp | Phạm vi |
|---|---|
| `test_gates.py` | tính unita của từng cổng, các đồng nhất thức đại số, khai triển Kronecker, ma trận CNOT |
| `test_simulator.py` | chuẩn hóa, hành vi của Pauli/Hadamard, H hai lần, bảng chân trị CNOT, trạng thái Bell và GHZ, so sánh với ma trận đặc, đầu vào không hợp lệ |
| `test_measurement.py` | quy tắc Born, phân bố biên, lấy mẫu có hạt giống, thống kê, sụp đổ và chuẩn hóa lại |
| `test_states.py` | vết riêng phần, vectơ Bloch, độ thuần, entropy vướng víu |
| `test_circuit.py` | dựng và chạy mạch, cổng có điều kiện, bố cục sơ đồ |
| `test_noise.py` | các kênh bảo toàn vết, kết quả giải tích, tổng đầy đủ trên các quỹ đạo lỗi |
| `test_protocols.py` | bốn trạng thái Bell, viễn tải ở cả bốn nhánh |
| `test_algorithms.py` | Grover so với công thức đóng, Deutsch–Jozsa cho mọi hàm cân bằng 2 và 3 đầu vào |
| `test_visualization.py` | hình vẽ chứa đúng dữ liệu |
| `test_translations.py` | 15 ngôn ngữ, khóa và chỗ giữ giống hệt nhau, mọi khóa giao diện dùng đều tồn tại |
| `test_app.py` | ứng dụng Streamlit từ đầu đến cuối (headless), ở mọi ngôn ngữ |

Các phép so sánh số dùng dung sai (10⁻¹² cho biên độ, dải 5σ cho thống kê lấy mẫu) thay vì so sánh dấu phẩy động chính xác.

Các tổ hợp đã kiểm chứng: Python 3.11 + NumPy 1.26.4 / Streamlit 1.50.0 / Plotly 5.24.0; Python 3.13 + NumPy 2.5.4 / Streamlit 1.67.0 / Plotly 7.1.0.

## Hiệu năng và giới hạn

| Đại lượng | Vectơ trạng thái | Ma trận mật độ |
|---|---|---|
| Bộ nhớ | 16 · 2ⁿ bytes | 16 · 4ⁿ bytes |
| Một cổng k qubit | O(2ⁿ · 2ᵏ) | O(4ⁿ · 2ᵏ) |
| Giới hạn cứng trong mã | `MAX_QUBITS = 20` (16 MiB) | `MAX_DENSITY_QUBITS = 10` (16 MiB) |
| Giới hạn trong giao diện | 6 qubits | 6 qubits |

Phiên bản 1.0 dựng một ma trận đặc 2ⁿ × 2ⁿ cho mỗi cổng; 2.0 co cổng với tenxơ trạng thái. Đo bằng `benchmarks/bench_gates.py` (một cổng Hadamard, lần tốt nhất trong vài lần chạy, một máy; chỉ mang tính tham khảo):

| Qubits | Ma trận đặc (1.0) | Phép co (2.0) | Tỉ số |
|---|---|---|---|
| 3 | 35 µs | 40 µs | 0.9× |
| 6 | 100 µs | 43 µs | 2× |
| 8 | 553 µs | 44 µs | 13× |
| 10 | 7.6 ms | 49 µs | 155× |
| 12 | 184 ms | 57 µs | ≈ 3200× |

Ở giới hạn cũ ba qubit không có tăng tốc (kiểm tra đầu vào tốn vài micro giây); lợi ích là các thanh ghi lớn hơn trở nên khả thi. Chi phí mô phỏng vẫn tăng gấp đôi với mỗi qubit. Đây là công cụ giảng dạy cho thanh ghi nhỏ, không phải trình mô phỏng đa dụng.

## Hạn chế đã biết

- Giao diện cung cấp 1–6 qubit; các cổng ở thanh bên là I, X, Y, Z, H, S, T và CNOT. Cổng quay chỉ có trong API Python.
- Phép đo chỉ thực hiện trong cơ sở tính toán (Z).
- Nhiễu là nhiễu Pauli một qubit sau các cổng. Không có suy giảm biên độ, lỗi đọc, nhiễu khi chờ hay nhiễu tương quan.
- Grover tìm một phần tử được đánh dấu duy nhất; oracle Deutsch–Jozsa được áp dụng như một khối unita thay vì phân rã thành các cổng cơ bản.
- Mạch chỉ cho phép thêm vào (không hoàn tác, không chỉnh sửa, không kéo thả).
- Sơ đồ mạch là văn bản đơn cách; mạch rất dài sẽ cuộn ngang.
- Tiếng Ả Rập đã được dịch nhưng bố cục trang không được lật từ phải sang trái.
- 80 chuỗi thêm vào ở 2.0 được dịch mà chưa qua người bản ngữ rà soát; rất hoan nghênh các chỉnh sửa.
- Không kết nối với phần cứng lượng tử thật hay dịch vụ đám mây.

## Những thay đổi so với 1.0 có thể ảnh hưởng tới bạn

- **Kết quả CNOT khác đi vì kết quả cũ sai.** Bản 1.0 trộn hai thứ tự qubit, nên các mạch kết hợp cổng một qubit với CNOT cho trạng thái sai (xem `docs/AUDIT.md`, phát hiện Q1).
- `QuantumSimulator` chuyển từ `main.py` sang `quantum_lab`. Các phương thức của bản 1.0 (`apply_gate`, `get_probabilities`, `get_amplitudes`, `measure`, `reset`, `_expand_gate`, `_create_cnot_matrix`) được giữ lại. Đầu vào không hợp lệ giờ phát sinh `ValueError`/`TypeError` thay vì được chấp nhận âm thầm, `state` chỉ đọc và ma trận không unita bị từ chối.
- Biểu đồ tần suất phép đo xuất hiện sau khi nhấn *Run Measurement* thay vì được tạo lại ở mỗi tương tác.
- Biểu đồ dùng Plotly thay cho Matplotlib. Các nút *Save …* giờ tải về HTML tương tác; xuất PNG nằm trên thanh công cụ của từng biểu đồ.
- `matplotlib` và `qiskit` (không dùng tới) đã bị gỡ khỏi `requirements.txt`; `plotly` được thêm vào.

## Triển khai trên Streamlit Community Cloud

1. Đẩy kho mã (hoặc bản fork của bạn) lên GitHub.
2. Đăng nhập <https://share.streamlit.io> bằng GitHub và tạo một app mới.
3. Chọn kho mã và nhánh, rồi đặt main file path là `main.py`.
4. Trong advanced settings chọn Python 3.11 trở lên rồi triển khai.

Các phụ thuộc được cài từ `requirements.txt`; không cần secret hay biến môi trường. Các bước này được viết dựa trên kinh nghiệm với nền tảng và chưa thể đối chiếu với tài liệu hiện hành khi chuẩn bị bản phát hành này. Nếu màn hình khác đi, hãy làm theo <https://docs.streamlit.io/deploy/streamlit-community-cloud>.

Cấu hình `.devcontainer` khởi động Streamlit với bảo vệ CORS và XSRF bị tắt, điều mà tính năng chuyển tiếp cổng của GitHub Codespaces yêu cầu. Đừng dùng lại các tùy chọn đó cho bản triển khai công khai.

## Lộ trình

- Cổng quay (Rx, Ry, Rz) và thêm cổng hai qubit (CZ, SWAP) ở thanh bên
- Hoàn tác và chỉnh sửa mạch; lưu và nạp mạch
- Đo trong các cơ sở khác; giá trị kỳ vọng của các đại lượng quan sát Pauli
- Các kênh suy giảm biên độ và lỗi đọc
- Xuất mạch sang OpenQASM
- Người bản ngữ rà soát bản dịch; bố cục từ phải sang trái

## Giấy phép và ghi công

Phát hành theo [Giấy phép MIT](LICENSE), Copyright (c) 2025 rasidi3112. Tệp giấy phép không thay đổi.

Mini Quantum Lab do [Rasidi](https://github.com/rasidi3112) tạo ra, người đã viết ứng dụng, giao diện và các bản dịch ban đầu. Phiên bản 2.0 (lõi mô phỏng, kiểm thử, trực quan hóa và các tính năng bổ sung) được xây dựng trên công trình đó.
