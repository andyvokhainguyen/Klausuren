# 📋 Alle Codes zum Abtippen & Üben

Alle Grundgerüste der **4 großen Themen** auf einen Blick – in der Form aus Skript/Altklausur.
So nutzen: Code lesen → in VSCode abtippen → **ausführen** → zuklappen → aus dem Kopf neu schreiben.

Inhalt: **1) Testen · 2) Kommandozeile + Datei-IO · 3) Datenstrukturen · 4) Sortierverfahren**

---

# 1) TESTEN

### pytest-Gerüst
```python
from src import aufgabe02        # Datei aufgabe02.py im Ordner src/

import pytest


def test_normalfall():
    assert aufgabe02.funktion(80) == 1

def test_grenzwert():
    assert aufgabe02.funktion(50) == 4      # genau AUF der Grenze testen

def test_randfall():
    assert aufgabe02.funktion(-1) == "ungültig"
```

### Regeln zum Testfälle-Finden (keine Codes, aber wichtig)
- **if/elif/else** → je Kategorie 1 Wert **+ Grenzwert**
- **Liste** → leer `[]` / 1 Element / mehrere / (mit/ohne Duplikate)
- **Schleife** → 0× / 1× / mehrfach · **Rekursion** → Basisfall / 1× / mehrfach

### Assertions (defensive Programmierung, WS2526)
```python
def funktion(values, limit):
    assert type(values) == list
    assert isinstance(limit, int), "limit muss eine ganze Zahl sein"
    ...

# im Test prüfen, dass die Assertion anschlägt:
def test_falscher_typ():
    with pytest.raises(AssertionError):
        aufgabe02a.funktion([1, 2], 10.5)
```

---

# 2) KOMMANDOZEILE + DATEI-IO

### Datei lesen & schreiben
```python
# Skript-Form:
f = open("datei.txt", "r")
print(f.read())                  # gesamter Inhalt; f.readline() = eine Zeile
f.close()

f = open("datei.txt", "w")       # "w"=überschreiben, "a"=anhängen
f.write("Zeile1\nZeile2")        # \n selbst anhängen!
f.close()

# with-Form (zeilenweise, Altklausur-Standard):
with open("log.txt", "r", encoding="utf-8") as datei:
    for zeile in datei:
        if zeile.strip() == "":
            continue
        print(zeile.strip())

with open("ergebnis.txt", "w", encoding="utf-8") as datei:
    datei.write("Text\n")
```

### sys.argv
```python
import sys

if len(sys.argv) != 4:
    print("Aufruf: python prog.py <a> <b> <c>")
    sys.exit()
a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]
```

### getopt
```python
import sys
import getopt


def main(argv):
    inputfile = ""
    outputfile = ""
    befehl = ""

    try:
        opts, args = getopt.getopt(argv, "i:o:b:h",
                                   ["input=", "output=", "befehl=", "help"])
    except getopt.GetoptError:
        print("prog.py -i <in> -o <out> -b <befehl>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("prog.py -i <in> -o <out> -b <befehl>")
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg
        elif opt in ("-b", "--befehl"):
            befehl = arg

    if inputfile == "" or outputfile == "" or befehl == "":
        print("Fehler: -i, -o und -b sind erforderlich.")
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
```

### argparse
```python
import argparse


def main():
    parser = argparse.ArgumentParser(description="...")
    parser.add_argument("--input",  "-i", required=True)
    parser.add_argument("--output", "-o", required=True)
    parser.add_argument("--befehl", "-b", required=True,
                        choices=["a", "b", "c"])
    args = parser.parse_args()
    # args.input, args.output, args.befehl


if __name__ == "__main__":
    main()
```

### Logdatei auswerten (SS25/WS2526-Muster)
```python
def werte_logdatei_aus(pfad, befehl):
    zaehler = {}
    with open(pfad, "r", encoding="utf-8") as datei:
        for zeile in datei:
            teile = zeile.strip().split(";")     # "...;INFO;alice;login"
            if len(teile) != 4:
                continue
            _zeitstempel, level, user, action = teile

            if befehl == "level":
                schluessel = level
            elif befehl == "user":
                schluessel = user
            else:
                schluessel = action

            if schluessel in zaehler:
                zaehler[schluessel] += 1
            else:
                zaehler[schluessel] = 1
    return zaehler


def schreibe_ergebnis(pfad, befehl, zaehler):
    with open(pfad, "w", encoding="utf-8") as datei:
        datei.write(f"Befehl: {befehl}\n")
        for schluessel, anzahl in zaehler.items():
            datei.write(f"{schluessel}: {anzahl}\n")


# häufigstes Element (NICHT auf dem Hilfsmittelblatt -> merken!):
# haeufigstes = max(zaehler, key=zaehler.get)
```

---

# 3) DATENSTRUKTUREN

### Einfach verkettete Liste (Skript 05)
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:           # Kopf-Sonderfall
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
```

### Stack (LIFO – hinten) & Queue (FIFO – vorne) (Skript 05)
```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        removed_item = self.stack[-1]        # hinten!
        del self.stack[-1]
        return removed_item

    def display(self):
        print(self.stack)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)             # vorne!  <<< DER Unterschied

    def display(self):
        print(self.queue)


# Erweiterung (WS2324-Klausur), für Stack ODER Queue:
#   def peek(self):     return None wenn leer, sonst self.stack[-1] (Queue: [0])
#   def is_empty(self): return len(self.stack) == 0
```

### Binärer Suchbaum (Skript 05, search aus Übungsblatt 6)
```python
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):           # Signatur: (data, node) – data zuerst!
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def print_tree(self):                    # In-order -> sortierte Ausgabe
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)      # links
            print(str(node.data))            # ich
            self._print_tree(node.right)     # rechts

    def search(self, data):
        return self._search(data, self.root)

    def _search(self, data, node):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search(data, node.left)
        else:
            return self._search(data, node.right)
```

### Extras – nur einmal durchlesen (niedrige Priorität)
```python
# Trie (WS2526): Kinder als dict
class Node:
    def __init__(self):
        self.kinder = {}
        self.ist_wortende = False

class Trie:
    def __init__(self):
        self.wurzel = Node()
    def einfuegen(self, wort):
        akt = self.wurzel
        for ch in wort:
            if ch not in akt.kinder:
                akt.kinder[ch] = Node()
            akt = akt.kinder[ch]
        akt.ist_wortende = True

# Ternärer Baum (SS25): Einordnung nach Wortlänge -> links/mitte/rechts
# Zirkuläre Liste (WS2425): letzter Knoten .next = self.head
# Doppelt verkettete Liste (SS23): Node zusätzlich mit self.prev
# (vollständig in 6_Klausur_Grundgeruest_Codes.md)
```

---

# 4) SORTIERVERFAHREN

### Bubble / Selection / Insertion (Skript 06, in-place)
```python
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        list_sorted = True
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                list_sorted = False
        if list_sorted:
            return


def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]


def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):
        pivot = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > pivot:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = pivot
```

### Quicksort (SS23-Klausur-Form) & Mergesort (Skript 06)
```python
def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    kleiner = [x for x in numbers[1:] if x <= pivot]     # <= behält Duplikate
    groesser = [x for x in numbers[1:] if x > pivot]
    return quicksort(kleiner) + [pivot] + quicksort(groesser)


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    left_half = merge_sort(numbers[:mid])
    right_half = merge_sort(numbers[mid:])
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged
```

### Heapsort (Skript 06 / SS25)
```python
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):      # Max-Heap aufbauen
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):            # größtes ans Ende
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

### 🔑 Nur die Vergleichszeile ändern (so in den Altklausuren)
| Aufgabe | Vergleich |
|---|---|
| Zahlen aufsteigend | `numbers[j] > numbers[j + 1]` |
| Strings nach Länge (SS25/WS2526) | `len(a[j]) > len(a[j + 1])` |
| Dict nach Feld | `a[j]["gehalt"] > a[j + 1]["gehalt"]` |
| Länge, dann alphabetisch | `(len(a[j]), a[j]) > (len(a[j + 1]), a[j + 1])` |
| absteigend | `>` durch `<` ersetzen |

### Komplexität
| Verfahren | best | mittel | schlecht |
|---|---|---|---|
| Bubble | O(n) | O(n²) | O(n²) |
| Selection | O(n²) | O(n²) | O(n²) |
| Insertion | O(n) | O(n²) | O(n²) |
| Quick | O(n·log n) | O(n·log n) | O(n²) |
| Merge / Heap | O(n·log n) | O(n·log n) | O(n·log n) |
