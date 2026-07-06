"""
Aufgabe 5 - Klausur Programmierung
"""

def heapsort(input_liste):
    """
    Sortiert die Strings in input_liste aufsteigend
    nach ihrer Länge mithilfe des Heapsort-Verfahrens.
    """
    liste = list(input_liste)
    n = len(liste)

    # Max-Heap aufbauen (bezueglich Wortlaenge)
    for i in range(n // 2 - 1, -1, -1):
        heapify(liste, n, i)

    # Wurzel (laengstes Wort) ans Ende tauschen und Heap verkleinern
    for i in range(n - 1, 0, -1):
        liste[0], liste[i] = liste[i], liste[0]
        heapify(liste, i, 0)

    return liste


def heapify(liste, n, i):
    """
    Stellt sicher, dass der Teilbaum mit Wurzel an Index i
    die Max-Heap-Eigenschaft bezüglich der Wortlänge erfüllt.
    """
    groesster = i
    links = 2 * i + 1
    rechts = 2 * i + 2

    if links < n and len(liste[links]) > len(liste[groesster]):
        groesster = links

    if rechts < n and len(liste[rechts]) > len(liste[groesster]):
        groesster = rechts

    if groesster != i:
        liste[i], liste[groesster] = liste[groesster], liste[i]
        heapify(liste, n, groesster)
        
        
wort_liste = ["Hallo", "Python", "Wirtschaftsinformatiker", "Aufgabe", "Sortieren"]

print(heapsort(wort_liste))