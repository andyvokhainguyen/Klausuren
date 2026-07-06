"""
Aufgabe 2 - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

from src import aufgabe02
import pytest

def test_foo():
    assert not aufgabe02.foo(1,2) == 1

def test_vereinigung():
    assert aufgabe02.vereinigung([1, 2, 3], [1, 2]) == [3, 1, 2]
