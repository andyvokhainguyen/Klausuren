"""
Aufgabe 4 - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

import sys
import getopt


def zahl_einlesen(text):
    """Wandelt einen String in int (falls moeglich) oder float um."""
    try:
        return int(text)
    except ValueError:
        return float(text)


def berechne(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        if b == 0:
            raise ZeroDivisionError
        return a / b
    else:
        raise ValueError("Unbekannte Operation: " + str(operation))


def main(argv):
    a = b = None
    operation = ""
    dateiname = ""

    # Kommandozeilenargumente mit getopt einlesen
    try:
        opts, args = getopt.getopt(argv, "a:b:o:f:h", ["help"])
    except getopt.GetoptError:
        print("Fehler: aufgabe04.py -a <zahl> -b <zahl> -o <add|sub|mul|div> "
              "-f <dateiname>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("aufgabe04.py -a <zahl> -b <zahl> -o <add|sub|mul|div> "
                  "-f <dateiname>")
            sys.exit()
        elif opt == "-a":
            a = zahl_einlesen(arg)
        elif opt == "-b":
            b = zahl_einlesen(arg)
        elif opt == "-o":
            operation = arg
        elif opt == "-f":
            dateiname = arg

    # Pruefen, ob alle noetigen Argumente vorhanden sind
    if a is None or b is None or operation == "" or dateiname == "":
        print("Fehler: Es fehlen Argumente. Erforderlich: -a, -b, -o, -f")
        sys.exit(2)

    # Berechnung durchfuehren (mit Fehlerbehandlung)
    try:
        ergebnis = berechne(a, b, operation)
    except ZeroDivisionError:
        print("Fehler: Division durch Null ist nicht erlaubt.")
        sys.exit(1)
    except ValueError as fehler:
        print("Fehler:", fehler)
        sys.exit(1)

    # Ergebnis in die Datei schreiben
    with open(dateiname, "w", encoding="utf-8") as datei:
        datei.write("Ergebnis: " + str(ergebnis) + "\n")


if __name__ == "__main__":
    main(sys.argv[1:])
