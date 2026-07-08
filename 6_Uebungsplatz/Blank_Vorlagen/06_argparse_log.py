"""
Übung 06: Log-Analyse-Tool mit argparse (ALTERNATIVE zu getopt)

Gleiche Aufgabe wie 05, aber mit argparse. Hinweis: In der Klausur ist laut
Hilfsmittelblatt nur getopt erlaubt - argparse hier nur zum Vergleich/Üben.
argparse übernimmt Pflicht (required) und Gültigkeit (choices) automatisch.

Beispielaufruf:  python3 06_argparse_log.py -i log.txt -o ergebnis.txt -b level
"""

import argparse


def zaehle(dateiname, befehl):
    # ✍️ SELBST: wie in 05 - Datei zeilenweise einlesen und je nach befehl zählen
    zaehler = {}
    with open(dateiname, "r", encoding="utf-8") as datei:
        for zeile in datei:
            teile = zeile.strip().split(";")
            if len(teile) != 4:
                continue
            _zeit, level, user, action = teile
            if befehl == "level":
                schluessel = level
            elif befehl == "user":
                schluessel = user
            else:
                schluessel = action
            zaehler[schluessel] = zaehler.get(schluessel, 0) + 1
    return zaehler


def schreibe_ergebnis(dateiname, befehl, zaehler):
    # ✍️ SELBST: wie in 05 - Ergebnis in die Datei schreiben
    with open(dateiname, "w", encoding="utf-8") as datei:
        datei.write(f"Befehl: {befehl}\n")
        for schluessel, anzahl in zaehler.items():
            datei.write(f"{schluessel}: {anzahl}\n")


def main():
    # ✍️ SELBST: Parser aufbauen
    #   parser = argparse.ArgumentParser(description="...")
    #   parser.add_argument("--input",  "-i", required=True)
    #   parser.add_argument("--output", "-o", required=True)
    #   parser.add_argument("--befehl", "-b", required=True,
    #                       choices=["level", "user", "action"])
    #   args = parser.parse_args()
    #   ergebnis = zaehle(args.input, args.befehl)
    #   schreibe_ergebnis(args.output, args.befehl, ergebnis)
    parser = argparse.ArgumentParser(description="Analyse-Tool für Logdateien.")
    parser.add_argument("--input", "-i", required=True)
    parser.add_argument("--output", "-o", required=True)
    parser.add_argument("--befehl", "-b", required=True,
                        choices=["level", "user", "action"])
    args = parser.parse_args()

    ergebnis = zaehle(args.input, args.befehl)
    schreibe_ergebnis(args.output, args.befehl, ergebnis)


if __name__ == "__main__":
    main()
