"""
Aufgabe 2 - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

def foo(x, a):
    """
    x: Ein positiver ganzzahliger Parameter
    a: Ein positiver ganzzahliger Parameter
    Gibt eine ganze Zahl zurück
    """
    zaehler = 0

    while x >= a:
        zaehler += 1
        x = x - a

    return zaehler


def vereinigung(menge1, menge2):
    """
    menge1 und menge2 sind Sammlungen von Objekten, von denen jede leer sein könnte.
    Jede Menge hat innerhalb ihrer selbst keine Duplikate, es kann jedoch Objekte ge-ben,
    die in beiden Mengen vorkommen. Es wird angenommen, dass die Objekte vom gleichen Typ sind.

    Diese Funktion gibt eine Menge zurück, die alle Elemente aus beiden Eingabemengen enthält,
    jedoch ohne Duplikate.
    """
    if len(menge1) == 0:
        return menge2
    elif menge1[0] in menge2:
        return vereinigung(menge1[1:], menge2)
    else:
        return [menge1[0]] + vereinigung(menge1[1:], menge2)


# Beispielaufruf
print(vereinigung([1, 2, 3], [1, 2]))
print(vereinigung(["a", "d", "f"], ["f", "t"]))
