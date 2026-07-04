"""
Aufgabe 6 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

import argparse


# Hilfs-Funktion für Verschlüsselung
def caesar_chiffrieren(input_string, verschiebung):
    chiffrierter_text = ""

    for char in input_string:
        # Überprüfen, ob das Zeichen ein Buchstabe ist
        if char.isalpha():
            # Feststellen, ob das Zeichen ein Groß- oder Kleinbuchstabe ist
            ascii_offset = 65 if char.isupper() else 97
            chiffrierter_text += chr(
                (ord(char) - ascii_offset + verschiebung) % 26 + ascii_offset
            )
        else:
            chiffrierter_text += char
    return chiffrierter_text


# Hilfs-Funktion für Entschlüsselung
def caesar_dechiffrieren(input_string, verschiebung):
    return caesar_chiffrieren(input_string, -verschiebung)


def main():
    parser = argparse.ArgumentParser(
        description="Verschluesselt/entschluesselt eine Textdatei zeilenweise "
                    "mit einer Caesar-Verschiebung."
    )
    parser.add_argument("--infile", "-i", required=True,
                        help="gibt die Eingabedatei an")
    parser.add_argument("--outfile", "-o", required=True,
                        help="gibt die Ausgabedatei an")
    parser.add_argument("--shift", "-s", type=int, required=True,
                        help="Shift um Anzahl Zeichen im Alphabet")
    # -c und -d schliessen sich gegenseitig aus (genau eins muss gewaehlt werden)
    gruppe = parser.add_mutually_exclusive_group(required=True)
    gruppe.add_argument("--chiffrieren", "-c", action="store_true",
                        help="Eingabedatei verschluesseln")
    gruppe.add_argument("--dechiffrieren", "-d", action="store_true",
                        help="Eingabedatei entschluesseln")
    args = parser.parse_args()

    # Eingabedatei zeilenweise lesen, verarbeiten und in Ausgabedatei schreiben
    with open(args.infile, "r", encoding="utf-8") as ein, \
         open(args.outfile, "w", encoding="utf-8") as aus:
        for zeile in ein:
            if args.chiffrieren:
                aus.write(caesar_chiffrieren(zeile, args.shift))
            else:  # args.dechiffrieren
                aus.write(caesar_dechiffrieren(zeile, args.shift))


if __name__ == "__main__":
    main()
