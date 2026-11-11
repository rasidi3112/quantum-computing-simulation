"""Mini Quantum Lab — quantum simulation core.

Modules
-------
``gates``          gate matrices, unitarity checks, dense reference expansions
``simulator``      state-vector simulator (``QuantumSimulator``)
``measurement``    Born-rule probabilities, shot sampling, projective collapse
``states``         reduced density matrices, Bloch vectors, entropy
``circuit``        circuit model, execution, text diagrams
``density``        density-matrix simulator for mixed states
``noise``          bit-flip, phase-flip and depolarizing channels
``protocols``      Bell / GHZ states and quantum teleportation
``algorithms``     Grover search and Deutsch-Jozsa
``visualization``  Plotly figures (imported on demand; needs ``plotly``)

Qubit ordering is big-endian everywhere: qubit 0 is the leftmost bit of a
basis label and the top wire of a circuit diagram.  See :mod:`quantum_lab.gates`.
"""

from .circuit import Circuit, Operation
from .density import MAX_DENSITY_QUBITS, DensityMatrix
from .simulator import MAX_QUBITS, QuantumSimulator

__version__ = "2.0.0"

__all__ = [
    "MAX_DENSITY_QUBITS",
    "MAX_QUBITS",
    "Circuit",
    "DensityMatrix",
    "Operation",
    "QuantumSimulator",
    "__version__",
]
