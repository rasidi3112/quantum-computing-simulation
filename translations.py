# translations.py
# Multi-language support for Quantum Computing Simulation
# Supported languages: English, Indonesian, Spanish, Mandarin, Arabic, French, Japanese, Korean, German, Portuguese, Russian, Hindi, Turkish, Italian, Vietnamese

TRANSLATIONS = {
    "English": {
        "lang_code": "en",
        "flag": "🇬🇧",
         
        # Page config
        "page_title": "Quantum Computing Simulation",
        
        # Main title
        "main_title": " Interactive Quantum Computing Simulation",
        
        # Introduction section
        "intro_header": "ℹ️ What is Quantum Computing?",
        "intro_title": "### ⚛️ Introduction to Quantum Computing",
        "intro_content": """
**Quantum Computing** is a computing paradigm that utilizes quantum mechanical phenomena such as **superposition** and **entanglement**.

#### 🔹 Qubit (Quantum Bit)
Unlike classical bits (0 or 1), **qubits** can exist in **superposition** of both states:
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1 (normalization)

#### 🔹 Quantum Gates
**Quantum gates** are operations that manipulate qubit states, analogous to classical logic gates but **reversible** and **unitary**.

#### 🔹 Measurement
When measured, a qubit **collapses** to one of the basis states (|0⟩ or |1⟩) with probabilities |α|² and |β|².
""",
        
        # Sidebar
        "sidebar_settings": "⚙️ Simulation Settings",
        "num_qubits_label": "Number of Qubits:",
        "num_qubits_help": "Select the number of qubits for the quantum system (1-{max_qubits} qubits)",
        "add_gate_header": "🎛️ Add Quantum Gate",
        "select_gate": "Select Gate:",
        "select_gate_help": "Select the quantum gate to apply",
        "target_qubit": "Target Qubit:",
        "target_qubit_help": "Qubit that will receive the gate",
        "apply_gate_btn": "➕ Apply Gate",
        "gate_applied_success": "✅ {gate_name} applied to Q{target}",
        
        # CNOT section
        "cnot_header": "🔗 CNOT Gate (2-Qubit)",
        "control_label": "Control:",
        "target_label": "Target:",
        "cnot_info": "🔗 **CNOT**: Flip target qubit if control qubit = |1⟩",
        "apply_cnot_btn": "➕ Apply CNOT",
        "cnot_applied_success": "✅ CNOT applied (C: Q{control}, T: Q{target})",
        
        # Reset
        "reset_btn": "🔄 Reset System",
        "reset_warning": "⚠️ System reset to |0...0⟩",
        
        # Main area
        "state_vector_header": " State Vector Visualization",
        "save_state_vector_btn": "💾 Save State Vector Graph",
        "measurement_header": " Measurement Simulation",
        "shots_label": "Number of Shots:",
        "save_measurement_btn": "💾 Save Measurement Histogram",
        
        # State info
        "state_info_header": " State Information",
        "current_state": "#### 📍 Current State:",
        "circuit_history": "#### 🔧 Circuit History:",
        "no_gates_applied": "No gates applied yet",
        "show_matrix": "📐 Show Gate Matrix",
        "matrix_title": "Matrix",
        
        # Plot labels
        "basis_state_label": "Basis State |x⟩",
        "probability_label": "Probability P(x)",
        "probability_dist_title": "📊 Measurement Probability Distribution",
        "amplitude_label": "Amplitude",
        "amplitude_title": "🌊 Complex Amplitude State Vector",
        "real_label": "Real",
        "imaginary_label": "Imaginary",
        "measurement_result_label": "Measurement Result",
        "frequency_label": "Frequency (from {shots} shots)",
        "histogram_title": "Measurement Histogram ({shots} Shots)",
        
        # Footer
        "footer": "⚛️ Created with Rasidi using Streamlit & NumPy | Quantum Computing Simulator v2.0",
        
        # Gate descriptions
        "gate_hadamard_desc": "Creates superposition: transforms |0⟩ → (|0⟩ + |1⟩)/√2 and |1⟩ → (|0⟩ - |1⟩)/√2",
        "gate_pauli_x_desc": "Bit flip: swaps |0⟩ ↔ |1⟩ (like classical NOT gate)",
        "gate_pauli_y_desc": "Rotation of π radians on the Y axis of the Bloch sphere",
        "gate_pauli_z_desc": "Phase flip: changes the phase of |1⟩ to -|1⟩",
        "gate_s_desc": "Phase shift π/2: adds phase i to |1⟩",
        "gate_t_desc": "Phase shift π/4: important for universal computation",
        
        # Language selector
        "language_label": "🌐 Language:",
    },
    
    "Indonesia": {
        "lang_code": "id",
        "flag": "🇮🇩",
        
        # Page config
        "page_title": "Simulasi Quantum Computing",
        
        # Main title
        "main_title": " Simulasi Quantum Computing Interaktif",
        
        # Introduction section
        "intro_header": "ℹ️ Apa itu Quantum Computing?",
        "intro_title": "### ⚛️ Pengantar Quantum Computing",
        "intro_content": """
**Quantum Computing** adalah paradigma komputasi yang memanfaatkan fenomena mekanika kuantum seperti **superposisi** dan **entanglement**.

#### 🔹 Qubit (Quantum Bit)
Berbeda dengan bit klasik (0 atau 1), **qubit** dapat berada dalam **superposisi** dari kedua state:
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1 (normalisasi)

#### 🔹 Quantum Gates
**Gate kuantum** adalah operasi yang memanipulasi state qubit, analog dengan logic gate klasik namun **reversible** dan **unitary**.

#### 🔹 Pengukuran
Saat diukur, qubit **collapse** ke salah satu basis state (|0⟩ atau |1⟩) dengan probabilitas |α|² dan |β|².
""",
        
        # Sidebar
        "sidebar_settings": "⚙️ Pengaturan Simulasi",
        "num_qubits_label": "Jumlah Qubit:",
        "num_qubits_help": "Pilih jumlah qubit untuk sistem kuantum (1-{max_qubits} qubit)",
        "add_gate_header": "🎛️ Tambahkan Quantum Gate",
        "select_gate": "Pilih Gate:",
        "select_gate_help": "Pilih quantum gate yang akan diterapkan",
        "target_qubit": "Target Qubit:",
        "target_qubit_help": "Qubit yang akan dikenai gate",
        "apply_gate_btn": "➕ Aplikasikan Gate",
        "gate_applied_success": "✅ {gate_name} diterapkan pada Q{target}",
        
        # CNOT section
        "cnot_header": "🔗 CNOT Gate (2-Qubit)",
        "control_label": "Control:",
        "target_label": "Target:",
        "cnot_info": "🔗 **CNOT**: Flip target qubit jika control qubit = |1⟩",
        "apply_cnot_btn": "➕ Aplikasikan CNOT",
        "cnot_applied_success": "✅ CNOT diterapkan (C: Q{control}, T: Q{target})",
        
        # Reset
        "reset_btn": "🔄 Reset Sistem",
        "reset_warning": "⚠️ Sistem direset ke |0...0⟩",
        
        # Main area
        "state_vector_header": " Visualisasi State Vector",
        "save_state_vector_btn": "💾 Simpan Grafik State Vector",
        "measurement_header": " Simulasi Pengukuran",
        "shots_label": "Jumlah Shots:",
        "save_measurement_btn": "💾 Simpan Histogram Pengukuran",
        
        # State info
        "state_info_header": " Informasi State",
        "current_state": "#### 📍 State Saat Ini:",
        "circuit_history": "#### 🔧 Riwayat Circuit:",
        "no_gates_applied": "Belum ada gate yang diterapkan",
        "show_matrix": "📐 Tampilkan Matrix Gate",
        "matrix_title": "Matrix",
        
        # Plot labels
        "basis_state_label": "Basis State |x⟩",
        "probability_label": "Probabilitas P(x)",
        "probability_dist_title": "📊 Distribusi Probabilitas Pengukuran",
        "amplitude_label": "Amplitudo",
        "amplitude_title": "🌊 Amplitudo Kompleks State Vector",
        "real_label": "Real",
        "imaginary_label": "Imajiner",
        "measurement_result_label": "Hasil Pengukuran",
        "frequency_label": "Frekuensi (dari {shots} shots)",
        "histogram_title": "Histogram Pengukuran ({shots} Shots)",
        
        # Footer
        "footer": "⚛️ Dibuat dengan Rasidi menggunakan Streamlit & NumPy | Quantum Computing Simulator v2.0",
        
        # Gate descriptions
        "gate_hadamard_desc": "Menciptakan superposisi: mengubah |0⟩ → (|0⟩ + |1⟩)/√2 dan |1⟩ → (|0⟩ - |1⟩)/√2",
        "gate_pauli_x_desc": "Flip bit: menukar |0⟩ ↔ |1⟩ (seperti NOT gate klasik)",
        "gate_pauli_y_desc": "Rotasi π radian pada sumbu Y di Bloch sphere",
        "gate_pauli_z_desc": "Phase flip: mengubah tanda fase |1⟩ menjadi -|1⟩",
        "gate_s_desc": "Phase shift π/2: menambah fase i pada |1⟩",
        "gate_t_desc": "Phase shift π/4: penting untuk komputasi universal",
        
        # Language selector
        "language_label": "🌐 Bahasa:",
    },
    
    "Español": {
        "lang_code": "es",
        "flag": "🇪🇸",
        
        # Page config
        "page_title": "Simulación de Computación Cuántica",
        
        # Main title
        "main_title": " Simulación Interactiva de Computación Cuántica",
        
        # Introduction section
        "intro_header": "ℹ️ ¿Qué es la Computación Cuántica?",
        "intro_title": "### ⚛️ Introducción a la Computación Cuántica",
        "intro_content": """
**La Computación Cuántica** es un paradigma de computación que utiliza fenómenos de la mecánica cuántica como la **superposición** y el **entrelazamiento**.

#### 🔹 Qubit (Bit Cuántico)
A diferencia de los bits clásicos (0 o 1), los **qubits** pueden existir en **superposición** de ambos estados:
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1 (normalización)

#### 🔹 Puertas Cuánticas
Las **puertas cuánticas** son operaciones que manipulan estados de qubits, análogas a las puertas lógicas clásicas pero **reversibles** y **unitarias**.

#### 🔹 Medición
Al medirse, un qubit **colapsa** a uno de los estados base (|0⟩ o |1⟩) con probabilidades |α|² y |β|².
""",
        
        # Sidebar
        "sidebar_settings": "⚙️ Configuración de Simulación",
        "num_qubits_label": "Número de Qubits:",
        "num_qubits_help": "Seleccione el número de qubits para el sistema cuántico (1-{max_qubits} qubits)",
        "add_gate_header": "🎛️ Añadir Puerta Cuántica",
        "select_gate": "Seleccionar Puerta:",
        "select_gate_help": "Seleccione la puerta cuántica a aplicar",
        "target_qubit": "Qubit Objetivo:",
        "target_qubit_help": "Qubit que recibirá la puerta",
        "apply_gate_btn": "➕ Aplicar Puerta",
        "gate_applied_success": "✅ {gate_name} aplicado a Q{target}",
        
        # CNOT section
        "cnot_header": "🔗 Puerta CNOT (2-Qubit)",
        "control_label": "Control:",
        "target_label": "Objetivo:",
        "cnot_info": "🔗 **CNOT**: Invierte el qubit objetivo si el qubit de control = |1⟩",
        "apply_cnot_btn": "➕ Aplicar CNOT",
        "cnot_applied_success": "✅ CNOT aplicado (C: Q{control}, T: Q{target})",
        
        # Reset
        "reset_btn": "🔄 Reiniciar Sistema",
        "reset_warning": "⚠️ Sistema reiniciado a |0...0⟩",
        
        # Main area
        "state_vector_header": " Visualización del Vector de Estado",
        "save_state_vector_btn": "💾 Guardar Gráfico del Vector de Estado",
        "measurement_header": " Simulación de Medición",
        "shots_label": "Número de Disparos:",
        "save_measurement_btn": "💾 Guardar Histograma de Medición",
        
        # State info
        "state_info_header": " Información del Estado",
        "current_state": "#### 📍 Estado Actual:",
        "circuit_history": "#### 🔧 Historial del Circuito:",
        "no_gates_applied": "Aún no se han aplicado puertas",
        "show_matrix": "📐 Mostrar Matriz de la Puerta",
        "matrix_title": "Matriz",
        
        # Plot labels
        "basis_state_label": "Estado Base |x⟩",
        "probability_label": "Probabilidad P(x)",
        "probability_dist_title": "📊 Distribución de Probabilidad de Medición",
        "amplitude_label": "Amplitud",
        "amplitude_title": "🌊 Vector de Estado de Amplitud Compleja",
        "real_label": "Real",
        "imaginary_label": "Imaginario",
        "measurement_result_label": "Resultado de Medición",
        "frequency_label": "Frecuencia (de {shots} disparos)",
        "histogram_title": "Histograma de Medición ({shots} Disparos)",
        
        # Footer
        "footer": "⚛️ Creado con Rasidi usando Streamlit & NumPy | Quantum Computing Simulator v2.0",
        
        # Gate descriptions
        "gate_hadamard_desc": "Crea superposición: transforma |0⟩ → (|0⟩ + |1⟩)/√2 y |1⟩ → (|0⟩ - |1⟩)/√2",
        "gate_pauli_x_desc": "Inversión de bit: intercambia |0⟩ ↔ |1⟩ (como puerta NOT clásica)",
        "gate_pauli_y_desc": "Rotación de π radianes en el eje Y de la esfera de Bloch",
        "gate_pauli_z_desc": "Inversión de fase: cambia la fase de |1⟩ a -|1⟩",
        "gate_s_desc": "Desplazamiento de fase π/2: añade fase i a |1⟩",
        "gate_t_desc": "Desplazamiento de fase π/4: importante para computación universal",
        
        # Language selector
        "language_label": "🌐 Idioma:",
    },
    
    "中文": {
        "lang_code": "zh",
        "flag": "🇨🇳",
        
        # Page config
        "page_title": "量子计算模拟",
        
        # Main title
        "main_title": " 交互式量子计算模拟",
        
        # Introduction section
        "intro_header": "ℹ️ 什么是量子计算？",
        "intro_title": "### ⚛️ 量子计算简介",
        "intro_content": """
**量子计算**是一种利用量子力学现象如**叠加**和**纠缠**的计算范式。

#### 🔹 量子比特（Qubit）
与经典比特（0或1）不同，**量子比特**可以处于两种状态的**叠加**：
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1（归一化）

#### 🔹 量子门
**量子门**是操控量子比特状态的操作，类似于经典逻辑门，但具有**可逆性**和**幺正性**。

#### 🔹 测量
测量时，量子比特会**坍缩**到基态（|0⟩ 或 |1⟩）之一，概率分别为|α|² 和 |β|²。
""",
        
        # Sidebar
        "sidebar_settings": "⚙️ 模拟设置",
        "num_qubits_label": "量子比特数量：",
        "num_qubits_help": "选择量子系统的量子比特数量（1-{max_qubits}个量子比特）",
        "add_gate_header": "🎛️ 添加量子门",
        "select_gate": "选择门：",
        "select_gate_help": "选择要应用的量子门",
        "target_qubit": "目标量子比特：",
        "target_qubit_help": "将接收门操作的量子比特",
        "apply_gate_btn": "➕ 应用门",
        "gate_applied_success": "✅ {gate_name} 已应用于 Q{target}",
        
        # CNOT section
        "cnot_header": "🔗 CNOT门（2量子比特）",
        "control_label": "控制：",
        "target_label": "目标：",
        "cnot_info": "🔗 **CNOT**：当控制量子比特 = |1⟩ 时翻转目标量子比特",
        "apply_cnot_btn": "➕ 应用CNOT",
        "cnot_applied_success": "✅ CNOT已应用（控制：Q{control}，目标：Q{target}）",
        
        # Reset
        "reset_btn": "🔄 重置系统",
        "reset_warning": "⚠️ 系统已重置为 |0...0⟩",
        
        # Main area
        "state_vector_header": " 状态向量可视化",
        "save_state_vector_btn": "💾 保存状态向量图",
        "measurement_header": " 测量模拟",
        "shots_label": "测量次数：",
        "save_measurement_btn": "💾 保存测量直方图",
        
        # State info
        "state_info_header": " 状态信息",
        "current_state": "#### 📍 当前状态：",
        "circuit_history": "#### 🔧 电路历史：",
        "no_gates_applied": "尚未应用任何门",
        "show_matrix": "📐 显示门矩阵",
        "matrix_title": "矩阵",
        
        # Plot labels
        "basis_state_label": "基态 |x⟩",
        "probability_label": "概率 P(x)",
        "probability_dist_title": "📊 测量概率分布",
        "amplitude_label": "振幅",
        "amplitude_title": "🌊 复数振幅状态向量",
        "real_label": "实部",
        "imaginary_label": "虚部",
        "measurement_result_label": "测量结果",
        "frequency_label": "频率（共{shots}次测量）",
        "histogram_title": "测量直方图（{shots}次测量）",
        
        # Footer
        "footer": "⚛️ 由Rasidi使用Streamlit和NumPy创建 | 量子计算模拟器 v2.0",
        
        # Gate descriptions
        "gate_hadamard_desc": "创建叠加：将 |0⟩ → (|0⟩ + |1⟩)/√2 和 |1⟩ → (|0⟩ - |1⟩)/√2",
        "gate_pauli_x_desc": "比特翻转：交换 |0⟩ ↔ |1⟩（类似经典NOT门）",
        "gate_pauli_y_desc": "在布洛赫球Y轴上旋转π弧度",
        "gate_pauli_z_desc": "相位翻转：将 |1⟩ 的相位变为 -|1⟩",
        "gate_s_desc": "相位偏移π/2：为 |1⟩ 添加相位i",
        "gate_t_desc": "相位偏移π/4：对通用计算很重要",
        
        # Language selector
        "language_label": "🌐 语言：",
    },

    "العربية": {
        "lang_code": "ar",
        "flag": "🇸🇦",
        "page_title": "محاكاة الحوسبة الكمية",
        "main_title": " محاكاة الحوسبة الكمية التفاعلية",
        "intro_header": "ℹ️ ما هي الحوسبة الكمية؟",
        "intro_title": "### ⚛️ مقدمة في الحوسبة الكمية",
        "intro_content": """
**الحوسبة الكمية** هي نموذج حوسبة يستخدم ظواهر ميكانيكا الكم مثل **التراكب** و**التشابك**.

#### 🔹 البت الكمي (Qubit)
على عكس البتات الكلاسيكية (0 أو 1)، يمكن أن يكون **البت الكمي** في **تراكب** من كلتا الحالتين:
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1 (التطبيع)

#### 🔹 البوابات الكمية
**البوابات الكمية** هي عمليات تتحكم في حالات البتات الكمية، مشابهة للبوابات المنطقية الكلاسيكية لكنها **عكوسة** و**أحادية**.

#### 🔹 القياس
عند القياس، **ينهار** البت الكمي إلى إحدى حالات الأساس (|0⟩ أو |1⟩) باحتمالات |α|² و|β|².
""",
        "sidebar_settings": "⚙️ إعدادات المحاكاة",
        "num_qubits_label": "عدد البتات الكمية:",
        "num_qubits_help": "اختر عدد البتات الكمية للنظام الكمي (1-{max_qubits} بتات كمية)",
        "add_gate_header": "🎛️ إضافة بوابة كمية",
        "select_gate": "اختر البوابة:",
        "select_gate_help": "اختر البوابة الكمية المراد تطبيقها",
        "target_qubit": "البت الكمي المستهدف:",
        "target_qubit_help": "البت الكمي الذي سيستقبل البوابة",
        "apply_gate_btn": "➕ تطبيق البوابة",
        "gate_applied_success": "✅ {gate_name} تم تطبيقه على Q{target}",
        "cnot_header": "🔗 بوابة CNOT (2-بت كمي)",
        "control_label": "التحكم:",
        "target_label": "الهدف:",
        "cnot_info": "🔗 **CNOT**: قلب البت الكمي المستهدف إذا كان بت التحكم = |1⟩",
        "apply_cnot_btn": "➕ تطبيق CNOT",
        "cnot_applied_success": "✅ تم تطبيق CNOT (تحكم: Q{control}، هدف: Q{target})",
        "reset_btn": "🔄 إعادة تعيين النظام",
        "reset_warning": "⚠️ تم إعادة تعيين النظام إلى |0...0⟩",
        "state_vector_header": " تصور متجه الحالة",
        "save_state_vector_btn": "💾 حفظ رسم متجه الحالة",
        "measurement_header": " محاكاة القياس",
        "shots_label": "عدد الطلقات:",
        "save_measurement_btn": "💾 حفظ مخطط القياس",
        "state_info_header": " معلومات الحالة",
        "current_state": "#### 📍 الحالة الحالية:",
        "circuit_history": "#### 🔧 سجل الدائرة:",
        "no_gates_applied": "لم يتم تطبيق أي بوابات بعد",
        "show_matrix": "📐 عرض مصفوفة البوابة",
        "matrix_title": "المصفوفة",
        "basis_state_label": "حالة الأساس |x⟩",
        "probability_label": "الاحتمال P(x)",
        "probability_dist_title": "📊 توزيع احتمالات القياس",
        "amplitude_label": "السعة",
        "amplitude_title": "🌊 متجه حالة السعة المركبة",
        "real_label": "حقيقي",
        "imaginary_label": "تخيلي",
        "measurement_result_label": "نتيجة القياس",
        "frequency_label": "التردد (من {shots} طلقة)",
        "histogram_title": "مخطط القياس ({shots} طلقة)",
        "footer": "⚛️ تم الإنشاء بواسطة Rasidi باستخدام Streamlit و NumPy | محاكي الحوسبة الكمية v2.0",
        "gate_hadamard_desc": "ينشئ تراكبًا: يحول |0⟩ → (|0⟩ + |1⟩)/√2 و|1⟩ → (|0⟩ - |1⟩)/√2",
        "gate_pauli_x_desc": "قلب البت: يبدل |0⟩ ↔ |1⟩ (مثل بوابة NOT الكلاسيكية)",
        "gate_pauli_y_desc": "دوران π راديان على محور Y في كرة بلوخ",
        "gate_pauli_z_desc": "قلب الطور: يغير طور |1⟩ إلى -|1⟩",
        "gate_s_desc": "إزاحة الطور π/2: يضيف الطور i إلى |1⟩",
        "gate_t_desc": "إزاحة الطور π/4: مهم للحوسبة الشاملة",
        "language_label": "🌐 اللغة:",
    },

    "Français": {
        "lang_code": "fr",
        "flag": "🇫🇷",
        "page_title": "Simulation d'Informatique Quantique",
        "main_title": " Simulation Interactive d'Informatique Quantique",
        "intro_header": "ℹ️ Qu'est-ce que l'Informatique Quantique ?",
        "intro_title": "### ⚛️ Introduction à l'Informatique Quantique",
        "intro_content": """
**L'informatique quantique** est un paradigme de calcul qui utilise des phénomènes de mécanique quantique tels que la **superposition** et l'**intrication**.

#### 🔹 Qubit (Bit Quantique)
Contrairement aux bits classiques (0 ou 1), les **qubits** peuvent exister en **superposition** des deux états :
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1 (normalisation)

#### 🔹 Portes Quantiques
Les **portes quantiques** sont des opérations qui manipulent les états des qubits, analogues aux portes logiques classiques mais **réversibles** et **unitaires**.

#### 🔹 Mesure
Lors de la mesure, un qubit **s'effondre** vers l'un des états de base (|0⟩ ou |1⟩) avec des probabilités |α|² et |β|².
""",
        "sidebar_settings": "⚙️ Paramètres de Simulation",
        "num_qubits_label": "Nombre de Qubits :",
        "num_qubits_help": "Sélectionnez le nombre de qubits pour le système quantique (1-{max_qubits} qubits)",
        "add_gate_header": "🎛️ Ajouter une Porte Quantique",
        "select_gate": "Sélectionner la Porte :",
        "select_gate_help": "Sélectionnez la porte quantique à appliquer",
        "target_qubit": "Qubit Cible :",
        "target_qubit_help": "Qubit qui recevra la porte",
        "apply_gate_btn": "➕ Appliquer la Porte",
        "gate_applied_success": "✅ {gate_name} appliqué à Q{target}",
        "cnot_header": "🔗 Porte CNOT (2-Qubit)",
        "control_label": "Contrôle :",
        "target_label": "Cible :",
        "cnot_info": "🔗 **CNOT** : Inverse le qubit cible si le qubit de contrôle = |1⟩",
        "apply_cnot_btn": "➕ Appliquer CNOT",
        "cnot_applied_success": "✅ CNOT appliqué (C : Q{control}, T : Q{target})",
        "reset_btn": "🔄 Réinitialiser le Système",
        "reset_warning": "⚠️ Système réinitialisé à |0...0⟩",
        "state_vector_header": " Visualisation du Vecteur d'État",
        "save_state_vector_btn": "💾 Enregistrer le Graphique du Vecteur d'État",
        "measurement_header": " Simulation de Mesure",
        "shots_label": "Nombre de Tirs :",
        "save_measurement_btn": "💾 Enregistrer l'Histogramme de Mesure",
        "state_info_header": " Informations sur l'État",
        "current_state": "#### 📍 État Actuel :",
        "circuit_history": "#### 🔧 Historique du Circuit :",
        "no_gates_applied": "Aucune porte appliquée pour le moment",
        "show_matrix": "📐 Afficher la Matrice de la Porte",
        "matrix_title": "Matrice",
        "basis_state_label": "État de Base |x⟩",
        "probability_label": "Probabilité P(x)",
        "probability_dist_title": "📊 Distribution de Probabilité de Mesure",
        "amplitude_label": "Amplitude",
        "amplitude_title": "🌊 Vecteur d'État d'Amplitude Complexe",
        "real_label": "Réel",
        "imaginary_label": "Imaginaire",
        "measurement_result_label": "Résultat de Mesure",
        "frequency_label": "Fréquence ({shots} tirs)",
        "histogram_title": "Histogramme de Mesure ({shots} Tirs)",
        "footer": "⚛️ Créé avec Rasidi en utilisant Streamlit & NumPy | Quantum Computing Simulator v2.0",
        "gate_hadamard_desc": "Crée une superposition : transforme |0⟩ → (|0⟩ + |1⟩)/√2 et |1⟩ → (|0⟩ - |1⟩)/√2",
        "gate_pauli_x_desc": "Inversion de bit : échange |0⟩ ↔ |1⟩ (comme la porte NOT classique)",
        "gate_pauli_y_desc": "Rotation de π radians sur l'axe Y de la sphère de Bloch",
        "gate_pauli_z_desc": "Inversion de phase : change la phase de |1⟩ en -|1⟩",
        "gate_s_desc": "Décalage de phase π/2 : ajoute la phase i à |1⟩",
        "gate_t_desc": "Décalage de phase π/4 : important pour le calcul universel",
        "language_label": "🌐 Langue :",
    },

    "日本語": {
        "lang_code": "ja",
        "flag": "🇯🇵",
        "page_title": "量子コンピューティングシミュレーション",
        "main_title": " インタラクティブ量子コンピューティングシミュレーション",
        "intro_header": "ℹ️ 量子コンピューティングとは？",
        "intro_title": "### ⚛️ 量子コンピューティング入門",
        "intro_content": """
**量子コンピューティング**は、**重ね合わせ**や**量子もつれ**などの量子力学現象を利用する計算パラダイムです。

#### 🔹 量子ビット（Qubit）
古典ビット（0または1）とは異なり、**量子ビット**は両方の状態の**重ね合わせ**に存在できます：
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1（正規化）

#### 🔹 量子ゲート
**量子ゲート**は量子ビットの状態を操作する演算で、古典論理ゲートに類似していますが、**可逆的**で**ユニタリ**です。

#### 🔹 測定
測定時、量子ビットは基底状態（|0⟩または|1⟩）の一つに**崩壊**し、その確率は|α|²と|β|²です。
""",
        "sidebar_settings": "⚙️ シミュレーション設定",
        "num_qubits_label": "量子ビット数：",
        "num_qubits_help": "量子システムの量子ビット数を選択（1-{max_qubits}量子ビット）",
        "add_gate_header": "🎛️ 量子ゲートを追加",
        "select_gate": "ゲートを選択：",
        "select_gate_help": "適用する量子ゲートを選択",
        "target_qubit": "ターゲット量子ビット：",
        "target_qubit_help": "ゲートを受ける量子ビット",
        "apply_gate_btn": "➕ ゲートを適用",
        "gate_applied_success": "✅ {gate_name} が Q{target} に適用されました",
        "cnot_header": "🔗 CNOTゲート（2量子ビット）",
        "control_label": "制御：",
        "target_label": "ターゲット：",
        "cnot_info": "🔗 **CNOT**：制御量子ビット = |1⟩ の場合、ターゲット量子ビットを反転",
        "apply_cnot_btn": "➕ CNOTを適用",
        "cnot_applied_success": "✅ CNOTが適用されました（制御：Q{control}、ターゲット：Q{target}）",
        "reset_btn": "🔄 システムをリセット",
        "reset_warning": "⚠️ システムが |0...0⟩ にリセットされました",
        "state_vector_header": " 状態ベクトルの可視化",
        "save_state_vector_btn": "💾 状態ベクトルグラフを保存",
        "measurement_header": " 測定シミュレーション",
        "shots_label": "ショット数：",
        "save_measurement_btn": "💾 測定ヒストグラムを保存",
        "state_info_header": " 状態情報",
        "current_state": "#### 📍 現在の状態：",
        "circuit_history": "#### 🔧 回路の履歴：",
        "no_gates_applied": "まだゲートが適用されていません",
        "show_matrix": "📐 ゲート行列を表示",
        "matrix_title": "行列",
        "basis_state_label": "基底状態 |x⟩",
        "probability_label": "確率 P(x)",
        "probability_dist_title": "📊 測定確率分布",
        "amplitude_label": "振幅",
        "amplitude_title": "🌊 複素振幅状態ベクトル",
        "real_label": "実部",
        "imaginary_label": "虚部",
        "measurement_result_label": "測定結果",
        "frequency_label": "頻度（{shots}ショット）",
        "histogram_title": "測定ヒストグラム（{shots}ショット）",
        "footer": "⚛️ RasidiによりStreamlitとNumPyを使用して作成 | 量子コンピューティングシミュレーター v2.0",
        "gate_hadamard_desc": "重ね合わせを作成：|0⟩ → (|0⟩ + |1⟩)/√2 および |1⟩ → (|0⟩ - |1⟩)/√2 に変換",
        "gate_pauli_x_desc": "ビット反転：|0⟩ ↔ |1⟩ を交換（古典NOTゲートと同様）",
        "gate_pauli_y_desc": "ブロッホ球のY軸上でπラジアン回転",
        "gate_pauli_z_desc": "位相反転：|1⟩ の位相を -|1⟩ に変更",
        "gate_s_desc": "位相シフトπ/2：|1⟩ に位相iを追加",
        "gate_t_desc": "位相シフトπ/4：ユニバーサル計算に重要",
        "language_label": "🌐 言語：",
    },

    "한국어": {
        "lang_code": "ko",
        "flag": "🇰🇷",
        "page_title": "양자 컴퓨팅 시뮬레이션",
        "main_title": " 인터랙티브 양자 컴퓨팅 시뮬레이션",
        "intro_header": "ℹ️ 양자 컴퓨팅이란?",
        "intro_title": "### ⚛️ 양자 컴퓨팅 소개",
        "intro_content": """
**양자 컴퓨팅**은 **중첩**과 **얽힘** 같은 양자 역학 현상을 활용하는 컴퓨팅 패러다임입니다.

#### 🔹 큐비트 (양자 비트)
고전 비트(0 또는 1)와 달리, **큐비트**는 두 상태의 **중첩**에 존재할 수 있습니다:
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1 (정규화)

#### 🔹 양자 게이트
**양자 게이트**는 큐비트 상태를 조작하는 연산으로, 고전 논리 게이트와 유사하지만 **가역적**이고 **유니터리**합니다.

#### 🔹 측정
측정 시, 큐비트는 기저 상태(|0⟩ 또는 |1⟩) 중 하나로 **붕괴**하며, 확률은 |α|²과 |β|²입니다.
""",
        "sidebar_settings": "⚙️ 시뮬레이션 설정",
        "num_qubits_label": "큐비트 수:",
        "num_qubits_help": "양자 시스템의 큐비트 수를 선택하세요 (1-{max_qubits} 큐비트)",
        "add_gate_header": "🎛️ 양자 게이트 추가",
        "select_gate": "게이트 선택:",
        "select_gate_help": "적용할 양자 게이트를 선택하세요",
        "target_qubit": "타겟 큐비트:",
        "target_qubit_help": "게이트를 받을 큐비트",
        "apply_gate_btn": "➕ 게이트 적용",
        "gate_applied_success": "✅ {gate_name}이(가) Q{target}에 적용되었습니다",
        "cnot_header": "🔗 CNOT 게이트 (2-큐비트)",
        "control_label": "제어:",
        "target_label": "타겟:",
        "cnot_info": "🔗 **CNOT**: 제어 큐비트 = |1⟩일 때 타겟 큐비트를 반전",
        "apply_cnot_btn": "➕ CNOT 적용",
        "cnot_applied_success": "✅ CNOT 적용됨 (제어: Q{control}, 타겟: Q{target})",
        "reset_btn": "🔄 시스템 초기화",
        "reset_warning": "⚠️ 시스템이 |0...0⟩으로 초기화되었습니다",
        "state_vector_header": " 상태 벡터 시각화",
        "save_state_vector_btn": "💾 상태 벡터 그래프 저장",
        "measurement_header": " 측정 시뮬레이션",
        "shots_label": "측정 횟수:",
        "save_measurement_btn": "💾 측정 히스토그램 저장",
        "state_info_header": " 상태 정보",
        "current_state": "#### 📍 현재 상태:",
        "circuit_history": "#### 🔧 회로 기록:",
        "no_gates_applied": "아직 적용된 게이트가 없습니다",
        "show_matrix": "📐 게이트 행렬 표시",
        "matrix_title": "행렬",
        "basis_state_label": "기저 상태 |x⟩",
        "probability_label": "확률 P(x)",
        "probability_dist_title": "📊 측정 확률 분포",
        "amplitude_label": "진폭",
        "amplitude_title": "🌊 복소 진폭 상태 벡터",
        "real_label": "실수부",
        "imaginary_label": "허수부",
        "measurement_result_label": "측정 결과",
        "frequency_label": "빈도 ({shots}회 측정)",
        "histogram_title": "측정 히스토그램 ({shots}회 측정)",
        "footer": "⚛️ Rasidi가 Streamlit & NumPy를 사용하여 제작 | 양자 컴퓨팅 시뮬레이터 v2.0",
        "gate_hadamard_desc": "중첩 생성: |0⟩ → (|0⟩ + |1⟩)/√2 및 |1⟩ → (|0⟩ - |1⟩)/√2로 변환",
        "gate_pauli_x_desc": "비트 반전: |0⟩ ↔ |1⟩ 교환 (고전 NOT 게이트와 유사)",
        "gate_pauli_y_desc": "블로흐 구의 Y축에서 π 라디안 회전",
        "gate_pauli_z_desc": "위상 반전: |1⟩의 위상을 -|1⟩로 변경",
        "gate_s_desc": "위상 이동 π/2: |1⟩에 위상 i 추가",
        "gate_t_desc": "위상 이동 π/4: 범용 계산에 중요",
        "language_label": "🌐 언어:",
    },

    "Deutsch": {
        "lang_code": "de",
        "flag": "🇩🇪",
        "page_title": "Quantencomputing-Simulation",
        "main_title": " Interaktive Quantencomputing-Simulation",
        "intro_header": "ℹ️ Was ist Quantencomputing?",
        "intro_title": "### ⚛️ Einführung in das Quantencomputing",
        "intro_content": """
**Quantencomputing** ist ein Rechenparadigma, das quantenmechanische Phänomene wie **Superposition** und **Verschränkung** nutzt.

#### 🔹 Qubit (Quantenbit)
Im Gegensatz zu klassischen Bits (0 oder 1) können **Qubits** in einer **Superposition** beider Zustände existieren:
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1 (Normalisierung)

#### 🔹 Quantengatter
**Quantengatter** sind Operationen, die Qubit-Zustände manipulieren, analog zu klassischen Logikgattern, aber **reversibel** und **unitär**.

#### 🔹 Messung
Bei der Messung **kollabiert** ein Qubit in einen der Basiszustände (|0⟩ oder |1⟩) mit den Wahrscheinlichkeiten |α|² und |β|².
""",
        "sidebar_settings": "⚙️ Simulationseinstellungen",
        "num_qubits_label": "Anzahl der Qubits:",
        "num_qubits_help": "Wählen Sie die Anzahl der Qubits für das Quantensystem (1-{max_qubits} Qubits)",
        "add_gate_header": "🎛️ Quantengatter hinzufügen",
        "select_gate": "Gatter auswählen:",
        "select_gate_help": "Wählen Sie das anzuwendende Quantengatter",
        "target_qubit": "Ziel-Qubit:",
        "target_qubit_help": "Qubit, das das Gatter empfängt",
        "apply_gate_btn": "➕ Gatter anwenden",
        "gate_applied_success": "✅ {gate_name} auf Q{target} angewendet",
        "cnot_header": "🔗 CNOT-Gatter (2-Qubit)",
        "control_label": "Steuerung:",
        "target_label": "Ziel:",
        "cnot_info": "🔗 **CNOT**: Ziel-Qubit umkehren, wenn Steuer-Qubit = |1⟩",
        "apply_cnot_btn": "➕ CNOT anwenden",
        "cnot_applied_success": "✅ CNOT angewendet (S: Q{control}, Z: Q{target})",
        "reset_btn": "🔄 System zurücksetzen",
        "reset_warning": "⚠️ System auf |0...0⟩ zurückgesetzt",
        "state_vector_header": " Zustandsvektor-Visualisierung",
        "save_state_vector_btn": "💾 Zustandsvektor-Graph speichern",
        "measurement_header": " Messsimulation",
        "shots_label": "Anzahl der Schüsse:",
        "save_measurement_btn": "💾 Messhistogramm speichern",
        "state_info_header": " Zustandsinformationen",
        "current_state": "#### 📍 Aktueller Zustand:",
        "circuit_history": "#### 🔧 Schaltkreis-Verlauf:",
        "no_gates_applied": "Noch keine Gatter angewendet",
        "show_matrix": "📐 Gattermatrix anzeigen",
        "matrix_title": "Matrix",
        "basis_state_label": "Basiszustand |x⟩",
        "probability_label": "Wahrscheinlichkeit P(x)",
        "probability_dist_title": "📊 Messwahrscheinlichkeitsverteilung",
        "amplitude_label": "Amplitude",
        "amplitude_title": "🌊 Komplexer Amplituden-Zustandsvektor",
        "real_label": "Realteil",
        "imaginary_label": "Imaginärteil",
        "measurement_result_label": "Messergebnis",
        "frequency_label": "Häufigkeit ({shots} Schüsse)",
        "histogram_title": "Messhistogramm ({shots} Schüsse)",
        "footer": "⚛️ Erstellt mit Rasidi unter Verwendung von Streamlit & NumPy | Quantum Computing Simulator v2.0",
        "gate_hadamard_desc": "Erzeugt Superposition: transformiert |0⟩ → (|0⟩ + |1⟩)/√2 und |1⟩ → (|0⟩ - |1⟩)/√2",
        "gate_pauli_x_desc": "Bit-Umkehrung: tauscht |0⟩ ↔ |1⟩ (wie klassisches NOT-Gatter)",
        "gate_pauli_y_desc": "Rotation um π Radiant auf der Y-Achse der Bloch-Kugel",
        "gate_pauli_z_desc": "Phasenumkehrung: ändert die Phase von |1⟩ zu -|1⟩",
        "gate_s_desc": "Phasenverschiebung π/2: fügt Phase i zu |1⟩ hinzu",
        "gate_t_desc": "Phasenverschiebung π/4: wichtig für universelle Berechnung",
        "language_label": "🌐 Sprache:",
    },

    "Português": {
        "lang_code": "pt",
        "flag": "🇧🇷",
        "page_title": "Simulação de Computação Quântica",
        "main_title": " Simulação Interativa de Computação Quântica",
        "intro_header": "ℹ️ O que é Computação Quântica?",
        "intro_title": "### ⚛️ Introdução à Computação Quântica",
        "intro_content": """
**Computação Quântica** é um paradigma de computação que utiliza fenômenos da mecânica quântica como **superposição** e **emaranhamento**.

#### 🔹 Qubit (Bit Quântico)
Diferente dos bits clássicos (0 ou 1), os **qubits** podem existir em **superposição** de ambos os estados:
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1 (normalização)

#### 🔹 Portas Quânticas
**Portas quânticas** são operações que manipulam estados de qubits, análogas às portas lógicas clássicas, mas **reversíveis** e **unitárias**.

#### 🔹 Medição
Quando medido, um qubit **colapsa** para um dos estados base (|0⟩ ou |1⟩) com probabilidades |α|² e |β|².
""",
        "sidebar_settings": "⚙️ Configurações de Simulação",
        "num_qubits_label": "Número de Qubits:",
        "num_qubits_help": "Selecione o número de qubits para o sistema quântico (1-{max_qubits} qubits)",
        "add_gate_header": "🎛️ Adicionar Porta Quântica",
        "select_gate": "Selecionar Porta:",
        "select_gate_help": "Selecione a porta quântica a ser aplicada",
        "target_qubit": "Qubit Alvo:",
        "target_qubit_help": "Qubit que receberá a porta",
        "apply_gate_btn": "➕ Aplicar Porta",
        "gate_applied_success": "✅ {gate_name} aplicado a Q{target}",
        "cnot_header": "🔗 Porta CNOT (2-Qubit)",
        "control_label": "Controle:",
        "target_label": "Alvo:",
        "cnot_info": "🔗 **CNOT**: Inverte o qubit alvo se o qubit de controle = |1⟩",
        "apply_cnot_btn": "➕ Aplicar CNOT",
        "cnot_applied_success": "✅ CNOT aplicado (C: Q{control}, A: Q{target})",
        "reset_btn": "🔄 Reiniciar Sistema",
        "reset_warning": "⚠️ Sistema reiniciado para |0...0⟩",
        "state_vector_header": " Visualização do Vetor de Estado",
        "save_state_vector_btn": "💾 Salvar Gráfico do Vetor de Estado",
        "measurement_header": " Simulação de Medição",
        "shots_label": "Número de Disparos:",
        "save_measurement_btn": "💾 Salvar Histograma de Medição",
        "state_info_header": " Informações do Estado",
        "current_state": "#### 📍 Estado Atual:",
        "circuit_history": "#### 🔧 Histórico do Circuito:",
        "no_gates_applied": "Nenhuma porta aplicada ainda",
        "show_matrix": "📐 Mostrar Matriz da Porta",
        "matrix_title": "Matriz",
        "basis_state_label": "Estado Base |x⟩",
        "probability_label": "Probabilidade P(x)",
        "probability_dist_title": "📊 Distribuição de Probabilidade de Medição",
        "amplitude_label": "Amplitude",
        "amplitude_title": "🌊 Vetor de Estado de Amplitude Complexa",
        "real_label": "Real",
        "imaginary_label": "Imaginário",
        "measurement_result_label": "Resultado da Medição",
        "frequency_label": "Frequência ({shots} disparos)",
        "histogram_title": "Histograma de Medição ({shots} Disparos)",
        "footer": "⚛️ Criado com Rasidi usando Streamlit & NumPy | Quantum Computing Simulator v2.0",
        "gate_hadamard_desc": "Cria superposição: transforma |0⟩ → (|0⟩ + |1⟩)/√2 e |1⟩ → (|0⟩ - |1⟩)/√2",
        "gate_pauli_x_desc": "Inversão de bit: troca |0⟩ ↔ |1⟩ (como porta NOT clássica)",
        "gate_pauli_y_desc": "Rotação de π radianos no eixo Y da esfera de Bloch",
        "gate_pauli_z_desc": "Inversão de fase: muda a fase de |1⟩ para -|1⟩",
        "gate_s_desc": "Deslocamento de fase π/2: adiciona fase i a |1⟩",
        "gate_t_desc": "Deslocamento de fase π/4: importante para computação universal",
        "language_label": "🌐 Idioma:",
    },

    "Русский": {
        "lang_code": "ru",
        "flag": "🇷🇺",
        "page_title": "Симуляция квантовых вычислений",
        "main_title": " Интерактивная симуляция квантовых вычислений",
        "intro_header": "ℹ️ Что такое квантовые вычисления?",
        "intro_title": "### ⚛️ Введение в квантовые вычисления",
        "intro_content": """
**Квантовые вычисления** — это парадигма вычислений, использующая явления квантовой механики, такие как **суперпозиция** и **запутанность**.

#### 🔹 Кубит (Квантовый бит)
В отличие от классических битов (0 или 1), **кубиты** могут находиться в **суперпозиции** обоих состояний:
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1 (нормализация)

#### 🔹 Квантовые вентили
**Квантовые вентили** — это операции, манипулирующие состояниями кубитов, аналогичные классическим логическим элементам, но **обратимые** и **унитарные**.

#### 🔹 Измерение
При измерении кубит **коллапсирует** в одно из базисных состояний (|0⟩ или |1⟩) с вероятностями |α|² и |β|².
""",
        "sidebar_settings": "⚙️ Настройки симуляции",
        "num_qubits_label": "Количество кубитов:",
        "num_qubits_help": "Выберите количество кубитов для квантовой системы (1-{max_qubits} кубита)",
        "add_gate_header": "🎛️ Добавить квантовый вентиль",
        "select_gate": "Выбрать вентиль:",
        "select_gate_help": "Выберите квантовый вентиль для применения",
        "target_qubit": "Целевой кубит:",
        "target_qubit_help": "Кубит, к которому будет применён вентиль",
        "apply_gate_btn": "➕ Применить вентиль",
        "gate_applied_success": "✅ {gate_name} применён к Q{target}",
        "cnot_header": "🔗 Вентиль CNOT (2-кубита)",
        "control_label": "Управление:",
        "target_label": "Цель:",
        "cnot_info": "🔗 **CNOT**: Инвертирует целевой кубит, если управляющий кубит = |1⟩",
        "apply_cnot_btn": "➕ Применить CNOT",
        "cnot_applied_success": "✅ CNOT применён (У: Q{control}, Ц: Q{target})",
        "reset_btn": "🔄 Сбросить систему",
        "reset_warning": "⚠️ Система сброшена в |0...0⟩",
        "state_vector_header": " Визуализация вектора состояния",
        "save_state_vector_btn": "💾 Сохранить график вектора состояния",
        "measurement_header": " Симуляция измерения",
        "shots_label": "Количество выстрелов:",
        "save_measurement_btn": "💾 Сохранить гистограмму измерений",
        "state_info_header": " Информация о состоянии",
        "current_state": "#### 📍 Текущее состояние:",
        "circuit_history": "#### 🔧 История схемы:",
        "no_gates_applied": "Вентили ещё не применены",
        "show_matrix": "📐 Показать матрицу вентиля",
        "matrix_title": "Матрица",
        "basis_state_label": "Базисное состояние |x⟩",
        "probability_label": "Вероятность P(x)",
        "probability_dist_title": "📊 Распределение вероятностей измерения",
        "amplitude_label": "Амплитуда",
        "amplitude_title": "🌊 Комплексный амплитудный вектор состояния",
        "real_label": "Действительная часть",
        "imaginary_label": "Мнимая часть",
        "measurement_result_label": "Результат измерения",
        "frequency_label": "Частота ({shots} выстрелов)",
        "histogram_title": "Гистограмма измерений ({shots} выстрелов)",
        "footer": "⚛️ Создано Rasidi с использованием Streamlit & NumPy | Quantum Computing Simulator v2.0",
        "gate_hadamard_desc": "Создаёт суперпозицию: преобразует |0⟩ → (|0⟩ + |1⟩)/√2 и |1⟩ → (|0⟩ - |1⟩)/√2",
        "gate_pauli_x_desc": "Инверсия бита: меняет |0⟩ ↔ |1⟩ (как классический элемент NOT)",
        "gate_pauli_y_desc": "Вращение на π радиан по оси Y сферы Блоха",
        "gate_pauli_z_desc": "Инверсия фазы: изменяет фазу |1⟩ на -|1⟩",
        "gate_s_desc": "Сдвиг фазы π/2: добавляет фазу i к |1⟩",
        "gate_t_desc": "Сдвиг фазы π/4: важен для универсальных вычислений",
        "language_label": "🌐 Язык:",
    },

    "हिन्दी": {
        "lang_code": "hi",
        "flag": "🇮🇳",
        "page_title": "क्वांटम कंप्यूटिंग सिमुलेशन",
        "main_title": " इंटरएक्टिव क्वांटम कंप्यूटिंग सिमुलेशन",
        "intro_header": "ℹ️ क्वांटम कंप्यूटिंग क्या है?",
        "intro_title": "### ⚛️ क्वांटम कंप्यूटिंग का परिचय",
        "intro_content": """
**क्वांटम कंप्यूटिंग** एक कंप्यूटिंग प्रतिमान है जो **सुपरपोजिशन** और **एंटैंगलमेंट** जैसी क्वांटम यांत्रिकी घटनाओं का उपयोग करता है।

#### 🔹 क्यूबिट (क्वांटम बिट)
शास्त्रीय बिट्स (0 या 1) के विपरीत, **क्यूबिट** दोनों अवस्थाओं के **सुपरपोजिशन** में मौजूद हो सकते हैं:
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1 (सामान्यीकरण)

#### 🔹 क्वांटम गेट
**क्वांटम गेट** ऐसी संक्रियाएँ हैं जो क्यूबिट अवस्थाओं को संशोधित करती हैं, शास्त्रीय लॉजिक गेट के समान लेकिन **प्रतिवर्ती** और **एकात्मक** हैं।

#### 🔹 मापन
मापने पर, एक क्यूबिट आधार अवस्थाओं (|0⟩ या |1⟩) में से एक में **संकुचित** हो जाता है, जिसकी प्रायिकता |α|² और |β|² होती है।
""",
        "sidebar_settings": "⚙️ सिमुलेशन सेटिंग्स",
        "num_qubits_label": "क्यूबिट्स की संख्या:",
        "num_qubits_help": "क्वांटम सिस्टम के लिए क्यूबिट्स की संख्या चुनें (1-{max_qubits} क्यूबिट)",
        "add_gate_header": "🎛️ क्वांटम गेट जोड़ें",
        "select_gate": "गेट चुनें:",
        "select_gate_help": "लागू करने के लिए क्वांटम गेट चुनें",
        "target_qubit": "लक्ष्य क्यूबिट:",
        "target_qubit_help": "क्यूबिट जो गेट प्राप्त करेगा",
        "apply_gate_btn": "➕ गेट लागू करें",
        "gate_applied_success": "✅ {gate_name} Q{target} पर लागू किया गया",
        "cnot_header": "🔗 CNOT गेट (2-क्यूबिट)",
        "control_label": "नियंत्रण:",
        "target_label": "लक्ष्य:",
        "cnot_info": "🔗 **CNOT**: यदि नियंत्रण क्यूबिट = |1⟩ तो लक्ष्य क्यूबिट को पलटें",
        "apply_cnot_btn": "➕ CNOT लागू करें",
        "cnot_applied_success": "✅ CNOT लागू किया गया (नि: Q{control}, ल: Q{target})",
        "reset_btn": "🔄 सिस्टम रीसेट करें",
        "reset_warning": "⚠️ सिस्टम |0...0⟩ पर रीसेट किया गया",
        "state_vector_header": " स्टेट वेक्टर विज़ुअलाइज़ेशन",
        "save_state_vector_btn": "💾 स्टेट वेक्टर ग्राफ़ सहेजें",
        "measurement_header": " मापन सिमुलेशन",
        "shots_label": "शॉट्स की संख्या:",
        "save_measurement_btn": "💾 मापन हिस्टोग्राम सहेजें",
        "state_info_header": " स्टेट जानकारी",
        "current_state": "#### 📍 वर्तमान स्टेट:",
        "circuit_history": "#### 🔧 सर्किट इतिहास:",
        "no_gates_applied": "अभी तक कोई गेट लागू नहीं किया गया",
        "show_matrix": "📐 गेट मैट्रिक्स दिखाएँ",
        "matrix_title": "मैट्रिक्स",
        "basis_state_label": "आधार अवस्था |x⟩",
        "probability_label": "प्रायिकता P(x)",
        "probability_dist_title": "📊 मापन प्रायिकता वितरण",
        "amplitude_label": "आयाम",
        "amplitude_title": "🌊 सम्मिश्र आयाम स्टेट वेक्टर",
        "real_label": "वास्तविक",
        "imaginary_label": "काल्पनिक",
        "measurement_result_label": "मापन परिणाम",
        "frequency_label": "आवृत्ति ({shots} शॉट्स)",
        "histogram_title": "मापन हिस्टोग्राम ({shots} शॉट्स)",
        "footer": "⚛️ Rasidi द्वारा Streamlit और NumPy का उपयोग करके बनाया गया | Quantum Computing Simulator v2.0",
        "gate_hadamard_desc": "सुपरपोजिशन बनाता है: |0⟩ → (|0⟩ + |1⟩)/√2 और |1⟩ → (|0⟩ - |1⟩)/√2 में रूपांतरित करता है",
        "gate_pauli_x_desc": "बिट फ्लिप: |0⟩ ↔ |1⟩ को बदलता है (शास्त्रीय NOT गेट की तरह)",
        "gate_pauli_y_desc": "ब्लॉख गोले के Y अक्ष पर π रेडियन का घूर्णन",
        "gate_pauli_z_desc": "फेज़ फ्लिप: |1⟩ के फेज़ को -|1⟩ में बदलता है",
        "gate_s_desc": "फेज़ शिफ्ट π/2: |1⟩ में फेज़ i जोड़ता है",
        "gate_t_desc": "फेज़ शिफ्ट π/4: सार्वभौमिक गणना के लिए महत्वपूर्ण",
        "language_label": "🌐 भाषा:",
    },

    "Türkçe": {
        "lang_code": "tr",
        "flag": "🇹🇷",
        "page_title": "Kuantum Bilişim Simülasyonu",
        "main_title": " İnteraktif Kuantum Bilişim Simülasyonu",
        "intro_header": "ℹ️ Kuantum Bilişim Nedir?",
        "intro_title": "### ⚛️ Kuantum Bilişime Giriş",
        "intro_content": """
**Kuantum Bilişim**, **süperpozisyon** ve **dolanıklık** gibi kuantum mekanik olaylarını kullanan bir hesaplama paradigmasıdır.

#### 🔹 Kübit (Kuantum Bit)
Klasik bitlerden (0 veya 1) farklı olarak, **kübitler** her iki durumun **süperpozisyonunda** bulunabilir:
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1 (normalizasyon)

#### 🔹 Kuantum Kapıları
**Kuantum kapıları**, kübit durumlarını manipüle eden, klasik mantık kapılarına benzer ancak **terslenebilir** ve **üniter** işlemlerdir.

#### 🔹 Ölçüm
Ölçüldüğünde, bir kübit |α|² ve |β|² olasılıklarıyla temel durumlardan (|0⟩ veya |1⟩) birine **çöker**.
""",
        "sidebar_settings": "⚙️ Simülasyon Ayarları",
        "num_qubits_label": "Kübit Sayısı:",
        "num_qubits_help": "Kuantum sistemi için kübit sayısını seçin (1-{max_qubits} kübit)",
        "add_gate_header": "🎛️ Kuantum Kapısı Ekle",
        "select_gate": "Kapı Seçin:",
        "select_gate_help": "Uygulanacak kuantum kapısını seçin",
        "target_qubit": "Hedef Kübit:",
        "target_qubit_help": "Kapıyı alacak kübit",
        "apply_gate_btn": "➕ Kapıyı Uygula",
        "gate_applied_success": "✅ {gate_name} Q{target}'e uygulandı",
        "cnot_header": "🔗 CNOT Kapısı (2-Kübit)",
        "control_label": "Kontrol:",
        "target_label": "Hedef:",
        "cnot_info": "🔗 **CNOT**: Kontrol kübiti = |1⟩ ise hedef kübiti çevir",
        "apply_cnot_btn": "➕ CNOT Uygula",
        "cnot_applied_success": "✅ CNOT uygulandı (K: Q{control}, H: Q{target})",
        "reset_btn": "🔄 Sistemi Sıfırla",
        "reset_warning": "⚠️ Sistem |0...0⟩'a sıfırlandı",
        "state_vector_header": " Durum Vektörü Görselleştirmesi",
        "save_state_vector_btn": "💾 Durum Vektörü Grafiğini Kaydet",
        "measurement_header": " Ölçüm Simülasyonu",
        "shots_label": "Atış Sayısı:",
        "save_measurement_btn": "💾 Ölçüm Histogramını Kaydet",
        "state_info_header": " Durum Bilgisi",
        "current_state": "#### 📍 Mevcut Durum:",
        "circuit_history": "#### 🔧 Devre Geçmişi:",
        "no_gates_applied": "Henüz kapı uygulanmadı",
        "show_matrix": "📐 Kapı Matrisini Göster",
        "matrix_title": "Matris",
        "basis_state_label": "Temel Durum |x⟩",
        "probability_label": "Olasılık P(x)",
        "probability_dist_title": "📊 Ölçüm Olasılık Dağılımı",
        "amplitude_label": "Genlik",
        "amplitude_title": "🌊 Karmaşık Genlik Durum Vektörü",
        "real_label": "Gerçek",
        "imaginary_label": "Sanal",
        "measurement_result_label": "Ölçüm Sonucu",
        "frequency_label": "Frekans ({shots} atış)",
        "histogram_title": "Ölçüm Histogramı ({shots} Atış)",
        "footer": "⚛️ Rasidi tarafından Streamlit & NumPy kullanılarak oluşturuldu | Quantum Computing Simulator v2.0",
        "gate_hadamard_desc": "Süperpozisyon oluşturur: |0⟩ → (|0⟩ + |1⟩)/√2 ve |1⟩ → (|0⟩ - |1⟩)/√2'ye dönüştürür",
        "gate_pauli_x_desc": "Bit çevirme: |0⟩ ↔ |1⟩ değiştirir (klasik NOT kapısı gibi)",
        "gate_pauli_y_desc": "Bloch küresinin Y ekseni üzerinde π radyan döndürme",
        "gate_pauli_z_desc": "Faz çevirme: |1⟩'in fazını -|1⟩'e değiştirir",
        "gate_s_desc": "Faz kayması π/2: |1⟩'e i fazı ekler",
        "gate_t_desc": "Faz kayması π/4: evrensel hesaplama için önemli",
        "language_label": "🌐 Dil:",
    },

    "Italiano": {
        "lang_code": "it",
        "flag": "🇮🇹",
        "page_title": "Simulazione di Calcolo Quantistico",
        "main_title": " Simulazione Interattiva di Calcolo Quantistico",
        "intro_header": "ℹ️ Cos'è il Calcolo Quantistico?",
        "intro_title": "### ⚛️ Introduzione al Calcolo Quantistico",
        "intro_content": """
**Il Calcolo Quantistico** è un paradigma di calcolo che utilizza fenomeni della meccanica quantistica come la **sovrapposizione** e l'**entanglement**.

#### 🔹 Qubit (Bit Quantistico)
A differenza dei bit classici (0 o 1), i **qubit** possono esistere in **sovrapposizione** di entrambi gli stati:
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1 (normalizzazione)

#### 🔹 Porte Quantistiche
Le **porte quantistiche** sono operazioni che manipolano gli stati dei qubit, analoghe alle porte logiche classiche ma **reversibili** e **unitarie**.

#### 🔹 Misurazione
Quando misurato, un qubit **collassa** in uno degli stati base (|0⟩ o |1⟩) con probabilità |α|² e |β|².
""",
        "sidebar_settings": "⚙️ Impostazioni di Simulazione",
        "num_qubits_label": "Numero di Qubit:",
        "num_qubits_help": "Seleziona il numero di qubit per il sistema quantistico (1-{max_qubits} qubit)",
        "add_gate_header": "🎛️ Aggiungi Porta Quantistica",
        "select_gate": "Seleziona Porta:",
        "select_gate_help": "Seleziona la porta quantistica da applicare",
        "target_qubit": "Qubit Obiettivo:",
        "target_qubit_help": "Qubit che riceverà la porta",
        "apply_gate_btn": "➕ Applica Porta",
        "gate_applied_success": "✅ {gate_name} applicato a Q{target}",
        "cnot_header": "🔗 Porta CNOT (2-Qubit)",
        "control_label": "Controllo:",
        "target_label": "Obiettivo:",
        "cnot_info": "🔗 **CNOT**: Inverte il qubit obiettivo se il qubit di controllo = |1⟩",
        "apply_cnot_btn": "➕ Applica CNOT",
        "cnot_applied_success": "✅ CNOT applicato (C: Q{control}, O: Q{target})",
        "reset_btn": "🔄 Reimposta Sistema",
        "reset_warning": "⚠️ Sistema reimpostato a |0...0⟩",
        "state_vector_header": " Visualizzazione del Vettore di Stato",
        "save_state_vector_btn": "💾 Salva Grafico del Vettore di Stato",
        "measurement_header": " Simulazione di Misurazione",
        "shots_label": "Numero di Colpi:",
        "save_measurement_btn": "💾 Salva Istogramma di Misurazione",
        "state_info_header": " Informazioni sullo Stato",
        "current_state": "#### 📍 Stato Attuale:",
        "circuit_history": "#### 🔧 Cronologia del Circuito:",
        "no_gates_applied": "Nessuna porta applicata ancora",
        "show_matrix": "📐 Mostra Matrice della Porta",
        "matrix_title": "Matrice",
        "basis_state_label": "Stato Base |x⟩",
        "probability_label": "Probabilità P(x)",
        "probability_dist_title": "📊 Distribuzione di Probabilità di Misurazione",
        "amplitude_label": "Ampiezza",
        "amplitude_title": "🌊 Vettore di Stato ad Ampiezza Complessa",
        "real_label": "Reale",
        "imaginary_label": "Immaginario",
        "measurement_result_label": "Risultato della Misurazione",
        "frequency_label": "Frequenza ({shots} colpi)",
        "histogram_title": "Istogramma di Misurazione ({shots} Colpi)",
        "footer": "⚛️ Creato con Rasidi usando Streamlit & NumPy | Quantum Computing Simulator v2.0",
        "gate_hadamard_desc": "Crea sovrapposizione: trasforma |0⟩ → (|0⟩ + |1⟩)/√2 e |1⟩ → (|0⟩ - |1⟩)/√2",
        "gate_pauli_x_desc": "Inversione di bit: scambia |0⟩ ↔ |1⟩ (come porta NOT classica)",
        "gate_pauli_y_desc": "Rotazione di π radianti sull'asse Y della sfera di Bloch",
        "gate_pauli_z_desc": "Inversione di fase: cambia la fase di |1⟩ in -|1⟩",
        "gate_s_desc": "Spostamento di fase π/2: aggiunge fase i a |1⟩",
        "gate_t_desc": "Spostamento di fase π/4: importante per il calcolo universale",
        "language_label": "🌐 Lingua:",
    },

    "Tiếng Việt": {
        "lang_code": "vi",
        "flag": "🇻🇳",
        "page_title": "Mô phỏng Điện toán Lượng tử",
        "main_title": " Mô phỏng Điện toán Lượng tử Tương tác",
        "intro_header": "ℹ️ Điện toán Lượng tử là gì?",
        "intro_title": "### ⚛️ Giới thiệu về Điện toán Lượng tử",
        "intro_content": """
**Điện toán Lượng tử** là một mô hình tính toán sử dụng các hiện tượng cơ học lượng tử như **chồng chất** và **vướng víu lượng tử**.

#### 🔹 Qubit (Bit Lượng tử)
Khác với bit cổ điển (0 hoặc 1), **qubit** có thể tồn tại ở trạng thái **chồng chất** của cả hai:
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1 (chuẩn hóa)

#### 🔹 Cổng Lượng tử
**Cổng lượng tử** là các phép toán thao tác trên trạng thái qubit, tương tự cổng logic cổ điển nhưng **khả nghịch** và **đơn nhất**.

#### 🔹 Đo lường
Khi đo, một qubit **sụp đổ** về một trong các trạng thái cơ sở (|0⟩ hoặc |1⟩) với xác suất |α|² và |β|².
""",
        "sidebar_settings": "⚙️ Cài đặt Mô phỏng",
        "num_qubits_label": "Số lượng Qubit:",
        "num_qubits_help": "Chọn số lượng qubit cho hệ thống lượng tử (1-{max_qubits} qubit)",
        "add_gate_header": "🎛️ Thêm Cổng Lượng tử",
        "select_gate": "Chọn Cổng:",
        "select_gate_help": "Chọn cổng lượng tử để áp dụng",
        "target_qubit": "Qubit Mục tiêu:",
        "target_qubit_help": "Qubit sẽ nhận cổng",
        "apply_gate_btn": "➕ Áp dụng Cổng",
        "gate_applied_success": "✅ {gate_name} đã áp dụng cho Q{target}",
        "cnot_header": "🔗 Cổng CNOT (2-Qubit)",
        "control_label": "Điều khiển:",
        "target_label": "Mục tiêu:",
        "cnot_info": "🔗 **CNOT**: Đảo qubit mục tiêu nếu qubit điều khiển = |1⟩",
        "apply_cnot_btn": "➕ Áp dụng CNOT",
        "cnot_applied_success": "✅ CNOT đã áp dụng (ĐK: Q{control}, MT: Q{target})",
        "reset_btn": "🔄 Đặt lại Hệ thống",
        "reset_warning": "⚠️ Hệ thống đã đặt lại về |0...0⟩",
        "state_vector_header": " Trực quan hóa Vectơ Trạng thái",
        "save_state_vector_btn": "💾 Lưu Đồ thị Vectơ Trạng thái",
        "measurement_header": " Mô phỏng Đo lường",
        "shots_label": "Số lần Bắn:",
        "save_measurement_btn": "💾 Lưu Biểu đồ Đo lường",
        "state_info_header": " Thông tin Trạng thái",
        "current_state": "#### 📍 Trạng thái Hiện tại:",
        "circuit_history": "#### 🔧 Lịch sử Mạch:",
        "no_gates_applied": "Chưa áp dụng cổng nào",
        "show_matrix": "📐 Hiển thị Ma trận Cổng",
        "matrix_title": "Ma trận",
        "basis_state_label": "Trạng thái Cơ sở |x⟩",
        "probability_label": "Xác suất P(x)",
        "probability_dist_title": "📊 Phân phối Xác suất Đo lường",
        "amplitude_label": "Biên độ",
        "amplitude_title": "🌊 Vectơ Trạng thái Biên độ Phức",
        "real_label": "Thực",
        "imaginary_label": "Ảo",
        "measurement_result_label": "Kết quả Đo lường",
        "frequency_label": "Tần suất ({shots} lần bắn)",
        "histogram_title": "Biểu đồ Đo lường ({shots} Lần bắn)",
        "footer": "⚛️ Được tạo bởi Rasidi sử dụng Streamlit & NumPy | Quantum Computing Simulator v2.0",
        "gate_hadamard_desc": "Tạo chồng chất: biến đổi |0⟩ → (|0⟩ + |1⟩)/√2 và |1⟩ → (|0⟩ - |1⟩)/√2",
        "gate_pauli_x_desc": "Đảo bit: hoán đổi |0⟩ ↔ |1⟩ (như cổng NOT cổ điển)",
        "gate_pauli_y_desc": "Quay π radian trên trục Y của cầu Bloch",
        "gate_pauli_z_desc": "Đảo pha: thay đổi pha của |1⟩ thành -|1⟩",
        "gate_s_desc": "Dịch pha π/2: thêm pha i cho |1⟩",
        "gate_t_desc": "Dịch pha π/4: quan trọng cho tính toán phổ quát",
        "language_label": "🌐 Ngôn ngữ:",
    },
}

# Available languages for the selector
# Strings added in Mini Quantum Lab 2.0 live in translations_extra.py.
from translations_extra import EXTRA_TRANSLATIONS

for _lang, _table in EXTRA_TRANSLATIONS.items():
    TRANSLATIONS[_lang].update(_table)
del _lang, _table

AVAILABLE_LANGUAGES = ["English", "Indonesia", "Español", "中文", "العربية", "Français", "日本語", "한국어", "Deutsch", "Português", "Русский", "हिन्दी", "Türkçe", "Italiano", "Tiếng Việt"]

def get_text(lang, key, **kwargs):
    """
    Get translated text for a given key.
    Falls back to English if key not found.
    """
    if lang not in TRANSLATIONS:
        lang = "English"
    
    text = TRANSLATIONS[lang].get(key, TRANSLATIONS["English"].get(key, key))
    
    # Format with any provided kwargs
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, ValueError):
            pass
    
    return text

def get_gate_description(lang, gate_name):
    """Get translated gate description"""
    gate_desc_map = {
        "Hadamard (H)": "gate_hadamard_desc",
        "Pauli-X": "gate_pauli_x_desc",
        "Pauli-Y": "gate_pauli_y_desc",
        "Pauli-Z": "gate_pauli_z_desc",
        "S Gate": "gate_s_desc",
        "T Gate": "gate_t_desc",
        "Identity (I)": "gate_identity_desc",
    }
    
    key = gate_desc_map.get(gate_name, "")
    if key:
        return get_text(lang, key)
    return ""
