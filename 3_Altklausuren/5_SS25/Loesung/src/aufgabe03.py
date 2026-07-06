"""
Aufgabe 3 - Klausur Programmierung

Kleines Analyse-Tool fuer Logdateien im Format:
YYYY-MM-DD HH:MM:SS [LEVEL] Nachricht

Beispielaufruf:
    python3 aufgabe03.py -i log.txt -o ergebnis.txt -b errors
"""

import argparse


def zaehle(pfad, befehl):
    """
    Liest die Logdatei unter `pfad` ein und wertet sie je nach `befehl`
    aus:
    - count    : Anzahl aller Zeilen in der Datei
    - errors   : Anzahl der Zeilen, die das Wort ERROR enthalten
    - warnings : Anzahl der Zeilen, die das Wort WARNING enthalten
    """
    anzahl = 0
    with open(pfad, "r", encoding="utf-8") as datei:
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


def schreibe_ergebnis(pfad, befehl, ergebnis):
    with open(pfad, "w", encoding="utf-8") as datei:
        datei.write(f"Befehl: {befehl}\n")
        datei.write(f"Ergebnis: {ergebnis}\n")


def erstelle_parser():
    parser = argparse.ArgumentParser(
        description="Analyse-Tool fuer Logdateien."
    )
    parser.add_argument(
        "--input", "-i", required=True,
        help="Name der Eingabedatei (Pfad zu einer Textdatei im Log-Format)"
    )
    parser.add_argument(
        "--output", "-o", required=True,
        help="Name der Ausgabedatei, in die das Ergebnis geschrieben wird"
    )
    parser.add_argument(
        "--befehl", "-b", required=True,
        choices=["count", "errors", "warnings"],
        help="Auszufuehrender Befehl: 'count', 'errors' oder 'warnings'"
    )
    return parser


def main():
    parser = erstelle_parser()
    args = parser.parse_args()

    ergebnis = zaehle(args.input, args.befehl)
    schreibe_ergebnis(args.output, args.befehl, ergebnis)


if __name__ == "__main__":
    main()
