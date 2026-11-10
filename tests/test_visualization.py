"""Plotly figure builders: structure and data fidelity (no rendering needed)."""

import numpy as np
import pytest

from quantum_lab import visualization as viz

LABELS = ["00", "01", "10", "11"]
BELL = np.array([1, 0, 0, 1]) / np.sqrt(2)


def test_palette_selection():
    assert viz.palette_for("dark") is viz.DARK
    assert viz.palette_for("light") is viz.LIGHT
    assert viz.palette_for(None) is viz.LIGHT


def test_ket_labels():
    assert viz.ket_labels(["0", "11"]) == ["|0⟩", "|11⟩"]


def test_probability_figure_plots_the_given_numbers():
    probs = np.abs(BELL) ** 2
    fig = viz.probability_figure(probs, LABELS, title="T", x_title="x", y_title="y")
    (bar,) = fig.data
    assert list(bar.x) == ["|00⟩", "|01⟩", "|10⟩", "|11⟩"]
    assert np.allclose(bar.y, probs)
    assert bar.marker.color == viz.LIGHT.series_1  # one series, one colour
    assert fig.layout.title.text == "T"
    assert tuple(fig.layout.yaxis.range) == (0, 1.08)


def test_probability_figure_highlight_uses_emphasis_not_a_ramp():
    fig = viz.probability_figure([0.1, 0.7, 0.1, 0.1], LABELS, title="", x_title="",
                                 y_title="", highlight=1, palette=viz.DARK)
    colors = list(fig.data[0].marker.color)
    assert colors[1] == viz.DARK.series_1
    assert set(colors[:1] + colors[2:]) == {viz.DARK.neutral}


def test_amplitude_figure_has_real_and_imaginary_series():
    amplitudes = np.array([0.5, 0.5j, -0.5, -0.5j])
    fig = viz.amplitude_figure(amplitudes, LABELS, title="", x_title="", y_title="",
                               real_label="Re", imag_label="Im")
    real, imag = fig.data
    assert (real.name, imag.name) == ("Re", "Im")
    assert np.allclose(real.y, amplitudes.real) and np.allclose(imag.y, amplitudes.imag)
    assert real.marker.color != imag.marker.color
    assert fig.layout.barmode == "group"


def test_phase_figure_reports_phase_in_units_of_pi():
    amplitudes = np.array([0.5, 0.5j, -0.5, -0.5j])  # phases 0, pi/2, pi, -pi/2
    fig = viz.phase_figure(amplitudes, LABELS, title="", x_title="")
    (points,) = fig.data
    assert np.allclose(points.y, [0.0, 0.5, 1.0, -0.5])
    assert np.allclose(points.customdata, 0.5)
    assert len(fig.layout.shapes) == 4  # one stem per defined phase


def test_phase_is_undefined_for_zero_amplitudes():
    fig = viz.phase_figure(BELL, LABELS, title="", x_title="")
    y = np.asarray(fig.data[0].y, dtype=float)
    assert y[0] == 0 and y[3] == 0
    assert np.isnan(y[1]) and np.isnan(y[2])
    assert len(fig.layout.shapes) == 2


def test_minus_pi_and_plus_pi_are_drawn_as_the_same_phase():
    fig = viz.phase_figure(np.array([np.exp(-1j * np.pi), 0]), ["0", "1"], title="", x_title="")
    assert fig.data[0].y[0] == pytest.approx(1.0)


def test_histogram_figure():
    counts = np.array([480, 0, 0, 520])
    fig = viz.histogram_figure(counts, [500, 0, 0, 500], LABELS, title="", x_title="",
                               y_title="", measured_label="M", expected_label="E")
    measured, expected = fig.data
    assert measured.type == "bar" and expected.type == "scatter"
    assert list(measured.y) == [480, 0, 0, 520]
    assert list(expected.y) == [500, 0, 0, 500]
    assert np.allclose(measured.customdata, [48.0, 0, 0, 52.0])
    assert fig.layout.yaxis.range[1] > 520


def test_comparison_and_curve_figures():
    fig = viz.comparison_figure([0.5, 0, 0, 0.5], [0.4, 0.1, 0.1, 0.4], LABELS, title="",
                                x_title="", y_title="", first_label="A", second_label="B")
    assert [trace.name for trace in fig.data] == ["A", "B"]
    assert np.allclose(fig.data[1].y, [0.4, 0.1, 0.1, 0.4])

    fig = viz.curve_figure([0, 1, 2], [0.25, 1.0, 0.25], [0, 1, 2], [0.25, 1.0, 0.25], title="",
                           x_title="", y_title="", simulated_label="S", theory_label="T",
                           marker_x=1)
    theory, simulated = fig.data
    assert theory.mode == "lines" and simulated.mode == "markers"
    assert list(simulated.y) == [0.25, 1.0, 0.25]
    assert len(fig.layout.shapes) == 1


# ------------------------------------------------------------- Bloch sphere
def _vector_trace(fig):
    return next(tr for tr in fig.data if tr.type == "scatter3d" and tr.mode == "lines+markers")


@pytest.mark.parametrize("vector", [(0, 0, 1), (1, 0, 0), (0, -1, 0), (0.3, -0.4, 0.5)])
def test_bloch_vector_is_drawn_at_its_true_coordinates(vector):
    fig = viz.bloch_figure(vector)
    trace = _vector_trace(fig)
    assert (trace.x[0], trace.y[0], trace.z[0]) == (0, 0, 0)
    assert (trace.x[1], trace.y[1], trace.z[1]) == pytest.approx(vector)
    assert f"|r| = {np.linalg.norm(vector):.4f}" in trace.hovertemplate


def test_bloch_sphere_has_axes_and_cardinal_state_labels():
    fig = viz.bloch_figure((0, 0, 1), title="Q0")
    text = next(tr for tr in fig.data if tr.type == "scatter3d" and tr.mode == "text")
    joined = " ".join(text.text)
    for label in ("|0⟩", "|1⟩", "|+⟩", "|−⟩", "|+i⟩", "|−i⟩", "x", "y", "z"):
        assert label in joined
    assert any(tr.type == "surface" for tr in fig.data)
    assert fig.layout.title.text == "Q0"
    assert fig.layout.scene.aspectmode == "cube"


def test_mixed_state_arrow_is_shorter_and_maximally_mixed_has_no_arrowhead():
    pure = viz.bloch_figure((0, 0, 1))
    mixed = viz.bloch_figure((0, 0, 0.5))
    centre = viz.bloch_figure((0, 0, 0))
    assert _vector_trace(mixed).z[1] == 0.5
    assert any(tr.type == "cone" for tr in pure.data)
    assert any(tr.type == "cone" for tr in mixed.data)
    assert not any(tr.type == "cone" for tr in centre.data)
    assert tuple(_vector_trace(centre).z) == (0, 0)


@pytest.mark.parametrize("bad", [(0, 0), (0, 0, 1.5), (np.nan, 0, 0), (1, 1, 1)])
def test_bloch_figure_rejects_unphysical_vectors(bad):
    with pytest.raises(ValueError):
        viz.bloch_figure(bad)
