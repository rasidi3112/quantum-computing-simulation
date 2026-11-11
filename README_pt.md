<h1 align="center">Mini Quantum Lab 2.0</h1>

<p align="center">
  <b>Um simulador de computação quântica interativo e testado para aprender</b><br>
  Python · NumPy · Streamlit · Plotly · 15 idiomas de interface
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
  <b>Português</b> ·
  <a href="README_ru.md">Русский</a> ·
  <a href="README_tr.md">Türkçe</a> ·
  <a href="README_vi.md">Tiếng Việt</a> ·
  <a href="README_zh.md">中文</a>
</p>

---

## Visão geral

O Mini Quantum Lab é uma aplicação web educacional para explorar os fundamentos da computação quântica: construir pequenos circuitos porta a porta, observar o vetor de estado, ver cada qubit numa esfera de Bloch, medir, adicionar ruído e executar alguns protocolos e algoritmos de livro-texto.

A versão 2.0 mantém a aparência e o fluxo de trabalho do projeto original e substitui o que está por baixo: um pacote de simulação separado com testes unitários, uma única convenção documentada de ordenação de qubits, medição fisicamente consistente e novas visualizações. A auditoria que motivou as mudanças está em [`docs/AUDIT.md`](docs/AUDIT.md).

> Este projeto é inspirado no estilo visual de ferramentas como o IBM Quantum Composer e o Qiskit. É um projeto educacional independente e **não é afiliado à IBM nem endossado por ela** ou por qualquer outra organização de computação quântica. Ele simula qubits ideais e com ruído num computador clássico; não se conecta a hardware quântico.

## Recursos

| Área | O que você pode fazer |
|---|---|
| **Laboratório** | 1–6 qubits; portas I, X, Y, Z, H, S, T em qualquer qubit; CNOT entre quaisquer dois qubits; diagrama do circuito ao vivo, tabela de estado e histórico de portas |
| **Visualização do estado** | Distribuição de probabilidade, amplitudes reais/imaginárias e a fase de cada amplitude, com rótulos dos estados de base |
| **Esfera de Bloch** | Esfera 3D interativa por qubit, desenhada a partir do *estado reduzido* do qubit, com comprimento do vetor e pureza para distinguir estados puros e mistos |
| **Medição** | Amostragem por disparos (100–10 000 disparos) com semente, e medição projetiva de um ou de todos os qubits com colapso do estado |
| **Emaranhamento** | Gerador dos quatro estados de Bell com entropia e demonstração do colapso; teletransporte quântico de três qubits de qualquer estado de um qubit |
| **Ruído** | Canais de inversão de bit, inversão de fase e despolarizante aplicados após cada porta, simulados de forma exata com uma matriz densidade |
| **Algoritmos** | Busca de Grover (2–5 qubits) e Deutsch–Jozsa (1–4 qubits de entrada) com explicações e circuitos |
| **Idiomas** | English, Indonesian, Spanish, Mandarin Chinese, Arabic, French, Japanese, Korean, German, Portuguese, Russian, Hindi, Turkish, Italian, Vietnamese |

## Capturas de tela

| Laboratório: circuito, probabilidades, amplitudes | Esferas de Bloch (Q0 e Q1 emaranhados, Q2 puro) |
|---|---|
| <img src="assets/screenshot_lab.png" alt="Lab" width="420"/> | <img src="assets/screenshot_bloch.png" alt="Bloch" width="420"/> |

| Amostragem por disparos e medição projetiva | Teletransporte quântico |
|---|---|
| <img src="assets/screenshot_measurement.png" alt="Measurement" width="420"/> | <img src="assets/screenshot_teleportation.png" alt="Teleportation" width="420"/> |

| Ruído: estado de Bell ideal vs. despolarizado | Grover e Deutsch–Jozsa |
|---|---|
| <img src="assets/screenshot_noise.png" alt="Noise" width="420"/> | <img src="assets/screenshot_algorithms.png" alt="Algorithms" width="420"/> |

## Instalação

Requer Python 3.11 ou mais recente (testado em 3.11 e 3.13).

```bash
git clone https://github.com/rasidi3112/quantum-computing-simulation.git
cd quantum-computing-simulation
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

Depois abra <http://localhost:8501>.

As dependências de execução são `numpy`, `streamlit` e `plotly`. O pacote de simulação em si (`quantum_lab`, sem `visualization`) precisa apenas do NumPy.

## Uso

1. Escolha o **número de qubits** na barra lateral (alterá-lo inicia um circuito novo e vazio).
2. Escolha uma porta e um qubit alvo e pressione **Apply Gate**; com dois ou mais qubits, escolha controle e alvo e pressione **Apply CNOT**.
3. Leia o resultado nas abas:
   - **Lab**: diagrama do circuito, probabilidades, amplitudes, fases, tabela de estado;
   - **Bloch Sphere**: uma esfera por qubit;
   - **Measurement**: *Run Measurement* amostra disparos sem tocar no estado; *Measure Qubit* / *Measure All Qubits* fazem-no colapsar;
   - **Entanglement**, **Noise**, **Algorithms**: demonstrações independentes. *Load into Lab* copia um circuito de Bell para o laboratório.
4. **Reset System** volta a |0…0⟩ e reinicia o gerador aleatório a partir da semente.

Os gráficos são interativos (passar o cursor, zoom, rotação). O botão da câmera na barra de ferramentas de um gráfico salva um PNG; os botões *Save …* baixam um arquivo HTML interativo independente.

### Circuitos de exemplo

| Objetivo | Passos | Resultado esperado |
|---|---|---|
| Superposição | 1 qubit: H → Q0 | P(0) = P(1) = 0.5; vetor de Bloch em +x |
| Estado de Bell \|Φ+⟩ | 2 qubits: H → Q0, CNOT Q0 → Q1 | (\|00⟩ + \|11⟩)/√2; P(00) = P(11) = 0.5, P(01) = P(10) = 0; ambos os vetores de Bloch têm comprimento 0 |
| H·Z·H = X | 1 qubit: H, Z, H → Q0 | \|1⟩ |
| Estado GHZ | 3 qubits: H → Q0, CNOT Q0 → Q1, CNOT Q1 → Q2 | (\|000⟩ + \|111⟩)/√2 |
| Colapso | Estado de Bell e depois *Measure Qubit* Q0 | \|00⟩ / \|11⟩; Q1 fica determinado |

```
q0: ──[H]──●──
           │
q1: ───────⊕──
```

### Usando o simulador a partir do Python

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

## Convenções matemáticas quânticas

**Estado.** Um registrador de *n* qubits é um vetor complexo de 2ⁿ amplitudes αᵢ com Σ|αᵢ|² = 1, inicializado em |0…0⟩.

**Ordenação dos qubits: big-endian, usada em todo lugar.** O qubit 0 é o bit *mais à esquerda* de um rótulo de base e o fio *superior* de um diagrama:

```
|q0 q1 … q(n-1)⟩      index = Σ_k q_k · 2^(n-1-k)      |ψ⟩ = |q0⟩ ⊗ |q1⟩ ⊗ … ⊗ |q(n-1)⟩
```

Assim, com dois qubits, X em Q0 transforma |00⟩ em |10⟩ (índice 2). Uma matriz que atua na lista de qubits `[a, b]` trata `a` como seu bit mais significativo; em particular, `gates.CNOT` é a matriz para `[control, target]`. Esta é a convenção dos livros-texto (Nielsen & Chuang). **O Qiskit usa a ordem oposta, little-endian**; inverta as cadeias de bits ao comparar.

**Evolução.** Cada operador é verificado quanto à unitariedade (U†U = I, tolerância 10⁻¹⁰) antes de ser aplicado, e o estado nunca é renormalizado durante a evolução unitária. Os testes confirmam que a norma permanece a menos de 10⁻¹⁰ de 1 após 3000 portas.

**Medição (base computacional):**

- A *amostragem por disparos* sorteia resultados de P(i) = |αᵢ|². Ela modela preparar novamente o mesmo estado a cada disparo; o estado não muda.
- A *medição projetiva* do qubit *k* sorteia m ∈ {0, 1} com P(m) = Σ_{i: bit k = m} |αᵢ|² e substitui o estado por P_m|ψ⟩ / √P(m). Medir todos os qubits deixa um estado de base.
- *Aleatoriedade.* Uma semente inteira dá resultados reprodutíveis (`numpy.random.default_rng`). Na aplicação, a amostragem por disparos usa a semente diretamente (mesma semente e estado → mesmo histograma), enquanto as medições projetivas consomem um gerador que é reiniciado ao redefinir, ao mudar a semente e ao mudar o tamanho do registrador.

**Vetor de Bloch.** Para o qubit *k*, a matriz densidade reduzida ρ_k = Tr_{others} |ψ⟩⟨ψ| fornece r = (Tr ρ_kX, Tr ρ_kY, Tr ρ_kZ) com ρ_k = (I + r·σ)/2. |r| = 1 para um qubit puro, |r| < 1 quando ele está emaranhado com outros qubits ou afetado por ruído, e a pureza é Tr ρ_k² = (1 + |r|²)/2. Um registrador emaranhado não tem um único vetor de Bloch, portanto nenhum é desenhado.

**Ruído.** Após cada porta, o canal selecionado atua em cada qubit tocado por essa porta (probabilidade de erro *p* por aplicação):

| Canal | Mapa |
|---|---|
| Inversão de bit | ρ → (1 − p)ρ + p XρX |
| Inversão de fase | ρ → (1 − p)ρ + p ZρZ |
| Despolarizante | ρ → (1 − p)ρ + (p/3)(XρX + YρY + ZρZ) |

Com esta parametrização, o canal despolarizante escala o vetor de Bloch por 1 − 4p/3 (p = 3/4 é o estado maximamente misto). Qubits ociosos e medições não têm ruído. A matriz densidade é evoluída de forma exata; medições dentro de um circuito com ruído são calculadas como média sobre seus resultados.

**Fidelidade.** ⟨ψ|ρ|ψ⟩ em relação a uma referência pura, e a fidelidade de Uhlmann (Tr √(√ρ σ √ρ))² em geral.

## Portas quânticas suportadas

| Porta | Matriz | Ação |
|---|---|---|
| Identity (I) | [[1, 0], [0, 1]] | deixa o qubit inalterado |
| Pauli-X | [[0, 1], [1, 0]] | inversão de bit \|0⟩ ↔ \|1⟩ |
| Pauli-Y | [[0, −i], [i, 0]] | Y\|0⟩ = i\|1⟩, Y\|1⟩ = −i\|0⟩ |
| Pauli-Z | [[1, 0], [0, −1]] | inversão de fase \|1⟩ → −\|1⟩ |
| Hadamard (H) | [[1, 1], [1, −1]]/√2 | \|0⟩ → \|+⟩, \|1⟩ → \|−⟩ |
| S | diag(1, i) | fase π/2 |
| T | diag(1, e^{iπ/4}) | fase π/4 |
| CNOT | \|0⟩⟨0\| ⊗ I + \|1⟩⟨1\| ⊗ X | inverte o alvo se o controle for |1⟩ |

A API Python oferece ainda `rx`, `ry`, `rz`, `phase`, unitárias arbitrárias em qualquer lista de qubits e portas de um qubit com vários controles; elas são usadas pelos circuitos de teletransporte e de Grover, mas ainda não estão na barra lateral.

## Algoritmos e protocolos

- **Estados de Bell.** Portas X selecionam a entrada; depois H e CNOT.
- **Teletransporte.** Q0 carrega cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩, e Q1–Q2 compartilham um par de Bell. Alice aplica CNOT e H e mede Q0 e Q1; Bob aplica X se m₁ = 1 e Z se m₀ = 1. A fidelidade exibida é calculada a partir do estado simulado e vale 1 nos quatro ramos.
- **Grover.** Oráculo = X nos bits zero do item marcado, Z multicontrolada e X novamente; difusão = Hⁿ Xⁿ (MCZ) Xⁿ Hⁿ. A probabilidade de sucesso simulada coincide com sin²((2k+1)θ), sin θ = 1/√N.
- **Deutsch–Jozsa.** O oráculo U_f|x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩ é construído a partir da tabela-verdade de f. A aplicação oferece funções constantes, paridades de bits selecionados e funções balanceadas aleatórias.

## Arquitetura

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

As dependências apontam num único sentido: `main.py` → `quantum_lab` e `translations`; dentro do pacote, `visualization` é o único módulo que importa o Plotly e nenhum importa o Streamlit, de modo que o núcleo pode ser usado e testado isoladamente.

## Testes

```bash
pip install -r requirements-dev.txt
pytest
pytest --ignore=tests/test_app.py
ruff check .
python benchmarks/bench_gates.py
```

`pytest` leva cerca de 1,5 minuto (a maior parte são os testes de interface sem navegador); com `--ignore=tests/test_app.py` apenas o núcleo é testado, em poucos segundos.

| Arquivo | Cobre |
|---|---|
| `test_gates.py` | unitariedade de cada porta, identidades algébricas, expansão de Kronecker, matrizes CNOT |
| `test_simulator.py` | normalização, comportamento de Pauli/Hadamard, H duas vezes, tabelas-verdade da CNOT, estados de Bell e GHZ, comparação com matrizes densas, entradas inválidas |
| `test_measurement.py` | regra de Born, marginais, amostragem com semente, estatística, colapso e renormalização |
| `test_states.py` | traço parcial, vetores de Bloch, pureza, entropia de emaranhamento |
| `test_circuit.py` | construção e execução de circuitos, portas condicionadas, layout do diagrama |
| `test_noise.py` | os canais preservam o traço, resultados analíticos, soma exaustiva sobre trajetórias de erro |
| `test_protocols.py` | os quatro estados de Bell, teletransporte nos quatro ramos |
| `test_algorithms.py` | Grover contra a fórmula fechada, Deutsch–Jozsa para toda função balanceada de 2 e 3 entradas |
| `test_visualization.py` | as figuras contêm os dados corretos |
| `test_translations.py` | 15 idiomas, chaves e marcadores idênticos, toda chave usada pela interface existe |
| `test_app.py` | a aplicação Streamlit de ponta a ponta (headless), em todos os idiomas |

As comparações numéricas usam tolerâncias (10⁻¹² para amplitudes, faixas de 5σ para a estatística de amostragem) em vez de igualdade exata de ponto flutuante.

Combinações verificadas: Python 3.11 + NumPy 1.26.4 / Streamlit 1.50.0 / Plotly 5.24.0; Python 3.13 + NumPy 2.5.4 / Streamlit 1.67.0 / Plotly 7.1.0.

## Desempenho e limites

| Grandeza | Vetor de estado | Matriz densidade |
|---|---|---|
| Memória | 16 · 2ⁿ bytes | 16 · 4ⁿ bytes |
| Uma porta de k qubits | O(2ⁿ · 2ᵏ) | O(4ⁿ · 2ᵏ) |
| Limite rígido no código | `MAX_QUBITS = 20` (16 MiB) | `MAX_DENSITY_QUBITS = 10` (16 MiB) |
| Limite na interface | 6 qubits | 6 qubits |

A versão 1.0 construía uma matriz densa 2ⁿ × 2ⁿ para cada porta; a 2.0 contrai a porta com o tensor de estado. Medido com `benchmarks/bench_gates.py` (uma Hadamard, melhor de várias execuções, uma única máquina; considere indicativo):

| Qubits | Matriz densa (1.0) | Contração (2.0) | Razão |
|---|---|---|---|
| 3 | 35 µs | 40 µs | 0.9× |
| 6 | 100 µs | 43 µs | 2× |
| 8 | 553 µs | 44 µs | 13× |
| 10 | 7.6 ms | 49 µs | 155× |
| 12 | 184 ms | 57 µs | ≈ 3200× |

No antigo limite de três qubits não há ganho de velocidade (a validação de entrada custa alguns microssegundos); o benefício é que registradores maiores se tornaram práticos. O custo da simulação ainda dobra a cada qubit. Esta é uma ferramenta didática para registradores pequenos, não um simulador de uso geral.

## Limitações conhecidas

- A interface oferece 1–6 qubits; as portas da barra lateral são I, X, Y, Z, H, S, T e CNOT. Portas de rotação existem apenas na API Python.
- A medição é feita apenas na base computacional (Z).
- O ruído é ruído de Pauli de um qubit após as portas. Não há amortecimento de amplitude, erro de leitura, ruído em repouso nem ruído correlacionado.
- Grover procura um único item marcado; o oráculo de Deutsch–Jozsa é aplicado como uma única caixa unitária em vez de ser decomposto em portas elementares.
- O circuito só aceita acréscimos (sem desfazer, sem edição, sem arrastar e soltar).
- O diagrama do circuito é texto monoespaçado; circuitos muito longos rolam horizontalmente.
- O árabe está traduzido, mas o layout da página não é espelhado da direita para a esquerda.
- As 80 strings adicionadas na 2.0 foram traduzidas sem revisão por falantes nativos; correções são bem-vindas.
- Não há conexão com hardware quântico real nem com back ends em nuvem.

## Mudanças em relação à 1.0 que podem afetar você

- **Os resultados da CNOT diferem porque os antigos estavam errados.** A 1.0 misturava duas ordenações de qubits, de modo que circuitos combinando portas de um qubit com CNOT davam estados incorretos (veja `docs/AUDIT.md`, achado Q1).
- `QuantumSimulator` foi movido de `main.py` para `quantum_lab`. Seus métodos da 1.0 (`apply_gate`, `get_probabilities`, `get_amplitudes`, `measure`, `reset`, `_expand_gate`, `_create_cnot_matrix`) foram mantidos. Entradas inválidas agora lançam `ValueError`/`TypeError` em vez de serem aceitas silenciosamente, `state` é somente leitura e matrizes não unitárias são rejeitadas.
- O histograma de medição aparece depois de pressionar *Run Measurement*, em vez de ser regenerado a cada interação.
- Os gráficos são do Plotly em vez do Matplotlib. Os botões *Save …* agora baixam HTML interativo; a exportação em PNG está na barra de ferramentas de cada gráfico.
- `matplotlib` e o `qiskit` não utilizado foram removidos de `requirements.txt`; `plotly` foi adicionado.

## Implantação no Streamlit Community Cloud

1. Envie o repositório (ou o seu fork) para o GitHub.
2. Entre em <https://share.streamlit.io> com o GitHub e crie uma nova app.
3. Selecione o repositório e o branch, e defina main file path como `main.py`.
4. Em advanced settings escolha Python 3.11 ou mais recente e faça o deploy.

As dependências são instaladas a partir de `requirements.txt`; não são necessários segredos nem variáveis de ambiente. Estes passos foram escritos com base na experiência com a plataforma e não puderam ser conferidos com a documentação atual ao preparar esta versão. Se as telas forem diferentes, siga <https://docs.streamlit.io/deploy/streamlit-community-cloud>.

A configuração `.devcontainer` inicia o Streamlit com a proteção CORS e XSRF desativada, o que o encaminhamento de portas do GitHub Codespaces exige. Não reutilize essas opções numa implantação pública.

## Roteiro

- Portas de rotação (Rx, Ry, Rz) e mais portas de dois qubits (CZ, SWAP) na barra lateral
- Desfazer e edição do circuito; salvar e carregar circuitos
- Medição em outras bases; valores esperados de observáveis de Pauli
- Canais de amortecimento de amplitude e de erro de leitura
- Exportação de circuitos para OpenQASM
- Revisão das traduções por falantes nativos; layout da direita para a esquerda

## Licença e atribuição

Distribuído sob a [Licença MIT](LICENSE), Copyright (c) 2025 rasidi3112. O arquivo de licença não foi alterado.

O Mini Quantum Lab foi criado por [Rasidi](https://github.com/rasidi3112), autor da aplicação, da interface e das traduções originais. A versão 2.0 (núcleo de simulação, testes, visualizações e recursos adicionados) baseia-se nesse trabalho.
