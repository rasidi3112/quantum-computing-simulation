"""Translation tables: 15 languages, identical keys, consistent placeholders."""

import re
import string
from pathlib import Path

import pytest

import translations
from translations import AVAILABLE_LANGUAGES, TRANSLATIONS, get_gate_description, get_text
from translations_extra import EXTRA_TRANSLATIONS

EXPECTED_LANGUAGES = [
    "English", "Indonesia", "Español", "中文", "العربية", "Français", "日本語", "한국어",
    "Deutsch", "Português", "Русский", "हिन्दी", "Türkçe", "Italiano", "Tiếng Việt",
]
MAIN_SOURCE = (Path(__file__).resolve().parent.parent / "main.py").read_text(encoding="utf-8")
ENGLISH = TRANSLATIONS["English"]


def placeholders(text):
    return sorted({name for _, name, _, _ in string.Formatter().parse(text) if name})


def test_all_fifteen_languages_are_still_available():
    assert AVAILABLE_LANGUAGES == EXPECTED_LANGUAGES
    assert set(TRANSLATIONS) == set(EXPECTED_LANGUAGES)
    assert set(EXTRA_TRANSLATIONS) == set(EXPECTED_LANGUAGES)


@pytest.mark.parametrize("lang", EXPECTED_LANGUAGES)
def test_language_has_exactly_the_english_keys(lang):
    assert set(TRANSLATIONS[lang]) == set(ENGLISH)
    assert set(EXTRA_TRANSLATIONS[lang]) == set(EXTRA_TRANSLATIONS["English"])


@pytest.mark.parametrize("lang", EXPECTED_LANGUAGES)
def test_no_empty_strings(lang):
    for key, text in TRANSLATIONS[lang].items():
        assert isinstance(text, str) and text.strip(), f"{lang}/{key} is empty"


@pytest.mark.parametrize("lang", EXPECTED_LANGUAGES)
def test_placeholders_match_english(lang):
    for key, text in ENGLISH.items():
        assert placeholders(TRANSLATIONS[lang][key]) == placeholders(text), f"{lang}/{key}"


@pytest.mark.parametrize("lang", [name for name in EXPECTED_LANGUAGES if name != "English"])
def test_new_explanations_are_actually_translated(lang):
    # Long educational texts must not be English copies.
    for key in ("bloch_intro", "sampling_info", "projective_info", "bell_explain",
                "teleport_explain", "noise_intro", "grover_explain", "dj_explain"):
        assert TRANSLATIONS[lang][key] != ENGLISH[key], f"{lang}/{key} is untranslated"


def test_every_key_used_by_the_interface_exists():
    used = set(re.findall(r"""\bt\(\s*["']([a-z0-9_]+)["']""", MAIN_SOURCE))
    used |= set(re.findall(r"""get_text\([^,]+,\s*["']([a-z0-9_]+)["']""", MAIN_SOURCE))
    used |= {f"channel_{name}" for name in ("bit_flip", "phase_flip", "depolarizing")}
    assert len(used) > 100
    assert used <= set(ENGLISH), f"missing keys: {sorted(used - set(ENGLISH))}"


def test_no_unused_new_keys():
    used = set(re.findall(r"""["']([a-z0-9_]+)["']""", MAIN_SOURCE))
    used |= {f"channel_{name}" for name in ("bit_flip", "phase_flip", "depolarizing")}
    used.add("gate_identity_desc")  # resolved through get_gate_description
    assert set(EXTRA_TRANSLATIONS["English"]) <= used


@pytest.mark.parametrize("lang", EXPECTED_LANGUAGES)
def test_formatting_with_arguments(lang):
    assert "6" in get_text(lang, "num_qubits_help", max_qubits=6)
    assert "{" not in get_text(lang, "num_qubits_help", max_qubits=6)
    assert "512" in get_text(lang, "histogram_title", shots=512)
    assert "9" in get_text(lang, "dj_queries", classical=9)
    text = get_text(lang, "collapse_if", outcome=1, prob="0.50", state="|11⟩")
    assert "|11⟩" in text and "0.50" in text and "{" not in text


def test_fallbacks():
    assert get_text("Klingon", "page_title") == ENGLISH["page_title"]
    assert get_text("English", "no_such_key") == "no_such_key"


@pytest.mark.parametrize("lang", EXPECTED_LANGUAGES)
def test_every_gate_has_a_description(lang):
    from quantum_lab.gates import GATES

    for spec in GATES.values():
        assert get_gate_description(lang, spec.name), f"{lang}: no description for {spec.name}"


def test_language_metadata():
    codes = [TRANSLATIONS[lang]["lang_code"] for lang in EXPECTED_LANGUAGES]
    assert len(set(codes)) == 15
    assert all(TRANSLATIONS[lang]["flag"] for lang in EXPECTED_LANGUAGES)
    assert hasattr(translations, "EXTRA_TRANSLATIONS")
