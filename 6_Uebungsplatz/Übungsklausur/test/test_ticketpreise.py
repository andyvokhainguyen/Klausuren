from src import aufgabe4a

import pytest

def test_ticket_ungültig():
    assert aufgabe4a.berechne_ticketpreis(-5) == "Ungültiges Alter"

def test_ticket_kind():
    assert aufgabe4a.berechne_ticketpreis(10) == 5.0

def test_ticket_erwachsener():
    assert aufgabe4a.berechne_ticketpreis(50) == 10.0

def test_ticket_senior():
    assert aufgabe4a.berechne_ticketpreis(70) == 7.5

def test_ticket_grenzwert():
    assert aufgabe4a.berechne_ticketpreis(65) == 10.0