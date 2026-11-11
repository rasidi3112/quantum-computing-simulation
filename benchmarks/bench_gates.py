from __future__ import annotations

import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from quantum_lab import QuantumSimulator, gates  # noqa: E402


def best_of(func, repeats: int) -> float:
    times = []
    for _ in range(repeats):
        start = time.perf_counter()
        func()
        times.append(time.perf_counter() - start)
    return min(times)


def main() -> None:
    rng = np.random.default_rng(0)
    print(f"{'qubits':>6} {'dense (v1.0)':>14} {'contraction (v2.0)':>19} {'speed-up':>9} "
          f"{'dense matrix':>13} {'state':>10}")
    for n in (3, 6, 8, 10, 12):
        state = rng.normal(size=2**n) + 1j * rng.normal(size=2**n)
        state /= np.linalg.norm(state)
        target = n // 2
        sim = QuantumSimulator(n)
        sim.set_state(state)

        def dense(n=n, target=target, state=state):
            return gates.expand_gate(gates.HADAMARD, target, n) @ state

        def contraction(sim=sim, target=target):
            sim.apply(gates.HADAMARD, [target])

        check = QuantumSimulator(n)
        check.set_state(state)
        check.apply(gates.HADAMARD, [target])
        assert np.allclose(check.state, dense())

        repeats = 200 if n <= 8 else 20 if n <= 10 else 3
        t_dense, t_fast = best_of(dense, repeats), best_of(contraction, max(repeats, 50))
        print(f"{n:>6} {t_dense * 1e6:>11.1f} µs {t_fast * 1e6:>16.1f} µs "
              f"{t_dense / t_fast:>8.0f}x {16 * 4**n / 2**20:>9.2f} MiB "
              f"{16 * 2**n / 2**10:>6.1f} KiB")

    n = 20
    sim = QuantumSimulator(n)
    elapsed = best_of(lambda: sim.apply(gates.HADAMARD, [n // 2]), 5)
    print(f"\n{n} qubits (the hard limit): one gate in {elapsed * 1e3:.1f} ms, "
          f"state = {16 * 2**n / 2**20:.0f} MiB; a dense matrix would need "
          f"{16 * 4**n / 2**40:.0f} TiB.")


if __name__ == "__main__":
    main()
