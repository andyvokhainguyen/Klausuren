"""
Aufgabe 4 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

import argparse


# Hilfs-Funktion für Verschlüsselung
def atbash_chiffrieren(input_string):
    chiffrierter_text = ""

    for char in input_string:
        if char.isalpha():
            # Bestimmen der Position des Buchstabens im Alphabet
            ascii_offset = 65 if char.isupper() else 97
            chiffrierter_text += chr(25 - (ord(char) - ascii_offset) + ascii_offset)
        else:
            chiffrierter_text += char
    return chiffrierter_text


def atbash_dechiffrieren(input_string):
    # Bei der Atbash-Chiffre ist die Chiffrierung identisch mit der Dechiffrierung
    return atbash_chiffrieren(input_string)


def main():
    parser = argparse.ArgumentParser(
        description="Verschluesselt/entschluesselt eine Textdatei zeilenweise "
                    "mit der Atbash-Chiffre."
    )
    parser.add_argument("--infile", "-i", required=True,
                        help="gibt die Eingabedatei an")
    parser.add_argument("--outfile", "-o", required=True,
                        help="gibt die Ausgabedatei an")
    parser.add_argument("--chiffrieren", "-c", action="store_true",
                        help="Eingabedatei verschluesseln")
    parser.add_argument("--dechiffrieren", "-d", action="store_true",
                        help="Eingabedatei entschluesseln")
    args = parser.parse_args()

    # -c und -d schliessen sich gegenseitig aus (ohne mutually_exclusive_group
    # selbst pruefen): genau eins muss gewaehlt sein.
    if args.chiffrieren == args.dechiffrieren:
        parser.error("Bitte genau eine Option angeben: -c ODER -d.")

    # Eingabedatei zeilenweise lesen, verarbeiten und in Ausgabedatei schreiben.
    # (Bei Atbash sind Ver- und Entschluesselung identisch; beide Flags werden
    #  dennoch korrekt akzeptiert.)
    with open(args.infile, "r", encoding="utf-8") as ein, \
         open(args.outfile, "w", encoding="utf-8") as aus:
        for zeile in ein:
            if args.chiffrieren:
                aus.write(atbash_chiffrieren(zeile))
            else:  # args.dechiffrieren
                aus.write(atbash_dechiffrieren(zeile))


if __name__ == "__main__":
    main()
