<h1 align="center">Mini Quantum Lab 2.0</h1>

<p align="center">
  <b>一个经过测试的交互式量子计算学习模拟器</b><br>
  Python · NumPy · Streamlit · Plotly · 15 种界面语言
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
  <a href="README_vi.md">Tiếng Việt</a> ·
  <b>中文</b>
</p>

---

## 概述

Mini Quantum Lab 是一个用于探索量子计算基础的教学网页应用：逐个添加量子门来搭建小型电路，观察状态向量，在布洛赫球上查看每个量子比特，进行测量，加入噪声，并运行几个教科书式的协议和算法。

2.0 版保留了原项目的外观和使用流程，替换了底层实现：一个独立且带单元测试的模拟包、一套有文档说明的统一量子比特顺序约定、物理上自洽的测量以及新的可视化。促成这些改动的审计见 [`docs/AUDIT.md`](docs/AUDIT.md)。

> 本项目的视觉风格受 IBM Quantum Composer 和 Qiskit 等工具启发。它是一个独立的教学项目，**与 IBM 及其他任何量子计算机构均无隶属关系，也未获其认可**。它在经典计算机上模拟理想和含噪的量子比特，不连接量子硬件。

## 功能

| 模块 | 可以做什么 |
|---|---|
| **实验室** | 1–6 个量子比特；可对任意量子比特施加 I、X、Y、Z、H、S、T 门；任意两个量子比特之间的 CNOT；实时电路图、状态表和门历史 |
| **状态可视化** | 概率分布、振幅的实部和虚部以及每个振幅的相位，并带有基态标签 |
| **布洛赫球** | 每个量子比特一个可交互的三维球，由该量子比特的*约化态*绘制，并给出向量长度和纯度，以区分纯态和混合态 |
| **测量** | 带种子的多次采样（100–10 000 次），以及对单个或全部量子比特的投影测量与状态坍缩 |
| **纠缠** | 四个贝尔态的生成器，带纠缠熵和坍缩演示；可传送任意单量子比特状态的三量子比特量子隐形传态 |
| **噪声** | 在每个门之后施加比特翻转、相位翻转和去极化信道，用密度矩阵精确模拟 |
| **算法** | Grover 搜索（2–5 个量子比特）和 Deutsch–Jozsa 算法（1–4 个输入量子比特），附说明和电路 |
| **语言** | English, Indonesian, Spanish, Mandarin Chinese, Arabic, French, Japanese, Korean, German, Portuguese, Russian, Hindi, Turkish, Italian, Vietnamese |

## 截图

| 实验室：电路、概率、振幅 | 布洛赫球（Q0 与 Q1 纠缠，Q2 为纯态） |
|---|---|
| <img src="assets/screenshot_lab.png" alt="Lab" width="420"/> | <img src="assets/screenshot_bloch.png" alt="Bloch" width="420"/> |

| 多次采样与投影测量 | 量子隐形传态 |
|---|---|
| <img src="assets/screenshot_measurement.png" alt="Measurement" width="420"/> | <img src="assets/screenshot_teleportation.png" alt="Teleportation" width="420"/> |

| 噪声：理想贝尔态与去极化后的贝尔态 | Grover 与 Deutsch–Jozsa |
|---|---|
| <img src="assets/screenshot_noise.png" alt="Noise" width="420"/> | <img src="assets/screenshot_algorithms.png" alt="Algorithms" width="420"/> |

## 安装

需要 Python 3.11 或更高版本（已在 3.11 和 3.13 上测试）。

```bash
git clone https://github.com/rasidi3112/quantum-computing-simulation.git
cd quantum-computing-simulation
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

然后打开 <http://localhost:8501>.

运行时依赖为 `numpy`、`streamlit` 和 `plotly`。模拟包本身（`quantum_lab`，不含 `visualization`）只需要 NumPy。

## 使用方法

1. 在侧边栏选择**量子比特数量**（更改后会开始一个新的空电路）。
2. 选择一个门和目标量子比特，点击 **Apply Gate**；有两个或更多量子比特时，选择控制位和目标位，点击 **Apply CNOT**。
3. 在各标签页中查看结果：
   - **Lab**: 电路图、概率、振幅、相位、状态表；
   - **Bloch Sphere**: 每个量子比特一个球；
   - **Measurement**: *Run Measurement* 进行采样而不改变状态；*Measure Qubit* / *Measure All Qubits* 会使状态坍缩；
   - **Entanglement**, **Noise**, **Algorithms**: 独立的演示。*Load into Lab* 会把贝尔电路复制到实验室。
4. **Reset System** 回到 |0…0⟩，并根据种子重新启动随机数生成器。

图表可交互（悬停、缩放、旋转）。图表工具栏中的相机按钮可保存 PNG；*Save …* 按钮下载独立的交互式 HTML 文件。

### 示例电路

| 目标 | 步骤 | 预期结果 |
|---|---|---|
| 叠加 | 1 qubit: H → Q0 | P(0) = P(1) = 0.5; 布洛赫向量指向 +x |
| 贝尔态 \|Φ+⟩ | 2 qubits: H → Q0, CNOT Q0 → Q1 | (\|00⟩ + \|11⟩)/√2; P(00) = P(11) = 0.5, P(01) = P(10) = 0; 两个布洛赫向量的长度均为 0 |
| H·Z·H = X | 1 qubit: H, Z, H → Q0 | \|1⟩ |
| GHZ 态 | 3 qubits: H → Q0, CNOT Q0 → Q1, CNOT Q1 → Q2 | (\|000⟩ + \|111⟩)/√2 |
| 坍缩 | 贝尔态，然后对 Q0 执行 *Measure Qubit* | \|00⟩ / \|11⟩; Q1 随之确定 |

```
q0: ──[H]──●──
           │
q1: ───────⊕──
```

### 在 Python 中使用模拟器

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

## 量子数学约定

**状态。** *n* 个量子比特的寄存器是由 2ⁿ 个振幅 αᵢ 构成的复向量，满足 Σ|αᵢ|² = 1，初始为 |0…0⟩。

**量子比特顺序：大端序，全局统一。** 量子比特 0 是基态标签中*最左边*的比特，也是电路图中*最上面*的线：

```
|q0 q1 … q(n-1)⟩      index = Σ_k q_k · 2^(n-1-k)      |ψ⟩ = |q0⟩ ⊗ |q1⟩ ⊗ … ⊗ |q(n-1)⟩
```

因此在两个量子比特的情况下，对 Q0 施加 X 会把 |00⟩ 变为 |10⟩（索引 2）。作用在量子比特列表 `[a, b]` 上的矩阵把 `a` 视为最高有效位；特别地，`gates.CNOT` 是对应 `[control, target]` 的矩阵。这是教科书（Nielsen & Chuang）的约定。**Qiskit 使用相反的小端序**；比较时请把比特串反转。

**演化。** 每个算符在施加前都会检查幺正性（U†U = I，容差 10⁻¹⁰），幺正演化过程中从不重新归一化状态。测试确认经过 3000 个门后范数与 1 的偏差不超过 10⁻¹⁰。

**测量（计算基）：**

- *多次采样*按 P(i) = |αᵢ|² 抽取结果。它模拟每次采样前重新制备相同的状态；状态不变。
- 对量子比特 *k* 的*投影测量*以 P(m) = Σ_{i: bit k = m} |αᵢ|² 抽取 m ∈ {0, 1}，然后把状态替换为 P_m|ψ⟩ / √P(m)。测量全部量子比特后得到一个基态。
- *随机性。*整数种子可给出可复现的结果（`numpy.random.default_rng`）。在应用中，多次采样直接使用种子（相同的种子和状态 → 相同的直方图），而投影测量共用一个生成器，该生成器在重置、种子改变和寄存器大小改变时重新启动。

**布洛赫向量。** 对量子比特 *k*，约化密度矩阵 ρ_k = Tr_{others} |ψ⟩⟨ψ| 给出 r = (Tr ρ_kX, Tr ρ_kY, Tr ρ_kZ)，其中 ρ_k = (I + r·σ)/2。纯态量子比特有 |r| = 1；与其他量子比特纠缠或受噪声影响时 |r| < 1；纯度为 Tr ρ_k² = (1 + |r|²)/2。纠缠的寄存器没有单一的布洛赫向量，因此不会绘制。

**噪声。** 每个门之后，所选信道作用于该门涉及的每个量子比特（每次施加的错误概率为 *p*）：

| 信道 | 映射 |
|---|---|
| 比特翻转 | ρ → (1 − p)ρ + p XρX |
| 相位翻转 | ρ → (1 − p)ρ + p ZρZ |
| 去极化 | ρ → (1 − p)ρ + (p/3)(XρX + YρY + ZρZ) |

在这种参数化下，去极化信道把布洛赫向量缩放 1 − 4p/3 倍（p = 3/4 对应最大混合态）。空闲的量子比特和测量不含噪声。密度矩阵被精确演化；含噪电路中的测量按其结果取平均。

**保真度。** 相对于纯态参考为 ⟨ψ|ρ|ψ⟩，一般情况下为 Uhlmann 保真度 (Tr √(√ρ σ √ρ))²。

## 支持的量子门

| 门 | 矩阵 | 作用 |
|---|---|---|
| Identity (I) | [[1, 0], [0, 1]] | 保持量子比特不变 |
| Pauli-X | [[0, 1], [1, 0]] | 比特翻转 \|0⟩ ↔ \|1⟩ |
| Pauli-Y | [[0, −i], [i, 0]] | Y\|0⟩ = i\|1⟩, Y\|1⟩ = −i\|0⟩ |
| Pauli-Z | [[1, 0], [0, −1]] | 相位翻转 \|1⟩ → −\|1⟩ |
| Hadamard (H) | [[1, 1], [1, −1]]/√2 | \|0⟩ → \|+⟩, \|1⟩ → \|−⟩ |
| S | diag(1, i) | 相位 π/2 |
| T | diag(1, e^{iπ/4}) | 相位 π/4 |
| CNOT | \|0⟩⟨0\| ⊗ I + \|1⟩⟨1\| ⊗ X | 当控制位为 |1⟩ 时翻转目标位 |

Python API 还提供 `rx`、`ry`、`rz`、`phase`、作用于任意量子比特列表的任意幺正算符以及多控制单量子比特门；隐形传态和 Grover 电路会用到它们，但侧边栏中暂未提供。

## 算法与协议

- **贝尔态。** X 门选择输入，然后施加 H 和 CNOT。
- **隐形传态。** Q0 携带 cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩，Q1–Q2 共享一个贝尔对。Alice 施加 CNOT 和 H 并测量 Q0、Q1；若 m₁ = 1，Bob 施加 X，若 m₀ = 1，施加 Z。显示的保真度由模拟得到的状态计算，在四个分支中均为 1。
- **Grover.** Oracle = 在被标记项的零比特上施加 X、多控制 Z、再次施加 X；扩散 = Hⁿ Xⁿ (MCZ) Xⁿ Hⁿ。模拟得到的成功概率与 sin²((2k+1)θ)，sin θ = 1/√N 一致。
- **Deutsch–Jozsa.** Oracle U_f|x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩ 由 f 的真值表构造。应用提供常数函数、所选比特的奇偶函数和随机平衡函数。

## 架构

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

依赖关系是单向的：`main.py` → `quantum_lab` 和 `translations`；在包内，只有 `visualization` 模块导入 Plotly，没有任何模块导入 Streamlit，因此核心部分可以单独使用和测试。

## 测试

```bash
pip install -r requirements-dev.txt
pytest
pytest --ignore=tests/test_app.py
ruff check .
python benchmarks/bench_gates.py
```

`pytest` 大约需要 1.5 分钟（主要是无浏览器的界面测试）；加上 `--ignore=tests/test_app.py` 则只测试核心，几秒即可完成。

| 文件 | 覆盖内容 |
|---|---|
| `test_gates.py` | 每个门的幺正性、代数恒等式、克罗内克展开、CNOT 矩阵 |
| `test_simulator.py` | 归一化、Pauli/Hadamard 的行为、两次 H、CNOT 真值表、贝尔态和 GHZ 态、与稠密矩阵的比较、无效输入 |
| `test_measurement.py` | 玻恩定则、边缘分布、带种子的采样、统计、坍缩与重新归一化 |
| `test_states.py` | 偏迹、布洛赫向量、纯度、纠缠熵 |
| `test_circuit.py` | 电路的构建与执行、条件门、电路图布局 |
| `test_noise.py` | 信道保迹、解析结果、对错误轨迹的穷举求和 |
| `test_protocols.py` | 四个贝尔态、四个分支中的隐形传态 |
| `test_algorithms.py` | Grover 与闭式解的比较、针对 2 和 3 个输入的所有平衡函数的 Deutsch–Jozsa |
| `test_visualization.py` | 图表包含正确的数据 |
| `test_translations.py` | 15 种语言、键和占位符完全一致、界面用到的每个键都存在 |
| `test_app.py` | 端到端运行 Streamlit 应用（无浏览器），覆盖每种语言 |

数值比较使用容差（振幅为 10⁻¹²，采样统计为 5σ 范围），而不是严格的浮点相等。

已验证的组合： Python 3.11 + NumPy 1.26.4 / Streamlit 1.50.0 / Plotly 5.24.0; Python 3.13 + NumPy 2.5.4 / Streamlit 1.67.0 / Plotly 7.1.0.

## 性能与限制

| 量 | 状态向量 | 密度矩阵 |
|---|---|---|
| 内存 | 16 · 2ⁿ bytes | 16 · 4ⁿ bytes |
| 一个 k 量子比特门 | O(2ⁿ · 2ᵏ) | O(4ⁿ · 2ᵏ) |
| 代码中的硬性上限 | `MAX_QUBITS = 20` (16 MiB) | `MAX_DENSITY_QUBITS = 10` (16 MiB) |
| 界面中的上限 | 6 qubits | 6 qubits |

1.0 版为每个门构造一个 2ⁿ × 2ⁿ 的稠密矩阵；2.0 版把门与状态张量直接缩并。使用 `benchmarks/bench_gates.py` 测得（一个 Hadamard 门，多次运行取最优，单台机器；仅供参考）：

| Qubits | 稠密矩阵 (1.0) | 缩并 (2.0) | 比值 |
|---|---|---|---|
| 3 | 35 µs | 40 µs | 0.9× |
| 6 | 100 µs | 43 µs | 2× |
| 8 | 553 µs | 44 µs | 13× |
| 10 | 7.6 ms | 49 µs | 155× |
| 12 | 184 ms | 57 µs | ≈ 3200× |

在原先三量子比特的上限处没有加速（输入校验要花几微秒）；好处在于更大的寄存器变得可行。模拟开销仍然随每个量子比特翻倍。这是面向小型寄存器的教学工具，不是通用模拟器。

## 已知限制

- 界面提供 1–6 个量子比特；侧边栏中的门为 I、X、Y、Z、H、S、T 和 CNOT。旋转门只存在于 Python API 中。
- 只能在计算基（Z）下测量。
- 噪声是门之后的单量子比特 Pauli 噪声。没有振幅阻尼、读出错误、空闲噪声和关联噪声。
- Grover 只搜索一个被标记项；Deutsch–Jozsa 的 oracle 作为一个幺正方块施加，没有分解为基本门。
- 电路只能追加（没有撤销、编辑和拖放）。
- 电路图是等宽文本；很长的电路会水平滚动。
- 阿拉伯语已翻译，但页面布局没有做从右到左的镜像。
- 2.0 中新增的 80 条文本未经母语者审校；欢迎指正。
- 不连接真实的量子硬件或云端后端。

## 相对 1.0 可能影响你的变更

- **CNOT 的结果不同了，因为旧结果是错的。** 1.0 混用了两种量子比特顺序，导致把单量子比特门与 CNOT 组合的电路给出错误的状态（见 `docs/AUDIT.md`，发现 Q1）。
- `QuantumSimulator` 从 `main.py` 移到了 `quantum_lab`。1.0 的方法（`apply_gate`、`get_probabilities`、`get_amplitudes`、`measure`、`reset`、`_expand_gate`、`_create_cnot_matrix`）均保留。无效输入现在会抛出 `ValueError`/`TypeError`，不再被悄悄接受；`state` 为只读；非幺正矩阵会被拒绝。
- 测量直方图在点击 *Run Measurement* 后出现，不再在每次交互时重新生成。
- 图表改用 Plotly，不再使用 Matplotlib。*Save …* 按钮现在下载交互式 HTML；PNG 导出位于每个图表的工具栏中。
- 已从 `requirements.txt` 中移除 `matplotlib` 和未使用的 `qiskit`，并添加了 `plotly`。

## 部署到 Streamlit Community Cloud

1. 把仓库（或你的 fork）推送到 GitHub。
2. 用 GitHub 登录 <https://share.streamlit.io> 并创建新应用。
3. 选择仓库和分支，把 main file path 设为 `main.py`。
4. 在 advanced settings 中选择 Python 3.11 或更高版本，然后部署。

依赖从 `requirements.txt` 安装；不需要任何密钥或环境变量。以上步骤根据对该平台的使用经验写成，准备本次发布时未能对照其最新文档核实。如果界面有所不同，请参照 <https://docs.streamlit.io/deploy/streamlit-community-cloud>.

`.devcontainer` 配置在启动 Streamlit 时关闭了 CORS 和 XSRF 保护，这是 GitHub Codespaces 端口转发所需要的。公开部署时请不要沿用这些参数。

## 路线图

- 在侧边栏加入旋转门（Rx、Ry、Rz）和更多双量子比特门（CZ、SWAP）
- 撤销与电路编辑；保存和载入电路
- 在其他基下测量；Pauli 可观测量的期望值
- 振幅阻尼和读出错误信道
- 把电路导出为 OpenQASM
- 由母语者审校翻译；从右到左的布局

## 许可与署名

以 [MIT 许可证](LICENSE) 发布，Copyright (c) 2025 rasidi3112。许可证文件未作改动。

Mini Quantum Lab 由 [Rasidi](https://github.com/rasidi3112) 创建，他编写了最初的应用、界面和翻译。2.0 版（模拟核心、测试、可视化和新增功能）在此基础上构建。
