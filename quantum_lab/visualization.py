from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

import numpy as np
import plotly.graph_objects as go

#: Amplitudes below this magnitude have no meaningful phase.
PHASE_EPS = 1e-9


@dataclass(frozen=True)
class Palette:
    series_1: str  # primary series
    series_2: str  # comparison series
    neutral: str  # de-emphasised marks, reference lines
    ink: str  # text and thin reference marks drawn on the surface
    grid: str  # hairlines
    sphere: str  # Bloch-sphere surface tint


LIGHT = Palette("#2a78d6", "#eb6834", "#b9b8b2", "#3d3d3a", "#e4e3de", "#8a8a85")
DARK = Palette("#3987e5", "#d95926", "#5c5c58", "#d6d5cf", "#383835", "#9a9a94")


def palette_for(base: str | None) -> Palette:
    return DARK if base == "dark" else LIGHT


def ket_labels(labels: Sequence[str]) -> list[str]:
    return [f"|{label}⟩" for label in labels]


def _base_layout(fig: go.Figure, title: str, x_title: str, y_title: str, pal: Palette,
                 height: int = 360) -> go.Figure:
    fig.update_layout(
        title=dict(text=title, font=dict(size=15)),
        height=height,
        margin=dict(l=56, r=16, t=56, b=48),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        barcornerradius=4,
        hoverlabel=dict(font_size=13),
        legend=dict(orientation="h", yanchor="bottom", y=1.0, xanchor="right", x=1.0),
    )
    categories = max((len(trace.x) for trace in fig.data if trace.x is not None), default=0)
    fig.update_layout(bargap=0.6 if categories <= 4 else 0.45 if categories <= 8 else 0.3)
    fig.update_xaxes(title_text=x_title, type="category", showgrid=False,
                     linecolor=pal.grid, tickfont=dict(family="monospace"))
    fig.update_yaxes(title_text=y_title, gridcolor=pal.grid, zerolinecolor=pal.neutral,
                     zerolinewidth=1)
    return fig


def probability_figure(
    probs: Sequence[float],
    labels: Sequence[str],
    *,
    title: str,
    x_title: str,
    y_title: str,
    palette: Palette = LIGHT,
    highlight: int | None = None,
) -> go.Figure:
    probs = np.asarray(probs, dtype=float)
    kets = ket_labels(labels)
    colors: str | list[str] = palette.series_1
    text = [f"{p:.3f}" if p > 0.005 else "" for p in probs] if len(probs) <= 8 else None
    if highlight is not None:
        colors = [palette.series_1 if i == highlight else palette.neutral
                  for i in range(len(probs))]
        # label only the bar the chart is about
        text = [f"{p:.3f}" if i == highlight else "" for i, p in enumerate(probs)]
    fig = go.Figure(
        go.Bar(
            x=kets,
            y=probs,
            marker_color=colors,
            text=text,
            textposition="outside",
            cliponaxis=False,
            hovertemplate="%{x}<br>P = %{y:.6f}<extra></extra>",
        )
    )
    _base_layout(fig, title, x_title, y_title, palette)
    fig.update_yaxes(range=[0, 1.08])
    fig.update_layout(showlegend=False)
    return fig


def amplitude_figure(
    amplitudes: Sequence[complex],
    labels: Sequence[str],
    *,
    title: str,
    x_title: str,
    y_title: str,
    real_label: str,
    imag_label: str,
    palette: Palette = LIGHT,
) -> go.Figure:
    amplitudes = np.asarray(amplitudes, dtype=complex)
    kets = ket_labels(labels)
    fig = go.Figure(
        [
            go.Bar(name=real_label, x=kets, y=amplitudes.real, marker_color=palette.series_1,
                   hovertemplate="%{x}<br>" + real_label + " = %{y:.6f}<extra></extra>"),
            go.Bar(name=imag_label, x=kets, y=amplitudes.imag, marker_color=palette.series_2,
                   hovertemplate="%{x}<br>" + imag_label + " = %{y:.6f}<extra></extra>"),
        ]
    )
    _base_layout(fig, title, x_title, y_title, palette)
    fig.update_layout(barmode="group", bargroupgap=0.08)
    fig.update_yaxes(range=[-1.08, 1.08])
    return fig


def phase_figure(
    amplitudes: Sequence[complex],
    labels: Sequence[str],
    *,
    title: str,
    x_title: str,
    palette: Palette = LIGHT,
) -> go.Figure:
    amplitudes = np.asarray(amplitudes, dtype=complex)
    kets = ket_labels(labels)
    magnitude = np.abs(amplitudes)
    defined = magnitude > PHASE_EPS
    phase = np.where(defined, np.angle(amplitudes) / np.pi, np.nan)
    # -pi and +pi are the same phase; show it once, as +1.
    phase = np.where(np.isclose(phase, -1.0), 1.0, phase)
    fig = go.Figure()
    for ket, value in zip(kets, phase, strict=True):
        if np.isfinite(value):
            fig.add_shape(type="line", x0=ket, x1=ket, y0=0, y1=float(value),
                          line=dict(color=palette.series_1, width=2))
    fig.add_trace(
        go.Scatter(
            x=kets,
            y=phase,
            mode="markers",
            marker=dict(size=11, color=palette.series_1),
            customdata=magnitude,
            hovertemplate="%{x}<br>arg(α) = %{y:.4f} π<br>|α| = %{customdata:.6f}<extra></extra>",
        )
    )
    _base_layout(fig, title, x_title, "arg(α) / π", palette)
    fig.update_xaxes(categoryorder="array", categoryarray=kets, range=[-0.5, len(kets) - 0.5])
    fig.update_yaxes(range=[-1.1, 1.1], tickvals=[-1, -0.5, 0, 0.5, 1],
                     ticktext=["−π", "−π/2", "0", "π/2", "π"])
    fig.update_layout(showlegend=False)
    return fig


def histogram_figure(
    counts: Sequence[int],
    expected: Sequence[float],
    labels: Sequence[str],
    *,
    title: str,
    x_title: str,
    y_title: str,
    measured_label: str,
    expected_label: str,
    palette: Palette = LIGHT,
) -> go.Figure:
    counts = np.asarray(counts)
    expected = np.asarray(expected, dtype=float)
    shots = int(counts.sum())
    kets = ket_labels(labels)
    percent = counts / shots * 100 if shots else np.zeros_like(expected)
    fig = go.Figure(
        [
            go.Bar(
                name=measured_label, x=kets, y=counts, marker_color=palette.series_1,
                customdata=percent,
                text=[f"{c}" if c else "" for c in counts] if len(counts) <= 8 else None,
                textposition="inside", insidetextanchor="middle",
                textfont=dict(color="#ffffff"),
                hovertemplate="%{x}<br>" + measured_label
                + ": %{y} (%{customdata:.2f}%)<extra></extra>",
            ),
            go.Scatter(
                name=expected_label, x=kets, y=expected, mode="markers",
                marker=dict(symbol="line-ew", size=22,
                            line=dict(width=2.5, color=palette.ink)),
                hovertemplate="%{x}<br>" + expected_label + ": %{y:.1f}<extra></extra>",
            ),
        ]
    )
    _base_layout(fig, title, x_title, y_title, palette)
    top = max(float(counts.max(initial=0)), float(expected.max(initial=0)), 1.0)
    fig.update_yaxes(range=[0, top * 1.15])
    return fig


def comparison_figure(
    first: Sequence[float],
    second: Sequence[float],
    labels: Sequence[str],
    *,
    title: str,
    x_title: str,
    y_title: str,
    first_label: str,
    second_label: str,
    palette: Palette = LIGHT,
) -> go.Figure:
    kets = ket_labels(labels)
    fig = go.Figure(
        [
            go.Bar(name=first_label, x=kets, y=np.asarray(first, dtype=float),
                   marker_color=palette.series_1,
                   hovertemplate="%{x}<br>" + first_label + ": %{y:.6f}<extra></extra>"),
            go.Bar(name=second_label, x=kets, y=np.asarray(second, dtype=float),
                   marker_color=palette.series_2,
                   hovertemplate="%{x}<br>" + second_label + ": %{y:.6f}<extra></extra>"),
        ]
    )
    _base_layout(fig, title, x_title, y_title, palette)
    fig.update_layout(barmode="group", bargroupgap=0.08)
    fig.update_yaxes(range=[0, 1.08])
    return fig


def curve_figure(
    x: Sequence[float],
    simulated: Sequence[float],
    theory_x: Sequence[float],
    theory_y: Sequence[float],
    *,
    title: str,
    x_title: str,
    y_title: str,
    simulated_label: str,
    theory_label: str,
    palette: Palette = LIGHT,
    marker_x: float | None = None,
) -> go.Figure:
    fig = go.Figure(
        [
            go.Scatter(name=theory_label, x=list(theory_x), y=list(theory_y), mode="lines",
                       line=dict(color=palette.series_1, width=2), hoverinfo="skip"),
            go.Scatter(name=simulated_label, x=list(x), y=list(simulated), mode="markers",
                       marker=dict(size=10, color=palette.series_2,
                                   line=dict(width=2, color="rgba(0,0,0,0)")),
                       hovertemplate="k = %{x}<br>P = %{y:.6f}<extra></extra>"),
        ]
    )
    _base_layout(fig, title, x_title, y_title, palette)
    fig.update_xaxes(type="linear", dtick=1, showgrid=False)
    fig.update_yaxes(range=[0, 1.08])
    if marker_x is not None:
        fig.add_vline(x=marker_x, line=dict(color=palette.neutral, width=1))
    return fig


# ---------------------------------------------------------------- Bloch sphere
_SPHERE_CACHE: dict[int, tuple[np.ndarray, np.ndarray, np.ndarray]] = {}


def _sphere_mesh(resolution: int = 40):
    if resolution not in _SPHERE_CACHE:
        u = np.linspace(0, 2 * np.pi, resolution)
        v = np.linspace(0, np.pi, resolution // 2)
        _SPHERE_CACHE[resolution] = (
            np.outer(np.cos(u), np.sin(v)),
            np.outer(np.sin(u), np.sin(v)),
            np.outer(np.ones_like(u), np.cos(v)),
        )
    return _SPHERE_CACHE[resolution]


def bloch_figure(
    vector: Sequence[float],
    *,
    title: str = "",
    palette: Palette = LIGHT,
    height: int = 380,
) -> go.Figure:
    r = np.asarray(vector, dtype=float).reshape(-1)
    if r.shape != (3,) or not np.all(np.isfinite(r)):
        raise ValueError("Bloch vector must have three finite components")
    length = float(np.linalg.norm(r))
    if length > 1.0 + 1e-6:
        raise ValueError(f"Bloch vector length {length:.6f} exceeds 1")

    xs, ys, zs = _sphere_mesh()
    fig = go.Figure()
    fig.add_trace(
        go.Surface(x=xs, y=ys, z=zs, opacity=0.10, showscale=False, hoverinfo="skip",
                   colorscale=[[0, palette.sphere], [1, palette.sphere]],
                   lighting=dict(ambient=1.0, diffuse=0.0, specular=0.0))
    )
    t = np.linspace(0, 2 * np.pi, 120)
    zero = np.zeros_like(t)
    for cx, cy, cz in ((np.cos(t), np.sin(t), zero), (np.cos(t), zero, np.sin(t)),
                       (zero, np.cos(t), np.sin(t))):
        fig.add_trace(go.Scatter3d(x=cx, y=cy, z=cz, mode="lines", hoverinfo="skip",
                                   line=dict(color=palette.neutral, width=2)))
    for axis in np.eye(3):
        fig.add_trace(go.Scatter3d(x=[-axis[0], axis[0]], y=[-axis[1], axis[1]],
                                   z=[-axis[2], axis[2]], mode="lines", hoverinfo="skip",
                                   line=dict(color=palette.ink, width=2)))
    cardinal = {
        "|0⟩  z": (0, 0, 1.22), "|1⟩": (0, 0, -1.22),
        "|+⟩  x": (1.28, 0, 0), "|−⟩": (-1.28, 0, 0),
        "|+i⟩  y": (0, 1.28, 0), "|−i⟩": (0, -1.28, 0),
    }
    fig.add_trace(
        go.Scatter3d(
            x=[p[0] for p in cardinal.values()], y=[p[1] for p in cardinal.values()],
            z=[p[2] for p in cardinal.values()], mode="text", text=list(cardinal),
            textfont=dict(size=13, color=palette.ink), hoverinfo="skip",
        )
    )

    hover = (f"⟨X⟩ = {r[0]:+.4f}<br>⟨Y⟩ = {r[1]:+.4f}<br>⟨Z⟩ = {r[2]:+.4f}"
             f"<br>|r| = {length:.4f}<extra></extra>")
    fig.add_trace(
        go.Scatter3d(x=[0, r[0]], y=[0, r[1]], z=[0, r[2]], mode="lines+markers",
                     line=dict(color=palette.series_1, width=8),
                     marker=dict(size=[3, 6], color=palette.series_1),
                     hovertemplate=hover)
    )
    if length >= 0.25:
        unit = r / length
        fig.add_trace(
            go.Cone(x=[r[0]], y=[r[1]], z=[r[2]], u=[unit[0]], v=[unit[1]], w=[unit[2]],
                    anchor="tip", sizemode="absolute", sizeref=0.22, showscale=False,
                    colorscale=[[0, palette.series_1], [1, palette.series_1]],
                    hoverinfo="skip")
        )

    hidden = dict(visible=False, range=[-1.35, 1.35])
    fig.update_layout(
        title=dict(text=title, font=dict(size=14)),
        height=height,
        margin=dict(l=0, r=0, t=40 if title else 0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        scene=dict(xaxis=hidden, yaxis=hidden, zaxis=hidden, aspectmode="cube",
                   bgcolor="rgba(0,0,0,0)",
                   camera=dict(eye=dict(x=1.1, y=0.85, z=0.6))),
    )
    return fig
