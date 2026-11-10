"""Quantum noise channels and noisy circuit simulation.

Noise model
-----------
*Gate noise*: after every gate, the chosen single-qubit channel acts
independently on each qubit the gate touched (controls and targets).  Idle
qubits and measurements are noiseless.  The simulation is exact — it evolves
the density matrix — rather than a Monte-Carlo average.

Channels (``p`` is the error probability per application, ``0 <= p <= 1``):

* bit flip        ``rho -> (1-p) rho + p X rho X``
* phase flip      ``rho -> (1-p) rho + p Z rho Z``
* depolarizing    ``rho -> (1-p) rho + (p/3)(X rho X + Y rho Y + Z rho Z)``

The depolarizing channel shrinks the Bloch vector by ``1 - 4p/3``; ``p = 3/4``
gives the maximally mixed state.
"""

from __future__ import annotations

import numpy as np

from . import gates
from .circuit import GATE, MEASURE, UNITARY, Circuit
from .density import DensityMatrix

BIT_FLIP, PHASE_FLIP, DEPOLARIZING = "bit_flip", "phase_flip", "depolarizing"
CHANNELS = (BIT_FLIP, PHASE_FLIP, DEPOLARIZING)


def _check_probability(p: float) -> float:
    if isinstance(p, (bool, np.bool_)) or not isinstance(p, (int, float, np.integer, np.floating)):
        raise TypeError(f"error probability must be a number, got {p!r}")
    if not np.isfinite(p) or not 0.0 <= p <= 1.0:
        raise ValueError(f"error probability must be in [0, 1], got {p!r}")
    return float(p)


def bit_flip_kraus(p: float) -> list[np.ndarray]:
    p = _check_probability(p)
    return [np.sqrt(1 - p) * gates.IDENTITY, np.sqrt(p) * gates.PAULI_X]


def phase_flip_kraus(p: float) -> list[np.ndarray]:
    p = _check_probability(p)
    return [np.sqrt(1 - p) * gates.IDENTITY, np.sqrt(p) * gates.PAULI_Z]


def depolarizing_kraus(p: float) -> list[np.ndarray]:
    p = _check_probability(p)
    return [
        np.sqrt(1 - p) * gates.IDENTITY,
        np.sqrt(p / 3) * gates.PAULI_X,
        np.sqrt(p / 3) * gates.PAULI_Y,
        np.sqrt(p / 3) * gates.PAULI_Z,
    ]


_FACTORIES = {
    BIT_FLIP: bit_flip_kraus,
    PHASE_FLIP: phase_flip_kraus,
    DEPOLARIZING: depolarizing_kraus,
}


def kraus_operators(channel: str, p: float) -> list[np.ndarray]:
    """Kraus operators of a named channel with error probability ``p``."""
    if channel not in _FACTORIES:
        raise ValueError(f"unknown noise channel {channel!r}; expected one of {CHANNELS}")
    return _FACTORIES[channel](p)


def simulate_density(circuit: Circuit, channel: str | None = None, p: float = 0.0) -> DensityMatrix:
    """Run ``circuit`` on a density matrix, optionally with gate noise.

    Measurements are *non-selective*: the result is the ensemble average over
    all outcomes, weighted by their probabilities.  Classically conditioned
    gates are handled exactly by tracking one unnormalised branch per
    classical record (at most ``2**n`` branches, merged when records agree).
    With ``channel=None`` (or ``p == 0``) this is the ideal reference.
    """
    kraus = kraus_operators(channel, p) if channel is not None and p > 0 else None
    if channel is not None:
        _check_probability(p)
    n = circuit.num_qubits
    # classical record (sorted tuple of (qubit, bit)) -> unnormalised branch
    branches: dict[tuple, DensityMatrix] = {(): DensityMatrix(n)}

    for op in circuit.ops:
        if op.kind == MEASURE:
            qubit = op.targets[0]
            split: dict[tuple, DensityMatrix] = {}
            for record, rho in branches.items():
                for bit in (0, 1):
                    part = rho.copy()
                    if part.project(qubit, bit) < 1e-15:
                        continue
                    key = tuple(sorted({**dict(record), qubit: bit}.items()))
                    if key in split:
                        split[key] = DensityMatrix.from_matrix(
                            split[key].matrix + part.matrix, n
                        )
                    else:
                        split[key] = part
            branches = split
            continue

        for record, rho in branches.items():
            if op.kind == UNITARY:
                rho.apply(op.matrix, op.targets)
            elif op.kind == GATE:
                if op.condition is not None:
                    bits = dict(record)
                    if op.condition not in bits:
                        raise ValueError(
                            f"gate {op.name} is conditioned on qubit {op.condition}, "
                            "which has not been measured"
                        )
                    if bits[op.condition] == 0:
                        continue
                rho.apply_controlled(
                    gates.gate_matrix(op.name, op.params), op.controls, op.targets[0]
                )
            if kraus is not None:
                for qubit in op.qubits:
                    rho.apply_channel(kraus, qubit)

    total = sum(rho.matrix for rho in branches.values())
    return DensityMatrix.from_matrix(total, n)
