"""
Aufgabe 2b - Klausur Programmierung
"""

def schnittmenge(menge1, menge2):
    """
    Bestimmt die Schnittmenge zweier Listen, indem alle Elemente,
    die in beiden Listen vorkommen, gesammelt werden.

    Die Funktion arbeitet rekursiv und prüft jedes Element aus `menge1`,
    ob es auch in `menge2` vorhanden ist. Die Reihenfolge der gefundenen
    Elemente entspricht der Reihenfolge in `menge1`.

    Parameter:
    ----------
    menge1 : list
        Eine Liste von beliebigen Objekten. Die Liste kann leer sein.
    
    menge2 : list
        Eine weitere Liste von beliebigen Objekten. Die Liste kann ebenfalls leer sein.

    Rückgabewert:
    -------------
    list
        Eine Liste aller Elemente, die sowohl in `menge1` als auch in `menge2` vorkommen.
        Falls keine gemeinsamen Elemente existieren, wird eine leere Liste zurückgegeben.

    Hinweise:
    ---------
    - Die Funktion prüft jedes Element einzeln und rekursiv.
    - Mehrfache Vorkommen eines Elements in `menge1` werden mehrfach in der Rückgabe enthalten,
      sofern das Element in `menge2` existiert.
    - Die Reihenfolge der Rückgabewerte entspricht der von `menge1`.
    - Die Funktion verwendet keine Mengenoperationen und ist nicht auf bestimmte Datentypen beschränkt.
    """
    if not menge1:
        return []
    elif menge1[0] in menge2:
        return [menge1[0]] + schnittmenge(menge1[1:], menge2)
    else:
        return schnittmenge(menge1[1:], menge2)
