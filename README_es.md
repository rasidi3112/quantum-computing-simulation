<h1 align="center">Mini Quantum Lab 2.0</h1>

<p align="center">
  <b>Un simulador de computación cuántica interactivo y probado para aprender</b><br>
  Python · NumPy · Streamlit · Plotly · 15 idiomas de interfaz
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="README_ar.md">العربية</a> ·
  <a href="README_de.md">Deutsch</a> ·
  <b>Español</b> ·
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
  <a href="README_zh.md">中文</a>
</p>

---

## Descripción general

Mini Quantum Lab es una aplicación web educativa para explorar los fundamentos de la computación cuántica: construir pequeños circuitos puerta a puerta, observar el vector de estado, ver cada qubit en una esfera de Bloch, medir, añadir ruido y ejecutar algunos protocolos y algoritmos de libro de texto.

La versión 2.0 conserva el aspecto y el flujo de trabajo del proyecto original y sustituye lo que hay debajo: un paquete de simulación independiente con pruebas unitarias, una única convención documentada de ordenación de qubits, una medición físicamente coherente y nuevas visualizaciones. La auditoría que motivó los cambios está en [`docs/AUDIT.md`](docs/AUDIT.md).

> Este proyecto se inspira en el estilo visual de herramientas como IBM Quantum Composer y Qiskit. Es un proyecto educativo independiente y **no está afiliado a IBM ni cuenta con su respaldo**, ni con el de ninguna otra organización de computación cuántica. Simula qubits ideales y con ruido en un ordenador clásico; no se conecta a hardware cuántico.

## Características

| Área | Qué se puede hacer |
|---|---|
| **Laboratorio** | 1–6 qubits; puertas I, X, Y, Z, H, S, T sobre cualquier qubit; CNOT entre dos qubits cualesquiera; diagrama del circuito en vivo, tabla de estado e historial de puertas |
| **Visualización del estado** | Distribución de probabilidad, amplitudes reales/imaginarias y la fase de cada amplitud, con etiquetas de los estados base |
| **Esfera de Bloch** | Esfera 3D interactiva por qubit, dibujada a partir del *estado reducido* del qubit, con la longitud del vector y la pureza para distinguir estados puros y mixtos |
| **Medición** | Muestreo por disparos (100–10 000 disparos) con semilla, y medición proyectiva de uno o de todos los qubits con colapso del estado |
| **Entrelazamiento** | Generador de los cuatro estados de Bell con entropía y demostración del colapso; teleportación cuántica de tres qubits de cualquier estado de un qubit |
| **Ruido** | Canales de inversión de bit, inversión de fase y despolarizante aplicados tras cada puerta, simulados de forma exacta con una matriz de densidad |
| **Algoritmos** | Búsqueda de Grover (2–5 qubits) y Deutsch–Jozsa (1–4 qubits de entrada) con explicaciones y circuitos |
| **Idiomas** | English, Indonesian, Spanish, Mandarin Chinese, Arabic, French, Japanese, Korean, German, Portuguese, Russian, Hindi, Turkish, Italian, Vietnamese |

## Capturas de pantalla

| Laboratorio: circuito, probabilidades, amplitudes | Esferas de Bloch (Q0 y Q1 entrelazados, Q2 puro) |
|---|---|
| <img src="assets/screenshot_lab.png" alt="Lab" width="420"/> | <img src="assets/screenshot_bloch.png" alt="Bloch" width="420"/> |

| Muestreo por disparos y medición proyectiva | Teleportación cuántica |
|---|---|
| <img src="assets/screenshot_measurement.png" alt="Measurement" width="420"/> | <img src="assets/screenshot_teleportation.png" alt="Teleportation" width="420"/> |

| Ruido: estado de Bell ideal frente a despolarizado | Grover y Deutsch–Jozsa |
|---|---|
| <img src="assets/screenshot_noise.png" alt="Noise" width="420"/> | <img src="assets/screenshot_algorithms.png" alt="Algorithms" width="420"/> |

## Instalación

Requiere Python 3.11 o posterior (probado en 3.11 y 3.13).

```bash
git clone https://github.com/rasidi3112/quantum-computing-simulation.git
cd quantum-computing-simulation
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

Después abra <http://localhost:8501>.

Las dependencias de ejecución son `numpy`, `streamlit` y `plotly`. El paquete de simulación en sí (`quantum_lab`, sin `visualization`) solo necesita NumPy.

## Uso

1. Elija el **número de qubits** en la barra lateral (cambiarlo inicia un circuito nuevo y vacío).
2. Elija una puerta y un qubit objetivo y pulse **Apply Gate**; con dos o más qubits, elija control y objetivo y pulse **Apply CNOT**.
3. Lea el resultado en las pestañas:
   - **Lab**: diagrama del circuito, probabilidades, amplitudes, fases, tabla de estado;
   - **Bloch Sphere**: una esfera por qubit;
   - **Measurement**: *Run Measurement* muestrea disparos sin tocar el estado; *Measure Qubit* / *Measure All Qubits* lo colapsan;
   - **Entanglement**, **Noise**, **Algorithms**: demostraciones independientes. *Load into Lab* copia un circuito de Bell al laboratorio.
4. **Reset System** vuelve a |0…0⟩ y reinicia el generador aleatorio a partir de la semilla.

Los gráficos son interactivos (pasar el cursor, zoom, rotar). El botón de la cámara en la barra de cada gráfico guarda un PNG; los botones *Save …* descargan un archivo HTML interactivo independiente.

### Circuitos de ejemplo

| Objetivo | Pasos | Resultado esperado |
|---|---|---|
| Superposición | 1 qubit: H → Q0 | P(0) = P(1) = 0.5; vector de Bloch en +x |
| Estado de Bell \|Φ+⟩ | 2 qubits: H → Q0, CNOT Q0 → Q1 | (\|00⟩ + \|11⟩)/√2; P(00) = P(11) = 0.5, P(01) = P(10) = 0; ambos vectores de Bloch tienen longitud 0 |
| H·Z·H = X | 1 qubit: H, Z, H → Q0 | \|1⟩ |
| Estado GHZ | 3 qubits: H → Q0, CNOT Q0 → Q1, CNOT Q1 → Q2 | (\|000⟩ + \|111⟩)/√2 |
| Colapso | Estado de Bell y después *Measure Qubit* Q0 | \|00⟩ / \|11⟩; Q1 queda determinado |

```
q0: ──[H]──●──
           │
q1: ───────⊕──
```

### Uso del simulador desde Python

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

## Convenciones matemáticas cuánticas

**Estado.** Un registro de *n* qubits es un vector complejo de 2ⁿ amplitudes αᵢ con Σ|αᵢ|² = 1, inicializado en |0…0⟩.

**Ordenación de qubits: big-endian, en todas partes.** El qubit 0 es el bit *más a la izquierda* de una etiqueta base y el cable *superior* de un diagrama:

```
|q0 q1 … q(n-1)⟩      index = Σ_k q_k · 2^(n-1-k)      |ψ⟩ = |q0⟩ ⊗ |q1⟩ ⊗ … ⊗ |q(n-1)⟩
```

Así, con dos qubits, X sobre Q0 convierte |00⟩ en |10⟩ (índice 2). Una matriz que actúa sobre la lista de qubits `[a, b]` trata `a` como su bit más significativo; en particular, `gates.CNOT` es la matriz para `[control, target]`. Es la convención de los libros de texto (Nielsen & Chuang). **Qiskit usa el orden opuesto, little-endian**; invierta las cadenas de bits al comparar.

**Evolución.** Se comprueba la unitariedad de cada operador (U†U = I, tolerancia 10⁻¹⁰) antes de aplicarlo, y el estado nunca se renormaliza durante la evolución unitaria. Las pruebas confirman que la norma se mantiene a menos de 10⁻¹⁰ de 1 tras 3000 puertas.

**Medición (base computacional):**

- El *muestreo por disparos* extrae resultados de P(i) = |αᵢ|². Modela preparar de nuevo el mismo estado en cada disparo; el estado no cambia.
- La *medición proyectiva* del qubit *k* extrae m ∈ {0, 1} con P(m) = Σ_{i: bit k = m} |αᵢ|² y sustituye el estado por P_m|ψ⟩ / √P(m). Medir todos los qubits deja un estado base.
- *Aleatoriedad.* Una semilla entera da resultados reproducibles (`numpy.random.default_rng`). En la aplicación, el muestreo por disparos usa la semilla directamente (misma semilla y estado → mismo histograma), mientras que las mediciones proyectivas consumen un generador que se reinicia al restablecer, al cambiar la semilla y al cambiar el tamaño del registro.

**Vector de Bloch.** Para el qubit *k*, la matriz de densidad reducida ρ_k = Tr_{others} |ψ⟩⟨ψ| da r = (Tr ρ_kX, Tr ρ_kY, Tr ρ_kZ) con ρ_k = (I + r·σ)/2. |r| = 1 para un qubit puro, |r| < 1 cuando está entrelazado con otros qubits o afectado por ruido, y la pureza es Tr ρ_k² = (1 + |r|²)/2. Un registro entrelazado no tiene un único vector de Bloch, por lo que no se dibuja ninguno.

**Ruido.** Después de cada puerta, el canal seleccionado actúa sobre cada qubit que tocó esa puerta (probabilidad de error *p* por aplicación):

| Canal | Mapa |
|---|---|
| Inversión de bit | ρ → (1 − p)ρ + p XρX |
| Inversión de fase | ρ → (1 − p)ρ + p ZρZ |
| Despolarizante | ρ → (1 − p)ρ + (p/3)(XρX + YρY + ZρZ) |

Con esta parametrización, el canal despolarizante escala el vector de Bloch por 1 − 4p/3 (p = 3/4 es el estado máximamente mixto). Los qubits inactivos y las mediciones no tienen ruido. La matriz de densidad se evoluciona de forma exacta; las mediciones dentro de un circuito con ruido se promedian sobre sus resultados.

**Fidelidad.** ⟨ψ|ρ|ψ⟩ frente a una referencia pura, y la fidelidad de Uhlmann (Tr √(√ρ σ √ρ))² en general.

## Puertas cuánticas admitidas

| Puerta | Matriz | Acción |
|---|---|---|
| Identity (I) | [[1, 0], [0, 1]] | deja el qubit sin cambios |
| Pauli-X | [[0, 1], [1, 0]] | inversión de bit \|0⟩ ↔ \|1⟩ |
| Pauli-Y | [[0, −i], [i, 0]] | Y\|0⟩ = i\|1⟩, Y\|1⟩ = −i\|0⟩ |
| Pauli-Z | [[1, 0], [0, −1]] | inversión de fase \|1⟩ → −\|1⟩ |
| Hadamard (H) | [[1, 1], [1, −1]]/√2 | \|0⟩ → \|+⟩, \|1⟩ → \|−⟩ |
| S | diag(1, i) | fase π/2 |
| T | diag(1, e^{iπ/4}) | fase π/4 |
| CNOT | \|0⟩⟨0\| ⊗ I + \|1⟩⟨1\| ⊗ X | invierte el objetivo si el control es |1⟩ |

La API de Python ofrece además `rx`, `ry`, `rz`, `phase`, unitarias arbitrarias sobre cualquier lista de qubits y puertas de un qubit con varios controles; las usan los circuitos de teleportación y de Grover, pero aún no están en la barra lateral.

## Algoritmos y protocolos

- **Estados de Bell.** Las puertas X seleccionan la entrada; después H y CNOT.
- **Teleportación.** Q0 lleva cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩, y Q1–Q2 comparten un par de Bell. Alice aplica CNOT y H y mide Q0 y Q1; Bob aplica X si m₁ = 1 y Z si m₀ = 1. La fidelidad mostrada se calcula a partir del estado simulado y vale 1 en las cuatro ramas.
- **Grover.** Oráculo = X sobre los bits cero del elemento marcado, Z multicontrolada y X de nuevo; difusión = Hⁿ Xⁿ (MCZ) Xⁿ Hⁿ. La probabilidad de éxito simulada coincide con sin²((2k+1)θ), sin θ = 1/√N.
- **Deutsch–Jozsa.** El oráculo U_f|x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩ se construye a partir de la tabla de verdad de f. La aplicación ofrece funciones constantes, paridades de bits seleccionados y funciones balanceadas aleatorias.

## Arquitectura

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

Las dependencias van en un solo sentido: `main.py` → `quantum_lab` y `translations`; dentro del paquete, `visualization` es el único módulo que importa Plotly y ninguno importa Streamlit, de modo que el núcleo puede usarse y probarse por separado.

## Pruebas

```bash
pip install -r requirements-dev.txt
pytest
pytest --ignore=tests/test_app.py
ruff check .
python benchmarks/bench_gates.py
```

`pytest` tarda alrededor de 1,5 minutos (la mayor parte son las pruebas de interfaz sin navegador); con `--ignore=tests/test_app.py` solo se prueba el núcleo, en unos segundos.

| Archivo | Cubre |
|---|---|
| `test_gates.py` | unitariedad de cada puerta, identidades algebraicas, expansión de Kronecker, matrices CNOT |
| `test_simulator.py` | normalización, comportamiento de Pauli/Hadamard, H dos veces, tablas de verdad de CNOT, estados de Bell y GHZ, comparación con matrices densas, entradas no válidas |
| `test_measurement.py` | regla de Born, marginales, muestreo con semilla, estadística, colapso y renormalización |
| `test_states.py` | traza parcial, vectores de Bloch, pureza, entropía de entrelazamiento |
| `test_circuit.py` | construcción y ejecución de circuitos, puertas condicionadas, disposición del diagrama |
| `test_noise.py` | los canales conservan la traza, resultados analíticos, suma exhaustiva sobre trayectorias de error |
| `test_protocols.py` | los cuatro estados de Bell, teleportación en las cuatro ramas |
| `test_algorithms.py` | Grover frente a la fórmula cerrada, Deutsch–Jozsa para toda función balanceada de 2 y 3 entradas |
| `test_visualization.py` | las figuras contienen los datos correctos |
| `test_translations.py` | 15 idiomas, claves y marcadores idénticos, existe cada clave usada por la interfaz |
| `test_app.py` | la aplicación Streamlit de extremo a extremo (sin navegador), en todos los idiomas |

Las comparaciones numéricas usan tolerancias (10⁻¹² para amplitudes, bandas de 5σ para la estadística de muestreo) en lugar de igualdad exacta en coma flotante.

Combinaciones verificadas: Python 3.11 + NumPy 1.26.4 / Streamlit 1.50.0 / Plotly 5.24.0; Python 3.13 + NumPy 2.5.4 / Streamlit 1.67.0 / Plotly 7.1.0.

## Rendimiento y límites

| Magnitud | Vector de estado | Matriz de densidad |
|---|---|---|
| Memoria | 16 · 2ⁿ bytes | 16 · 4ⁿ bytes |
| Una puerta de k qubits | O(2ⁿ · 2ᵏ) | O(4ⁿ · 2ᵏ) |
| Límite estricto en el código | `MAX_QUBITS = 20` (16 MiB) | `MAX_DENSITY_QUBITS = 10` (16 MiB) |
| Límite en la interfaz | 6 qubits | 6 qubits |

La versión 1.0 construía una matriz densa 2ⁿ × 2ⁿ para cada puerta; la 2.0 contrae la puerta con el tensor de estado. Medido con `benchmarks/bench_gates.py` (una Hadamard, la mejor de varias ejecuciones, una sola máquina; tómese como orientativo):

| Qubits | Matriz densa (1.0) | Contracción (2.0) | Relación |
|---|---|---|---|
| 3 | 35 µs | 40 µs | 0.9× |
| 6 | 100 µs | 43 µs | 2× |
| 8 | 553 µs | 44 µs | 13× |
| 10 | 7.6 ms | 49 µs | 155× |
| 12 | 184 ms | 57 µs | ≈ 3200× |

En el antiguo límite de tres qubits no hay aceleración (la validación de entradas cuesta unos microsegundos); la ventaja es que los registros mayores se han vuelto prácticos. El coste de la simulación sigue duplicándose con cada qubit. Es una herramienta didáctica para registros pequeños, no un simulador de propósito general.

## Limitaciones conocidas

- La interfaz ofrece 1–6 qubits; las puertas de la barra lateral son I, X, Y, Z, H, S, T y CNOT. Las puertas de rotación solo existen en la API de Python.
- La medición es solo en la base computacional (Z).
- El ruido es ruido de Pauli de un qubit tras las puertas. No hay amortiguamiento de amplitud, error de lectura, ruido en reposo ni ruido correlacionado.
- Grover busca un único elemento marcado; el oráculo de Deutsch–Jozsa se aplica como una sola caja unitaria en lugar de descomponerse en puertas elementales.
- El circuito solo admite añadir (sin deshacer, sin edición, sin arrastrar y soltar).
- El diagrama del circuito es texto monoespaciado; los circuitos muy largos se desplazan horizontalmente.
- El árabe está traducido, pero el diseño de la página no se refleja de derecha a izquierda.
- Las 80 cadenas añadidas en la 2.0 se tradujeron sin revisión de hablantes nativos; se agradecen correcciones.
- No hay conexión con hardware cuántico real ni con servicios en la nube.

## Cambios respecto a la 1.0 que pueden afectarle

- **Los resultados de CNOT difieren porque los antiguos eran incorrectos.** La 1.0 mezclaba dos ordenaciones de qubits, por lo que los circuitos que combinaban puertas de un qubit con CNOT daban estados erróneos (véase `docs/AUDIT.md`, hallazgo Q1).
- `QuantumSimulator` pasó de `main.py` a `quantum_lab`. Se conservan sus métodos de la 1.0 (`apply_gate`, `get_probabilities`, `get_amplitudes`, `measure`, `reset`, `_expand_gate`, `_create_cnot_matrix`). Las entradas no válidas ahora lanzan `ValueError`/`TypeError` en lugar de aceptarse en silencio, `state` es de solo lectura y se rechazan las matrices no unitarias.
- El histograma de medición aparece tras pulsar *Run Measurement* en lugar de regenerarse en cada interacción.
- Los gráficos son de Plotly en lugar de Matplotlib. Los botones *Save …* descargan ahora HTML interactivo; la exportación a PNG está en la barra de cada gráfico.
- Se eliminaron `matplotlib` y `qiskit` (sin uso) de `requirements.txt`; se añadió `plotly`.

## Despliegue en Streamlit Community Cloud

1. Suba el repositorio (o su fork) a GitHub.
2. Inicie sesión en <https://share.streamlit.io> con GitHub y cree una nueva app.
3. Seleccione el repositorio y la rama, y establezca main file path en `main.py`.
4. En advanced settings elija Python 3.11 o posterior y despliegue.

Las dependencias se instalan desde `requirements.txt`; no se necesitan secretos ni variables de entorno. Estos pasos se escribieron a partir de la experiencia con la plataforma y no pudieron contrastarse con su documentación actual al preparar esta versión. Si las pantallas difieren, siga <https://docs.streamlit.io/deploy/streamlit-community-cloud>.

La configuración de `.devcontainer` inicia Streamlit con la protección CORS y XSRF desactivada, algo que requiere el reenvío de puertos de GitHub Codespaces. No reutilice esas opciones en un despliegue público.

## Hoja de ruta

- Puertas de rotación (Rx, Ry, Rz) y más puertas de dos qubits (CZ, SWAP) en la barra lateral
- Deshacer y edición del circuito; guardar y cargar circuitos
- Medición en otras bases; valores esperados de observables de Pauli
- Canales de amortiguamiento de amplitud y de error de lectura
- Exportación de circuitos a OpenQASM
- Revisión de las traducciones por hablantes nativos; diseño de derecha a izquierda

## Licencia y atribución

Publicado bajo la [Licencia MIT](LICENSE), Copyright (c) 2025 rasidi3112. El archivo de licencia no se ha modificado.

Mini Quantum Lab fue creado por [Rasidi](https://github.com/rasidi3112), autor de la aplicación, la interfaz y las traducciones originales. La versión 2.0 (núcleo de simulación, pruebas, visualizaciones y funciones añadidas) se basa en ese trabajo.
