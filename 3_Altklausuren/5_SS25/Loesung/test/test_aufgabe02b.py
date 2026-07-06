"""
Aufgabe 2b - Klausur Programmierung
Tests entsprechend der White-Box-Pfade aus prog_ss25/src/aufgabe02b.txt
"""

from src import aufgabe02b

import pytest


def test_schnittmenge_leere_menge1():
    # P1: Basisfall, menge1 bereits leer
    assert aufgabe02b.schnittmenge([], [1, 2, 3]) == []


def test_schnittmenge_alle_elemente_gemeinsam():
    # P2: jedes Element von menge1 wird in menge2 gefunden
    assert aufgabe02b.schnittmenge([1, 2], [1, 2]) == [1, 2]


def test_schnittmenge_keine_gemeinsamen_elemente():
    # P3: kein Element von menge1 wird in menge2 gefunden
    assert aufgabe02b.schnittmenge([1, 2, 3], [4, 5]) == []


def test_schnittmenge_gemischte_treffer():
    # P4: abwechselnd Treffer/Nicht-Treffer ueber mehrere Rekursionsstufen
    assert aufgabe02b.schnittmenge([1, 2, 3], [2, 4]) == [2]


def test_schnittmenge_leere_menge2():
    # P5: menge2 ist leer
    assert aufgabe02b.schnittmenge([1, 2, 3], []) == []


def test_schnittmenge_mehrfache_vorkommen_in_menge1():
    # Mehrfachvorkommen in menge1 muessen laut Spezifikation mehrfach
    # in der Rueckgabe enthalten sein
    assert aufgabe02b.schnittmenge([2, 2, 3], [2]) == [2, 2]
