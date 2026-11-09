"""Mini Quantum Lab — quantum simulation core.

Qubit ordering is big-endian everywhere: qubit 0 is the leftmost bit of a
basis label.  See :mod:`quantum_lab.gates` for details.
"""

from .simulator import MAX_QUBITS, QuantumSimulator

__version__ = "2.0.0"

__all__ = ["MAX_QUBITS", "QuantumSimulator", "__version__"]
