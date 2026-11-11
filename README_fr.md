<h1 align="center">Mini Quantum Lab 2.0</h1>

<p align="center">
  <b>Un simulateur d'informatique quantique interactif et testé pour apprendre</b><br>
  Python · NumPy · Streamlit · Plotly · 15 langues d'interface
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="README_ar.md">العربية</a> ·
  <a href="README_de.md">Deutsch</a> ·
  <a href="README_es.md">Español</a> ·
  <b>Français</b> ·
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

## Présentation

Mini Quantum Lab est une application web éducative pour explorer les bases de l'informatique quantique : construire de petits circuits porte après porte, observer le vecteur d'état, regarder chaque qubit sur une sphère de Bloch, mesurer, ajouter du bruit et exécuter quelques protocoles et algorithmes classiques.

La version 2.0 conserve l'apparence et le fonctionnement du projet d'origine et remplace ce qui se trouve dessous : un paquet de simulation séparé et testé unitairement, une convention unique et documentée pour l'ordre des qubits, une mesure physiquement cohérente et de nouvelles visualisations. L'audit à l'origine de ces changements se trouve dans [`docs/AUDIT.md`](docs/AUDIT.md).

> Ce projet s'inspire du style visuel d'outils tels qu'IBM Quantum Composer et Qiskit. C'est un projet éducatif indépendant qui **n'est ni affilié à IBM ni approuvé par IBM** ou par toute autre organisation d'informatique quantique. Il simule des qubits idéaux et bruités sur un ordinateur classique ; il ne se connecte à aucun matériel quantique.

## Fonctionnalités

| Domaine | Ce que vous pouvez faire |
|---|---|
| **Laboratoire** | 1–6 qubits ; portes I, X, Y, Z, H, S, T sur n'importe quel qubit ; CNOT entre deux qubits quelconques ; diagramme du circuit en direct, table d'état et historique des portes |
| **Visualisation de l'état** | Distribution de probabilité, amplitudes réelles/imaginaires et phase de chaque amplitude, avec les étiquettes des états de base |
| **Sphère de Bloch** | Sphère 3D interactive par qubit, tracée à partir de l'*état réduit* du qubit, avec la longueur du vecteur et la pureté pour distinguer états purs et mixtes |
| **Mesure** | Échantillonnage par tirs (100–10 000 tirs) avec graine, et mesure projective d'un ou de tous les qubits avec effondrement de l'état |
| **Intrication** | Générateur des quatre états de Bell avec entropie et démonstration de l'effondrement ; téléportation quantique à trois qubits de n'importe quel état à un qubit |
| **Bruit** | Canaux d'inversion de bit, d'inversion de phase et dépolarisant appliqués après chaque porte, simulés exactement avec une matrice densité |
| **Algorithmes** | Recherche de Grover (2–5 qubits) et Deutsch–Jozsa (1–4 qubits d'entrée) avec explications et circuits |
| **Langues** | English, Indonesian, Spanish, Mandarin Chinese, Arabic, French, Japanese, Korean, German, Portuguese, Russian, Hindi, Turkish, Italian, Vietnamese |

## Captures d'écran

| Laboratoire : circuit, probabilités, amplitudes | Sphères de Bloch (Q0 et Q1 intriqués, Q2 pur) |
|---|---|
| <img src="assets/screenshot_lab.png" alt="Lab" width="420"/> | <img src="assets/screenshot_bloch.png" alt="Bloch" width="420"/> |

| Échantillonnage par tirs et mesure projective | Téléportation quantique |
|---|---|
| <img src="assets/screenshot_measurement.png" alt="Measurement" width="420"/> | <img src="assets/screenshot_teleportation.png" alt="Teleportation" width="420"/> |

| Bruit : état de Bell idéal et dépolarisé | Grover et Deutsch–Jozsa |
|---|---|
| <img src="assets/screenshot_noise.png" alt="Noise" width="420"/> | <img src="assets/screenshot_algorithms.png" alt="Algorithms" width="420"/> |

## Installation

Nécessite Python 3.11 ou plus récent (testé avec 3.11 et 3.13).

```bash
git clone https://github.com/rasidi3112/quantum-computing-simulation.git
cd quantum-computing-simulation
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

Ouvrez ensuite <http://localhost:8501>.

Les dépendances d'exécution sont `numpy`, `streamlit` et `plotly`. Le paquet de simulation lui-même (`quantum_lab`, sans `visualization`) n'a besoin que de NumPy.

## Utilisation

1. Choisissez le **nombre de qubits** dans la barre latérale (le modifier démarre un nouveau circuit vide).
2. Choisissez une porte et un qubit cible puis appuyez sur **Apply Gate** ; avec deux qubits ou plus, choisissez contrôle et cible puis appuyez sur **Apply CNOT**.
3. Lisez le résultat dans les onglets :
   - **Lab**: diagramme du circuit, probabilités, amplitudes, phases, table d'état ;
   - **Bloch Sphere**: une sphère par qubit ;
   - **Measurement**: *Run Measurement* échantillonne des tirs sans toucher à l'état ; *Measure Qubit* / *Measure All Qubits* le font s'effondrer ;
   - **Entanglement**, **Noise**, **Algorithms**: démonstrations autonomes. *Load into Lab* copie un circuit de Bell dans le laboratoire.
4. **Reset System** revient à |0…0⟩ et redémarre le générateur aléatoire à partir de la graine.

Les graphiques sont interactifs (survol, zoom, rotation). Le bouton appareil photo de la barre d'outils d'un graphique enregistre un PNG ; les boutons *Save …* téléchargent un fichier HTML interactif autonome.

### Exemples de circuits

| Objectif | Étapes | Résultat attendu |
|---|---|---|
| Superposition | 1 qubit: H → Q0 | P(0) = P(1) = 0.5; vecteur de Bloch sur +x |
| État de Bell \|Φ+⟩ | 2 qubits: H → Q0, CNOT Q0 → Q1 | (\|00⟩ + \|11⟩)/√2; P(00) = P(11) = 0.5, P(01) = P(10) = 0; les deux vecteurs de Bloch ont une longueur 0 |
| H·Z·H = X | 1 qubit: H, Z, H → Q0 | \|1⟩ |
| État GHZ | 3 qubits: H → Q0, CNOT Q0 → Q1, CNOT Q1 → Q2 | (\|000⟩ + \|111⟩)/√2 |
| Effondrement | État de Bell, puis *Measure Qubit* Q0 | \|00⟩ / \|11⟩; Q1 est désormais déterminé |

```
q0: ──[H]──●──
           │
q1: ───────⊕──
```

### Utiliser le simulateur depuis Python

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

## Conventions mathématiques quantiques

**État.** Un registre de *n* qubits est un vecteur complexe de 2ⁿ amplitudes αᵢ avec Σ|αᵢ|² = 1, initialisé à |0…0⟩.

**Ordre des qubits : big-endian, partout.** Le qubit 0 est le bit *le plus à gauche* d'une étiquette de base et le fil *du haut* d'un diagramme :

```
|q0 q1 … q(n-1)⟩      index = Σ_k q_k · 2^(n-1-k)      |ψ⟩ = |q0⟩ ⊗ |q1⟩ ⊗ … ⊗ |q(n-1)⟩
```

Ainsi, avec deux qubits, X sur Q0 transforme |00⟩ en |10⟩ (indice 2). Une matrice agissant sur la liste de qubits `[a, b]` traite `a` comme son bit de poids fort ; en particulier, `gates.CNOT` est la matrice pour `[control, target]`. C'est la convention des manuels (Nielsen & Chuang). **Qiskit utilise l'ordre inverse, little-endian** ; inversez les chaînes de bits pour comparer.

**Évolution.** L'unitarité de chaque opérateur est vérifiée (U†U = I, tolérance 10⁻¹⁰) avant son application, et l'état n'est jamais renormalisé pendant l'évolution unitaire. Les tests confirment que la norme reste à moins de 10⁻¹⁰ de 1 après 3000 portes.

**Mesure (base de calcul) :**

- L'*échantillonnage par tirs* tire des résultats selon P(i) = |αᵢ|². Il modélise la préparation du même état à chaque tir ; l'état est inchangé.
- La *mesure projective* du qubit *k* tire m ∈ {0, 1} avec P(m) = Σ_{i: bit k = m} |αᵢ|², puis remplace l'état par P_m|ψ⟩ / √P(m). Mesurer tous les qubits laisse un état de base.
- *Aléa.* Une graine entière donne des résultats reproductibles (`numpy.random.default_rng`). Dans l'application, l'échantillonnage par tirs utilise directement la graine (même graine et même état → même histogramme), tandis que les mesures projectives consomment un générateur redémarré à la réinitialisation, au changement de graine et au changement de taille du registre.

**Vecteur de Bloch.** Pour le qubit *k*, la matrice densité réduite ρ_k = Tr_{others} |ψ⟩⟨ψ| donne r = (Tr ρ_kX, Tr ρ_kY, Tr ρ_kZ) avec ρ_k = (I + r·σ)/2. |r| = 1 pour un qubit pur, |r| < 1 lorsqu'il est intriqué avec d'autres qubits ou affecté par le bruit, et la pureté vaut Tr ρ_k² = (1 + |r|²)/2. Un registre intriqué n'a pas de vecteur de Bloch unique, donc aucun n'est tracé.

**Bruit.** Après chaque porte, le canal choisi agit sur chaque qubit touché par cette porte (probabilité d'erreur *p* par application) :

| Canal | Application |
|---|---|
| Inversion de bit | ρ → (1 − p)ρ + p XρX |
| Inversion de phase | ρ → (1 − p)ρ + p ZρZ |
| Dépolarisant | ρ → (1 − p)ρ + (p/3)(XρX + YρY + ZρZ) |

Avec cette paramétrisation, le canal dépolarisant multiplie le vecteur de Bloch par 1 − 4p/3 (p = 3/4 correspond à l'état maximalement mixte). Les qubits inactifs et les mesures sont sans bruit. La matrice densité est évoluée exactement ; les mesures à l'intérieur d'un circuit bruité sont moyennées sur leurs résultats.

**Fidélité.** ⟨ψ|ρ|ψ⟩ par rapport à une référence pure, et la fidélité d'Uhlmann (Tr √(√ρ σ √ρ))² en général.

## Portes quantiques prises en charge

| Porte | Matrice | Action |
|---|---|---|
| Identity (I) | [[1, 0], [0, 1]] | laisse le qubit inchangé |
| Pauli-X | [[0, 1], [1, 0]] | inversion de bit \|0⟩ ↔ \|1⟩ |
| Pauli-Y | [[0, −i], [i, 0]] | Y\|0⟩ = i\|1⟩, Y\|1⟩ = −i\|0⟩ |
| Pauli-Z | [[1, 0], [0, −1]] | inversion de phase \|1⟩ → −\|1⟩ |
| Hadamard (H) | [[1, 1], [1, −1]]/√2 | \|0⟩ → \|+⟩, \|1⟩ → \|−⟩ |
| S | diag(1, i) | phase π/2 |
| T | diag(1, e^{iπ/4}) | phase π/4 |
| CNOT | \|0⟩⟨0\| ⊗ I + \|1⟩⟨1\| ⊗ X | inverse la cible si le contrôle vaut |1⟩ |

L'API Python propose en outre `rx`, `ry`, `rz`, `phase`, des unitaires arbitraires sur n'importe quelle liste de qubits et des portes à un qubit à plusieurs contrôles ; elles sont utilisées par les circuits de téléportation et de Grover mais ne figurent pas encore dans la barre latérale.

## Algorithmes et protocoles

- **États de Bell.** Des portes X sélectionnent l'entrée, puis H et CNOT.
- **Téléportation.** Q0 porte cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩, Q1–Q2 partagent une paire de Bell. Alice applique CNOT et H puis mesure Q0 et Q1 ; Bob applique X si m₁ = 1 et Z si m₀ = 1. La fidélité affichée est calculée à partir de l'état simulé et vaut 1 dans les quatre branches.
- **Grover.** Oracle = X sur les bits à zéro de l'élément marqué, Z multi-contrôlée, puis X de nouveau ; diffusion = Hⁿ Xⁿ (MCZ) Xⁿ Hⁿ. La probabilité de succès simulée coïncide avec sin²((2k+1)θ), sin θ = 1/√N.
- **Deutsch–Jozsa.** L'oracle U_f|x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩ est construit à partir de la table de vérité de f. L'application propose des fonctions constantes, des parités de bits choisis et des fonctions équilibrées aléatoires.

## Architecture

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

Les dépendances vont dans un seul sens : `main.py` → `quantum_lab` et `translations` ; dans le paquet, `visualization` est le seul module qui importe Plotly et aucun n'importe Streamlit, de sorte que le cœur peut être utilisé et testé seul.

## Tests

```bash
pip install -r requirements-dev.txt
pytest
pytest --ignore=tests/test_app.py
ruff check .
python benchmarks/bench_gates.py
```

`pytest` prend environ 1,5 minute (surtout les tests d'interface sans navigateur) ; avec `--ignore=tests/test_app.py`, seul le cœur est testé, en quelques secondes.

| Fichier | Couvre |
|---|---|
| `test_gates.py` | unitarité de chaque porte, identités algébriques, développement de Kronecker, matrices CNOT |
| `test_simulator.py` | normalisation, comportement de Pauli/Hadamard, H deux fois, tables de vérité du CNOT, états de Bell et GHZ, comparaison avec des matrices denses, entrées invalides |
| `test_measurement.py` | règle de Born, marginales, échantillonnage avec graine, statistiques, effondrement et renormalisation |
| `test_states.py` | trace partielle, vecteurs de Bloch, pureté, entropie d'intrication |
| `test_circuit.py` | construction et exécution de circuits, portes conditionnées, mise en page du diagramme |
| `test_noise.py` | les canaux préservent la trace, résultats analytiques, somme exhaustive sur les trajectoires d'erreur |
| `test_protocols.py` | les quatre états de Bell, téléportation dans les quatre branches |
| `test_algorithms.py` | Grover face à la formule fermée, Deutsch–Jozsa pour toute fonction équilibrée à 2 et 3 entrées |
| `test_visualization.py` | les figures contiennent les bonnes données |
| `test_translations.py` | 15 langues, clés et paramètres identiques, chaque clé utilisée par l'interface existe |
| `test_app.py` | l'application Streamlit de bout en bout (sans navigateur), dans chaque langue |

Les comparaisons numériques utilisent des tolérances (10⁻¹² pour les amplitudes, bandes à 5σ pour les statistiques d'échantillonnage) plutôt qu'une égalité exacte en virgule flottante.

Combinaisons vérifiées : Python 3.11 + NumPy 1.26.4 / Streamlit 1.50.0 / Plotly 5.24.0; Python 3.13 + NumPy 2.5.4 / Streamlit 1.67.0 / Plotly 7.1.0.

## Performances et limites

| Grandeur | Vecteur d'état | Matrice densité |
|---|---|---|
| Mémoire | 16 · 2ⁿ bytes | 16 · 4ⁿ bytes |
| Une porte à k qubits | O(2ⁿ · 2ᵏ) | O(4ⁿ · 2ᵏ) |
| Limite stricte dans le code | `MAX_QUBITS = 20` (16 MiB) | `MAX_DENSITY_QUBITS = 10` (16 MiB) |
| Limite dans l'interface | 6 qubits | 6 qubits |

La version 1.0 construisait une matrice dense 2ⁿ × 2ⁿ pour chaque porte ; la 2.0 contracte la porte avec le tenseur d'état. Mesuré avec `benchmarks/bench_gates.py` (une Hadamard, meilleur de plusieurs essais, une seule machine ; à considérer comme indicatif) :

| Qubits | Matrice dense (1.0) | Contraction (2.0) | Rapport |
|---|---|---|---|
| 3 | 35 µs | 40 µs | 0.9× |
| 6 | 100 µs | 43 µs | 2× |
| 8 | 553 µs | 44 µs | 13× |
| 10 | 7.6 ms | 49 µs | 155× |
| 12 | 184 ms | 57 µs | ≈ 3200× |

À l'ancienne limite de trois qubits, il n'y a pas d'accélération (la validation des entrées coûte quelques microsecondes) ; l'intérêt est que des registres plus grands deviennent praticables. Le coût de la simulation double toujours à chaque qubit. C'est un outil pédagogique pour de petits registres, pas un simulateur généraliste.

## Limites connues

- L'interface propose 1–6 qubits ; les portes de la barre latérale sont I, X, Y, Z, H, S, T et CNOT. Les portes de rotation n'existent que dans l'API Python.
- La mesure se fait uniquement dans la base de calcul (Z).
- Le bruit est un bruit de Pauli à un qubit après les portes. Pas d'amortissement d'amplitude, pas d'erreur de lecture, pas de bruit au repos ni de bruit corrélé.
- Grover recherche un seul élément marqué ; l'oracle de Deutsch–Jozsa est appliqué comme une seule boîte unitaire plutôt que décomposé en portes élémentaires.
- Le circuit ne permet que l'ajout (pas d'annulation, pas d'édition, pas de glisser-déposer).
- Le diagramme du circuit est un texte à chasse fixe ; les circuits très longs défilent horizontalement.
- L'arabe est traduit mais la mise en page n'est pas inversée de droite à gauche.
- Les 80 chaînes ajoutées dans la 2.0 ont été traduites sans relecture par des locuteurs natifs ; les corrections sont bienvenues.
- Aucune connexion à du matériel quantique réel ni à des services en nuage.

## Changements depuis la 1.0 susceptibles de vous concerner

- **Les résultats du CNOT diffèrent parce que les anciens étaient faux.** La 1.0 mélangeait deux ordres de qubits, si bien que les circuits combinant portes à un qubit et CNOT donnaient des états incorrects (voir `docs/AUDIT.md`, constat Q1).
- `QuantumSimulator` est passé de `main.py` à `quantum_lab`. Ses méthodes de la 1.0 (`apply_gate`, `get_probabilities`, `get_amplitudes`, `measure`, `reset`, `_expand_gate`, `_create_cnot_matrix`) sont conservées. Les entrées invalides lèvent désormais `ValueError`/`TypeError` au lieu d'être acceptées en silence, `state` est en lecture seule et les matrices non unitaires sont rejetées.
- L'histogramme de mesure apparaît après un appui sur *Run Measurement* au lieu d'être régénéré à chaque interaction.
- Les graphiques utilisent Plotly au lieu de Matplotlib. Les boutons *Save …* téléchargent désormais du HTML interactif ; l'export PNG se trouve dans la barre d'outils de chaque graphique.
- `matplotlib` et `qiskit` (inutilisé) ont été retirés de `requirements.txt` ; `plotly` a été ajouté.

## Déploiement sur Streamlit Community Cloud

1. Poussez le dépôt (ou votre fork) sur GitHub.
2. Connectez-vous sur <https://share.streamlit.io> avec GitHub et créez une nouvelle app.
3. Sélectionnez le dépôt et la branche, et définissez main file path sur `main.py`.
4. Dans advanced settings, choisissez Python 3.11 ou plus récent, puis déployez.

Les dépendances sont installées depuis `requirements.txt` ; aucun secret ni variable d'environnement n'est nécessaire. Ces étapes ont été rédigées d'après l'expérience de la plateforme et n'ont pas pu être vérifiées dans sa documentation actuelle lors de la préparation de cette version. Si les écrans diffèrent, suivez <https://docs.streamlit.io/deploy/streamlit-community-cloud>.

La configuration `.devcontainer` lance Streamlit avec les protections CORS et XSRF désactivées, ce qu'exige la redirection de ports de GitHub Codespaces. Ne réutilisez pas ces options pour un déploiement public.

## Feuille de route

- Portes de rotation (Rx, Ry, Rz) et autres portes à deux qubits (CZ, SWAP) dans la barre latérale
- Annulation et édition du circuit ; enregistrement et chargement de circuits
- Mesure dans d'autres bases ; valeurs moyennes d'observables de Pauli
- Canaux d'amortissement d'amplitude et d'erreur de lecture
- Export des circuits vers OpenQASM
- Relecture des traductions par des locuteurs natifs ; mise en page de droite à gauche

## Licence et attribution

Publié sous [licence MIT](LICENSE), Copyright (c) 2025 rasidi3112. Le fichier de licence est inchangé.

Mini Quantum Lab a été créé par [Rasidi](https://github.com/rasidi3112), auteur de l'application, de l'interface et des traductions d'origine. La version 2.0 (cœur de simulation, tests, visualisations et fonctionnalités ajoutées) s'appuie sur ce travail.
