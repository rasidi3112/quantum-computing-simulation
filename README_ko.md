<h1 align="center">Mini Quantum Lab 2.0</h1>

<p align="center">
  <b>학습을 위한, 테스트를 거친 대화형 양자 컴퓨팅 시뮬레이터</b><br>
  Python · NumPy · Streamlit · Plotly · 15개 인터페이스 언어
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
  <b>한국어</b> ·
  <a href="README_ms.md">Bahasa Melayu</a> ·
  <a href="README_pl.md">Polski</a> ·
  <a href="README_pt.md">Português</a> ·
  <a href="README_ru.md">Русский</a> ·
  <a href="README_tr.md">Türkçe</a> ·
  <a href="README_vi.md">Tiếng Việt</a> ·
  <a href="README_zh.md">中文</a>
</p>

---

## 개요

Mini Quantum Lab은 양자 컴퓨팅의 기초를 탐구하기 위한 교육용 웹 애플리케이션입니다. 게이트를 하나씩 더해 작은 회로를 만들고, 상태 벡터를 관찰하고, 각 큐비트를 블로흐 구에서 확인하고, 측정하고, 노이즈를 추가하고, 교과서에 나오는 몇 가지 프로토콜과 알고리즘을 실행할 수 있습니다.

버전 2.0은 원래 프로젝트의 모습과 사용 흐름을 유지하면서 내부를 교체했습니다. 단위 테스트가 있는 독립된 시뮬레이션 패키지, 문서화된 하나의 큐비트 순서 규약, 물리적으로 일관된 측정, 새로운 시각화가 그것입니다. 변경의 계기가 된 감사 내용은 [`docs/AUDIT.md`](docs/AUDIT.md)에 있습니다.

> 이 프로젝트는 IBM Quantum Composer와 Qiskit 같은 도구의 시각적 스타일에서 영감을 받았습니다. 독립적인 교육 프로젝트이며 **IBM을 비롯한 어떤 양자 컴퓨팅 기관과도 제휴하지 않았고 그 승인을 받지도 않았습니다**. 고전 컴퓨터에서 이상적인 큐비트와 노이즈가 있는 큐비트를 시뮬레이션하며, 양자 하드웨어에 연결하지 않습니다.

## 기능

| 영역 | 할 수 있는 일 |
|---|---|
| **실험실** | 1–6 큐비트. 임의의 큐비트에 I, X, Y, Z, H, S, T 게이트. 임의의 두 큐비트 사이의 CNOT. 실시간 회로도, 상태 표, 게이트 기록 |
| **상태 시각화** | 확률 분포, 진폭의 실수부와 허수부, 각 진폭의 위상을 기저 상태 레이블과 함께 표시 |
| **블로흐 구** | 큐비트마다 하나씩 제공되는 대화형 3D 구. 큐비트의 *축소 상태*로 그리며, 벡터 길이와 순도를 함께 보여 주어 순수 상태와 혼합 상태를 구별할 수 있습니다 |
| **측정** | 시드를 사용하는 샷 샘플링(100–10 000샷)과, 하나 또는 모든 큐비트에 대한 사영 측정 및 상태 붕괴 |
| **얽힘** | 엔트로피와 붕괴 시연이 포함된 네 가지 벨 상태 생성기. 임의의 단일 큐비트 상태에 대한 3큐비트 양자 순간이동 |
| **노이즈** | 각 게이트 뒤에 적용되는 비트 반전, 위상 반전, 탈분극 채널. 밀도 행렬로 정확하게 시뮬레이션 |
| **알고리즘** | 그로버 탐색(2–5 큐비트)과 도이치–조사(입력 큐비트 1–4개). 설명과 회로 포함 |
| **언어** | English, Indonesian, Spanish, Mandarin Chinese, Arabic, French, Japanese, Korean, German, Portuguese, Russian, Hindi, Turkish, Italian, Vietnamese |

## 스크린샷

| 실험실: 회로, 확률, 진폭 | 블로흐 구(Q0과 Q1은 얽힘, Q2는 순수 상태) |
|---|---|
| <img src="assets/screenshot_lab.png" alt="Lab" width="420"/> | <img src="assets/screenshot_bloch.png" alt="Bloch" width="420"/> |

| 샷 샘플링과 사영 측정 | 양자 순간이동 |
|---|---|
| <img src="assets/screenshot_measurement.png" alt="Measurement" width="420"/> | <img src="assets/screenshot_teleportation.png" alt="Teleportation" width="420"/> |

| 노이즈: 이상적인 벨 상태와 탈분극된 벨 상태 | 그로버와 도이치–조사 |
|---|---|
| <img src="assets/screenshot_noise.png" alt="Noise" width="420"/> | <img src="assets/screenshot_algorithms.png" alt="Algorithms" width="420"/> |

## 설치

Python 3.11 이상이 필요합니다(3.11과 3.13에서 테스트).

```bash
git clone https://github.com/rasidi3112/quantum-computing-simulation.git
cd quantum-computing-simulation
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

그런 다음 아래 주소를 엽니다: <http://localhost:8501>.

실행 시 의존성은 `numpy`, `streamlit`, `plotly`입니다. 시뮬레이션 패키지 자체(`visualization`을 제외한 `quantum_lab`)는 NumPy만 필요합니다.

## 사용법

1. 사이드바에서 **큐비트 수**를 선택합니다(변경하면 빈 회로가 새로 시작됩니다).
2. 게이트와 타겟 큐비트를 고르고 **Apply Gate**를 누릅니다. 큐비트가 둘 이상이면 제어와 타겟을 고르고 **Apply CNOT**을 누릅니다.
3. 탭에서 결과를 확인합니다:
   - **Lab**: 회로도, 확률, 진폭, 위상, 상태 표
   - **Bloch Sphere**: 큐비트마다 구 하나
   - **Measurement**: *Run Measurement*는 상태를 건드리지 않고 샷을 샘플링하고, *Measure Qubit* / *Measure All Qubits*는 상태를 붕괴시킵니다
   - **Entanglement**, **Noise**, **Algorithms**: 독립적인 시연입니다. *Load into Lab*은 벨 회로를 실험실로 복사합니다.
4. **Reset System**은 |0…0⟩으로 돌아가고 난수 생성기를 시드에서 다시 시작합니다.

차트는 대화형입니다(마우스 올리기, 확대, 회전). 차트 도구 모음의 카메라 버튼은 PNG를 저장하고, *Save …* 버튼은 독립 실행형 대화형 HTML 파일을 내려받습니다.

### 예제 회로

| 목표 | 단계 | 예상 결과 |
|---|---|---|
| 중첩 | 1 qubit: H → Q0 | P(0) = P(1) = 0.5; 블로흐 벡터가 +x 방향 |
| 벨 상태 \|Φ+⟩ | 2 qubits: H → Q0, CNOT Q0 → Q1 | (\|00⟩ + \|11⟩)/√2; P(00) = P(11) = 0.5, P(01) = P(10) = 0; 두 블로흐 벡터의 길이가 모두 0 |
| H·Z·H = X | 1 qubit: H, Z, H → Q0 | \|1⟩ |
| GHZ 상태 | 3 qubits: H → Q0, CNOT Q0 → Q1, CNOT Q1 → Q2 | (\|000⟩ + \|111⟩)/√2 |
| 붕괴 | 벨 상태를 만든 뒤 Q0에 *Measure Qubit* | \|00⟩ / \|11⟩; Q1도 결정됩니다 |

```
q0: ──[H]──●──
           │
q1: ───────⊕──
```

### Python에서 시뮬레이터 사용하기

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

## 양자 수학 규약

**상태.** *n*큐비트 레지스터는 Σ|αᵢ|² = 1을 만족하는 2ⁿ개의 진폭 αᵢ로 이루어진 복소 벡터이며 |0…0⟩으로 초기화됩니다.

**큐비트 순서: 빅 엔디언, 모든 곳에서 동일.** 큐비트 0은 기저 레이블의 *가장 왼쪽* 비트이자 회로도의 *맨 위* 선입니다:

```
|q0 q1 … q(n-1)⟩      index = Σ_k q_k · 2^(n-1-k)      |ψ⟩ = |q0⟩ ⊗ |q1⟩ ⊗ … ⊗ |q(n-1)⟩
```

따라서 2큐비트에서 Q0에 X를 적용하면 |00⟩이 |10⟩(인덱스 2)이 됩니다. 큐비트 목록 `[a, b]`에 작용하는 행렬은 `a`를 최상위 비트로 취급하며, 특히 `gates.CNOT`은 `[control, target]`에 대한 행렬입니다. 이는 교과서(Nielsen & Chuang)의 규약입니다. **Qiskit은 반대인 리틀 엔디언 순서를 사용**하므로 비교할 때는 비트 문자열을 뒤집으십시오.

**시간 전개.** 모든 연산자는 적용 전에 유니터리성(U†U = I, 허용 오차 10⁻¹⁰)을 검사하며, 유니터리 전개 중에는 상태를 다시 정규화하지 않습니다. 테스트는 3000개의 게이트 이후에도 노름이 1에서 10⁻¹⁰ 이내임을 확인합니다.

**측정(계산 기저):**

- *샷 샘플링*은 P(i) = |αᵢ|²에서 결과를 뽑습니다. 매 샷마다 같은 상태를 다시 준비하는 것을 모형화하며, 상태는 변하지 않습니다.
- 큐비트 *k*의 *사영 측정*은 P(m) = Σ_{i: bit k = m} |αᵢ|²로 m ∈ {0, 1}을 뽑은 뒤 상태를 P_m|ψ⟩ / √P(m)으로 바꿉니다. 모든 큐비트를 측정하면 기저 상태가 남습니다.
- *무작위성.* 정수 시드는 재현 가능한 결과를 줍니다(`numpy.random.default_rng`). 앱에서 샷 샘플링은 시드를 직접 사용하고(같은 시드와 상태 → 같은 히스토그램), 사영 측정은 하나의 생성기를 이어서 사용합니다. 이 생성기는 초기화할 때, 시드가 바뀔 때, 레지스터 크기가 바뀔 때 다시 시작됩니다.

**블로흐 벡터.** 큐비트 *k*에 대해 축소 밀도 행렬 ρ_k = Tr_{others} |ψ⟩⟨ψ|는 r = (Tr ρ_kX, Tr ρ_kY, Tr ρ_kZ)를 주며 ρ_k = (I + r·σ)/2입니다. 순수한 큐비트는 |r| = 1이고, 다른 큐비트와 얽혀 있거나 노이즈의 영향을 받으면 |r| < 1이며, 순도는 Tr ρ_k² = (1 + |r|²)/2입니다. 얽힌 레지스터에는 단일 블로흐 벡터가 없으므로 그리지 않습니다.

**노이즈.** 각 게이트 뒤에, 선택한 채널이 그 게이트가 작용한 모든 큐비트에 작용합니다(적용 1회당 오류 확률 *p*):

| 채널 | 사상 |
|---|---|
| 비트 반전 | ρ → (1 − p)ρ + p XρX |
| 위상 반전 | ρ → (1 − p)ρ + p ZρZ |
| 탈분극 | ρ → (1 − p)ρ + (p/3)(XρX + YρY + ZρZ) |

이 매개변수화에서 탈분극 채널은 블로흐 벡터를 1 − 4p/3배로 줄입니다(p = 3/4이면 최대 혼합 상태). 대기 중인 큐비트와 측정에는 노이즈가 없습니다. 밀도 행렬은 정확하게 전개되며, 노이즈가 있는 회로 안의 측정은 결과에 대해 평균됩니다.

**충실도.** 순수 상태 기준에 대해서는 ⟨ψ|ρ|ψ⟩, 일반적으로는 울만 충실도 (Tr √(√ρ σ √ρ))².

## 지원하는 양자 게이트

| 게이트 | 행렬 | 작용 |
|---|---|---|
| Identity (I) | [[1, 0], [0, 1]] | 큐비트를 그대로 둠 |
| Pauli-X | [[0, 1], [1, 0]] | 비트 반전 \|0⟩ ↔ \|1⟩ |
| Pauli-Y | [[0, −i], [i, 0]] | Y\|0⟩ = i\|1⟩, Y\|1⟩ = −i\|0⟩ |
| Pauli-Z | [[1, 0], [0, −1]] | 위상 반전 \|1⟩ → −\|1⟩ |
| Hadamard (H) | [[1, 1], [1, −1]]/√2 | \|0⟩ → \|+⟩, \|1⟩ → \|−⟩ |
| S | diag(1, i) | 위상 π/2 |
| T | diag(1, e^{iπ/4}) | 위상 π/4 |
| CNOT | \|0⟩⟨0\| ⊗ I + \|1⟩⟨1\| ⊗ X | 제어가 |1⟩이면 타겟을 반전 |

Python API는 추가로 `rx`, `ry`, `rz`, `phase`, 임의의 큐비트 목록에 대한 임의의 유니터리, 다중 제어 단일 큐비트 게이트를 제공합니다. 이들은 순간이동과 그로버 회로에서 쓰이지만 사이드바에는 아직 없습니다.

## 알고리즘과 프로토콜

- **벨 상태.** X 게이트로 입력을 고른 뒤 H와 CNOT을 적용합니다.
- **순간이동.** Q0은 cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩을 갖고, Q1–Q2는 벨 쌍을 공유합니다. 앨리스가 CNOT과 H를 적용하고 Q0, Q1을 측정하며, 밥은 m₁ = 1이면 X를, m₀ = 1이면 Z를 적용합니다. 표시되는 충실도는 시뮬레이션한 상태로부터 계산되며 네 가지 분기 모두에서 1입니다.
- **Grover.** 오라클 = 표시된 항목의 0인 비트에 X, 다중 제어 Z, 다시 X. 확산 = Hⁿ Xⁿ (MCZ) Xⁿ Hⁿ. 시뮬레이션한 성공 확률은 sin²((2k+1)θ), sin θ = 1/√N과 일치합니다.
- **Deutsch–Jozsa.** 오라클 U_f|x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩는 f의 진리표로부터 만듭니다. 앱은 상수 함수, 선택한 비트의 패리티, 무작위 균형 함수를 제공합니다.

## 아키텍처

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

의존성은 한 방향으로만 향합니다: `main.py` → `quantum_lab`과 `translations`. 패키지 안에서 Plotly를 가져오는 모듈은 `visualization`뿐이고 Streamlit을 가져오는 모듈은 없으므로, 코어를 따로 사용하고 테스트할 수 있습니다.

## 테스트

```bash
pip install -r requirements-dev.txt
pytest
pytest --ignore=tests/test_app.py
ruff check .
python benchmarks/bench_gates.py
```

`pytest`는 약 1.5분이 걸립니다(대부분 브라우저 없는 UI 테스트). `--ignore=tests/test_app.py`를 붙이면 코어만 몇 초 안에 테스트합니다.

| 파일 | 검증 내용 |
|---|---|
| `test_gates.py` | 모든 게이트의 유니터리성, 대수적 항등식, 크로네커 확장, CNOT 행렬 |
| `test_simulator.py` | 정규화, 파울리/아다마르의 동작, H 두 번, CNOT 진리표, 벨 상태와 GHZ 상태, 조밀 행렬과의 비교, 잘못된 입력 |
| `test_measurement.py` | 보른 규칙, 주변 분포, 시드를 쓰는 샘플링, 통계, 붕괴와 재정규화 |
| `test_states.py` | 부분 대각합, 블로흐 벡터, 순도, 얽힘 엔트로피 |
| `test_circuit.py` | 회로 구성과 실행, 조건부 게이트, 회로도 배치 |
| `test_noise.py` | 채널의 대각합 보존, 해석적 결과, 오류 궤적 전체에 대한 합 |
| `test_protocols.py` | 네 가지 벨 상태, 네 분기 모두에서의 순간이동 |
| `test_algorithms.py` | 닫힌 형식과 비교한 그로버, 입력 2개와 3개의 모든 균형 함수에 대한 도이치–조사 |
| `test_visualization.py` | 그림이 올바른 데이터를 담고 있는지 |
| `test_translations.py` | 15개 언어, 동일한 키와 자리 표시자, UI가 사용하는 모든 키의 존재 |
| `test_app.py` | Streamlit 앱 전체(헤드리스), 모든 언어 |

수치 비교는 정확한 부동소수점 동등성이 아니라 허용 오차를 사용합니다(진폭은 10⁻¹², 샘플링 통계는 5σ 범위).

검증된 조합: Python 3.11 + NumPy 1.26.4 / Streamlit 1.50.0 / Plotly 5.24.0; Python 3.13 + NumPy 2.5.4 / Streamlit 1.67.0 / Plotly 7.1.0.

## 성능과 한계

| 항목 | 상태 벡터 | 밀도 행렬 |
|---|---|---|
| 메모리 | 16 · 2ⁿ bytes | 16 · 4ⁿ bytes |
| k큐비트 게이트 하나 | O(2ⁿ · 2ᵏ) | O(4ⁿ · 2ᵏ) |
| 코드의 최대 한계 | `MAX_QUBITS = 20` (16 MiB) | `MAX_DENSITY_QUBITS = 10` (16 MiB) |
| 인터페이스의 한계 | 6 qubits | 6 qubits |

버전 1.0은 게이트마다 2ⁿ × 2ⁿ 조밀 행렬을 만들었지만, 2.0은 게이트를 상태 텐서와 축약합니다. `benchmarks/bench_gates.py`로 측정했습니다(아다마르 하나, 여러 번 실행 중 최선, 한 대의 기계. 참고용으로 보십시오):

| Qubits | 조밀 행렬 (1.0) | 축약 (2.0) | 비율 |
|---|---|---|---|
| 3 | 35 µs | 40 µs | 0.9× |
| 6 | 100 µs | 43 µs | 2× |
| 8 | 553 µs | 44 µs | 13× |
| 10 | 7.6 ms | 49 µs | 155× |
| 12 | 184 ms | 57 µs | ≈ 3200× |

예전 한계인 3큐비트에서는 속도 향상이 없습니다(입력 검증에 몇 마이크로초가 듭니다). 이점은 더 큰 레지스터가 실용적이 되었다는 것입니다. 시뮬레이션 비용은 여전히 큐비트가 하나 늘 때마다 두 배가 됩니다. 이것은 작은 레지스터를 위한 교육 도구이며 범용 시뮬레이터가 아닙니다.

## 알려진 제한 사항

- 인터페이스는 1–6 큐비트를 제공하며, 사이드바의 게이트는 I, X, Y, Z, H, S, T와 CNOT입니다. 회전 게이트는 Python API에만 있습니다.
- 측정은 계산 기저(Z)에서만 이루어집니다.
- 노이즈는 게이트 뒤의 단일 큐비트 파울리 노이즈입니다. 진폭 감쇠, 판독 오류, 대기 노이즈, 상관된 노이즈는 없습니다.
- 그로버는 표시된 항목 하나만 찾습니다. 도이치–조사 오라클은 기본 게이트로 분해하지 않고 하나의 유니터리 상자로 적용합니다.
- 회로는 추가만 가능합니다(실행 취소, 편집, 끌어다 놓기 없음).
- 회로도는 고정폭 텍스트이며, 매우 긴 회로는 가로로 스크롤됩니다.
- 아랍어는 번역되어 있지만 페이지 배치는 오른쪽에서 왼쪽으로 뒤집히지 않습니다.
- 2.0에서 추가된 80개의 문자열은 원어민 검토 없이 번역되었습니다. 수정 제안을 환영합니다.
- 실제 양자 하드웨어나 클라우드 백엔드에 연결하지 않습니다.

## 1.0에서 달라져 영향을 줄 수 있는 점

- **CNOT 결과가 달라졌습니다. 예전 결과가 틀렸기 때문입니다.** 1.0은 두 가지 큐비트 순서를 섞어 썼기 때문에, 단일 큐비트 게이트와 CNOT을 함께 쓰는 회로가 잘못된 상태를 냈습니다(`docs/AUDIT.md`의 발견 사항 Q1 참조).
- `QuantumSimulator`가 `main.py`에서 `quantum_lab`으로 옮겨졌습니다. 1.0의 메서드(`apply_gate`, `get_probabilities`, `get_amplitudes`, `measure`, `reset`, `_expand_gate`, `_create_cnot_matrix`)는 유지됩니다. 잘못된 입력은 이제 조용히 받아들여지지 않고 `ValueError`/`TypeError`를 일으키며, `state`는 읽기 전용이고, 유니터리가 아닌 행렬은 거부됩니다.
- 측정 히스토그램은 상호작용할 때마다 다시 만들어지는 대신 *Run Measurement*를 누른 뒤에 나타납니다.
- 그래프는 Matplotlib 대신 Plotly를 사용합니다. *Save …* 버튼은 이제 대화형 HTML을 내려받으며, PNG 내보내기는 각 차트의 도구 모음에 있습니다.
- `matplotlib`과 사용하지 않던 `qiskit`을 `requirements.txt`에서 제거하고 `plotly`를 추가했습니다.

## Streamlit Community Cloud에 배포하기

1. 저장소(또는 자신의 포크)를 GitHub에 푸시합니다.
2. GitHub 계정으로 <https://share.streamlit.io>에 로그인하고 새 앱을 만듭니다.
3. 저장소와 브랜치를 선택하고 main file path를 `main.py`로 설정합니다.
4. advanced settings에서 Python 3.11 이상을 선택한 뒤 배포합니다.

의존성은 `requirements.txt`에서 설치되며, 시크릿이나 환경 변수는 필요하지 않습니다. 이 단계는 플랫폼 사용 경험을 바탕으로 작성했으며, 이번 릴리스를 준비하는 동안 최신 문서와 대조하지 못했습니다. 화면이 다르면 다음 문서를 따르십시오: <https://docs.streamlit.io/deploy/streamlit-community-cloud>.

`.devcontainer` 설정은 CORS와 XSRF 보호를 끈 상태로 Streamlit을 시작합니다. 이는 GitHub Codespaces의 포트 포워딩에 필요한 것입니다. 공개 배포에는 이 옵션을 쓰지 마십시오.

## 로드맵

- 사이드바에 회전 게이트(Rx, Ry, Rz)와 더 많은 2큐비트 게이트(CZ, SWAP) 추가
- 실행 취소와 회로 편집, 회로 저장과 불러오기
- 다른 기저에서의 측정, 파울리 관측량의 기댓값
- 진폭 감쇠 채널과 판독 오류 채널
- 회로를 OpenQASM으로 내보내기
- 원어민의 번역 검토, 오른쪽에서 왼쪽으로의 배치

## 라이선스와 저작자 표시

[MIT 라이선스](LICENSE)로 배포됩니다. Copyright (c) 2025 rasidi3112. 라이선스 파일은 변경하지 않았습니다.

Mini Quantum Lab은 [Rasidi](https://github.com/rasidi3112)가 만들었으며, 원래의 애플리케이션과 인터페이스, 번역을 작성했습니다. 버전 2.0(시뮬레이션 코어, 테스트, 시각화, 추가 기능)은 그 작업을 바탕으로 합니다.
