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
    # Basisfall: 0 oder 1 Element ist bereits sortiert
    if len(input_liste) <= 1:
        return input_liste

    # Teilen: Liste in der Mitte in zwei Haelften aufteilen
    mitte = len(input_liste) // 2
    links = mergesort(input_liste[:mitte])   # rekursiv sortieren
    rechts = mergesort(input_liste[mitte:])

    # Zusammenfuehren mit der vorgegebenen merge-Funktion (sortiert nach Laenge)
    return merge(links, rechts)


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

# Hinweis: im vorgegebenen Rahmen stand faelschlich "mergesort(text)";
# korrekt ist die vorhandene Variable word_list.
print(mergesort(word_list))
