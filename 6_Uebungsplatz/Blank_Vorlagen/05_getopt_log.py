"""
Übung 05: Log-Analyse-Tool mit getopt (Kommandozeile + Datei, SS25/WS2526)

So gibt der Prof es vor: nur der Docstring mit Beispielaufruf. Rest selbst.
getopt ist das in der Klausur ERLAUBTE Verfahren.

Beispielaufruf:  python3 05_getopt_log.py -i log.txt -o ergebnis.txt -b level
Logformat je Zeile:  zeit;LEVEL;user;action
"""

import sys
import getopt


def zaehle(dateiname, befehl):
    # ✍️ SELBST:
    #   with open(dateiname, "r", encoding="utf-8") as datei:
    #       for zeile in datei:
    #           teile = zeile.strip().split(";")   # 4 Teile erwartet
    #           je nach befehl (level/user/action) das passende Feld zählen (dict)
    #   Zähler zurückgeben
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
            if schluessel in zaehler:
                zaehler[schluessel] += 1
            else:
                zaehler[schluessel] = 1
    return zaehler


def schreibe_ergebnis(dateiname, befehl, zaehler):
    # ✍️ SELBST:
    #   with open(dateiname, "w", encoding="utf-8") as datei:
    #       datei.write(f"Befehl: {befehl}\n")
    #       für jeden Eintrag: datei.write(f"{schluessel}: {anzahl}\n")
    with open(dateiname, "w", encoding="utf-8") as datei:
        datei.write(f"Befehl: {befehl}\n")
        for schluessel, anzahl in zaehler.items():
            datei.write(f"{schluessel}: {anzahl}\n")


def main(argv):
    eingabe = None
    ausgabe = None
    befehl = None
    # ✍️ SELBST: getopt-Optionen einlesen
    #   opts, args = getopt.getopt(argv, "i:o:b:h", ["input=","output=","befehl=","help"])
    #   for opt, wert in opts:  -i/-o/-b zuweisen; -h -> Hilfe + sys.exit()
    #   danach: Pflicht-Args prüfen; ergebnis = zaehle(...); schreibe_ergebnis(...)
    try:
        opts, args = getopt.getopt(argv, "i:o:b:h",
                                   ["input=", "output=", "befehl=", "help"])
    except getopt.GetoptError as fehler:
        print("Fehler:", fehler)
        sys.exit(2)

    for opt, wert in opts:
        if opt in ("-h", "--help"):
            print("prog.py -i <log> -o <out> -b <level|user|action>")
            sys.exit()
        elif opt in ("-i", "--input"):
            eingabe = wert
        elif opt in ("-o", "--output"):
            ausgabe = wert
        elif opt in ("-b", "--befehl"):
            befehl = wert

    if eingabe is None or ausgabe is None or befehl is None:
        print("Fehler: -i, -o, -b sind Pflicht.")
        sys.exit(2)
    if befehl not in ("level", "user", "action"):
        print("Fehler: -b muss level, user oder action sein.")
        sys.exit(2)

    ergebnis = zaehle(eingabe, befehl)
    schreibe_ergebnis(ausgabe, befehl, ergebnis)


if __name__ == "__main__":
    main(sys.argv[1:])
