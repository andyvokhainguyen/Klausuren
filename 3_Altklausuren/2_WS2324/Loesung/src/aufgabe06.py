"""
Aufgabe 6 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""


def insertionsort(input_text):
    # String in eine Liste von Zeichen umwandeln (Strings sind unveraenderlich)
    zeichen = list(input_text)
    n = len(zeichen)

    # Insertion-Sort: sortierten Bereich links aufbauen, jedes neue Zeichen
    # an die richtige Stelle einschieben.
    for i in range(1, n):
        pivot = zeichen[i]
        j = i - 1
        # groessere Zeichen nach rechts schieben
        while j >= 0 and zeichen[j] > pivot:
            zeichen[j + 1] = zeichen[j]
            j -= 1
        zeichen[j + 1] = pivot

    # sortierte Zeichenliste wieder zu einem String zusammensetzen
    return "".join(zeichen)


# Testen Sie Ihre Implementierung mit dem folgenden Code
text = input("Bitte Text ohne Sonder- und Leerzeichen eingeben: ").lower()

# Erwartete Ausgabe: identische Zeichen, jedoch alphabetisch sortiert
print(insertionsort(text))
