"""
Aufgabe 3 - Klausur Programmierung WS2025/26

Kleines Analyse-Tool fuer Logdateien im Format:
YYYY-MM-DD HH:MM:SS;LEVEL;USER;ACTION

Beispielaufruf:
    python3 aufgabe03.py -i log.txt -o ergebnis.txt -b level
"""

import argparse
from collections import Counter


def parse_zeile(zeile):
    """
    Zerlegt eine Logzeile im Format "YYYY-MM-DD HH:MM:SS;LEVEL;USER;ACTION"
    in ihre Bestandteile. Gibt None zurueck, wenn die Zeile nicht dem
    erwarteten Format entspricht (z.B. leere Zeile).
    """
    teile = zeile.strip().split(";")
    if len(teile) != 4:
        return None
    _zeitstempel, level, user, action = teile
    return level, user, action


def werte_logdatei_aus(pfad, befehl):
    """
    Liest die Logdatei unter `pfad` ein und zaehlt je nach `befehl` die
    Vorkommen pro ACTION, USER oder LEVEL. Gibt ein Counter-Objekt zurueck.
    """
    zaehler = Counter()
    with open(pfad, "r", encoding="utf-8") as datei:
        for zeile in datei:
            geparst = parse_zeile(zeile)
            if geparst is None:
                continue
            level, user, action = geparst
            if befehl == "actions":
                zaehler[action] += 1
            elif befehl == "user":
                zaehler[user] += 1
            elif befehl == "level":
                zaehler[level] += 1
    return zaehler


def schreibe_ergebnis(pfad, befehl, zaehler):
    with open(pfad, "w", encoding="utf-8") as datei:
        datei.write(f"Befehl: {befehl}\n")
        for schluessel, anzahl in zaehler.items():
            datei.write(f"{schluessel}: {anzahl}\n")


def erstelle_parser():
    parser = argparse.ArgumentParser(
        description="Analyse-Tool fuer Logdateien (Format: "
                     "YYYY-MM-DD HH:MM:SS;LEVEL;USER;ACTION)."
    )
    parser.add_argument(
        "--input", "-i", required=True,
        help="Pfad zur Eingabedatei (Textdatei im Log-Format)"
    )
    parser.add_argument(
        "--output", "-o", required=True,
        help="Name der Ausgabedatei, in die das Ergebnis geschrieben wird"
    )
    parser.add_argument(
        "--befehl", "-b", required=True,
        choices=["actions", "user", "level"],
        help="Auszufuehrender Befehl: 'actions', 'user' oder 'level'"
    )
    return parser


def main():
    parser = erstelle_parser()
    args = parser.parse_args()

    zaehler = werte_logdatei_aus(args.input, args.befehl)
    schreibe_ergebnis(args.output, args.befehl, zaehler)


if __name__ == "__main__":
    main()
