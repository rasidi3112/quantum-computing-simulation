import streamlit as st # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
from matplotlib.patches import Rectangle # type: ignore
import io

# Import translations
from translations import TRANSLATIONS, AVAILABLE_LANGUAGES, get_text, get_gate_description

# Initialize language in session state before page config
if 'language' not in st.session_state:
    st.session_state.language = "English"

# Get current language
lang = st.session_state.language

st.set_page_config(
    page_title=get_text(lang, "page_title"),
    page_icon="⚛️",
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


def get_gate_info(lang):
    """Get gate info with translated descriptions"""
    return {
        "Hadamard (H)": {
            "matrix": HADAMARD,
            "desc": get_gate_description(lang, "Hadamard (H)"),
            "emoji": "🌊"
        },
        "Pauli-X": {
            "matrix": PAULI_X,
            "desc": get_gate_description(lang, "Pauli-X"),
            "emoji": "🔄"
        },
        "Pauli-Y": {
            "matrix": PAULI_Y,
            "desc": get_gate_description(lang, "Pauli-Y"),
            "emoji": "🔃"
        },
        "Pauli-Z": {
            "matrix": PAULI_Z,
            "desc": get_gate_description(lang, "Pauli-Z"),
            "emoji": "⚡"
        },
        "S Gate": {
            "matrix": S_GATE,
            "desc": get_gate_description(lang, "S Gate"),
            "emoji": "📐"
        },
        "T Gate": {
            "matrix": T_GATE,
            "desc": get_gate_description(lang, "T Gate"),
            "emoji": "🎯"
        }
    }


def plot_state_vector(simulator, lang):
    """Visualisasi state vector (amplitudo dan fase)"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    amplitudes = simulator.get_amplitudes()
    probabilities = simulator.get_probabilities()
    basis_states = [bin(i)[2:].zfill(simulator.num_qubits) for i in range(simulator.dim)]
    

    colors = plt.cm.viridis(probabilities / probabilities.max() if probabilities.max() > 0 else probabilities)
    bars1 = ax1.bar(basis_states, probabilities, color=colors, edgecolor='black', linewidth=1.5)
    ax1.set_xlabel(get_text(lang, "basis_state_label"), fontsize=12, fontweight='bold')
    ax1.set_ylabel(get_text(lang, "probability_label"), fontsize=12, fontweight='bold')
    ax1.set_title(get_text(lang, "probability_dist_title"), fontsize=14, fontweight='bold')
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
    
    ax2.bar(x - width/2, real_parts, width, label=get_text(lang, "real_label"), color='#3498db', edgecolor='black')
    ax2.bar(x + width/2, imag_parts, width, label=get_text(lang, "imaginary_label"), color='#e74c3c', edgecolor='black')
    
    ax2.set_xlabel(get_text(lang, "basis_state_label"), fontsize=12, fontweight='bold')
    ax2.set_ylabel(get_text(lang, "amplitude_label"), fontsize=12, fontweight='bold')
    ax2.set_title(get_text(lang, "amplitude_title"), fontsize=14, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(basis_states)
    ax2.legend(fontsize=10)
    ax2.grid(axis='y', alpha=0.3, linestyle='--')
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
    
    plt.tight_layout()
    return fig

def plot_measurement_histogram(simulator, shots, lang):
    """Histogram hasil pengukuran"""
    outcomes = simulator.measure(shots)
    basis_states = [bin(i)[2:].zfill(simulator.num_qubits) for i in range(simulator.dim)]
    
    counts = np.bincount(outcomes, minlength=simulator.dim)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    colors = plt.cm.plasma(counts / counts.max() if counts.max() > 0 else counts)
    bars = ax.bar(basis_states, counts, color=colors, edgecolor='black', linewidth=1.5)
    
    ax.set_xlabel(get_text(lang, "measurement_result_label"), fontsize=12, fontweight='bold')
    ax.set_ylabel(get_text(lang, "frequency_label", shots=shots), fontsize=12, fontweight='bold')
    ax.set_title(get_text(lang, "histogram_title", shots=shots), fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    

    for bar, count in zip(bars, counts):
        if count > 0:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{count}\n({count/shots*100:.1f}%)',
                    ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    return fig

def display_matrix(matrix, title, lang):
    """Tampilkan representasi matrix gate"""
    st.markdown(f"### 🔢 {get_text(lang, 'matrix_title')} {title}")
    

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
    # Get current language
    lang = st.session_state.language
    
    # Get translated gate info
    GATE_INFO = get_gate_info(lang)
    
    st.title(get_text(lang, "main_title"))
    st.markdown("---")
    
    # Language selector at the top of sidebar
    st.sidebar.header(get_text(lang, "language_label"))
    
    # Create language options with flags
    lang_options = {f"{TRANSLATIONS[l]['flag']} {l}": l for l in AVAILABLE_LANGUAGES}
    current_lang_display = f"{TRANSLATIONS[lang]['flag']} {lang}"
    
    selected_lang_display = st.sidebar.selectbox(
        "",
        options=list(lang_options.keys()),
        index=list(lang_options.keys()).index(current_lang_display),
        label_visibility="collapsed"
    )
    
    selected_lang = lang_options[selected_lang_display]
    
    # Update language if changed
    if selected_lang != lang:
        st.session_state.language = selected_lang
        st.rerun()
    
    st.sidebar.markdown("---")
    
    with st.expander(get_text(lang, "intro_header"), expanded=False):
        st.markdown(get_text(lang, "intro_title"))
        st.markdown(get_text(lang, "intro_content"))
    
    st.markdown("---")
    
   
    st.sidebar.header(get_text(lang, "sidebar_settings"))
    
    
    num_qubits = st.sidebar.selectbox(
        get_text(lang, "num_qubits_label"),
        options=[1, 2, 3],
        index=0,
        help=get_text(lang, "num_qubits_help")
    )
    
   
    if 'simulator' not in st.session_state or st.session_state.get('num_qubits') != num_qubits:
        st.session_state.simulator = QuantumSimulator(num_qubits)
        st.session_state.num_qubits = num_qubits
        st.session_state.circuit = []
    
    simulator = st.session_state.simulator
    
    st.sidebar.markdown("---")
    st.sidebar.subheader(get_text(lang, "add_gate_header"))
    
    
    gate_name = st.sidebar.selectbox(
        get_text(lang, "select_gate"),
        options=list(GATE_INFO.keys()),
        help=get_text(lang, "select_gate_help")
    )
    
    
    target_qubit = st.sidebar.selectbox(
        get_text(lang, "target_qubit"),
        options=list(range(num_qubits)),
        format_func=lambda x: f"Q{x}",
        help=get_text(lang, "target_qubit_help")
    )
    

    gate_data = GATE_INFO[gate_name]
    st.sidebar.info(f"{gate_data['emoji']} **{gate_name}**\n\n{gate_data['desc']}")
    
   
    if st.sidebar.button(get_text(lang, "apply_gate_btn"), use_container_width=True):
        simulator.apply_gate(gate_data['matrix'], target_qubit)
        st.session_state.circuit.append(f"{gate_name} → Q{target_qubit}")
        st.sidebar.success(get_text(lang, "gate_applied_success", gate_name=gate_name, target=target_qubit))
    
    st.sidebar.markdown("---")
    
    
    if num_qubits > 1:
        st.sidebar.subheader(get_text(lang, "cnot_header"))
        
        col1, col2 = st.sidebar.columns(2)
        control_qubit = col1.selectbox(
            get_text(lang, "control_label"),
            options=list(range(num_qubits)),
            format_func=lambda x: f"Q{x}"
        )
        
        target_qubit_cnot = col2.selectbox(
            get_text(lang, "target_label"),
            options=[q for q in range(num_qubits) if q != control_qubit],
            format_func=lambda x: f"Q{x}"
        )
        
        st.sidebar.info(get_text(lang, "cnot_info"))
        
        if st.sidebar.button(get_text(lang, "apply_cnot_btn"), use_container_width=True):
            simulator.apply_gate(IDENTITY, target_qubit_cnot, control_qubit)
            st.session_state.circuit.append(f"CNOT: Q{control_qubit} → Q{target_qubit_cnot}")
            st.sidebar.success(get_text(lang, "cnot_applied_success", control=control_qubit, target=target_qubit_cnot))
    
    st.sidebar.markdown("---")
    
   
    if st.sidebar.button(get_text(lang, "reset_btn"), use_container_width=True, type="secondary"):
        simulator.reset()
        st.session_state.circuit = []
        st.sidebar.warning(get_text(lang, "reset_warning"))
        st.rerun()
    
    # Main area
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.subheader(get_text(lang, "state_vector_header"))
        
       
        fig_state = plot_state_vector(simulator, lang)
        st.pyplot(fig_state)
        
        # Opsi save gambar
        buf = io.BytesIO()
        fig_state.savefig(buf, format='png', dpi=150, bbox_inches='tight')
        buf.seek(0)
        
        st.download_button(
            label=get_text(lang, "save_state_vector_btn"),
            data=buf,
            file_name="quantum_state_vector.png",
            mime="image/png"
        )
        
        st.markdown("---")
        
        # Histogram pengukuran
        st.subheader(get_text(lang, "measurement_header"))
        shots = st.slider(get_text(lang, "shots_label"), min_value=100, max_value=10000, value=1000, step=100)
        
        fig_measurement = plot_measurement_histogram(simulator, shots, lang)
        st.pyplot(fig_measurement)
        
        # Opsi save gambar
        buf2 = io.BytesIO()
        fig_measurement.savefig(buf2, format='png', dpi=150, bbox_inches='tight')
        buf2.seek(0)
        
        st.download_button(
            label=get_text(lang, "save_measurement_btn"),
            data=buf2,
            file_name="quantum_measurement.png",
            mime="image/png"
        )
    
    with col_right:
        st.subheader(get_text(lang, "state_info_header"))
        
        # Current state info
        st.markdown(get_text(lang, "current_state"))
        
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
        st.markdown(get_text(lang, "circuit_history"))
        
        if st.session_state.circuit:
            for i, gate in enumerate(st.session_state.circuit, 1):
                st.markdown(f"{i}. {gate}")
        else:
            st.info(get_text(lang, "no_gates_applied"))
        
        st.markdown("---")
        
        # Matrix representation
        if st.checkbox(get_text(lang, "show_matrix")):
            display_matrix(gate_data['matrix'], gate_name, lang)
    
    # Footer
    st.markdown("---")
    st.markdown(f"""
    <div style='text-align: center; color: #7f8c8d; font-size: 12px;'>
        <p>{get_text(lang, "footer")}</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
