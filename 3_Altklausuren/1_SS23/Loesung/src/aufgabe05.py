"""
Aufgabe 5 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""


def string_operations(string_list, index):
    try:
        # a) TypeError: falscher Parametertyp intern ausloesen ...
        if not isinstance(string_list, list) or not isinstance(index, int):
            raise TypeError
        ergebnis = string_list[index].replace(" ", "").lower()
    except TypeError:
        # a) ... und mit benutzerdefinierter Fehlermeldung abfangen
        print("Fehler: Der erste Parameter muss eine Liste und der zweite "
              "Parameter ein Integer sein.")
    except IndexError:
        # b) Index ausserhalb des gueltigen Bereichs der Liste
        print("Fehler: Der angegebene Index liegt ausserhalb des Bereichs "
              "der Liste.")
    else:
        # c) nur wenn KEINE Exception auftrat, den modifizierten String zurueckgeben
        return ergebnis
    finally:
        # d) wird IMMER ausgefuehrt, egal ob eine Exception auftrat oder nicht
        print("Die Funktion string_operations wurde ausgefuehrt.")


# Beispielaufruf und Überprüfung
assert string_operations(["Hallo Welt", "Python Exceptions"], 0) == "hallowelt"

# Weitere Beispielaufrufe (zeigen die Fehlerbehandlung):
string_operations("kein_list", 0)   # -> TypeError-Meldung
string_operations(["nur ein Element"], 5)  # -> IndexError-Meldung
