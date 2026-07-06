"""
Aufgabe 4 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

import sys
import getopt


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
