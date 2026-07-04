# Lösungen – Übungsblatt 7 (Sortierverfahren)

Alle Aufgaben lösen dasselbe Muster: **Standardalgorithmus + Vergleich über den passenden Schlüssel**.
Genau die Themen (Bubble/Selection) sind heiße Klausurkandidaten (kamen nie in einer Altklausur, werden aber jetzt geübt).

---

## Aufgabe 1 – Bubble-Sort auf Verkaufsdaten (Dicts nach `Verkaufsbetrag`)

```python
def bubble_sort_sales_data(sales_data):
    n = len(sales_data)
    for i in range(n - 1):
        getauscht = False
        for j in range(0, n - i - 1):
            # Vergleich über den Schlüssel "Verkaufsbetrag" (aufsteigend)
            if sales_data[j]["Verkaufsbetrag"] > sales_data[j + 1]["Verkaufsbetrag"]:
                sales_data[j], sales_data[j + 1] = sales_data[j + 1], sales_data[j]
                getauscht = True
        if not getauscht:          # nichts getauscht -> bereits sortiert
            break
    return sales_data


sales_data = [
    {"Kunde": "Kunde 1", "Produkt": "Produkt A", "Verkaufsbetrag": 500},
    {"Kunde": "Kunde 2", "Produkt": "Produkt B", "Verkaufsbetrag": 1000},
    {"Kunde": "Kunde 3", "Produkt": "Produkt C", "Verkaufsbetrag": 750},
    {"Kunde": "Kunde 4", "Produkt": "Produkt D", "Verkaufsbetrag": 250},
]
bubble_sort_sales_data(sales_data)     # sortiert in-place
for data in sales_data:
    print(data)
# Kunde 4 (250), Kunde 1 (500), Kunde 3 (750), Kunde 2 (1000)
```

---

## Aufgabe 2 – Selection-Sort: Wörter nach Länge

```python
def selection_sort_word_length(words):
    n = len(words)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            # Vergleich über die Wortlänge (aufsteigend)
            if len(words[j]) < len(words[min_index]):
                min_index = j
        words[i], words[min_index] = words[min_index], words[i]
    return words


word_list = ["Hallo", "Python", "Wirtschaftsinformatiker", "Aufgabe", "Sortieren"]
print(selection_sort_word_length(word_list))
# -> ['Hallo', 'Python', 'Aufgabe', 'Sortieren', 'Wirtschaftsinformatiker']
#    Längen:      5         6          7            9              23
```

> ⚠️ **Hinweis zum Aufgabenblatt:** Dessen abgedruckte „Erwartete Ausgabe" listet `Aufgabe` (7) **vor** `Python` (6) – das wäre für eine aufsteigende Längensortierung falsch. Die korrekte Reihenfolge ist `Hallo(5), Python(6), Aufgabe(7), Sortieren(9), Wirtschaftsinformatiker(23)`. Der Fehler liegt im Blatt, nicht in deiner Lösung.

---

## Aufgabe 3 – Insertion-Sort mit zwei Kriterien (Preis ↑, bei Gleichstand Beliebtheit ↓)

```python
def kommt_nach(a, b):
    """True, wenn Produkt a in der Sortierung HINTER b stehen soll."""
    if a["preis"] != b["preis"]:
        return a["preis"] > b["preis"]              # Preis aufsteigend
    return a["beliebtheit"] < b["beliebtheit"]      # bei gleichem Preis: Beliebtheit absteigend


def insertion_sort_produkte(produktliste):
    n = len(produktliste)
    for i in range(1, n):
        pivot = produktliste[i]
        j = i - 1
        while j >= 0 and kommt_nach(produktliste[j], pivot):
            produktliste[j + 1] = produktliste[j]
            j -= 1
        produktliste[j + 1] = pivot
    return produktliste


produktliste = [
    {"name": "Produkt A", "preis": 50, "beliebtheit": 10},
    {"name": "Produkt B", "preis": 30, "beliebtheit": 8},
    {"name": "Produkt C", "preis": 30, "beliebtheit": 12},
    {"name": "Produkt D", "preis": 20, "beliebtheit": 5},
]
insertion_sort_produkte(produktliste)
print("Sortierte Produktliste:")
for p in produktliste:
    print(f'{p["name"]} - Preis: {p["preis"]}, Beliebtheit: {p["beliebtheit"]}')
# Produkt D (20, 5) | Produkt C (30, 12) | Produkt B (30, 8) | Produkt A (50, 10)
```

**Tupel-Trick als Alternative** zur `kommt_nach`-Funktion – Schlüssel `(preis, -beliebtheit)` aufsteigend:
```python
while j >= 0 and (produktliste[j]["preis"], -produktliste[j]["beliebtheit"]) \
              > (pivot["preis"], -pivot["beliebtheit"]):
```

---

## Aufgabe 4 – Quicksort: Dokumente nach Inhaltslänge, dann Titel

```python
def quicksort_documents(documents):
    if len(documents) <= 1:
        return documents

    def schluessel(dokument):
        titel, inhalt = dokument
        return (len(inhalt), titel)           # primär Länge, sekundär Titel

    pivot = documents[0]
    pivot_key = schluessel(pivot)

    # '<' bzw. '>=' erhält Dokumente mit gleichem Schlüssel (keine gehen verloren)
    kleiner = [d for d in documents[1:] if schluessel(d) < pivot_key]
    groesser_gleich = [d for d in documents[1:] if schluessel(d) >= pivot_key]

    return quicksort_documents(kleiner) + [pivot] + quicksort_documents(groesser_gleich)


documents = [
    ("Document A", "Dies ist der Inhalt von Dokument A."),
    ("Document B", "Dies ist der Inhalt von Dokument B."),
    ("Document C", "Dies ist der längere Inhalt von Dokument C."),
    ("Document D", "Dies ist der längere Inhalt von Dokument D."),
    ("Document E", "Dies ist der Inhalt von Dokument E."),
]
for dok in quicksort_documents(documents):
    print(dok)
# A, B, E (kurz, alphabetisch) -> dann C, D (länger)
```

---

## Aufgabe 5 – Quicksort vs. Bubble-Sort mit Zählern (fortgeschritten)

Wörter **absteigend nach Länge**; Rückgabe `(sortierte_liste, vergleiche, vertauschungen)`.
Hier muss **in-place** sortiert werden, damit „Vertauschungen" gezählt werden können.

```python
def bubblesort_words(words):
    vergleiche = 0
    vertauschungen = 0
    n = len(words)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            vergleiche += 1
            if len(words[j]) < len(words[j + 1]):     # '<' -> ABSTEIGEND
                words[j], words[j + 1] = words[j + 1], words[j]
                vertauschungen += 1
    return words, vergleiche, vertauschungen


def quicksort_words(words):
    vergleiche = 0
    vertauschungen = 0

    def partition(low, high):
        nonlocal vergleiche, vertauschungen
        pivot_len = len(words[high])          # Pivot = letztes Element (Lomuto)
        i = low - 1
        for j in range(low, high):
            vergleiche += 1
            if len(words[j]) >= pivot_len:     # '>=' -> ABSTEIGEND
                i += 1
                words[i], words[j] = words[j], words[i]
                vertauschungen += 1
        words[i + 1], words[high] = words[high], words[i + 1]
        vertauschungen += 1
        return i + 1

    def quicksort(low, high):
        if low < high:
            p = partition(low, high)
            quicksort(low, p - 1)
            quicksort(p + 1, high)

    quicksort(0, len(words) - 1)
    return words, vergleiche, vertauschungen


# Beispielaufruf
with open("textdatei.txt", "r", encoding="utf-8") as file:
    words = file.read().split()

q_res, q_comp, q_swaps = quicksort_words(words.copy())
print("Quicksort:", q_comp, "Vergleiche,", q_swaps, "Vertauschungen")

b_res, b_comp, b_swaps = bubblesort_words(words.copy())
print("Bubble-Sort:", b_comp, "Vergleiche,", b_swaps, "Vertauschungen")
```

**Erwartetes Ergebnis der Messung:** Bubble-Sort hat **deutlich mehr** Vergleiche/Vertauschungen (O(n²)) als Quicksort (Ø O(n·log n)) – die praktische Bestätigung der Komplexitätstabelle.

> Für die **Klausur** ist die einfache, rekursive Quicksort-Variante aus dem Skript (mit `less`/`greater`-List-Comprehensions) das Wichtigste zum Auswendiglernen. Die in-place-Lomuto-Variante hier brauchst du nur, wenn **Vertauschungen gezählt** werden sollen.

---

## Merksatz für alle Sortier-Klausuraufgaben
Nimm den Standardalgorithmus und ändere **nur die Vergleichszeile**:
- Zahlen: `a > b`
- Strings nach Länge: `len(a) > len(b)`
- Dict nach Feld: `a["feld"] > b["feld"]`
- Zwei Kriterien: Tupel `(a["k1"], -a["k2"]) > (b["k1"], -b["k2"])` oder eine `kommt_nach`-Hilfsfunktion
- **Absteigend** statt aufsteigend: Vergleich umdrehen (`>` ↔ `<`)
