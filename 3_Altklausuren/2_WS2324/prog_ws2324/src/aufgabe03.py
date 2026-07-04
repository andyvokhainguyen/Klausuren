"""
Aufgabe 3 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""


def get_ratio_at_position(list_a, list_b, pos_in_list):
    """Assumes: list_a and list_b are lists of equal length of numbers
    Returns: List_a[pos_in_list]/List_b[pos_in_list]"""

    try:
        # a) TypeError intern ausloesen, falls Parametertypen nicht stimmen ...
        if (
            not isinstance(list_a, list)
            or not isinstance(list_b, list)
            or not isinstance(pos_in_list, int)
        ):
            raise TypeError

        ergebnis = float(list_a[pos_in_list]) / float(list_b[pos_in_list])
    except TypeError:
        # a) ... und mit benutzerdefinierter Meldung abfangen
        print("Fehler: list_a und list_b muessen Listen sein und pos_in_list "
              "ein Integer.")
    except IndexError:
        # b) Index ausserhalb des gueltigen Bereichs der Listen
        print("Fehler: Der Index liegt ausserhalb des Bereichs der Listen.")
    except ZeroDivisionError:
        # c) Division durch Null (Wert in list_b ist 0)
        print("Fehler: Division durch Null ist nicht erlaubt.")
    except ValueError:
        # d) Listen enthalten nicht nur Zahlen (z.B. String) -> float() schlaegt fehl
        print("Fehler: Die Listen duerfen nur in Zahlen umwandelbare Werte "
              "enthalten.")
    else:
        # e) nur wenn KEINE Exception auftrat, das Ergebnis zurueckgeben
        return ergebnis
    finally:
        # f) wird IMMER ausgefuehrt
        print("Die Funktion get_ratio_at_position wurde ausgefuehrt.")


# Beispielaufruf und Überprüfung
assert get_ratio_at_position([2, 3, 6, 9], [1, 2, 3, 4], 2) == 2

assert not get_ratio_at_position([2, 3, 6, 9], [1, 2, 3, 4], 3) == 3

# Weitere Beispielaufrufe (zeigen die Fehlerbehandlung):
get_ratio_at_position("keine_liste", [1], 0)   # TypeError
get_ratio_at_position([1], [2], 5)              # IndexError
get_ratio_at_position([1], [0], 0)              # ZeroDivisionError
get_ratio_at_position([1], ["x"], 0)            # ValueError
