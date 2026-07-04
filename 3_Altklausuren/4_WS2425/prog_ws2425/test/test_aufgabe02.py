"""
Aufgabe 2 (Teile 3 und 4: White-Box-Pfade + pytest) - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

from prog_ws2425.src import aufgabe02

import pytest


# =========================================================================
# 3) White-Box-Pfade fuer minOfThree(a, b, c)
#    Zwei aufeinanderfolgende Verzweigungen -> 4 Pfadkombinationen.
#
#   P1 a<b = True,  c<kleiner = True   -> c ist Minimum   z.B. (2,3,1) -> 1
#   P2 a<b = True,  c<kleiner = False  -> a ist Minimum   z.B. (1,3,2) -> 1
#   P3 a<b = False, c<kleiner = True   -> c ist Minimum   z.B. (3,2,1) -> 1
#   P4 a<b = False, c<kleiner = False  -> b ist Minimum   z.B. (3,1,2) -> 1
# =========================================================================


def test_minOfThree_p1():
    assert aufgabe02.minOfThree(2, 3, 1) == 1


def test_minOfThree_p2():
    assert aufgabe02.minOfThree(1, 3, 2) == 1


def test_minOfThree_p3():
    assert aufgabe02.minOfThree(3, 2, 1) == 1


def test_minOfThree_p4():
    assert aufgabe02.minOfThree(3, 1, 2) == 1


# =========================================================================
# 4) White-Box-Pfade fuer ggt(a, b) (rekursiv)
#    Empfehlung fuer Rekursion: Basisfall / einmal / mehrfach rekursiv.
#
#   P1 Basisfall "b == 0":       gibt a sofort zurueck   z.B. ggt(5, 0) -> 5
#   P2 else, genau 1 Rekursion:  z.B. ggt(4, 2) -> ggt(2, 0) -> 2
#   P3 else, mehrfach rekursiv:  z.B. ggt(18, 27) -> 9 ; ggt(42, 70) -> 14
# =========================================================================


def test_ggt_basisfall():
    assert aufgabe02.ggt(5, 0) == 5


def test_ggt_eine_rekursion():
    assert aufgabe02.ggt(4, 2) == 2


def test_ggt_mehrfach_rekursion():
    assert aufgabe02.ggt(18, 27) == 9
    assert aufgabe02.ggt(42, 70) == 14
