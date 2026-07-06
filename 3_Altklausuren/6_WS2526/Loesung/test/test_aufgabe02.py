"""
Aufgabe 2e - Klausur Programmierung WS2025/26
"""

import pytest

from src import aufgabe02a


def test_normalize_and_pack_verwirft_negative_werte():
    assert aufgabe02a.normalize_and_pack([-3, -1], 10) == []


def test_normalize_and_pack_leere_liste_ergibt_leere_liste():
    assert aufgabe02a.normalize_and_pack([], 10) == []


def test_normalize_and_pack_einfaches_paket():
    assert aufgabe02a.normalize_and_pack([1, 2, 3], 10) == [[1, 2, 3]]


def test_normalize_and_pack_rundet_werte_python_standard():
    # Python rundet 2.5 kaufmaennisch auf die gerade Zahl (2), 3.5 auf 4
    assert aufgabe02a.normalize_and_pack([2.5, 3.5], 100) == [[2, 4]]


def test_normalize_and_pack_erzeugt_mehrere_pakete():
    assert aufgabe02a.normalize_and_pack([3, 4], 5) == [[3], [4]]


@pytest.mark.xfail(reason=(
    "Bekannter Grenzwert-Fehler aus Aufgabe 2c: Implementierung nutzt '<' "
    "statt '<=', daher wird ein Paket, dessen Summe exakt dem Limit "
    "entspricht, faelschlicherweise aufgeteilt."
))
def test_normalize_and_pack_summe_exakt_gleich_limit_passt_in_ein_paket():
    assert aufgabe02a.normalize_and_pack([5], 5) == [[5]]


def test_normalize_and_pack_negatives_limit_wirft_exception():
    with pytest.raises(ValueError):
        aufgabe02a.normalize_and_pack([1, 2], -1)


@pytest.mark.xfail(reason=(
    "Bekannter Grenzwert-Fehler aus Aufgabe 2c: Spezifikation verlangt eine "
    "Exception fuer limit <= 0, die Implementierung prueft aber nur "
    "'limit < 0'."
))
def test_normalize_and_pack_limit_null_wirft_exception():
    with pytest.raises(ValueError):
        aufgabe02a.normalize_and_pack([1, 2], 0)


def test_normalize_and_pack_wirft_bei_falschem_typ_in_values():
    with pytest.raises(AssertionError):
        aufgabe02a.normalize_and_pack(["nicht_numerisch"], 10)


def test_normalize_and_pack_wirft_bei_falschem_typ_fuer_limit():
    with pytest.raises(AssertionError):
        aufgabe02a.normalize_and_pack([1, 2], 10.5)
