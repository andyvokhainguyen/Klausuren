# 🎯 Alle Codes – was gibt der Prof vor, was schreibst du selbst?

Gleiche Codes wie in `3_Alle_Codes_zum_Abtippen.md`, aber **jede Zeile ist markiert**: Was stand schon in der Vorlage (🟩) und was musstest du selbst herleiten (🟨). Basiert auf dem direkten Vergleich `Vorlage/` ↔ `Loesung/` aller 6 Altklausuren.

## Legende
- 🟩 **VORGEGEBEN** – steht schon in der Vorlage (Klassengerüst, Signaturen, Docstrings, Testaufruf, oft eine Hilfsfunktion)
- 🟨 **SELBST** – musst du schreiben/herleiten (die eigentliche Logik)

## 📌 Das immer gleiche Vorgabe-Muster (merken!)
| Aufgabentyp | 🟩 Prof gibt | 🟨 Du schreibst |
|---|---|---|
| **Testen** | die zu testende Funktion (fertig, evtl. mit Bug) + `assert type(...)`-Beispiel | Testfälle/pytest, weitere Assertions, Äquivalenzklassen/Pfade |
| **Kommandozeile+Datei** | meist nur Docstring/TODO (selten eine Hilfsfunktion) | fast **alles**: getopt-Gerüst + Datei lesen/schreiben |
| **Datenstruktur** | `Node`-Klasse, `__init__`, Wrapper-Methoden, Testaufruf unten | die **Methodenrümpfe** (rekursive Helfer, insert/delete/search/traversal) |
| **Sortieren** | Signatur + Docstring + Testaufruf; bei Merge/Heap die **Hilfsfunktion** (`merge`/`heapify`) | den **Hauptalgorithmus** (bei Merge/Heap den Rest) |

---

# 1) TESTEN

**🟩 Prof gibt:** die zu testende Funktion (komplett – in WS2526 mit absichtlichen Bugs). **🟨 Du schreibst:** die Testdatei, zusätzliche Assertions, die Äquivalenzklassen bzw. White-Box-Pfade.

### pytest-Gerüst  → 🟨 komplett selbst (aus dem Kopf)
```python
from src import aufgabe02        # 🟨 Import auf die vorgegebene Datei
import pytest                    # 🟨

def test_normalfall():           # 🟨 Namen frei, muss mit test_ beginnen
    assert aufgabe02.funktion(80) == 1
def test_grenzwert():            # 🟨 genau AUF der Grenze testen
    assert aufgabe02.funktion(50) == 4
def test_randfall():             # 🟨
    assert aufgabe02.funktion(-1) == "ungültig"
```
💡 **Tipp:** Der Testaufruf ist reine Routine – Datei liegt in `src/`, Tests in `test/`, beide brauchen `__init__.py`. Testnamen MÜSSEN mit `test_` beginnen, Testdatei `test_*.py` heißen. Ausführen: `python3 -m pytest`.

### Assertions (defensive Programmierung, WS2526)
```python
def funktion(values, limit):
    assert type(values) == list                              # 🟩 gibt der Prof als Beispiel vor
    assert isinstance(limit, int), "limit muss int sein"     # 🟨 selbst ergänzen (2e)
    assert all(isinstance(v, (int, float)) for v in values), \
        "alle Elemente muessen int oder float sein"          # 🟨 selbst ergänzen
    ...

def test_falscher_typ():                                     # 🟨 selbst
    with pytest.raises(AssertionError):
        aufgabe02a.funktion([1, 2], 10.5)
```
💡 **Tipp:** Der Prof gibt dir `assert type(values) == list` als Vorlage-Zeile – die **weiteren** Assertions (Typ von `limit`, alle Elemente numerisch) sind deine Aufgabe. Denk an Muster: `isinstance(x, int)` + `all(... for ...)`.

💡 **Äquivalenzklassen/Pfade (🟨 selbst):** Black-Box = aus der Beschreibung Klassen bilden (leer / nur-negativ / gemischt / Grenzwert). White-Box = Code lesen: if/else → beide Zweige, Rekursion → Basisfall/1×/mehrfach.

---

# 2) KOMMANDOZEILE + DATEI-IO

**🟩 Prof gibt:** oft nur einen Docstring mit Beispielaufruf + `# TODO` (SS25 gab gar nichts). Manchmal eine fertige **Hilfsfunktion** (z. B. `combine_images` in SS24). **🟨 Du schreibst:** das komplette getopt-Gerüst und das Lesen/Schreiben der Datei.

### Datei lesen & schreiben → 🟨 selbst
```python
with open("log.txt", "r", encoding="utf-8") as datei:   # 🟨
    for zeile in datei:                                  # 🟨 zeilenweise
        if zeile.strip() == "":
            continue
        print(zeile.strip())

with open("ergebnis.txt", "w", encoding="utf-8") as datei:  # 🟨 "w"=überschreiben
    datei.write("Text\n")
```
💡 **Tipp:** `with` schließt die Datei automatisch. `"r"` lesen, `"w"` überschreiben, `"a"` anhängen. `\n` musst du beim Schreiben selbst setzen.

### getopt → 🟨 komplett selbst (Standard-Gerüst auswendig!)
```python
import sys                                               # 🟨
import getopt                                            # 🟨

def main(argv):
    inputfile = ""; outputfile = ""; befehl = ""
    try:
        opts, args = getopt.getopt(argv, "i:o:b:h",
                                   ["input=", "output=", "befehl=", "help"])
    except getopt.GetoptError:
        print("prog.py -i <in> -o <out> -b <befehl>"); sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("prog.py -i <in> -o <out> -b <befehl>"); sys.exit()
        elif opt in ("-i", "--input"):  inputfile = arg
        elif opt in ("-o", "--output"): outputfile = arg
        elif opt in ("-b", "--befehl"): befehl = arg
    if inputfile == "" or outputfile == "" or befehl == "":
        print("Fehler: -i, -o und -b sind erforderlich."); sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])
```
💡 **Tipp:** Merksatz für getopt: **Buchstabe mit `:` braucht einen Wert** (`i:o:b:`), `h` ohne `:` ist ein Schalter. `argv = sys.argv[1:]` (Programmname abschneiden). Pflichtargumente prüfst du **selbst** (getopt tut das nicht).

### argparse (Alternative – nur wenn erlaubt) → 🟨 selbst
```python
import argparse
def main():
    parser = argparse.ArgumentParser(description="...")
    parser.add_argument("--input",  "-i", required=True)   # required + choices
    parser.add_argument("--output", "-o", required=True)   # macht argparse selbst
    parser.add_argument("--befehl", "-b", required=True, choices=["a", "b", "c"])
    args = parser.parse_args()
if __name__ == "__main__":
    main()
```
💡 **Tipp:** In der Klausur ist laut Hilfsmittelblatt nur **getopt** erlaubt. Bei argparse übernimmt `required=True`/`choices=[...]` die Prüfung automatisch – bei getopt machst du das von Hand.

### Logdatei auswerten (SS25/WS2526) → 🟨 selbst
```python
def werte_logdatei_aus(pfad, befehl):                    # 🟨
    zaehler = {}
    with open(pfad, "r", encoding="utf-8") as datei:
        for zeile in datei:
            teile = zeile.strip().split(";")             # 🟨 "...;INFO;alice;login"
            if len(teile) != 4:
                continue
            _zeit, level, user, action = teile
            if befehl == "level":  schluessel = level    # 🟨 nur DIESE Zeilen wechseln
            elif befehl == "user": schluessel = user
            else:                  schluessel = action
            if schluessel in zaehler: zaehler[schluessel] += 1
            else:                     zaehler[schluessel] = 1
    return zaehler
```
💡 **Tipp:** Das Zählprinzip ist immer gleich – nur **welches Feld** gezählt wird (`level`/`user`/`action`) hängt am `befehl`. `haeufigstes = max(zaehler, key=zaehler.get)` steht NICHT auf dem Hilfsblatt → merken!

---

# 3) DATENSTRUKTUREN (Skript-Stoff)

**🟩 Prof gibt fast immer:** `Node`-Klasse, `__init__`, die „äußeren" Wrapper-Methoden und den Testaufruf unten. **🟨 Du schreibst:** die Methodenrümpfe (dort wo `pass` / `raise NotImplementedError` steht).

### Einfach verkettete Liste (Skript 05 / SS23)
```python
class Node:                                  # 🟩 vorgegeben
    def __init__(self, data):                # 🟩
        self.data = data
        self.next = None

class LinkedList:                            # 🟩
    def __init__(self):                      # 🟩
        self.head = None

    def insert(self, data):                  # 🟩 in SS23 KOMPLETT vorgegeben
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):                    # 🟩 in SS23 KOMPLETT vorgegeben
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def delete(self, data):                  # 🟨 selbst (Zusatzmethode)
        if self.head is None:
            return
        if self.head.data == data:           # 🟨 Kopf-Sonderfall!
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
```
💡 **Tipp:** In SS23 waren `insert`/`print_list` geschenkt; gefragt waren **Zusatzmethoden** (delete, get, insertAfterElement). Kern: mit `current = current.next` durchlaufen, beim Löschen den **Kopf-Sonderfall** getrennt behandeln.

### Stack (LIFO) & Queue (FIFO) (Skript 05 / WS2324)
```python
class Stack:                                 # 🟩
    def __init__(self):                      # 🟩
        self.stack = []
    def push(self, item):                    # 🟩 vorgegeben
        self.stack.append(item)

    def pop(self):                           # 🟨 selbst (Vorlage: raise NotImplementedError)
        if len(self.stack) < 1:
            return None
        removed = self.stack[-1]             # 🟨 hinten!
        del self.stack[-1]
        return removed
    def peek(self):                          # 🟨 selbst
        if len(self.stack) < 1: return None
        return self.stack[-1]
    def is_empty(self):                      # 🟨 selbst
        return len(self.stack) == 0
    def display(self):                       # 🟨 selbst
        print(self.stack)


class Queue:                                 # 🟩 __init__/enqueue vorgegeben
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):                       # 🟨 selbst: pop(0) = VORNE
        if len(self.queue) < 1: return None
        return self.queue.pop(0)
    def display(self):
        print(self.queue)
```
💡 **Tipp:** In WS2324 stand bei den zu schreibenden Methoden `raise NotImplementedError` – die ersetzt du. **Der einzige echte Unterschied Stack↔Queue:** entfernen hinten (`[-1]`/`pop()`) vs. vorne (`pop(0)`). Achtung: `del` ist reserviert → Methode `delete` nennen.

### Binärer Suchbaum (Skript 05 / SS24)
```python
class Node:                                  # 🟩
    def __init__(self, data):                # 🟩
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:                            # 🟩
    def __init__(self):                      # 🟩
        self.root = None

    def insert(self, data):                  # 🟩 Wrapper vorgegeben
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):           # 🟨 selbst (Vorlage: pass)
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

    def print_tree(self):                    # 🟨 selbst (Wrapper war teils vorgegeben)
        if self.root is not None:
            self._print_tree(self.root)
    def _print_tree(self, node):             # 🟨 In-order -> sortiert
        if node is not None:
            self._print_tree(node.left)      # links
            print(str(node.data))            # ich
            self._print_tree(node.right)     # rechts

    def search(self, data):                  # 🟨 selbst (aus Übungsblatt 6)
        return self._search(data, self.root)
    def _search(self, data, node):
        if node is None: return False
        if data == node.data: return True
        elif data < node.data: return self._search(data, node.left)
        else: return self._search(data, node.right)
```
💡 **Tipp:** In SS24 waren `Node`, `__init__`, `insert`-Wrapper geschenkt; du schreibst `_insert_rekursiv` und `print_tree`. Merke: **links < Knoten ≤ rechts**, und **In-order (links→ich→rechts) gibt sortiert aus**.

### Doppelt verkettete Liste (Skript-05-Übung) → 🟨 überwiegend selbst
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None                     # 🟨 der Zusatz ggü. einfacher Liste
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):                  # 🟨 am Ende + prev setzen
        neuer = Node(data)
        if self.head is None:
            self.head = neuer; return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = neuer
        neuer.prev = current
    def print_rueckwaerts(self):             # 🟨 ans Ende, dann über prev zurück
        current = self.head
        if current is None: return
        while current.next is not None:
            current = current.next
        while current is not None:
            print(current.data)
            current = current.prev
```
💡 **Tipp:** Im Skript ist das eine **Übung** (kein fertiger Code) – du leitest es aus der einfachen Liste ab: `Node` bekommt zusätzlich `self.prev`, beim Einfügen den Rückwärts-Zeiger mitsetzen.

---

# 4) SORTIERVERFAHREN

**🟩 Prof gibt:** Signatur + Docstring + Testaufruf unten. **Bei Merge/Heap zusätzlich die Hilfsfunktion** (`merge` bzw. `heapify`) komplett! **🟨 Du schreibst:** den Hauptalgorithmus.

### Bubble / Selection / Insertion → 🟨 Rumpf komplett selbst
```python
def bubble_sort(numbers):                    # 🟩 Signatur + 🟩 Testaufruf unten
    n = len(numbers)                         # 🟨 ab hier alles selbst
    for i in range(n - 1):
        list_sorted = True
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:  # 🟨 <- HIER Vergleich anpassen
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                list_sorted = False
        if list_sorted:
            return

def selection_sort(numbers):                 # 🟨 Rumpf selbst
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

def insertion_sort(numbers):                 # 🟨 Rumpf selbst
    for i in range(1, len(numbers)):
        pivot = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > pivot:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = pivot
```
💡 **Tipp:** Bei diesen dreien gibt der Prof nur `def ...(): pass` + Testaufruf – der **ganze** Algorithmus ist deine Aufgabe. Das Sortierkriterium sitzt in **einer** Vergleichszeile (siehe Tabelle unten).

### Quicksort → 🟨 komplett selbst · Mergesort → 🟩 `merge` gegeben, 🟨 `mergesort` selbst
```python
def quicksort(numbers):                      # 🟨 alles selbst (Vorlage: pass)
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    kleiner  = [x for x in numbers[1:] if x <= pivot]   # <= behält Duplikate
    groesser = [x for x in numbers[1:] if x > pivot]
    return quicksort(kleiner) + [pivot] + quicksort(groesser)


def mergesort(numbers):                      # 🟨 DU schreibst nur diese Funktion
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    left  = mergesort(numbers[:mid])
    right = mergesort(numbers[mid:])
    return merge(left, right)

def merge(left, right):                      # 🟩 in SS24/WS2526 KOMPLETT vorgegeben!
    result = []; i = 0; j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:               # (bei „nach Länge": len(left[i]) < len(right[j]))
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result
```
💡 **Tipp (wichtig!):** Bei Mergesort schenkt dir der Prof die `merge`-Funktion – du musst **nur die Teile-und-herrsche-Funktion** `mergesort` schreiben (mitte teilen, links/rechts rekursiv, `merge`). Das Sortierkriterium (`<` bzw. `len(...)` bzw. Tupel) steckt in der **vorgegebenen** merge-Zeile – prüfe, ob du sie noch anpassen musst.

### Heapsort → 🟩 `heapify` gegeben, 🟨 `heap_sort` selbst
```python
def heap_sort(arr):                          # 🟨 DU schreibst nur diese Funktion
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):      # 🟨 1) Max-Heap aufbauen
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):            # 🟨 2) größtes ans Ende, Heap verkleinern
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def heapify(arr, n, i):                      # 🟩 in SS25 KOMPLETT vorgegeben!
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
💡 **Tipp (wichtig!):** Wie bei Merge – `heapify` ist geschenkt, du schreibst nur `heap_sort`: **erst Heap bauen** (`n//2-1` rückwärts), **dann n-mal** Wurzel ans Ende tauschen + `heapify` aufrufen. Zwei Schleifen, mehr nicht.

### 🔑 Nur die Vergleichszeile ändern (🟨 das ist meist deine eigentliche Denkleistung)
| Aufgabe | Vergleich |
|---|---|
| Zahlen aufsteigend | `a[j] > a[j + 1]` |
| Strings nach Länge (SS25/WS2526) | `len(a[j]) > len(a[j + 1])` |
| Dict nach Feld | `a[j]["gehalt"] > a[j + 1]["gehalt"]` |
| Länge, dann alphabetisch | `(len(a[j]), a[j]) > (len(a[j + 1]), a[j + 1])` |
| absteigend | `>` durch `<` ersetzen |

---

# 5) ZUSATZ: DATENSTRUKTUREN NUR AUS ALTKLAUSUREN

> Nicht im Skript – kamen nur in je einer Klausur. Vorgabe-Muster ist dasselbe: `Node` + Gerüst + Testaufruf 🟩, Methodenrümpfe 🟨.

### Trie / Präfixbaum (WS2526)
```python
class Node:                                  # 🟩 vorgegeben
    def __init__(self):
        self.kinder = {}
        self.ist_wortende = False

class Trie:                                  # 🟩 Gerüst + alle Signaturen + Testaufruf vorgegeben
    def __init__(self):                      # 🟩
        self.wurzel = Node()

    def einfuegen(self, wort):               # 🟨 Rumpf selbst (Vorlage: pass)
        aktueller = self.wurzel
        for ch in wort:
            if ch not in aktueller.kinder:
                aktueller.kinder[ch] = Node()
            aktueller = aktueller.kinder[ch]
        aktueller.ist_wortende = True

    def enthaelt(self, wort):                # 🟨 Rumpf selbst
        aktueller = self.wurzel
        for ch in wort:
            if ch not in aktueller.kinder:
                return False
            aktueller = aktueller.kinder[ch]
        return aktueller.ist_wortende

    def woerter_mit_praefix(self, praefix):  # 🟨 Rumpf selbst
        aktueller = self.wurzel
        for ch in praefix:
            if ch not in aktueller.kinder:
                return []
            aktueller = aktueller.kinder[ch]
        ergebnis = []
        self._sammle_woerter(aktueller, praefix, ergebnis)
        return ergebnis

    def _sammle_woerter(self, knoten, gebaut, ergebnis):   # 🟨 Rumpf selbst
        if knoten.ist_wortende:
            ergebnis.append(gebaut)
        for ch in sorted(knoten.kinder.keys()):
            self._sammle_woerter(knoten.kinder[ch], gebaut + ch, ergebnis)
```
💡 **Tipp:** Der Prof gibt Node + alle 4 leeren Methoden (`pass`) + den Testaufruf. Du schreibst alle vier Rümpfe. Leerer Präfix → alle Wörter (keine Sonderbehandlung nötig, da die for-Schleife dann 0× läuft).

### Ternärer Suchbaum (SS25)
```python
class Node:                                  # 🟩
    def __init__(self, wort):
        self.wort = wort
        self.links = None; self.mitte = None; self.rechts = None

class TernaererSuchbaum:                     # 🟩 Gerüst + Testaufruf vorgegeben
    def __init__(self):                      # 🟩
        self.wurzel = None
    def einfuegen(self, wort):               # 🟩 Wrapper vorgegeben (Root-Fall)
        if self.wurzel is None:
            self.wurzel = Node(wort)
        else:
            self._einfuegen_rekursiv(self.wurzel, wort)

    def _einfuegen_rekursiv(self, knoten, wort):   # 🟨 selbst (Vorlage: pass)
        if len(wort) < len(knoten.wort):
            if knoten.links is None: knoten.links = Node(wort)
            else: self._einfuegen_rekursiv(knoten.links, wort)
        elif len(wort) == len(knoten.wort):
            if knoten.mitte is None: knoten.mitte = Node(wort)
            else: self._einfuegen_rekursiv(knoten.mitte, wort)
        else:
            if knoten.rechts is None: knoten.rechts = Node(wort)
            else: self._einfuegen_rekursiv(knoten.rechts, wort)

    def inorder_ausgabe(self):               # 🟩 Wrapper vorgegeben
        self._gesammelt = []
        self._inorder(self.wurzel)
        print(", ".join(self._gesammelt))
    def _inorder(self, knoten):              # 🟨 selbst (Vorlage: nur `if knoten is not None: pass`)
        if knoten is not None:
            self._inorder(knoten.links)
            self._inorder(knoten.mitte)
            self._gesammelt.append(knoten.wort)
            self._inorder(knoten.rechts)
```
💡 **Tipp:** Node, beide Wrapper (`einfuegen`, `inorder_ausgabe`) und der Testaufruf sind geschenkt. Deine Aufgabe: `_einfuegen_rekursiv` (kürzer→links, gleich→mitte, länger→rechts) und die 4 Rekursionszeilen im `_inorder`.

### Zirkuläre verkettete Liste (WS2425)
```python
class Node:                                  # 🟩
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:                    # 🟩 __init__ + leere Signaturen vorgegeben
    def __init__(self):                      # 🟩
        self.head = None

    def insert(self, key):                   # 🟨 selbst (Vorlage: pass)
        neuer = Node(key)
        if self.head is None:
            self.head = neuer
            neuer.next = self.head           # zeigt auf sich selbst
        else:
            current = self.head
            while current.next != self.head:  # Abbruch bei head, nicht None!
                current = current.next
            current.next = neuer
            neuer.next = self.head           # Kreis schließen

    def delete(self, key):                   # 🟨 selbst
        if self.head is None: return
        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None; return
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = self.head.next
            last.next = self.head
            return
        current = self.head
        while current.next != self.head:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next

    def display(self):                       # 🟨 selbst
        if self.head is None:
            print("Liste ist leer"); return
        current = self.head
        while True:
            print(current.data)
            current = current.next
            if current == self.head:         # wieder am Anfang -> Stopp
                break
```
💡 **Tipp:** Prof gibt Node + `__init__` + die drei leeren Methoden (`pass`). Der ganze Trick gegenüber der normalen Liste: **Abbruch bei `!= self.head`** statt `!= None`, und beim Einfügen/Löschen den **Kreis wieder schließen**. `display` braucht `while True … break`, sonst Endlosschleife.
