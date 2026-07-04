"""
Aufgabe 6 - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

def quicksort_documents(documents):
    # Basisfall: 0 oder 1 Dokument ist bereits sortiert
    if len(documents) <= 1:
        return documents

    # Vergleichsschluessel je Dokument (titel, inhalt):
    #   primaer  -> Laenge des Inhalts (Zeichen)
    #   sekundaer-> Titel alphabetisch
    def schluessel(dokument):
        titel, inhalt = dokument
        return (len(inhalt), titel)

    pivot = documents[0]
    pivot_key = schluessel(pivot)

    # '<' bzw. '>=' beim Vergleich der Tupel -> Dokumente mit gleichem Schluessel
    # bleiben erhalten (keine Duplikate gehen verloren).
    kleiner = [d for d in documents[1:] if schluessel(d) < pivot_key]
    groesser_gleich = [d for d in documents[1:] if schluessel(d) >= pivot_key]

    return quicksort_documents(kleiner) + [pivot] + quicksort_documents(groesser_gleich)

documents = [
    ("Document A", "Dies ist der Inhalt von Dokument A."),
    ("Document B", "Dies ist der Inhalt von Dokument B."),
    ("Document C", "Dies ist der längere Inhalt von Dokument C."),
    ("Document D", "Dies ist der längere Inhalt von Dokument D."),
    ("Document E", "Dies ist der Inhalt von Dokument E."),
    ("Document F", "Inhalt von F.")   
]

sorted_documents = quicksort_documents(documents)

for document in sorted_documents:
    print(document)


