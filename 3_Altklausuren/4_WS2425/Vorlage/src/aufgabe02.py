"""
Aufgabe 2 - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

def minOfThree(a, b, c):
    """ 
    a, b und c sind Zahlen
    Gibt das Minimum von a, b und c zurück
    """
    if a < b:
        kleiner = a
    else:
        kleiner = b

    if c < kleiner:
        kleiner = c

    return kleiner

# Beispielaufruf 
print(minOfThree(1,2,3))
print(minOfThree(47,23,24))

def ggt(a, b):
    """ 
    Berechnet den größten gemeinsamen Teiler (GGT) zweier Zahlen 
    a und b müssen ganze Zahlen größer als 0 sein.
    Gibt den GGT von a und b zurück.
    """
    if b == 0:
        return a
    else:
        return ggt(b, a % b)

# Beispielaufruf 
print(ggt(18, 27))
print(ggt(42, 70))
