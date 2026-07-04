"""
Aufgabe 5 - Klausur Programmierung WS2025/26
"""


def mergesort(input_liste):
    """
    Sortiert die Strings in input_liste
    1) aufsteigend nach ihrer Laenge
    2) bei gleicher Laenge alphabetisch aufsteigend
    und gibt die sortierte Liste zurueck.
    """
    if len(input_liste) <= 1:
        return input_liste

    mitte = len(input_liste) // 2
    links = mergesort(input_liste[:mitte])
    rechts = mergesort(input_liste[mitte:])
    return merge(links, rechts)


def merge(left, right):
    """
    Fuehrt zwei bereits sortierte Listen zusammen und gibt Liste sortiert zurueck
    Sortierkriterium:
    - zuerst len(s)
    - bei Gleichstand: alphabetisch
    """
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if (len(left[i]), left[i]) <= (len(right[j]), right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Testen Sie Ihre Implementierung mit dem folgenden Code
word_list = ["Hallo", "Python", "Wirtschaftsinformatiker", "Aufgabe", "Sortieren",
             "Kurs", "AI", "Zoo", "Auto"]

print(mergesort(word_list))
