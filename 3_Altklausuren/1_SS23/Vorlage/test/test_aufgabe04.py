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

from src import aufgabe04


def test_bmi():
    assert aufgabe04.bmi_klassifizierung(70, 1.75) == "Normalgewicht"


def test_addiere_positive_zahlen():
    assert aufgabe04.addiere_positive_zahlen([2, 4, 6, -8, 10]) == 22
