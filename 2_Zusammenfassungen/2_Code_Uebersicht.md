# Programmierung – Code-Zusammenfassung für die Klausur

Alle prüfungsrelevanten Codes aus den Skripten 02–06 (Skript 01 = reine Theorie, kein Code).
Ideal zum Nachbauen, Üben und Auswendiglernen. Reihenfolge: **Argumente → Datei-IO → Testen/Debuggen → Datenstrukturen → Sortierverfahren**.

---

## 1) Argumente & Kommandozeile (Skript 03)

Aufruf: `python test.py argument1 argument2` → durch Leerzeichen getrennte Strings.

### 1.1 Einfacher Fall: `sys.argv`
```python
import sys

if len(sys.argv) > 1:
    for arg in range(len(sys.argv)):
        print('Argument ' + str(arg) + ':', sys.argv[arg])
else:
    print('Keine Argumente angegeben')
```
- `sys.argv[0]` ist immer der Skriptname, die eigentlichen Argumente ab `sys.argv[1]`.
- Nachteil: manuelles Parsing, fehleranfällig, feste Reihenfolge.

### 1.2 `getopt` – Parser für kurze/lange Flags
Signatur: `getopt.getopt(args, shortopts, longopts)`
- **shortopts**: z.B. `'hab'` → Flags `-h -a -b`. Doppelpunkt = Argument nötig: `'ha:b'` → `-a` braucht Wert.
- **longopts**: Liste, z.B. `['help','simplex']` → `--help`. `=` = Argument nötig: `['option=']` → `--option=wert`.

```python
import sys
import getopt

args = sys.argv[1:]
inputfile = ''
outputfile = ''

try:
    opts, args = getopt.getopt(args, "hi:o:", ["infile=", "outfile="])
except getopt.GetoptError:
    print('test.py -i <inputfile> -o <outputfile>')
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print('args.py -i <inputfile> -o <outputfile>')
        sys.exit()
    elif opt in ("-i", "--infile"):
        inputfile = arg
    elif opt in ("-o", "--outfile"):
        outputfile = arg

print('Input file is "', inputfile)
print('Output file is "', outputfile)
```
- `opts`: Liste von (Flag, Argument)-Paaren. `args`: übrige Argumente ohne Flags.

### 1.3 `argparse` – aktueller/empfohlener Ansatz
```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Ein kleines Beispiel")
    parser.add_argument('zahl', type=int, help="Eine ganze Zahl eingeben")
    parser.add_argument('--verbose', action='store_true', help="Mehr Details ausgeben")
    args = parser.parse_args()

    ergebnis = args.zahl ** 2
    if args.verbose:
        print(f"Das Quadrat von {args.zahl} ist {ergebnis}.")
    else:
        print(ergebnis)

if __name__ == "__main__":
    main()
```
- Positionsargument: `'zahl'` (Pflicht, hier `type=int`).
- Optionales Flag: `'--verbose'` mit `action='store_true'` → True/False ohne Wert.

---

## 2) Datei-Handling und IO (Skript 04)

### 2.1 Öffnen-Modi (`open`)
| Zeichen | Bedeutung |
|---|---|
| `'r'` | reading (default) |
| `'w'` | writing, Datei wird zuerst geleert (truncate) |
| `'x'` | exclusive creation, Fehler wenn Datei existiert |
| `'a'` | writing, ans Ende anhängen (append) |
| `'b'` | binary mode |
| `'t'` | text mode (default) |
| `'+'` | updating (lesen und schreiben) |

Achtung: Python geht vom aktuellen Arbeitsverzeichnis aus.

### 2.2 Lesen
```python
f = open("morgenstern.txt", "r")
print(f.read())      # gesamter Inhalt; f.read(10) = 10 Zeichen
f.close()
```
Lese-Methoden: `read()` = alles, `read(x)` = x Zeichen, `readline()` = eine Zeile, `readlines()` = Liste aller Zeilen.

```python
f = open("morgenstern.txt", "r")
zeilennummer = 1
for zeile in f.readlines():
    print(zeilennummer, zeile, end='')
    zeilennummer += 1
f.close()
```
> Wichtig: Dateien sind **Streams** – der Lese-Zeiger wandert weiter. Ein zweites `read()` nach dem ersten liest nur noch den Rest.

### 2.3 Schreiben
```python
f = open("meinWitz.txt", 'w')
f.write("Treffen sich zwei Jäger.\nBeide tot.")   # ganzer Text als ein String
f.close()

f = open("meinWitz.txt", 'w')
f.writelines(["Treffen sich zwei Jäger.", "\nBeide tot."])  # Liste an Strings
f.close()
```

### 2.4 Dateiinhalte verändern (lesen → ändern → zurückschreiben)
```python
f = open("meinWitz.txt", "r")
l = f.readlines()
f.close()
print(l)
l.insert(3, "tralala\n")
print(l)

f = open("meinWitz.txt", "w")
f.writelines(l)
f.close()
```

### 2.5 Pfade prüfen: `os.path`
```python
import os.path
os.path.exists("morgenstern.txt")    # existiert? -> True/False
os.path.getsize("morgenstern.txt")   # Größe in Bytes -> 199
os.path.isabs("./")                  # absoluter Pfad? -> False
os.path.isfile("morgenstern.txt")    # Datei? -> True
os.path.isdir("morgenstern.txt")     # Verzeichnis? -> False
os.path.realpath("morgenstern.txt")  # absoluter Pfad als String
os.path.split("./morgenstern.txt")   # -> ('.', 'morgenstern.txt')
```

### 2.6 Randwissen (Bash / Rechte)
- Rechte: `r` (read), `w` (write/löschen), `x` (execute/zugreifen). Gruppen: user `u`, group `g`, other `o`, all `a`.
- `chmod a+rw test.txt` (Rechte hinzufügen), `chmod a-rw test.txt` (entfernen).
- Befehle: `cd`, `ls`, `pwd`, `mkdir`, `rm`, `cp`, `mv`, `touch`, `echo`.
- Shebang (erste Zeile, Datei muss ausführbar `+x` sein): `#!/usr/local/bin/python3` bzw. `#!/bin/bash`.

---

## 3) Testen und Debuggen (Skript 02)

Merksatz: **Defensive Programmierung** (Spezifikationen, Modularisierung, Asserts) → **Testen** (Input/Output vs. Spezifikation) → **Debuggen** (verstehen warum falsch).
Testpyramide: Unit-Tests → Regressionstests → Integrationstests.
Testansätze: intuitiv, zufallsbasiert, **Black-Box** (nur Spezifikation), **White-Box** (Code/Pfade). "Path-Complete" = jeder Pfad mind. 1× durchlaufen. Zusätzlich Randwerte testen!

### 3.1 Spezifikation via Docstring (Black-Box)
```python
def sqrt(x, epsilon):
    """ Annahme: x, epsilon floats, x >= 0, epsilon > 0
        Returns ergebnis: x-epsilon <= ergebnis*ergebnis <= x+epsilon"""
```

### 3.2 White-Box: Randwert-Beispiel
```python
def my_abs(x):
    """ Berechnet den Absolutwert einer Ganzzahl x."""
    if x < -1:          # FEHLER: Randwert -1 nicht abgedeckt
        return -x
    else:
        return x
```
> Merke: "Path-Complete" genügt hier NICHT – man muss Randwerte (hier x = -1) testen.

### 3.3 Verzweigungen testen
```python
def maxOfThree(a, b, c):
    """ a, b, and c are numbers
        returns: the maximum of a, b, and c """
    if a > b:
        bigger = a
    else:
        bigger = b
    if c > bigger:
        bigger = c
    return bigger
```

### 3.4 Rekursion testen (alle Pfade + Rekursionstiefen 0/1/n)
```python
def union(set1, set2):
    """ ... returns one set with all elements, no duplicates """
    if len(set1) == 0:
        return set2
    elif set1[0] in set2:
        return union(set1[1:], set2)
    else:
        return set1[0] + union(set1[1:], set2)
```

### 3.5 Schleifen testen (0, 1, mehrfach durchlaufen)
```python
def foo(x, a):
    """ x, a positive integer arguments; returns an integer """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count
```

### 3.6 Debugging-Beispiel (Fehler suchen)
```python
def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse          # BUG: fehlende Klammern -> temp.reverse()  (+ Kopie nötig)
    if temp == x:
        return True
    else:
        return False

def silly(n):
    for i in range(n):
        result = []
        elem = input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print('Yes')
    else:
        print('No')
```

### 3.7 Typische Exceptions
```python
test = [1, 2, 3]
test[4]          # -> IndexError
int(test)        # -> TypeError
a                # -> NameError (nicht existierende Variable)
'3' / 4          # -> TypeError (Datentypen gemischt)
a = len([1,2,3]  # -> SyntaxError (Klammer vergessen)
```

### 3.8 Assertions (defensive Programmierung)
```python
def avg(grades):
    assert not len(grades) == 0, 'no grades data'
    return sum(grades) / len(grades)
```
- Verletzte Assertion wirft `AssertionError` und stoppt die Funktion sofort.
- Nutzung: Prüfung von Typ, Violations (z.B. Duplikate), Constraints an Rückgaben.

### 3.9 pytest (Unit-Test-Framework)
Struktur: leere `__init__.py` im Ordner, `src/`- und `test/`-Ordner trennen, dann `pytest` aufrufen.
```python
"""Test uebungsblatt03_03.py"""
from Uebungsblatt_03.src import uebungsblatt03_05

def test_foo():
    """Test cases für rekursive Addition"""
    assert uebungsblatt03_05.foo(10, 3) == 3
    assert uebungsblatt03_05.foo(1, 4) == 0
    assert uebungsblatt03_05.foo(10, 6) == 1
```

---

## 4) Datenstrukturen (Skript 05)

### 4.1 Element / Node (mit Schlüssel)
```python
class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
```
Typische Operationen auf Menge D: INSERT, DELETE, SEARCH, SIZE, MAX, MIN, SUCC, PRED.

### 4.2 Feld / Array
```python
def insert_element(array, index, element):
    return array[:index] + [element] + array[index:]

def delete_element(array, index):
    return array[:index] + array[index + 1:]
```
Alternativ: `list.insert()`, `list.pop()`, `del`.

### 4.3 Verkettete Liste – insert & print
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

# Nutzung
linked_list = LinkedList()
linked_list.insert('A')
linked_list.insert('B')
linked_list.insert('C')
linked_list.print_list()
```

### 4.4 Verkettete Liste – delete
```python
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
```

### 4.5 Warteschlange / Queue (FIFO – First In First Out)
```python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):          # Add an element
        self.queue.append(item)

    def dequeue(self):                # Remove an element
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)
```

### 4.6 Stapel / Stack (LIFO – Last In First Out)
```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):             # Add an element
        self.stack.append(item)

    def pop(self):                    # Remove an element
        if len(self.stack) < 1:
            return None
        removed_item = self.stack[-1]
        del self.stack[-1]
        return removed_item

    def display(self):
        print(self.stack)
```

### 4.7 Binärer Suchbaum (BST) – insert & print
**Eigenschaft:** linker Teilbaum < Knoten < rechter Teilbaum (gilt für JEDEN Knoten). In-order-Traversierung liefert sortierte Reihenfolge.
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

    def _insert(self, data, node):
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

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(str(node.data))
            self._print_tree(node.right)

# Verwendung
bt = BinaryTree()
bt.insert(10); bt.insert(5); bt.insert(15); bt.insert(3)
bt.print_tree()
```

### 4.8 BST – delete
```python
    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self._find_min(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)
        return node

    def _find_min(self, node):
        if node.left is None:
            return node
        else:
            return self._find_min(node.left)
```

---

## 5) Such- und Sortierverfahren (Skript 06)

Naive Verfahren (Ø O(n²)): Bubble, Selection, Insertion.
Divide-and-Conquer (Ø O(n·log n)): Quicksort, Mergesort, Heapsort.
Beispiel-Liste in allen Übungen: `[55, 7, 78, 12, 42]`.

### 5.1 Bubble-Sort
Idee: größte Zahl "steigt" nach oben; benachbarte Elemente vergleichen und ggf. tauschen.
```python
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        list_sorted = True
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Tausche die Positionen
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                list_sorted = False
        if list_sorted:
            # kein Vertauschen erforderlich gewesen
            return
```

### 5.2 Selection-Sort
Idee: iterativ das kleinste Element suchen und nach vorne tauschen.
```python
def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        # Finde das Minimum im unsortierten Teil der Liste
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        # Tausche das Minimum mit dem aktuellen Element
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
```

### 5.3 Insertion-Sort
Idee: Menge in sortierten/unsortierten Teil; Element an korrekter Stelle einfügen.
```python
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

### 5.4 Quicksort (Teile-und-Herrsche)
```python
def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers[0]
        less = [x for x in numbers[1:] if x < pivot]
        greater = [x for x in numbers[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
```
> Achtung: Vergleich nur auf `<`/`>` eliminiert Duplikate. Sollen Duplikate erhalten bleiben, muss ein Vergleich `<=` verwenden.

### 5.5 Mergesort (Teile-und-Herrsche)
```python
def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    # Teile die Liste in zwei Hälften
    mid = len(numbers) // 2
    left_half = numbers[:mid]
    right_half = numbers[mid:]

    # Wende Mergesort rekursiv an
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Führe die sortierten Hälften zusammen
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Füge die Elemente in der richtigen Reihenfolge zusammen
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Füge die restlichen Elemente hinzu
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged
```

### 5.6 Heapsort (Max-Heap)
Prinzip: Daten als Max-Heap (Wurzel = größtes Element). Nachfolger von Index k: `2k` und `2k+1`.
Wiederholt Wurzel entnehmen und Heap wiederherstellen (versickern/percolate, max. log n Schritte).
```python
def heap_sort(arr):
    n = len(arr)

    # Erstellen eines Max-Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrahieren der Elemente aus dem Heap
    for i in range(n - 1, 0, -1):
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

### 5.7 Komplexität – Übersichtstabelle (auswendig!)
| Verfahren | bester Fall | mittlerer Fall | schlechtester Fall |
|---|---|---|---|
| Bubble | O(n) | O(n²) | O(n²) |
| Selection | O(n²) | O(n²) | O(n²) |
| Insertion | O(n) | O(n²) | O(n²) |
| Heap | O(n·log n) | O(n·log n) | O(n·log n) |
| Quick | O(n·log n) | O(n·log n) | O(n²) |
| Merge | O(n·log n) | O(n·log n) | O(n·log n) |
| Counting | O(n) | O(n) | O(n) |

---

## Kurz-Checkliste zum Auswendiglernen
- [ ] `sys.argv`, `getopt.getopt(args, short, long)`, `argparse` (add_argument, parse_args)
- [ ] Datei: `open(mode)`, `read/readline/readlines`, `write/writelines`, `close`, Streams, `os.path.*`
- [ ] Testen: Black-/White-Box, Path-Complete + Randwerte, `assert x, 'msg'`, pytest `test_*`
- [ ] Node / LinkedList (insert, print, delete)
- [ ] Queue (FIFO: append / pop(0)), Stack (LIFO: append / [-1] + del)
- [ ] BST (insert, _insert, in-order print, delete, _find_min)
- [ ] Sortierung: bubble, selection, insertion, quicksort, merge_sort+merge, heap_sort+heapify
- [ ] Komplexitätstabelle
