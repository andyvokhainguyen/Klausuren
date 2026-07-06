"""
Aufgabe 2 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

import pytest

from src import aufgabe02


def test_blutdruck_klassifizierung():
    assert aufgabe02.blutdruck_klassifizierung(100, 70) == "Normal"


def test_finde_erste_negative_zahl():
    assert aufgabe02.finde_erste_negative_zahl([2, 4, 6, -8, 10]) == -8
