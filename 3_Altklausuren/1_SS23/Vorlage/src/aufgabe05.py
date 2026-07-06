"""
Aufgabe 5 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

def string_operations(string_list, index):
    if not isinstance(string_list, list) or not isinstance(index, int):
        raise TypeError
    
    return string_list[index].replace(" ", "").lower()

# Beispielaufruf und Überprüfung
assert string_operations(["Hallo Welt", "Python Exceptions"], 0) == "hallowelt"

