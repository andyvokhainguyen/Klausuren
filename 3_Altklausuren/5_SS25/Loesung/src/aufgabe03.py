"""
Aufgabe 3 - Klausur Programmierung

Kleines Analyse-Tool fuer Logdateien im Format:
YYYY-MM-DD HH:MM:SS [LEVEL] Nachricht

Beispielaufruf:
    python3 aufgabe03.py -i log.txt -o ergebnis.txt -b errors
"""

import sys
import getopt


def zaehle(dateiname, befehl):
    """
    Liest die Logdatei `dateiname` (z.B. "log.txt") zeilenweise ein und
    wertet sie je nach `befehl` aus:
    - count    : Anzahl aller (nicht leeren) Zeilen
    - errors   : Anzahl der Zeilen, die das Wort ERROR enthalten
    - warnings : Anzahl der Zeilen, die das Wort WARNING enthalten
    """
    anzahl = 0
    with open(dateiname, "r", encoding="utf-8") as datei:
        for zeile in datei:
            if zeile.strip() == "":
                continue
            if befehl == "count":
                anzahl += 1
            elif befehl == "errors":
                if "ERROR" in zeile:
                    anzahl += 1
            elif befehl == "warnings":
                if "WARNING" in zeile:
                    anzahl += 1
    return anzahl


def schreibe_ergebnis(dateiname, befehl, ergebnis):
    with open(dateiname, "w", encoding="utf-8") as datei:
        datei.write(f"Befehl: {befehl}\n")
        datei.write(f"Ergebnis: {ergebnis}\n")


def main(argv):
    eingabe = None
    ausgabe = None
    befehl = None

    try:
        opts, args = getopt.getopt(argv, "i:o:b:h",
                                   ["input=", "output=", "befehl=", "help"])
    except getopt.GetoptError as fehler:
        print("Fehler:", fehler)
        sys.exit(2)

    for opt, wert in opts:
        if opt in ("-h", "--help"):
            print("Aufruf: python3 aufgabe03.py -i <logdatei> "
                  "-o <ausgabedatei> -b <count|errors|warnings>")
            sys.exit()
        elif opt in ("-i", "--input"):
            eingabe = wert
        elif opt in ("-o", "--output"):
            ausgabe = wert
        elif opt in ("-b", "--befehl"):
            befehl = wert

    if eingabe is None or befehl is None:
        print("Fehler: -i und -b sind Pflicht.")
        sys.exit(2)
    if befehl not in ("count", "errors", "warnings"):
        print("Fehler: -b muss count, errors oder warnings sein.")
        sys.exit(2)

    ergebnis = zaehle(eingabe, befehl)

    if ausgabe:
        schreibe_ergebnis(ausgabe, befehl, ergebnis)
    else:
        print(f"Befehl: {befehl}")
        print(f"Ergebnis: {ergebnis}")


if __name__ == "__main__":
    main(sys.argv[1:])
