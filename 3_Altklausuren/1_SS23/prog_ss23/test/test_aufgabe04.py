"""
Aufgabe 4 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

# Aufruf des Tests in der Kommandozeile mit folgendem Befehl: python -m pytest -v
# Alternativ links in Visual Studio Code die Test-Umgebung öffnen (Klick auf das Reagenzglas)

import pytest

from prog_ss23.src import aufgabe04


# =========================================================================
# a) Aequivalenzklassen fuer bmi_klassifizierung(gewicht, groesse)
#    (moeglichst ueberschneidungsfrei; je Klasse ein repraesentativer Wert)
#
#   K1 Untergewicht   bmi < 18.5           z.B. 50 kg / 1.75 m -> "Untergewicht"
#   K2 Normalgewicht  18.5 <= bmi < 25     z.B. 70 kg / 1.75 m -> "Normalgewicht"
#   K3 Uebergewicht   25 <= bmi < 30       z.B. 80 kg / 1.70 m -> "Uebergewicht"
#   K4 Adipositas     bmi >= 30            z.B. 100 kg / 1.70 m -> "Adipositas"
#   K5 GRENZWERT 18.5 bmi == 18.5          z.B. 74 kg / 2.00 m -> "Normalgewicht"
#
#   Begruendung: Jede der vier if/elif/else-Kategorien wird durch genau eine
#   Klasse abgedeckt (ueberschneidungsfrei), K5 prueft zusaetzlich die
#   kritische Grenze 18.5 (der Wert gehoert laut Code noch zu "Normalgewicht").
# =========================================================================


def test_bmi_untergewicht():
    assert aufgabe04.bmi_klassifizierung(50, 1.75) == "Untergewicht"


def test_bmi_normalgewicht():
    assert aufgabe04.bmi_klassifizierung(70, 1.75) == "Normalgewicht"


def test_bmi_uebergewicht():
    assert aufgabe04.bmi_klassifizierung(80, 1.70) == "Übergewicht"


def test_bmi_adipositas():
    assert aufgabe04.bmi_klassifizierung(100, 1.70) == "Adipositas"


def test_bmi_grenzwert_18_5():
    # 74 / (2.0**2) = 18.5 -> gehoert noch zu Normalgewicht
    assert aufgabe04.bmi_klassifizierung(74, 2.0) == "Normalgewicht"


# =========================================================================
# b) Aequivalenzklassen fuer addiere_positive_zahlen(zahlenliste)
#
#   K1 leere Liste                 []             -> 0
#   K2 nur positive Zahlen         [2, 4, 6]      -> 12
#   K3 nur negative Zahlen         [-1, -2, -3]   -> 0
#   K4 gemischt positiv/negativ    [2, 4, 6, -8, 10] -> 22
#   K5 enthaelt die 0 (Grenzwert)  [0, 5]         -> 5  (0 ist nicht > 0)
#
#   Begruendung: leere vs. nicht-leere Liste, ausschliesslich positiv vs.
#   ausschliesslich negativ vs. gemischt, sowie der Grenzwert 0 (der wegen
#   "zahl > 0" nicht mitgezaehlt werden darf).
# =========================================================================


def test_addiere_leere_liste():
    assert aufgabe04.addiere_positive_zahlen([]) == 0


def test_addiere_nur_positive():
    assert aufgabe04.addiere_positive_zahlen([2, 4, 6]) == 12


def test_addiere_nur_negative():
    assert aufgabe04.addiere_positive_zahlen([-1, -2, -3]) == 0


def test_addiere_gemischt():
    assert aufgabe04.addiere_positive_zahlen([2, 4, 6, -8, 10]) == 22


def test_addiere_grenzwert_null():
    assert aufgabe04.addiere_positive_zahlen([0, 5]) == 5
