"""
Aufgabe 8 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""


def quicksort(input_text):
    # Basisfall: 0 oder 1 Zeichen ist bereits sortiert
    if len(input_text) <= 1:
        return input_text

    # Pivot = erstes Zeichen; Rest in "kleiner-gleich" und "groesser" aufteilen.
    # '<=' behaelt mehrfach vorkommende (identische) Zeichen, sonst gingen sie verloren.
    pivot = input_text[0]
    kleiner = [zeichen for zeichen in input_text[1:] if zeichen <= pivot]
    groesser = [zeichen for zeichen in input_text[1:] if zeichen > pivot]

    # Rekursiv sortieren und wieder zu einem String zusammensetzen
    return quicksort("".join(kleiner)) + pivot + quicksort("".join(groesser))


# Testen Sie Ihre Implementierung mit dem folgenden Code
text = input("Bitte Text ohne Sonder- und Leerzeichen eingeben: ").lower()

# Erwartete Ausgabe: identische Zeichen, jedoch alphabetisch sortiert
print(quicksort(text))
