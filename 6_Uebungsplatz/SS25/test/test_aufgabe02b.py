"""
Aufgabe 2b - Klausur Programmierung
"""

from src import aufgabe02b

import pytest

def test_schnittmenge():
    assert aufgabe02b.schnittmenge([1, 2, 3], [2, 4]) == [2]
