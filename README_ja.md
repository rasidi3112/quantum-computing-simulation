<h1 align="center">Mini Quantum Lab 2.0</h1>

<p align="center">
  <b>学習のための、テスト済みのインタラクティブな量子コンピューティングシミュレーター</b><br>
  Python · NumPy · Streamlit · Plotly · 15 のインターフェース言語
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
  <b>日本語</b> ·
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

## 概要

Mini Quantum Lab は、量子コンピューティングの基礎を学ぶための教育用ウェブアプリです。ゲートを一つずつ置いて小さな回路を組み、状態ベクトルを観察し、各量子ビットをブロッホ球で確認し、測定し、ノイズを加え、教科書的なプロトコルやアルゴリズムをいくつか実行できます。

バージョン 2.0 は元のプロジェクトの見た目と操作の流れを保ちつつ、内部を置き換えました。単体テスト付きの独立したシミュレーションパッケージ、文書化された一貫した量子ビット順序の規約、物理的に整合した測定、新しい可視化です。変更のきっかけとなった監査は [`docs/AUDIT.md`](docs/AUDIT.md) にあります。

> 本プロジェクトは IBM Quantum Composer や Qiskit などのツールの視覚的なスタイルに着想を得ています。独立した教育プロジェクトであり、**IBM その他の量子コンピューティング関連組織とは提携しておらず、その承認も受けていません**。古典コンピューター上で理想的な量子ビットとノイズのある量子ビットをシミュレートするもので、量子ハードウェアには接続しません。

## 機能

| 領域 | できること |
|---|---|
| **ラボ** | 1〜6 量子ビット。任意の量子ビットに I、X、Y、Z、H、S、T ゲート。任意の 2 量子ビット間の CNOT。リアルタイムの回路図、状態表、ゲート履歴 |
| **状態の可視化** | 確率分布、振幅の実部と虚部、各振幅の位相を、基底状態のラベル付きで表示 |
| **ブロッホ球** | 量子ビットごとのインタラクティブな 3D 球。その量子ビットの*縮約状態*から描画し、ベクトルの長さと純粋度を示すので、純粋状態と混合状態を区別できます |
| **測定** | シード付きのショットサンプリング（100〜10 000 ショット）と、1 つまたはすべての量子ビットの射影測定（状態の収縮を伴う） |
| **量子もつれ** | 4 つのベル状態のジェネレーター（エントロピーと収縮のデモ付き）。任意の 1 量子ビット状態の 3 量子ビット量子テレポーテーション |
| **ノイズ** | 各ゲートの後に適用するビット反転、位相反転、脱分極チャネル。密度行列で厳密にシミュレート |
| **アルゴリズム** | グローバー探索（2〜5 量子ビット）とドイッチュ–ジョサ（入力 1〜4 量子ビット）。解説と回路付き |
| **言語** | English, Indonesian, Spanish, Mandarin Chinese, Arabic, French, Japanese, Korean, German, Portuguese, Russian, Hindi, Turkish, Italian, Vietnamese |

## スクリーンショット

| ラボ：回路、確率、振幅 | ブロッホ球（Q0 と Q1 はもつれ、Q2 は純粋状態） |
|---|---|
| <img src="assets/screenshot_lab.png" alt="Lab" width="420"/> | <img src="assets/screenshot_bloch.png" alt="Bloch" width="420"/> |

| ショットサンプリングと射影測定 | 量子テレポーテーション |
|---|---|
| <img src="assets/screenshot_measurement.png" alt="Measurement" width="420"/> | <img src="assets/screenshot_teleportation.png" alt="Teleportation" width="420"/> |

| ノイズ：理想的なベル状態と脱分極後のベル状態 | グローバーとドイッチュ–ジョサ |
|---|---|
| <img src="assets/screenshot_noise.png" alt="Noise" width="420"/> | <img src="assets/screenshot_algorithms.png" alt="Algorithms" width="420"/> |

## インストール

Python 3.11 以降が必要です（3.11 と 3.13 でテスト済み）。

```bash
git clone https://github.com/rasidi3112/quantum-computing-simulation.git
cd quantum-computing-simulation
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

その後、次を開きます： <http://localhost:8501>.

実行時の依存パッケージは `numpy`、`streamlit`、`plotly` です。シミュレーションパッケージ本体（`visualization` を除く `quantum_lab`）は NumPy だけで動作します。

## 使い方

1. サイドバーで**量子ビット数**を選びます（変更すると新しい空の回路が始まります）。
2. ゲートとターゲット量子ビットを選んで **Apply Gate** を押します。2 量子ビット以上の場合は、制御とターゲットを選んで **Apply CNOT** を押します。
3. 結果は各タブで確認します：
   - **Lab**: 回路図、確率、振幅、位相、状態表
   - **Bloch Sphere**: 量子ビットごとに 1 つの球
   - **Measurement**: *Run Measurement* は状態を変えずにショットをサンプリングし、*Measure Qubit* / *Measure All Qubits* は状態を収縮させます
   - **Entanglement**, **Noise**, **Algorithms**: 独立したデモです。*Load into Lab* はベル回路をラボにコピーします。
4. **Reset System** は |0…0⟩ に戻し、乱数生成器をシードから再スタートします。

グラフはインタラクティブです（ホバー、ズーム、回転）。グラフのツールバーにあるカメラボタンで PNG を保存でき、*Save …* ボタンは単体で動くインタラクティブな HTML ファイルをダウンロードします。

### 回路の例

| 目的 | 手順 | 期待される結果 |
|---|---|---|
| 重ね合わせ | 1 qubit: H → Q0 | P(0) = P(1) = 0.5; ブロッホベクトルは +x 方向 |
| ベル状態 \|Φ+⟩ | 2 qubits: H → Q0, CNOT Q0 → Q1 | (\|00⟩ + \|11⟩)/√2; P(00) = P(11) = 0.5, P(01) = P(10) = 0; 両方のブロッホベクトルの長さは 0 |
| H·Z·H = X | 1 qubit: H, Z, H → Q0 | \|1⟩ |
| GHZ 状態 | 3 qubits: H → Q0, CNOT Q0 → Q1, CNOT Q1 → Q2 | (\|000⟩ + \|111⟩)/√2 |
| 収縮 | ベル状態を作り、Q0 に *Measure Qubit* | \|00⟩ / \|11⟩; Q1 も確定します |

```
q0: ──[H]──●──
           │
q1: ───────⊕──
```

### Python からシミュレーターを使う

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

## 量子数学の規約

**状態。** *n* 量子ビットのレジスタは、Σ|αᵢ|² = 1 を満たす 2ⁿ 個の振幅 αᵢ からなる複素ベクトルで、|0…0⟩ に初期化されます。

**量子ビットの順序：ビッグエンディアン（全体で統一）。** 量子ビット 0 は基底ラベルの*最も左*のビットであり、回路図の*一番上*の線です：

```
|q0 q1 … q(n-1)⟩      index = Σ_k q_k · 2^(n-1-k)      |ψ⟩ = |q0⟩ ⊗ |q1⟩ ⊗ … ⊗ |q(n-1)⟩
```

したがって 2 量子ビットでは、Q0 への X は |00⟩ を |10⟩（インデックス 2）に変えます。量子ビットのリスト `[a, b]` に作用する行列は `a` を最上位ビットとして扱います。特に `gates.CNOT` は `[control, target]` に対する行列です。これは教科書（Nielsen & Chuang）の規約です。**Qiskit は逆のリトルエンディアン順を使う**ので、比較するときはビット列を反転してください。

**時間発展。** すべての演算子は適用前にユニタリ性（U†U = I、許容誤差 10⁻¹⁰）を検査し、ユニタリ発展の途中で状態を再規格化することはありません。テストでは、3000 ゲート後もノルムと 1 との差が 10⁻¹⁰ 以内であることを確認しています。

**測定（計算基底）：**

- *ショットサンプリング*は P(i) = |αᵢ|² から結果を抽出します。ショットごとに同じ状態を準備し直すことをモデル化しており、状態は変化しません。
- 量子ビット *k* の*射影測定*は P(m) = Σ_{i: bit k = m} |αᵢ|² で m ∈ {0, 1} を抽出し、状態を P_m|ψ⟩ / √P(m) に置き換えます。すべての量子ビットを測定すると基底状態が残ります。
- *乱数。*整数のシードを指定すると結果を再現できます（`numpy.random.default_rng`）。アプリでは、ショットサンプリングはシードを直接使い（同じシードと状態 → 同じヒストグラム）、射影測定は 1 つの生成器を使い続けます。この生成器はリセット時、シード変更時、レジスタサイズ変更時に再スタートします。

**ブロッホベクトル。** 量子ビット *k* について、縮約密度行列 ρ_k = Tr_{others} |ψ⟩⟨ψ| から r = (Tr ρ_kX, Tr ρ_kY, Tr ρ_kZ) が得られ、ρ_k = (I + r·σ)/2 です。純粋な量子ビットでは |r| = 1、他の量子ビットともつれている場合やノイズを受けた場合は |r| < 1 となり、純粋度は Tr ρ_k² = (1 + |r|²)/2 です。もつれたレジスタ全体には単一のブロッホベクトルがないため、描画しません。

**ノイズ。** 各ゲートの後、選択したチャネルがそのゲートの作用した各量子ビットに作用します（1 回の適用あたりのエラー確率 *p*）：

| チャネル | 写像 |
|---|---|
| ビット反転 | ρ → (1 − p)ρ + p XρX |
| 位相反転 | ρ → (1 − p)ρ + p ZρZ |
| 脱分極 | ρ → (1 − p)ρ + (p/3)(XρX + YρY + ZρZ) |

このパラメーター化では、脱分極チャネルはブロッホベクトルを 1 − 4p/3 倍に縮めます（p = 3/4 で最大混合状態）。待機中の量子ビットと測定にはノイズがありません。密度行列は厳密に発展させ、ノイズのある回路内の測定は結果について平均します。

**忠実度。** 純粋状態の基準に対しては ⟨ψ|ρ|ψ⟩、一般にはウールマン忠実度 (Tr √(√ρ σ √ρ))²。

## 対応している量子ゲート

| ゲート | 行列 | 作用 |
|---|---|---|
| Identity (I) | [[1, 0], [0, 1]] | 量子ビットを変化させない |
| Pauli-X | [[0, 1], [1, 0]] | ビット反転 \|0⟩ ↔ \|1⟩ |
| Pauli-Y | [[0, −i], [i, 0]] | Y\|0⟩ = i\|1⟩, Y\|1⟩ = −i\|0⟩ |
| Pauli-Z | [[1, 0], [0, −1]] | 位相反転 \|1⟩ → −\|1⟩ |
| Hadamard (H) | [[1, 1], [1, −1]]/√2 | \|0⟩ → \|+⟩, \|1⟩ → \|−⟩ |
| S | diag(1, i) | 位相 π/2 |
| T | diag(1, e^{iπ/4}) | 位相 π/4 |
| CNOT | \|0⟩⟨0\| ⊗ I + \|1⟩⟨1\| ⊗ X | 制御が |1⟩ のときターゲットを反転 |

Python API ではさらに `rx`、`ry`、`rz`、`phase`、任意の量子ビットリストに対する任意のユニタリ、多重制御の 1 量子ビットゲートを利用できます。これらはテレポーテーションとグローバーの回路で使われていますが、サイドバーにはまだありません。

## アルゴリズムとプロトコル

- **ベル状態。** X ゲートで入力を選び、続いて H と CNOT を適用します。
- **テレポーテーション。** Q0 は cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩ を持ち、Q1–Q2 はベル対を共有します。アリスは CNOT と H を適用して Q0、Q1 を測定し、ボブは m₁ = 1 なら X、m₀ = 1 なら Z を適用します。表示される忠実度はシミュレートした状態から計算したもので、4 つの分岐すべてで 1 です。
- **Grover.** オラクル = 印を付けた要素の 0 のビットに X、多重制御 Z、再び X。拡散 = Hⁿ Xⁿ (MCZ) Xⁿ Hⁿ。シミュレートした成功確率は sin²((2k+1)θ)、sin θ = 1/√N と一致します。
- **Deutsch–Jozsa.** オラクル U_f|x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩ は f の真理値表から構成します。アプリでは定数関数、選択したビットのパリティ、ランダムな均等関数を選べます。

## アーキテクチャ

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

依存関係は一方向です：`main.py` → `quantum_lab` と `translations`。パッケージ内で Plotly をインポートするのは `visualization` だけで、Streamlit をインポートするモジュールはないため、コアは単体で利用およびテストできます。

## テスト

```bash
pip install -r requirements-dev.txt
pytest
pytest --ignore=tests/test_app.py
ruff check .
python benchmarks/bench_gates.py
```

`pytest` は約 1.5 分かかります（大半はブラウザなしの UI テスト）。`--ignore=tests/test_app.py` を付けるとコアだけを数秒でテストします。

| ファイル | 対象 |
|---|---|
| `test_gates.py` | 各ゲートのユニタリ性、代数的恒等式、クロネッカー展開、CNOT 行列 |
| `test_simulator.py` | 規格化、パウリ/アダマールの振る舞い、H を 2 回、CNOT の真理値表、ベル状態と GHZ 状態、密行列との比較、不正な入力 |
| `test_measurement.py` | ボルンの規則、周辺分布、シード付きサンプリング、統計、収縮と再規格化 |
| `test_states.py` | 部分トレース、ブロッホベクトル、純粋度、エンタングルメントエントロピー |
| `test_circuit.py` | 回路の構築と実行、条件付きゲート、回路図のレイアウト |
| `test_noise.py` | チャネルのトレース保存性、解析的な結果、エラー軌道についての全数和 |
| `test_protocols.py` | 4 つのベル状態、4 つの分岐すべてでのテレポーテーション |
| `test_algorithms.py` | グローバーと閉形式の比較、2 入力および 3 入力のすべての均等関数に対するドイッチュ–ジョサ |
| `test_visualization.py` | 図が正しいデータを含むこと |
| `test_translations.py` | 15 言語、キーとプレースホルダーの一致、UI が使うすべてのキーの存在 |
| `test_app.py` | Streamlit アプリのエンドツーエンド（ヘッドレス）、全言語 |

数値の比較には、厳密な浮動小数点の等値ではなく許容誤差を使います（振幅は 10⁻¹²、サンプリング統計は 5σ の範囲）。

検証済みの組み合わせ： Python 3.11 + NumPy 1.26.4 / Streamlit 1.50.0 / Plotly 5.24.0; Python 3.13 + NumPy 2.5.4 / Streamlit 1.67.0 / Plotly 7.1.0.

## 性能と上限

| 項目 | 状態ベクトル | 密度行列 |
|---|---|---|
| メモリ | 16 · 2ⁿ bytes | 16 · 4ⁿ bytes |
| k 量子ビットゲート 1 つ | O(2ⁿ · 2ᵏ) | O(4ⁿ · 2ᵏ) |
| コード上の上限 | `MAX_QUBITS = 20` (16 MiB) | `MAX_DENSITY_QUBITS = 10` (16 MiB) |
| インターフェース上の上限 | 6 qubits | 6 qubits |

バージョン 1.0 はゲートごとに 2ⁿ × 2ⁿ の密行列を作っていましたが、2.0 はゲートを状態テンソルと縮約します。`benchmarks/bench_gates.py` による計測です（アダマール 1 つ、複数回実行の最良値、1 台のマシン。目安としてご覧ください）：

| Qubits | 密行列 (1.0) | 縮約 (2.0) | 比 |
|---|---|---|---|
| 3 | 35 µs | 40 µs | 0.9× |
| 6 | 100 µs | 43 µs | 2× |
| 8 | 553 µs | 44 µs | 13× |
| 10 | 7.6 ms | 49 µs | 155× |
| 12 | 184 ms | 57 µs | ≈ 3200× |

以前の上限である 3 量子ビットでは高速化はありません（入力検証に数マイクロ秒かかります）。利点は、より大きなレジスタが実用的になったことです。シミュレーションのコストは量子ビットが 1 つ増えるごとに 2 倍になる点は変わりません。これは小さなレジスタ向けの教材であり、汎用シミュレーターではありません。

## 既知の制限

- インターフェースで扱えるのは 1〜6 量子ビットで、サイドバーのゲートは I、X、Y、Z、H、S、T と CNOT です。回転ゲートは Python API にしかありません。
- 測定は計算基底（Z）のみです。
- ノイズはゲート後の 1 量子ビットパウリノイズです。振幅減衰、読み出しエラー、待機中のノイズ、相関のあるノイズはありません。
- グローバーは印を付けた要素 1 つを探します。ドイッチュ–ジョサのオラクルは基本ゲートに分解せず、1 つのユニタリのボックスとして適用します。
- 回路は追加のみです（元に戻す、編集、ドラッグ＆ドロップはありません）。
- 回路図は等幅テキストで、非常に長い回路は横にスクロールします。
- アラビア語は翻訳済みですが、ページのレイアウトは右から左へ反転しません。
- 2.0 で追加した 80 個の文字列はネイティブ話者の確認なしで翻訳しています。修正を歓迎します。
- 実際の量子ハードウェアやクラウドのバックエンドには接続しません。

## 1.0 からの変更点（影響がありうるもの）

- **CNOT の結果が変わりました。以前の結果が誤っていたためです。** 1.0 は 2 種類の量子ビット順序を混在させており、1 量子ビットゲートと CNOT を組み合わせた回路が誤った状態を返していました（`docs/AUDIT.md` の指摘 Q1 を参照）。
- `QuantumSimulator` は `main.py` から `quantum_lab` に移りました。1.0 のメソッド（`apply_gate`、`get_probabilities`、`get_amplitudes`、`measure`、`reset`、`_expand_gate`、`_create_cnot_matrix`）は残しています。不正な入力は黙って受け入れられる代わりに `ValueError`/`TypeError` を送出し、`state` は読み取り専用になり、非ユニタリ行列は拒否されます。
- 測定のヒストグラムは操作のたびに再生成されるのではなく、*Run Measurement* を押した後に表示されます。
- グラフは Matplotlib ではなく Plotly です。*Save …* ボタンはインタラクティブな HTML をダウンロードするようになり、PNG の書き出しは各グラフのツールバーにあります。
- `matplotlib` と未使用の `qiskit` を `requirements.txt` から削除し、`plotly` を追加しました。

## Streamlit Community Cloud へのデプロイ

1. リポジトリ（または自分のフォーク）を GitHub にプッシュします。
2. <https://share.streamlit.io> に GitHub でサインインし、新しいアプリを作成します。
3. リポジトリとブランチを選び、main file path を `main.py` に設定します。
4. advanced settings で Python 3.11 以降を選び、デプロイします。

依存パッケージは `requirements.txt` からインストールされ、シークレットや環境変数は不要です。この手順はプラットフォームの利用経験に基づいて書いたもので、このリリースの準備時点では最新のドキュメントと照合できていません。画面が異なる場合は次を参照してください： <https://docs.streamlit.io/deploy/streamlit-community-cloud>.

`.devcontainer` の設定は CORS と XSRF の保護を無効にして Streamlit を起動します。これは GitHub Codespaces のポート転送に必要なものです。公開デプロイではこれらのフラグを使わないでください。

## ロードマップ

- サイドバーへの回転ゲート（Rx、Ry、Rz）と 2 量子ビットゲート（CZ、SWAP）の追加
- 元に戻す機能と回路の編集、回路の保存と読み込み
- 他の基底での測定、パウリ観測量の期待値
- 振幅減衰チャネルと読み出しエラーチャネル
- 回路の OpenQASM への書き出し
- ネイティブ話者による翻訳の確認、右から左へのレイアウト

## ライセンスと帰属

[MIT ライセンス](LICENSE) で公開しています。Copyright (c) 2025 rasidi3112。ライセンスファイルは変更していません。

Mini Quantum Lab は [Rasidi](https://github.com/rasidi3112) が作成し、元のアプリケーション、インターフェース、翻訳を書きました。バージョン 2.0（シミュレーションコア、テスト、可視化、追加機能）はその成果の上に構築されています。
