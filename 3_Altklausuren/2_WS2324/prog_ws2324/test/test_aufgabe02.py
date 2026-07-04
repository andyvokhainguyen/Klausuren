"""
Aufgabe 2 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

import pytest

from prog_ws2324.src import aufgabe02


# =========================================================================
# a) Aequivalenzklassen fuer blutdruck_klassifizierung(systolisch, diastolisch)
#
#   K1 Normal                 sys < 120 und dia < 80      z.B. (100, 70)
#   K2 Erhoeht                120<=sys<130 und dia < 80    z.B. (125, 70)
#   K3 Bluthochdruck Stufe 1  130<=sys<140 oder 80<=dia<90 z.B. (135, 75)
#   K4 Bluthochdruck Stufe 2  sys>=140 oder dia>=90        z.B. (145, 95)
#   K5 GRENZWERT sys==120     untere Grenze von "Erhoeht"  z.B. (120, 70)
#
#   Begruendung: Jede erreichbare Kategorie der if/elif-Kette wird durch genau
#   eine Klasse abgedeckt; K5 prueft die kritische Grenze 120 (dort beginnt
#   "Erhoeht"). Hinweis: der else-Zweig "Hypertensiver Krisenzustand" ist mit
#   diesen Bedingungen praktisch NICHT erreichbar (toter Code) und daher nicht
#   sinnvoll testbar.
# =========================================================================


def test_blutdruck_normal():
    assert aufgabe02.blutdruck_klassifizierung(100, 70) == "Normal"


def test_blutdruck_erhoeht():
    assert aufgabe02.blutdruck_klassifizierung(125, 70) == "Erhöht"


def test_blutdruck_stufe1():
    assert aufgabe02.blutdruck_klassifizierung(135, 75) == "Bluthochdruck (Stufe 1)"


def test_blutdruck_stufe2():
    assert aufgabe02.blutdruck_klassifizierung(145, 95) == "Bluthochdruck (Stufe 2)"


def test_blutdruck_grenzwert_120():
    assert aufgabe02.blutdruck_klassifizierung(120, 70) == "Erhöht"


# =========================================================================
# b) Aequivalenzklassen fuer finde_erste_negative_zahl(zahlenliste)
#
#   K1 leere Liste                 []            -> "Keine negative Zahl gefunden"
#   K2 nur positive Zahlen         [1, 2, 3]     -> "Keine negative Zahl gefunden"
#   K3 erste Zahl ist negativ      [-5, 2, 3]    -> -5   (Randfall Anfang)
#   K4 nur letzte Zahl negativ     [2, 4, -8]    -> -8   (Schleife laeuft ganz durch)
#   K5 mehrere negative Zahlen     [3, -1, -2]   -> -1   (die ERSTE wird geliefert)
#
#   Begruendung: leere vs. nicht-leere Liste; keine negative Zahl vs. negative
#   Zahl am Anfang / am Ende / mehrfach. K5 prueft, dass wirklich die ERSTE
#   negative Zahl zurueckgegeben wird.
# =========================================================================


def test_negative_leere_liste():
    assert aufgabe02.finde_erste_negative_zahl([]) == "Keine negative Zahl gefunden"


def test_negative_nur_positive():
    assert aufgabe02.finde_erste_negative_zahl([1, 2, 3]) == "Keine negative Zahl gefunden"


def test_negative_am_anfang():
    assert aufgabe02.finde_erste_negative_zahl([-5, 2, 3]) == -5


def test_negative_am_ende():
    assert aufgabe02.finde_erste_negative_zahl([2, 4, -8]) == -8


def test_negative_mehrere():
    assert aufgabe02.finde_erste_negative_zahl([3, -1, -2]) == -1
