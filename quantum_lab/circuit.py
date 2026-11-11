from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field, replace

import numpy as np

from . import gates
from .simulator import QuantumSimulator

GATE, MEASURE, UNITARY = "gate", "measure", "unitary"


@dataclass(frozen=True)
class Operation:
    kind: str
    name: str
    targets: tuple[int, ...]
    controls: tuple[int, ...] = ()
    params: tuple[float, ...] = ()
    condition: int | None = None
    outcome: int | None = None
    matrix: np.ndarray | None = field(default=None, compare=False, repr=False)

    @property
    def qubits(self) -> tuple[int, ...]:
        return (*self.controls, *self.targets)

    def label(self) -> str:
        if self.kind == MEASURE:
            return "[M]" if self.outcome is None else f"[M={self.outcome}]"
        if self.kind == UNITARY:
            return f"[{self.name}]"
        if self.name == "X" and self.controls and self.condition is None:
            return "⊕"
        text = self.name
        if self.params:
            text += "(" + ",".join(f"{p / np.pi:.2f}π" for p in self.params) + ")"
        if self.condition is not None:
            text += f"^m{self.condition}"
        return f"[{text}]"


@dataclass
class RunResult:
    simulator: QuantumSimulator
    outcomes: dict[int, int]  #: last measurement result per measured qubit
    circuit: Circuit  #: executed circuit with measurement outcomes recorded


class Circuit:
    def __init__(self, num_qubits: int, ops: Sequence[Operation] = ()):
        QuantumSimulator(num_qubits)  # validates the register size
        self.num_qubits = int(num_qubits)
        self.ops: list[Operation] = []
        for op in ops:
            self.append(op)

    def __len__(self) -> int:
        return len(self.ops)

    def __iter__(self):
        return iter(self.ops)

    def copy(self) -> Circuit:
        return Circuit(self.num_qubits, self.ops)

    # ------------------------------------------------------------- building
    def append(self, op: Operation) -> Circuit:
        gates.validate_qubits(op.qubits, self.num_qubits)
        if op.condition is not None:
            gates.validate_qubits([op.condition], self.num_qubits)
        if op.kind == GATE:
            if len(op.targets) != 1:
                raise ValueError("a named gate acts on exactly one target qubit")
            gates.gate_matrix(op.name, op.params)
        elif op.kind == MEASURE:
            if len(op.targets) != 1 or op.controls or op.condition is not None:
                raise ValueError("a measurement acts on exactly one qubit")
            if op.outcome not in (None, 0, 1):
                raise ValueError("measurement outcome must be 0, 1 or None")
        elif op.kind == UNITARY:
            size = 2 ** len(op.targets)
            if op.matrix is None or np.shape(op.matrix) != (size, size):
                raise ValueError(f"unitary on {len(op.targets)} qubits needs a "
                                 f"{size}x{size} matrix")
            if not gates.is_unitary(op.matrix):
                raise ValueError("matrix is not unitary")
            if op.controls or op.condition is not None:
                raise ValueError("unitary boxes cannot be controlled")
        else:
            raise ValueError(f"unknown operation kind {op.kind!r}")
        self.ops.append(op)
        return self

    def gate(
        self,
        name: str,
        target: int,
        controls: Sequence[int] = (),
        params: Sequence[float] = (),
        condition: int | None = None,
    ) -> Circuit:
        return self.append(
            Operation(GATE, name, (target,), tuple(controls),
                      tuple(float(p) for p in params), condition)
        )

    def cnot(self, control: int, target: int) -> Circuit:
        return self.gate("X", target, controls=[control])

    def measure(self, qubit: int, outcome: int | None = None) -> Circuit:
        return self.append(Operation(MEASURE, "M", (qubit,), outcome=outcome))

    def unitary(self, name: str, qubits: Sequence[int], matrix: np.ndarray) -> Circuit:
        m = np.array(matrix, dtype=complex)
        m.setflags(write=False)
        return self.append(Operation(UNITARY, name, tuple(qubits), matrix=m))

    # ------------------------------------------------------------ execution
    def run(
        self,
        rng=None,
        forced: Mapping[int, int] | None = None,
        initial_state: np.ndarray | None = None,
    ) -> RunResult:
        from .measurement import make_rng

        rng = make_rng(rng)
        forced = dict(forced or {})
        sim = QuantumSimulator(self.num_qubits)
        if initial_state is not None:
            sim.set_state(initial_state)
        outcomes: dict[int, int] = {}
        executed: list[Operation] = []
        for op in self.ops:
            if op.kind == MEASURE:
                qubit = op.targets[0]
                if qubit in forced:
                    sim.project(qubit, forced[qubit])
                    result = int(forced[qubit])
                else:
                    result = sim.measure_qubit(qubit, rng)
                outcomes[qubit] = result
                executed.append(replace(op, outcome=result))
                continue
            executed.append(op)
            if op.kind == UNITARY:
                sim.apply(op.matrix, op.targets)
                continue
            if op.condition is not None:
                if op.condition not in outcomes:
                    raise ValueError(
                        f"gate {op.name} is conditioned on qubit {op.condition}, "
                        "which has not been measured"
                    )
                if outcomes[op.condition] == 0:
                    continue
            sim.apply_controlled(gates.gate_matrix(op.name, op.params), op.controls,
                                 op.targets[0])
        return RunResult(sim, outcomes, Circuit(self.num_qubits, executed))

    # -------------------------------------------------------------- drawing
    def layers(self) -> list[list[Operation]]:
        free = [0] * self.num_qubits  # first free column per wire
        columns: list[list[Operation]] = []
        for op in self.ops:
            involved = list(op.qubits)
            if op.condition is not None:
                involved.append(op.condition)  # must come after that measurement
            lo, hi = min(involved), max(involved)
            column = max(free[lo : hi + 1])
            for q in range(lo, hi + 1):
                free[q] = column + 1
            while len(columns) <= column:
                columns.append([])
            columns[column].append(op)
        return columns

    def draw(self) -> str:
        n = self.num_qubits
        prefix = [f"q{q}: " for q in range(n)]
        pad = max(len(p) for p in prefix)
        wires = [p.ljust(pad) + "──" for p in prefix]
        gaps = [" " * (pad + 2) for _ in range(n - 1)]

        for column in self.layers():
            cells: dict[int, str] = {}
            linked: set[int] = set()  # gap g sits between wire g and g + 1
            for op in column:
                qubits = op.qubits
                lo, hi = min(qubits), max(qubits)
                for q in range(lo, hi + 1):
                    cells[q] = "┼"
                for q in op.controls:
                    cells[q] = "●"
                for q in op.targets:
                    cells[q] = op.label()
                linked.update(range(lo, hi))
            width = max(len(text) for text in cells.values())
            width += 1 - width % 2  # odd width => a well-defined centre
            for q in range(n):
                text = cells.get(q, "")
                left = (width - len(text)) // 2
                wires[q] += "─" * left + text + "─" * (width - len(text) - left) + "──"
            for g in range(n - 1):
                mark = "│" if g in linked else " "
                gaps[g] += " " * (width // 2) + mark + " " * (width // 2) + "  "

        lines = []
        for q in range(n):
            lines.append(wires[q])
            if q < n - 1:
                lines.append(gaps[q].rstrip())
        return "\n".join(lines)
