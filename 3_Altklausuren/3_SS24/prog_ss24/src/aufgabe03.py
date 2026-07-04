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
    try:
        # a) TypeError intern ausloesen, falls Parametertypen nicht stimmen ...
        if (
            not isinstance(list_c, list)
            or not isinstance(list_d, list)
            or not isinstance(idx, int)
        ):
            raise TypeError

        ergebnis = float(list_c[idx]) - float(list_d[idx])
    except TypeError:
        # a) ... und mit benutzerdefinierter Meldung abfangen
        print("Fehler: list_c und list_d muessen Listen sein und idx ein Integer.")
    except IndexError:
        # b) Index ausserhalb des gueltigen Bereichs der Listen
        print("Fehler: Der Index liegt ausserhalb des Bereichs der Listen.")
    except ValueError:
        # c) nicht-numerische Elemente -> float() schlaegt fehl
        print("Fehler: Die Listen duerfen nur in Zahlen umwandelbare Werte enthalten.")
    else:
        # d) nur wenn KEINE Exception auftrat, das Ergebnis zurueckgeben
        return ergebnis
    finally:
        # e) wird IMMER ausgefuehrt
        print("Die Funktion calculate_difference_at_index wurde ausgefuehrt.")


# Beispielaufruf und Überprüfung
assert calculate_difference_at_index([10, 20, 30, 40], [1, 2, 3, 4], 2) == 27

assert not calculate_difference_at_index([10, 20, 30, 40], [1, 2, 3, 4], 3) == 3

# Weitere Beispielaufrufe (zeigen die Fehlerbehandlung):
calculate_difference_at_index("keine_liste", [1], 0)  # TypeError
calculate_difference_at_index([1], [2], 5)             # IndexError
calculate_difference_at_index([1], ["x"], 0)           # ValueError
