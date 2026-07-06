"""
Aufgabe 2a - Klausur Programmierung
Tests entsprechend der fuenf Aequivalenzklassen aus
prog_ss25/src/aufgabe02a.txt
"""

from src import aufgabe02a

import pytest


def test_finde_groesste_gerade_zahl_leere_liste():
    # K1: leere Liste
    assert aufgabe02a.finde_groesste_gerade_zahl([]) == "Keine gerade Zahl gefunden"


def test_finde_groesste_gerade_zahl_keine_gerade_zahl_vorhanden():
    # K2: ausschliesslich ungerade Zahlen
    assert aufgabe02a.finde_groesste_gerade_zahl([1, 3, 5, 7]) == "Keine gerade Zahl gefunden"


def test_finde_groesste_gerade_zahl_gemischte_liste():
    # K3: Normalfall, gemischte gerade/ungerade Zahlen
    assert aufgabe02a.finde_groesste_gerade_zahl([3, 7, 8, 2, 10, 5]) == 10


def test_finde_groesste_gerade_zahl_negative_werte():
    # K4: (auch) negative gerade Zahlen
    assert aufgabe02a.finde_groesste_gerade_zahl([-4, -2, -10, 3]) == -2


def test_finde_groesste_gerade_zahl_mehrfach_vorkommende_zahl():
    # K5: die groesste gerade Zahl kommt mehrfach vor
    assert aufgabe02a.finde_groesste_gerade_zahl([4, 8, 8, 2]) == 8
