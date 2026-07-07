from src import aufgabe4b

import pytest

def test_fakultaet_negativ():
    assert aufgabe4b.fakultaet(-5) == None

def test_fakultaet_basisfall():
    assert aufgabe4b.fakultaet(0) == 1

def test_fakultaet_eine_rekursion():
    assert aufgabe4b.fakultaet(1) == 1

def test_fakultaet_mehrere_rekursionen():
    assert aufgabe4b.fakultaet(5) == 120