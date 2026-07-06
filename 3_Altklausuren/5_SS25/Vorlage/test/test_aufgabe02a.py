"""
Aufgabe 2a - Klausur Programmierung
"""

from src import aufgabe02a

import pytest

def test_finde_groesste_gerade_zahl():
    assert aufgabe02a.finde_groesste_gerade_zahl([3, 7, 8, 2, 10, 5]) == 10
