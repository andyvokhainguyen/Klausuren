# ✍️ Übungsvorlagen zum Selberschreiben (Blank Page)

Hier steht **nur das, was der Professor vorgibt** (🟩). Überall wo `# ✍️ SELBST:` steht, musst **du** den Code schreiben – der kurze Hinweis sagt, was dort hingehört. Ideal zum Blank-Page-Üben: erst selbst versuchen, dann mit `3_Alle_Codes_zum_Abtippen.md` bzw. `7_Codes_Vorgabe_vs_Selbst.md` vergleichen.

**So üben:** Datei durchgehen → an jedem `# ✍️ SELBST:` stoppen → Code aus dem Kopf schreiben → mit der Lösungsdatei abgleichen.

---

# 1) TESTEN

**Gegeben:** die zu testende Funktion (fertig, in WS2526 mit eingebauten Bugs). **Selbst:** Tests + Assertions + Äquivalenzklassen.

### Assertions ergänzen (WS2526 Aufgabe 2e)
```python
def normalize_and_pack(values, limit):
    assert type(values) == list                  # 🟩 gegeben
    # ✍️ SELBST: weitere defensive Assertions
    #   - limit muss int sein         -> isinstance(limit, int)
    #   - alle Elemente numerisch     -> all(isinstance(v, (int, float)) for v in values)

    # 🟩 ab hier ist die Funktion vom Prof vorgegeben (evtl. mit Bug!)
    if limit < 0:
        raise ValueError("limit must be positive")
    ...
```

### pytest-Datei schreiben (test/test_aufgabe02.py)
```python
from src import aufgabe02        # 🟩 Import auf die gegebene Datei
import pytest

# ✍️ SELBST: pro Äquivalenzklasse / Pfad genau EIN Test
#   - Normalfall
#   - Grenzwert (genau AUF der Grenze)
#   - Randfall (leer / negativ / ungültig)
#   - pytest.raises(AssertionError) für falschen Typ
#   - @pytest.mark.xfail für bekannte Bugs

def test_beispiel():
    assert aufgabe02.funktion(80) == 1
    # ... weitere Tests hier
```
💡 **Hinweis:** Testnamen mit `test_` beginnen, Datei `test_*.py`. `with pytest.raises(ValueError):` für erwartete Exceptions.

---

# 2) KOMMANDOZEILE + DATEI-IO

**Gegeben:** meist nur der Docstring mit Beispielaufruf + ein `# TODO`. **Selbst:** so gut wie alles.

### Log-Analyse-Tool (so gibt der Prof es vor)
```python
"""
Aufgabe 3 - Analyse-Tool fuer Logdateien
Beispielaufruf:  python3 aufgabe03.py -i log.txt -o ergebnis.txt -b level
"""
# 🟩 mehr steht in der Vorlage NICHT.

# ✍️ SELBST: import sys, getopt

# ✍️ SELBST: def zaehle(dateiname, befehl):
#   with open(dateiname, "r", encoding="utf-8") as datei:
#       for zeile in datei: ... split(";") ... nach befehl zählen ...

# ✍️ SELBST: def schreibe_ergebnis(dateiname, befehl, ergebnis):
#   with open(dateiname, "w", ...) as datei: datei.write(...)

# ✍️ SELBST: def main(argv):
#   getopt.getopt(argv, "i:o:b:h", ["input=","output=","befehl=","help"])
#   Optionen in for-Schleife auslesen, Pflicht-Args + gültigen befehl prüfen

# ✍️ SELBST:
# if __name__ == "__main__":
#     main(sys.argv[1:])
```
💡 **Hinweis (getopt-Gerüst, komplett auswendig):**
```python
opts, args = getopt.getopt(argv, "i:o:b:h", ["input=", "output=", "befehl=", "help"])
for opt, arg in opts:
    if opt in ("-i", "--input"):  ...   # Buchstabe mit ':' braucht einen Wert
```

---

# 3) DATENSTRUKTUREN (Skript-Stoff)

**Gegeben:** `Node`, `__init__`, Wrapper-Methoden, Testaufruf. **Selbst:** die Methodenrümpfe.

### Einfach verkettete Liste (SS23)
```python
class Node:                                  # 🟩
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:                            # 🟩
    def __init__(self):                      # 🟩
        self.head = None

    def insert(self, data):                  # 🟩 vorgegeben
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):                    # 🟩 vorgegeben
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def delete(self, data):
        # ✍️ SELBST: Element mit Wert `data` entfernen
        #   1) Liste leer -> return
        #   2) Kopf-Sonderfall: self.head.data == data -> self.head = self.head.next
        #   3) sonst mit current.next durchlaufen und Knoten überspringen
        pass
```

### Stack (LIFO) & Queue (FIFO) (WS2324)
```python
class Stack:                                 # 🟩
    def __init__(self):                      # 🟩
        self.stack = []
    def push(self, item):                    # 🟩 vorgegeben
        self.stack.append(item)

    def pop(self):
        # ✍️ SELBST: oberstes (LETZTES) Element entfernen + zurückgeben; leer -> None
        pass
    def peek(self):
        # ✍️ SELBST: oberstes Element ansehen (self.stack[-1]); leer -> None
        pass
    def is_empty(self):
        # ✍️ SELBST: True, wenn len == 0
        pass
    def display(self):
        # ✍️ SELBST: print(self.stack)
        pass


class Queue:                                 # 🟩 __init__/enqueue vorgegeben
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        # ✍️ SELBST: VORDERSTES Element entfernen -> self.queue.pop(0); leer -> None
        pass
    def display(self):
        # ✍️ SELBST: print(self.queue)
        pass
```
💡 **Hinweis:** Einziger Unterschied Stack↔Queue: entfernen hinten (`[-1]`/`del`) vs. vorne (`pop(0)`).

### Binärer Suchbaum (SS24)
```python
class Node:                                  # 🟩
    def __init__(self, data):
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

    def _insert(self, data, node):
        # ✍️ SELBST: rekursiv einfügen
        #   data < node.data -> links; sonst rechts
        #   ist der Platz None -> neuen Node(data), sonst rekursiv weiter
        pass

    def print_tree(self):
        # ✍️ SELBST: Wrapper -> self._print_tree(self.root), falls root vorhanden
        pass
    def _print_tree(self, node):
        # ✍️ SELBST: In-order (links -> print(node.data) -> rechts) = sortierte Ausgabe
        pass
```

### Doppelt verkettete Liste (Skript-Übung)
```python
class Node:
    def __init__(self, data):
        self.data = data
        # ✍️ SELBST: zusätzlich self.prev = None   (das ist der Unterschied!)
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        # ✍️ SELBST: am Ende anhängen UND neuer.prev = letzter Knoten setzen
        pass
    def print_rueckwaerts(self):
        # ✍️ SELBST: bis ans Ende laufen, dann über .prev rückwärts ausgeben
        pass
```

---

# 4) SORTIERVERFAHREN

**Gegeben:** Signatur + Docstring + Testaufruf. **Bei Merge/Heap zusätzlich die Hilfsfunktion.** **Selbst:** der Hauptalgorithmus.

### Bubble / Selection / Insertion (nur Signatur + Testaufruf gegeben)
```python
def bubble_sort(numbers):
    # ✍️ SELBST: benachbarte tauschen, wenn numbers[j] > numbers[j+1]
    #   äußere Schleife range(n-1), innere range(0, n-i-1), Flag zum Früh-Abbruch
    pass

def selection_sort(numbers):
    # ✍️ SELBST: Minimum im unsortierten Rest suchen (min_index), dann tauschen
    pass

def insertion_sort(numbers):
    # ✍️ SELBST: pivot = numbers[i], größere nach rechts schieben, pivot einsetzen
    pass
```
💡 **Hinweis:** Bei diesen dreien kommt der **ganze** Algorithmus von dir. Sortierkriterium nur in der Vergleichszeile (`>` / `len(...)` / Tupel).

### Quicksort (nur Signatur + Testaufruf gegeben)
```python
def quicksort(numbers):
    # ✍️ SELBST:
    #   Basisfall: len <= 1 -> return numbers
    #   pivot = numbers[0]
    #   kleiner = [x ... if x <= pivot], groesser = [x ... if x > pivot]
    #   return quicksort(kleiner) + [pivot] + quicksort(groesser)
    pass
```

### Mergesort — 🟩 `merge` ist GESCHENKT, du schreibst nur `mergesort`
```python
def mergesort(numbers):
    # ✍️ SELBST: Teile-und-herrsche
    #   Basisfall len <= 1 -> return numbers
    #   mid = len//2; links = mergesort(numbers[:mid]); rechts = mergesort(numbers[mid:])
    #   return merge(links, rechts)
    pass

def merge(left, right):                      # 🟩 KOMPLETT vom Prof vorgegeben
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:               # (nach Länge: len(left[i]) < len(right[j]))
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```
💡 **Hinweis:** Du schreibst hier **nur 4 Zeilen** (`mergesort`). Prüfe, ob die vorgegebene `merge`-Vergleichszeile schon zum geforderten Kriterium passt.

### Heapsort — 🟩 `heapify` ist GESCHENKT, du schreibst nur `heap_sort`
```python
def heap_sort(arr):
    # ✍️ SELBST:
    #   n = len(arr)
    #   1) Max-Heap bauen: for i in range(n//2 - 1, -1, -1): heapify(arr, n, i)
    #   2) for i in range(n-1, 0, -1): arr[i],arr[0]=arr[0],arr[i]; heapify(arr, i, 0)
    pass

def heapify(arr, n, i):                      # 🟩 KOMPLETT vom Prof vorgegeben
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
💡 **Hinweis:** Du schreibst nur `heap_sort` (zwei Schleifen). `heapify` ist gegeben.

### 🔑 Vergleichszeile (das ist oft deine eigentliche Denkleistung)
| Aufgabe | Vergleich |
|---|---|
| Zahlen aufsteigend | `a[j] > a[j + 1]` |
| Strings nach Länge | `len(a[j]) > len(a[j + 1])` |
| Länge, dann alphabetisch | `(len(a[j]), a[j]) > (len(a[j + 1]), a[j + 1])` |
| absteigend | `>` durch `<` |

---

# 5) ZUSATZ: DATENSTRUKTUREN NUR AUS ALTKLAUSUREN

### Trie / Präfixbaum (WS2526) — Prof gibt Gerüst, alle 4 Methoden sind leer
```python
class Node:                                  # 🟩
    def __init__(self):
        self.kinder = {}
        self.ist_wortende = False

class Trie:                                  # 🟩 Gerüst + Testaufruf gegeben
    def __init__(self):                      # 🟩
        self.wurzel = Node()

    def einfuegen(self, wort):
        # ✍️ SELBST: pro Buchstabe: fehlt Kind -> Node(); am Ende ist_wortende = True
        pass
    def enthaelt(self, wort):
        # ✍️ SELBST: Wort ablaufen; fehlt Buchstabe -> False; am Ende ist_wortende zurück
        pass
    def woerter_mit_praefix(self, praefix):
        # ✍️ SELBST: zum Präfix-Knoten laufen, dann _sammle_woerter aufrufen
        pass
    def _sammle_woerter(self, knoten, gebaut, ergebnis):
        # ✍️ SELBST: wenn ist_wortende -> anhängen; für sorted(kinder) rekursiv sammeln
        pass

trie = Trie()                                # 🟩 Testaufruf vorgegeben
for w in ["cat", "car", "cart", "dog", "dot", "dove"]:
    trie.einfuegen(w)
print(trie.woerter_mit_praefix("ca"))
```

### Ternärer Suchbaum (SS25) — Wrapper gegeben, Rekursion selbst
```python
class Node:                                  # 🟩
    def __init__(self, wort):
        self.wort = wort
        self.links = None; self.mitte = None; self.rechts = None

class TernaererSuchbaum:                     # 🟩
    def __init__(self):                      # 🟩
        self.wurzel = None
    def einfuegen(self, wort):               # 🟩 Wrapper vorgegeben
        if self.wurzel is None:
            self.wurzel = Node(wort)
        else:
            self._einfuegen_rekursiv(self.wurzel, wort)

    def _einfuegen_rekursiv(self, knoten, wort):
        # ✍️ SELBST: nach LÄNGE einordnen
        #   len(wort) < len(knoten.wort) -> links
        #   ==                            -> mitte
        #   >                             -> rechts
        #   Platz None -> Node(wort), sonst rekursiv
        pass

    def inorder_ausgabe(self):               # 🟩 Wrapper vorgegeben
        self._gesammelt = []
        self._inorder(self.wurzel)
        print(", ".join(self._gesammelt))
    def _inorder(self, knoten):
        # ✍️ SELBST: links -> mitte -> knoten.wort anhängen -> rechts
        if knoten is not None:
            pass
```

### Zirkuläre verkettete Liste (WS2425) — Node + __init__ gegeben
```python
class Node:                                  # 🟩
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:                    # 🟩
    def __init__(self):                      # 🟩
        self.head = None

    def insert(self, key):
        # ✍️ SELBST: am Ende einfügen
        #   leer -> head = neuer; neuer.next = head (zeigt auf sich selbst)
        #   sonst bis current.next == self.head laufen, anhängen, Kreis schließen
        pass
    def delete(self, key):
        # ✍️ SELBST: head-Fall (auch "nur 1 Element") + Mitte/Ende (Knoten überspringen)
        pass
    def display(self):
        # ✍️ SELBST: while True: print; weiter; if current == self.head: break
        pass
```
💡 **Hinweis:** Der Trick überall: Abbruch bei `!= self.head` (nicht `!= None`) und Kreis wieder schließen.
