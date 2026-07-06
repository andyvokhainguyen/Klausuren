"""
Aufgabe 6 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

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
