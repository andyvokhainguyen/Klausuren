"""
Aufgabe 2 (Teile 3 und 4: White-Box-Pfade + pytest) - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

from prog_ss24.src import aufgabe02
import pytest


# =========================================================================
# 3) White-Box-Pfade fuer foo(x, a)  (while-Schleife)
#    Empfehlung fuer Schleifen: gar nicht / genau einmal / mehrfach durchlaufen.
#
#   P1 Schleife 0x:       x < a          z.B. foo(1, 2) -> 0
#   P2 Schleife genau 1x: x >= a, danach x-a < a   z.B. foo(3, 2) -> 1
#   P3 Schleife mehrfach: x >> a         z.B. foo(10, 3) -> 3
# =========================================================================


def test_foo_null_durchlaeufe():
    assert aufgabe02.foo(1, 2) == 0


def test_foo_ein_durchlauf():
    assert aufgabe02.foo(3, 2) == 1


def test_foo_mehrere_durchlaeufe():
    assert aufgabe02.foo(10, 3) == 3


# =========================================================================
# 4) White-Box-Pfade fuer vereinigung(menge1, menge2)  (rekursiv, if/elif/else)
#    Empfehlung fuer Rekursion: Basisfall / einmal / mehrfach + alle Zweige.
#
#   P1 Basisfall "len(menge1) == 0":     menge1 leer -> gibt menge2 zurueck
#                                        z.B. vereinigung([], [1,2]) -> [1,2]
#   P2 elif "menge1[0] in menge2":       Element schon in menge2 -> uebersprungen
#                                        z.B. vereinigung([1], [1,2]) -> [1,2]
#   P3 else:                             Element nicht in menge2 -> aufgenommen
#                                        z.B. vereinigung([3], [1,2]) -> [3,1,2]
#   P4 Kombination ueber mehrere Rekursionsstufen (P2 und P3 abwechselnd)
#                                        z.B. vereinigung([1,2,3],[1,2]) -> [3,1,2]
# =========================================================================


def test_vereinigung_basisfall_leer():
    assert aufgabe02.vereinigung([], [1, 2]) == [1, 2]


def test_vereinigung_element_bereits_enthalten():
    assert aufgabe02.vereinigung([1], [1, 2]) == [1, 2]


def test_vereinigung_element_neu():
    assert aufgabe02.vereinigung([3], [1, 2]) == [3, 1, 2]


def test_vereinigung_gemischt():
    assert aufgabe02.vereinigung([1, 2, 3], [1, 2]) == [3, 1, 2]
