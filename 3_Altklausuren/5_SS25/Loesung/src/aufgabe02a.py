"""
Aufgabe 2a - Klausur Programmierung
"""

def finde_groesste_gerade_zahl(zahlenliste):
    """
    Bestimmt die größte gerade Zahl in einer gegebenen Liste von Ganzzahlen.

    Parameter:
    ----------
    zahlenliste : list of int
        Eine Liste von Ganzzahlen. Die Liste kann beliebig viele Elemente enthalten, aber auch leer sein.

    Rückgabewert:
    -------------
    int oder str
        - Gibt die größte gerade Zahl in der Liste zurück, falls mindestens eine gerade Zahl vorhanden ist.
        - Gibt den String "Keine gerade Zahl gefunden" zurück, falls keine gerade Zahl in der Liste vorhanden ist.

    Hinweise:
    ---------
    - Die Reihenfolge der Elemente in der Liste ist beliebig.
    - Negative gerade Zahlen werden ebenfalls berücksichtigt.
    - Bei mehrfach vorkommenden gleichen geraden Zahlen wird der Wert nur einmal zurückgegeben.
    """
    groesste = None
    for zahl in zahlenliste:
        if zahl % 2 == 0:
            if groesste is None or zahl > groesste:
                groesste = zahl
    if groesste is None:
        return "Keine gerade Zahl gefunden"
    return groesste
