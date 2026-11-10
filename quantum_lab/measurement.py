"""Measurement engine: Born-rule probabilities, shot sampling and collapse.

Two different operations are provided and must not be confused:

* **Shot sampling** (:func:`sample_counts`, :func:`sample_outcomes`) models
  preparing the *same* state many times and measuring each copy once.  It
  returns statistics and leaves the state untouched.
* **Projective measurement** (:func:`measure_qubit`, :func:`measure_all`,
  :func:`project_qubit`) acts on *one* system: an outcome is drawn, the state
  collapses onto the matching subspace and is renormalised.

All functions take pure state vectors in the package's big-endian convention
(qubit 0 = leftmost bit) and return new arrays; nothing is modified in place.
"""

from __future__ import annotations

from typing import Sequence

import numpy as np

from .gates import validate_qubits

#: Maximum accepted deviation of ``sum(p)`` from 1 before sampling.
PROB_ATOL = 1e-8
#: Outcomes with probability below this are treated as impossible.
ZERO_PROB = 1e-12


def make_rng(seed=None) -> np.random.Generator:
    """Return a ``numpy.random.Generator``.

    ``seed`` may be ``None`` (fresh OS entropy), a non-negative integer (fully
    reproducible) or an existing ``Generator`` (returned unchanged, so a caller
    can thread one generator through a sequence of measurements).
    """
    if isinstance(seed, np.random.Generator):
        return seed
    if seed is not None:
        if isinstance(seed, (bool, np.bool_)) or not isinstance(seed, (int, np.integer)):
            raise TypeError("seed must be None, a non-negative integer or a Generator")
        if seed < 0:
            raise ValueError("seed must be non-negative")
    return np.random.default_rng(seed)


def num_qubits_of(state: np.ndarray) -> int:
    """Number of qubits of a state vector; raises if its length is not 2**n."""
    size = np.asarray(state).shape[0]
    n = int(size).bit_length() - 1
    if size < 2 or 2**n != size:
        raise ValueError(f"state length {size} is not a power of two >= 2")
    return n


def probabilities(state: np.ndarray) -> np.ndarray:
    """Born rule: ``P(i) = |alpha_i|^2``."""
    return np.abs(np.asarray(state)) ** 2


def marginal_probabilities(state: np.ndarray, qubits: Sequence[int]) -> np.ndarray:
    """Joint probability distribution of a subset of qubits.

    The result has ``2**len(qubits)`` entries; the first listed qubit is the
    most significant bit of its index.
    """
    n = num_qubits_of(state)
    qubits = validate_qubits(qubits, n)
    if not qubits:
        raise ValueError("at least one qubit is required")
    tensor = probabilities(state).reshape((2,) * n)
    others = tuple(q for q in range(n) if q not in qubits)
    reduced = tensor.sum(axis=others) if others else tensor
    # ``reduced`` keeps the kept axes in ascending qubit order; reorder them.
    order = np.argsort(np.argsort(qubits))
    return np.transpose(reduced, order).reshape(-1)


def _checked_distribution(probs: np.ndarray) -> np.ndarray:
    p = np.asarray(probs, dtype=float).reshape(-1)
    if p.size == 0 or not np.all(np.isfinite(p)) or np.any(p < -PROB_ATOL):
        raise ValueError("probabilities must be finite and non-negative")
    total = float(p.sum())
    if abs(total - 1.0) > PROB_ATOL:
        raise ValueError(f"probabilities must sum to 1 (sum = {total:.10g})")
    p = np.clip(p, 0.0, None)
    return p / p.sum()


def _checked_shots(shots: int) -> int:
    if isinstance(shots, (bool, np.bool_)) or not isinstance(shots, (int, np.integer)):
        raise TypeError(f"shots must be an integer, got {shots!r}")
    if shots < 1:
        raise ValueError("shots must be at least 1")
    return int(shots)


def sample_outcomes(probs: np.ndarray, shots: int, rng=None) -> np.ndarray:
    """Draw ``shots`` independent outcome indices from ``probs``."""
    p = _checked_distribution(probs)
    return make_rng(rng).choice(p.size, size=_checked_shots(shots), p=p)


def sample_counts(probs: np.ndarray, shots: int, rng=None) -> np.ndarray:
    """Number of times each outcome occurs in ``shots`` independent draws."""
    p = _checked_distribution(probs)
    return make_rng(rng).multinomial(_checked_shots(shots), p)


def project_qubit(
    state: np.ndarray, qubit: int, outcome: int
) -> tuple[np.ndarray, float]:
    """Project ``qubit`` onto ``|outcome>`` and renormalise.

    Returns ``(collapsed_state, probability_of_that_outcome)``.  Raises
    ``ValueError`` when the outcome has (numerically) zero probability, since
    the post-measurement state is then undefined.
    """
    n = num_qubits_of(state)
    (qubit,) = validate_qubits([qubit], n)
    if outcome not in (0, 1):
        raise ValueError(f"measurement outcome must be 0 or 1, got {outcome!r}")
    tensor = np.array(state, dtype=complex).reshape((2,) * n)
    index: list[slice | int] = [slice(None)] * n
    index[qubit] = 1 - int(outcome)
    tensor[tuple(index)] = 0.0
    collapsed = tensor.reshape(-1)
    prob = float(np.vdot(collapsed, collapsed).real)
    if prob < ZERO_PROB:
        raise ValueError(
            f"outcome {outcome} on qubit {qubit} has zero probability; "
            "cannot collapse onto it"
        )
    return collapsed / np.sqrt(prob), prob


def measure_qubit(state: np.ndarray, qubit: int, rng=None) -> tuple[np.ndarray, int]:
    """Projective measurement of a single qubit in the computational basis.

    Returns ``(collapsed_state, outcome)``.
    """
    p_one = float(marginal_probabilities(state, [qubit])[1])
    p_one = min(max(p_one, 0.0), 1.0)
    outcome = int(make_rng(rng).random() < p_one)
    collapsed, _ = project_qubit(state, qubit, outcome)
    return collapsed, outcome


def measure_all(state: np.ndarray, rng=None) -> tuple[np.ndarray, int]:
    """Projective measurement of every qubit.

    Returns ``(basis_state, index)``: the state collapses to the computational
    basis state ``|index>`` (global phase discarded).
    """
    index = int(sample_outcomes(probabilities(state), 1, rng)[0])
    collapsed = np.zeros(np.asarray(state).shape[0], dtype=complex)
    collapsed[index] = 1.0
    return collapsed, index
