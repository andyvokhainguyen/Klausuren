"""
Aufgabe 2 - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

from src import aufgabe02

import pytest

def test_minOfThree():
    assert not aufgabe02.minOfThree(1,2,3) == 7

def test_ggt():
    assert not aufgabe02.ggt(18, 27) == 48
