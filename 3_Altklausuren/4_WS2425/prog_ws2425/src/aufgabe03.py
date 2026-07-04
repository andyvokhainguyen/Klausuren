"""
Aufgabe 3 - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""


def fehlerhafte_berechnung(liste, index):
    """
    Nimmt an: liste ist eine Liste von Zahlen, index ist die Position des zu teilenden Werts.
    Gibt zurück: Den Wert an der gegebenen Indexposition, geteilt durch eine Benutzereingabe.
    """
    try:
        wert = liste[index]                 # a) evtl. IndexError

        eingabe = input("Geben Sie eine Zahl zum Dividieren ein: ")
        zahl = int(eingabe)                 # b) evtl. ValueError (keine Zahl)

        ergebnis = wert / zahl              # c) evtl. ZeroDivisionError
    except IndexError:
        # a) ungueltiger Index
        print("Fehler: Der angegebene Index liegt ausserhalb der Liste.")
    except ValueError:
        # b) Eingabe ist keine gueltige (ganze) Zahl
        print("Fehler: Bitte geben Sie eine gueltige Zahl ein.")
    except ZeroDivisionError:
        # c) Division durch Null
        print("Fehler: Division durch Null ist nicht erlaubt.")
    else:
        # d) nur wenn KEINE Exception auftrat: Ergebnis ausgeben und zurueckgeben
        print("Ergebnis:", ergebnis)
        return ergebnis
    finally:
        # e) wird IMMER ausgefuehrt
        print("Die Berechnung wurde abgeschlossen.")


# Beispielaufruf
liste = [10, 20, 30, 40]
index = int(input("Geben Sie den Index ein: "))
fehlerhafte_berechnung(liste, index)
