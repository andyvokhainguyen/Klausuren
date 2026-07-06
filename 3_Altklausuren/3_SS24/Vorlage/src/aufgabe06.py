"""
Aufgabe 6 - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""


def mergesort(input_liste):
    """
    Sortiert die Strings in input_liste aufsteigend
    nach ihrer Länge
    """
    pass


def merge(left, right):
    """
    Führt zwei nach Länge sortierte Listen zusammen und gibt eine
    nach Länge sortierte Liste zurück.
    """
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if len(left[i]) < len(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Testen Sie Ihre Implementierung mit dem folgenden Code
word_list = ["Hallo", "Python", "Wirtschaftsinformatiker", "Aufgabe", "Sortieren"]

print(mergesort(text))
