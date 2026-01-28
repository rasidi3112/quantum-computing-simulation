<h1 align="center">Mini Quantum Lab - Streamlit Quantum Simulator</h1>

<p align="center">
  <b>A lightweight interactive Quantum Computing Simulation Lab</b> built with Python, Streamlit, and NumPy.<br>
  Visualize <b>qubit superposition</b>, <b>entanglement</b>, and <b>quantum gates</b> in real time - directly in your browser.
</p>

<hr>

<h2> Overview</h2>

<p>
  <b>Mini Quantum Lab</b> is an educational web simulator designed to help learners explore the fundamentals of
  <b>quantum mechanics</b> and <b>quantum computing</b> interactively.<br><br>
  It enables users to visualize quantum state evolution, apply quantum gates dynamically, simulate qubit measurements, 
  and observe probabilistic outcomes.
</p>

<blockquote>
  ⚠️ <i>This project is inspired by IBM Quantum Lab and Qiskit visualization methods.<br>
  It is not affiliated with or endorsed by IBM.</i>
</blockquote>

<hr>

<h2> Technologies Used</h2>
<ul>
  <li> <b>Streamlit</b> - for an elegant, real-time web interface</li>
  <li> <b>NumPy</b> - for matrix-based quantum state calculations</li>
  <li> <b>Matplotlib</b> - for dynamic visualization of quantum states</li>
</ul>

<hr>

<h2> Key Features</h2>

<h3> Quantum State Simulation</h3>
<ul>
  <li>Initialize up to <b>3 qubits</b></li>
  <li>View live quantum state amplitudes & probabilities</li>
</ul>

<h3> Quantum Gate Application</h3>
<ul>
  <li>Supports <b>Hadamard</b>, <b>Pauli (X, Y, Z)</b>, <b>S</b>, <b>T</b>, and <b>CNOT</b> gates</li>
  <li>Apply gates to specific qubits with <b>interactive feedback</b></li>
</ul>

<h3> Measurement Simulation</h3>
<ul>
  <li>Perform <b>quantum measurements</b> with configurable shots (100–10,000)</li>
  <li>Observe <b>probability distributions</b> and <b>measurement histograms</b></li>
</ul>

<h3> Matrix Visualization</h3>
<ul>
  <li>Inspect the <b>unitary matrix</b> of any gate</li>
  <li>Explore <b>real & imaginary</b> components of the matrix</li>
</ul>

<h3> Circuit History Tracking</h3>
<ul>
  <li>Every applied gate is stored in a <b>real-time updating circuit log</b></li>
</ul>

<hr>

<h2> Visualization Example</h2>

<h3>Quantum State Vector</h3>
<p>Amplitude and phase of each quantum basis state:</p>
<img src="assets/quantum_state_vector.png" alt="Quantum State Vector" width="600"/>

<h3>Interactive Quantum Gate Simulation</h3>
<p>Visualize how applying quantum gates affects qubit states in real time:</p>
<img src="assets/quantum_measurement.png" alt="Quantum Gate Simulation" width="600"/>

<hr>

<h2> Project Structure</h2>

<pre>
quantum-computing-simulation/
├── assets/
│   ├── quantum_state_vector.png
│   └── quantum_gate_simulation.png
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
</pre>

<hr>

<h2> Installation</h2>

<pre>
git clone https://github.com/rasidi3112/quantum-computing-simulation.git
cd quantum-computing-simulation
pip install -r requirements.txt
streamlit run main.py
</pre>

<p>Then open  <a href="http://localhost:8501" target="_blank">http://localhost:8501</a> to explore the simulator.</p>

<hr>

<h2> Future Improvements</h2>
<ul>
  <li> Quantum circuit composer (drag & drop interface)</li>
  <li> Cloud-based quantum backend integration</li>
  <li> Bloch sphere 3D visualization</li>
</ul>

<hr>

<h2> License</h2>
<p>This project is licensed under the <b>MIT License</b> — feel free to use and modify with credit.</p>

<hr>

<h2> Hashtags</h2>
<p>
  #QuantumComputing #MiniQuantumLab #Streamlit #QuantumSimulator <br>
  #QuantumGateVisualizer #PythonAI #NumPy #Matplotlib #QubitSimulation
</p>

<hr>

<h3 align="center">👨‍💻 Created by🫰🫰 <a href="https://github.com/rasidi3112" target="_blank">Rasidi</a></h3>
