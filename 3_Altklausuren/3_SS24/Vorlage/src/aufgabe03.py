"""
Aufgabe 3 - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

def calculate_difference_at_index(list_c, list_d, idx):
    """
    Nimmt an: list_c und list_d sind Listen gleicher Länge mit Zahlen.
    Gibt zurück: list_c[idx] - list_d[idx]
    """

    if (
        not isinstance(list_c, list)
        or not isinstance(list_d, list)
        or not isinstance(idx, int)
    ):
        raise TypeError

    return float(list_c[idx]) - float(list_d[idx])


# Beispielaufruf und Überprüfung
assert calculate_difference_at_index([10, 20, 30, 40], [1, 2, 3, 4], 2) == 27

assert not calculate_difference_at_index([10, 20, 30, 40], [1, 2, 3, 4], 3) == 3
