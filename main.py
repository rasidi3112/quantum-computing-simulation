import streamlit as st # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
from matplotlib.patches import Rectangle # type: ignore
import io

st.set_page_config(
    page_title="Simulasi Quantum Computing",
    page_icon="",
    layout="wide"
)
class QuantumSimulator:
    """Simulator quantum computing sederhana"""
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.dim = 2 ** num_qubits
        self.state = np.zeros(self.dim, dtype=complex)
        self.state[0] = 1.0
        self.gate_history = []

    def reset(self):
        """Reset state ke |0...0⟩"""
        self.state = np.zeros(self.dim, dtype=complex)
        self.state[0] = 1.0
        self.gate_history = []
    
    def apply_gate(self, gate_matrix, target_qubit, control_qubit=None):
        """Aplikasikan gate ke qubit tertentu"""
        if control_qubit is not None:
        
            full_gate = self._create_cnot_matrix(control_qubit, target_qubit)
        else:
        
            full_gate = self._expand_gate(gate_matrix, target_qubit)
        
        self.state = full_gate @ self.state
        self.state /= np.linalg.norm(self.state)
    
    def _expand_gate(self, gate, target):
        """Ekspansi gate single-qubit ke sistem multi-qubit"""
        I = np.eye(2)
        matrices = []
        
        for i in range(self.num_qubits):
            if i == target:
                matrices.append(gate)
            else:
                matrices.append(I)
        

        result = matrices[0]
        for m in matrices[1:]:
            result = np.kron(result, m)
        
        return result
    
    def _create_cnot_matrix(self, control, target):
        """Buat matrix CNOT untuk control dan target qubit"""

        dim = self.dim
        cnot = np.eye(dim, dtype=complex)
        
        for i in range(dim):
            bits = [(i >> k) & 1 for k in range(self.num_qubits)]
            
            if bits[control] == 1:
            
                bits[target] = 1 - bits[target]
                j = sum(b << k for k, b in enumerate(bits))
                
            
                cnot[i, i] = 0
                cnot[i, j] = 1
        
        return cnot
    
    def get_probabilities(self):
        """Hitung probabilitas pengukuran setiap basis state"""
        return np.abs(self.state) ** 2
    
    def get_amplitudes(self):
        """Dapatkan amplitudo kompleks"""
        return self.state
    
    def measure(self, shots=1000):
        """Simulasi pengukuran"""
        probs = self.get_probabilities()
        outcomes = np.random.choice(self.dim, size=shots, p=probs)
        return outcomes



PAULI_X = np.array([[0, 1], [1, 0]], dtype=complex)
PAULI_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
PAULI_Z = np.array([[1, 0], [0, -1]], dtype=complex)


HADAMARD = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)


S_GATE = np.array([[1, 0], [0, 1j]], dtype=complex)
T_GATE = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=complex)


IDENTITY = np.eye(2, dtype=complex)


GATE_INFO = {
    "Hadamard (H)": {
        "matrix": HADAMARD,
        "desc": "Menciptakan superposisi: mengubah |0⟩ → (|0⟩ + |1⟩)/√2 dan |1⟩ → (|0⟩ - |1⟩)/√2",
        "emoji": "🌊"
    },
    "Pauli-X": {
        "matrix": PAULI_X,
        "desc": "Flip bit: menukar |0⟩ ↔ |1⟩ (seperti NOT gate klasik)",
        "emoji": "🔄"
    },
    "Pauli-Y": {
        "matrix": PAULI_Y,
        "desc": "Rotasi π radian pada sumbu Y di Bloch sphere",
        "emoji": "🔃"
    },
    "Pauli-Z": {
        "matrix": PAULI_Z,
        "desc": "Phase flip: mengubah tanda fase |1⟩ menjadi -|1⟩",
        "emoji": "⚡"
    },
    "S Gate": {
        "matrix": S_GATE,
        "desc": "Phase shift π/2: menambah fase i pada |1⟩",
        "emoji": "📐"
    },
    "T Gate": {
        "matrix": T_GATE,
        "desc": "Phase shift π/4: penting untuk komputasi universal",
        "emoji": "🎯"
    }
}


def plot_state_vector(simulator):
    """Visualisasi state vector (amplitudo dan fase)"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    amplitudes = simulator.get_amplitudes()
    probabilities = simulator.get_probabilities()
    basis_states = [bin(i)[2:].zfill(simulator.num_qubits) for i in range(simulator.dim)]
    

    colors = plt.cm.viridis(probabilities / probabilities.max() if probabilities.max() > 0 else probabilities)
    bars1 = ax1.bar(basis_states, probabilities, color=colors, edgecolor='black', linewidth=1.5)
    ax1.set_xlabel('Basis State |x⟩', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Probabilitas P(x)', fontsize=12, fontweight='bold')
    ax1.set_title('📊 Distribusi Probabilitas Pengukuran', fontsize=14, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    ax1.set_ylim([0, 1.1])
    
    for bar, prob in zip(bars1, probabilities):
        if prob > 0.01:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{prob:.3f}',
                    ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    x = np.arange(len(basis_states))
    width = 0.35
    
    real_parts = np.real(amplitudes)
    imag_parts = np.imag(amplitudes)
    
    ax2.bar(x - width/2, real_parts, width, label='Real', color='#3498db', edgecolor='black')
    ax2.bar(x + width/2, imag_parts, width, label='Imajiner', color='#e74c3c', edgecolor='black')
    
    ax2.set_xlabel('Basis State |x⟩', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Amplitudo', fontsize=12, fontweight='bold')
    ax2.set_title('🌊 Amplitudo Kompleks State Vector', fontsize=14, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(basis_states)
    ax2.legend(fontsize=10)
    ax2.grid(axis='y', alpha=0.3, linestyle='--')
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
    
    plt.tight_layout()
    return fig

def plot_measurement_histogram(simulator, shots=1000):
    """Histogram hasil pengukuran"""
    outcomes = simulator.measure(shots)
    basis_states = [bin(i)[2:].zfill(simulator.num_qubits) for i in range(simulator.dim)]
    
    counts = np.bincount(outcomes, minlength=simulator.dim)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    colors = plt.cm.plasma(counts / counts.max() if counts.max() > 0 else counts)
    bars = ax.bar(basis_states, counts, color=colors, edgecolor='black', linewidth=1.5)
    
    ax.set_xlabel('Hasil Pengukuran', fontsize=12, fontweight='bold')
    ax.set_ylabel(f'Frekuensi (dari {shots} shots)', fontsize=12, fontweight='bold')
    ax.set_title(f'Histogram Pengukuran ({shots} Shots)', fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    

    for bar, count in zip(bars, counts):
        if count > 0:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{count}\n({count/shots*100:.1f}%)',
                    ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    return fig

def display_matrix(matrix, title):
    """Tampilkan representasi matrix gate"""
    st.markdown(f"### 🔢 {title}")
    

    matrix_str = "```\n"
    for row in matrix:
        row_str = "["
        for val in row:
            real = np.real(val)
            imag = np.imag(val)
            
            if abs(imag) < 1e-10:
                row_str += f" {real:7.4f}      "
            elif abs(real) < 1e-10:
                row_str += f" {imag:7.4f}i     "
            else:
                row_str += f" {real:.3f}{imag:+.3f}i "
        row_str += "]\n"
        matrix_str += row_str
    matrix_str += "```"
    
    st.markdown(matrix_str)


def main():
   
    st.title(" Simulasi Quantum Computing Interaktif")
    st.markdown("---")
    
  
    with st.expander("ℹ️ Apa itu Quantum Computing?", expanded=False):
        st.markdown("""
        ###  Pengantar Quantum Computing
        
        **Quantum Computing** adalah paradigma komputasi yang memanfaatkan fenomena mekanika kuantum seperti **superposisi** dan **entanglement**.
        
        #### 🔹 Qubit (Quantum Bit)
        Berbeda dengan bit klasik (0 atau 1), **qubit** dapat berada dalam **superposisi** dari kedua state:
        - |ψ⟩ = α|0⟩ + β|1⟩
        - |α|² + |β|² = 1 (normalisasi)
        
        #### 🔹 Quantum Gates
        **Gate kuantum** adalah operasi yang memanipulasi state qubit, analog dengan logic gate klasik namun **reversible** dan **unitary**.
        
        #### 🔹 Pengukuran
        Saat diukur, qubit **collapse** ke salah satu basis state (|0⟩ atau |1⟩) dengan probabilitas |α|² dan |β|².
        """)
    
    st.markdown("---")
    
   
    st.sidebar.header("⚙️ Pengaturan Simulasi")
    
    
    num_qubits = st.sidebar.selectbox(
        "Jumlah Qubit:",
        options=[1, 2, 3],
        index=0,
        help="Pilih jumlah qubit untuk sistem kuantum (1-3 qubit)"
    )
    
   
    if 'simulator' not in st.session_state or st.session_state.get('num_qubits') != num_qubits:
        st.session_state.simulator = QuantumSimulator(num_qubits)
        st.session_state.num_qubits = num_qubits
        st.session_state.circuit = []
    
    simulator = st.session_state.simulator
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎛️ Tambahkan Quantum Gate")
    
    
    gate_name = st.sidebar.selectbox(
        "Pilih Gate:",
        options=list(GATE_INFO.keys()),
        help="Pilih quantum gate yang akan diterapkan"
    )
    
    
    target_qubit = st.sidebar.selectbox(
        "Target Qubit:",
        options=list(range(num_qubits)),
        format_func=lambda x: f"Q{x}",
        help="Qubit yang akan dikenai gate"
    )
    

    gate_data = GATE_INFO[gate_name]
    st.sidebar.info(f"{gate_data['emoji']} **{gate_name}**\n\n{gate_data['desc']}")
    
   
    if st.sidebar.button("➕ Aplikasikan Gate", use_container_width=True):
        simulator.apply_gate(gate_data['matrix'], target_qubit)
        st.session_state.circuit.append(f"{gate_name} → Q{target_qubit}")
        st.sidebar.success(f"✅ {gate_name} diterapkan pada Q{target_qubit}")
    
    st.sidebar.markdown("---")
    
    
    if num_qubits > 1:
        st.sidebar.subheader("🔗 CNOT Gate (2-Qubit)")
        
        col1, col2 = st.sidebar.columns(2)
        control_qubit = col1.selectbox(
            "Control:",
            options=list(range(num_qubits)),
            format_func=lambda x: f"Q{x}"
        )
        
        target_qubit_cnot = col2.selectbox(
            "Target:",
            options=[q for q in range(num_qubits) if q != control_qubit],
            format_func=lambda x: f"Q{x}"
        )
        
        st.sidebar.info("🔗 **CNOT**: Flip target qubit jika control qubit = |1⟩")
        
        if st.sidebar.button("➕ Aplikasikan CNOT", use_container_width=True):
            simulator.apply_gate(IDENTITY, target_qubit_cnot, control_qubit)
            st.session_state.circuit.append(f"CNOT: Q{control_qubit} → Q{target_qubit_cnot}")
            st.sidebar.success(f"✅ CNOT diterapkan (C: Q{control_qubit}, T: Q{target_qubit_cnot})")
    
    st.sidebar.markdown("---")
    
   
    if st.sidebar.button("🔄 Reset Sistem", use_container_width=True, type="secondary"):
        simulator.reset()
        st.session_state.circuit = []
        st.sidebar.warning("⚠️ Sistem direset ke |0...0⟩")
        st.rerun()
    
    # Main area
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.subheader(" Visualisasi State Vector")
        
       
        fig_state = plot_state_vector(simulator)
        st.pyplot(fig_state)
        
        # Opsi save gambar
        buf = io.BytesIO()
        fig_state.savefig(buf, format='png', dpi=150, bbox_inches='tight')
        buf.seek(0)
        
        st.download_button(
            label="💾 Simpan Grafik State Vector",
            data=buf,
            file_name="quantum_state_vector.png",
            mime="image/png"
        )
        
        st.markdown("---")
        
        # Histogram pengukuran
        st.subheader(" Simulasi Pengukuran")
        shots = st.slider("Jumlah Shots:", min_value=100, max_value=10000, value=1000, step=100)
        
        fig_measurement = plot_measurement_histogram(simulator, shots)
        st.pyplot(fig_measurement)
        
        # Opsi save gambar
        buf2 = io.BytesIO()
        fig_measurement.savefig(buf2, format='png', dpi=150, bbox_inches='tight')
        buf2.seek(0)
        
        st.download_button(
            label="💾 Simpan Histogram Pengukuran",
            data=buf2,
            file_name="quantum_measurement.png",
            mime="image/png"
        )
    
    with col_right:
        st.subheader(" Informasi State")
        
        # Current state info
        st.markdown("####  State Saat Ini:")
        
        basis_states = [bin(i)[2:].zfill(num_qubits) for i in range(simulator.dim)]
        amplitudes = simulator.get_amplitudes()
        probabilities = simulator.get_probabilities()
        
        state_str = ""
        for i, (basis, amp, prob) in enumerate(zip(basis_states, amplitudes, probabilities)):
            if abs(amp) > 1e-10:
                real = np.real(amp)
                imag = np.imag(amp)
                
                if abs(imag) < 1e-10:
                    amp_str = f"{real:.4f}"
                elif abs(real) < 1e-10:
                    amp_str = f"{imag:.4f}i"
                else:
                    amp_str = f"({real:.3f}{imag:+.3f}i)"
                
                state_str += f"**|{basis}⟩**: {amp_str} (P={prob:.4f})\n\n"
        
        st.markdown(state_str)
        
        st.markdown("---")
        
        # Circuit history
        st.markdown("#### 🔧 Riwayat Circuit:")
        
        if st.session_state.circuit:
            for i, gate in enumerate(st.session_state.circuit, 1):
                st.markdown(f"{i}. {gate}")
        else:
            st.info("Belum ada gate yang diterapkan")
        
        st.markdown("---")
        
        # Matrix representation
        if st.checkbox("📐 Tampilkan Matrix Gate"):
            display_matrix(gate_data['matrix'], f"Matrix {gate_name}")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #7f8c8d; font-size: 12px;'>
        <p>⚛️ Dibuat dengan Rasidi menggunakan Streamlit & NumPy | Quantum Computing Simulator v1.0</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
