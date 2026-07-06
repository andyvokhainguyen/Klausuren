"""
Aufgabe 2 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""


def blutdruck_klassifizierung(systolisch, diastolisch):
    if systolisch < 120 and diastolisch < 80:
        return "Normal"
    elif 120 <= systolisch < 130 and diastolisch < 80:
        return "Erhöht"
    elif 130 <= systolisch < 140 or 80 <= diastolisch < 90:
        return "Bluthochdruck (Stufe 1)"
    elif systolisch >= 140 or diastolisch >= 90:
        return "Bluthochdruck (Stufe 2)"
    else:
        return "Hypertensiver Krisenzustand"


def finde_erste_negative_zahl(zahlenliste):
    index = 0
    while index < len(zahlenliste):
        if zahlenliste[index] < 0:
            return zahlenliste[index]
        index += 1
    return "Keine negative Zahl gefunden"
