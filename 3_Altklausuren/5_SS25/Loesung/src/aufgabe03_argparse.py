"""
Aufgabe 3 - Klausur Programmierung (ALTERNATIVE mit argparse)

Gleiche Funktion wie aufgabe03.py, aber die Kommandozeile wird mit
argparse statt getopt eingelesen.

Hinweis: In der Klausur ist laut Hilfsmittelblatt nur getopt erlaubt -
diese Variante dient nur zum Vergleich.

Beispielaufruf:
    python3 aufgabe03_argparse.py -i log.txt -o ergebnis.txt -b errors
"""

import argparse


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


def erstelle_parser():
    parser = argparse.ArgumentParser(
        description="Analyse-Tool fuer Logdateien."
    )
    parser.add_argument(
        "--input", "-i", required=True,
        help="Name der Eingabedatei (z.B. log.txt)"
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
