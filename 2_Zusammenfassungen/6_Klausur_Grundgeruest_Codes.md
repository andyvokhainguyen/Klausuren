# Klausur-Grundgerüst (nur Codes) – was IMMER kommt

Vergleich aller 6 Altklausuren. Ergebnis: **jede Klausur hat dieselben 4 Code-Blöcke.**
**SS25 und WS2526 sind fast identisch** → das ist die wahrscheinlichste Vorlage für deine Klausur.

> ⚠️ **Nicht auf dem Hilfsmittel** (`Hilfsmittel_Klausur_Prog_25.pdf`, nur 1 Seite) – **das musst du auswendig können:** `argparse`, `max(dict, key=dict.get)` (häufigstes Element), `sorted(..., key=len)`, `if __name__ == "__main__":`, `with pytest.raises(...)`.
> **Aufgelistet/erlaubt** sind dagegen u.a.: `getopt.getopt`, `python file.py -a -b`, `open/read/readline(s)/write/writelines/close`, `pytest` + `assert`, `split`/`strip`/`replace`, `dict.get`, list/set/dict-Methoden, der Swap `a[j], a[j+1] = a[j+1], a[j]`.

## Übersicht: Welcher Code-Block in welcher Klausur

| Klausur | Block A: Testen | Block B: CLI + Datei | Block C: Datenstruktur | Block D: Sortieren |
|---|---|---|---|---|
| SS23 | bmi/addiere + pytest | argparse: Caesar-Datei | verkettete Liste (doppelt) | quicksort |
| WS2324 | blutdruck/negative + pytest | argparse: Atbash-Datei | **Stack** | insertionsort |
| SS24 | foo/vereinigung (White-Box) | getopt: Bilder kombinieren | **BST** | mergesort |
| WS2425 | minOfThree/ggt (White-Box) | getopt: Taschenrechner-Datei | zirkuläre Liste | quicksort |
| **SS25** | groesste_gerade/schnittmenge | **argparse: Logdatei** | **Baum (ternär)** | **heapsort (Strings n. Länge)** |
| **WS2526** | normalize_and_pack + Asserts | **getopt: Logdatei** | **Baum (Trie)** | **mergesort (Strings n. Länge)** |

➡️ **Diese 4 Blöcke kannst du fest einplanen.** (Die früher übliche Exception-Aufgabe fällt weg.)
➡️ **SS25 ≈ WS2526:** Logdatei-Tool + Baum + String-nach-Länge-Sortieren + Testfunktion. Genau das solltest du sicher können.

---

# BLOCK A – Testen (kommt IMMER)

**Muster:** Gegeben ist eine Funktion → (1) Äquivalenzklassen/Pfade bestimmen, (2) pytest schreiben.

### Grundgerüst pytest
```python
from src import aufgabeXX      # Modul importieren (Ordnerstruktur src/ + test/)

import pytest

def test_beschreibung():
    assert aufgabeXX.funktion(eingabe) == erwartet
```

### Regeln zum Testfälle-Finden (auswendig)
- **Black-Box (Äquivalenzklassen):** je if/elif/else-Kategorie eine Klasse + **Grenzwerte**; bei Listen: leer / 1 Element / mehrere / mit-ohne Duplikate.
- **White-Box (Pfade):** **Verzweigung** → beide Zweige; **Schleife** → 0/1/mehrfach; **Rekursion** → Basisfall/1×/mehrfach.

### Assertions (defensive Programmierung, WS2526-Typ)
```python
def funktion(werte, limit):
    assert type(werte) == list                              # Typ prüfen
    assert isinstance(limit, int), "limit muss int sein"    # mit Fehlermeldung
    assert all(isinstance(v, (int, float)) for v in werte)  # alle Elemente numerisch
    ...
# Verletzte Assertion -> AssertionError. In pytest so testen:
#   with pytest.raises(AssertionError):
#       funktion("kein_list", 10)
```

### Übung
```python
# Gegeben:
def note(punkte):
    if punkte < 0:      return "ungültig"
    elif punkte < 50:   return 5
    elif punkte < 60:   return 4
    else:               return 1

# TODO: 4-5 Äquivalenzklassen (inkl. Grenzwert 50) + je ein pytest-Test.
```
<details><summary>Lösung</summary>

```python
from src import aufgabeXX

def test_ungueltig():   assert aufgabeXX.note(-1) == "ungültig"
def test_fuenf():       assert aufgabeXX.note(30) == 5
def test_vier():        assert aufgabeXX.note(55) == 4
def test_eins():        assert aufgabeXX.note(80) == 1
def test_grenzwert_50():assert aufgabeXX.note(50) == 4   # 50 gehört zu "4"
```
</details>

---

# BLOCK B – Kommandozeile + Datei-IO (kommt IMMER)

**Muster (SS25/WS2526):** Datei einlesen → je nach Befehl zählen/auswerten → in Ausgabedatei schreiben.
Drei Zugänge zu den Argumenten – du musst **alle drei** erkennen und mindestens **getopt/argparse aktiv** können.

### Datei lesen/schreiben (auswendig)
```python
with open(pfad, "r", encoding="utf-8") as f:
    for zeile in f:              # zeilenweise
        zeile = zeile.strip()

with open(pfad, "w", encoding="utf-8") as f:
    f.write("Text\n")
```

### Grundgerüst 1 – sys.argv
```python
import sys
# sys.argv[0] = Skriptname, ab [1] die Argumente
if len(sys.argv) != 4:
    print("Aufruf: python prog.py <a> <b> <c>")
    sys.exit()
a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]
```

### Grundgerüst 2 – getopt
```python
import sys, getopt

def main(argv):
    inputfile = outputfile = befehl = ""
    try:
        opts, args = getopt.getopt(argv, "i:o:b:h",
                                   ["input=", "output=", "befehl=", "help"])
    except getopt.GetoptError:
        print("prog.py -i <in> -o <out> -b <befehl>"); sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"): print("..."); sys.exit()
        elif opt in ("-i", "--input"):  inputfile = arg
        elif opt in ("-o", "--output"): outputfile = arg
        elif opt in ("-b", "--befehl"): befehl = arg
    if inputfile == "" or outputfile == "" or befehl == "":
        print("Fehler: -i, -o, -b erforderlich"); sys.exit(2)
    # ... verarbeiten ...

if __name__ == "__main__":
    main(sys.argv[1:])
```

### Grundgerüst 3 – argparse
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

### Logdatei-Auswertung – das SS25/WS2526-Muster (auswendig!)
```python
from collections import Counter   # oder manuelles dict

def werte_aus(pfad, befehl):
    zaehler = Counter()
    with open(pfad, "r", encoding="utf-8") as f:
        for zeile in f:
            teile = zeile.strip().split(";")     # SS25: split()/"in", WS2526: ";"
            if len(teile) != 4:
                continue
            _zeit, level, user, action = teile
            if befehl == "level":  zaehler[level]  += 1
            elif befehl == "user": zaehler[user]   += 1
            elif befehl == "actions": zaehler[action] += 1
    return zaehler
```
*Häufigstes Wort/Element:* `max(zaehler, key=zaehler.get)`.

### Übung
```
Schreibe ein getopt-Tool 'zahlen.py -i <datei> -o <out> -b <summe|max>',
das eine Datei mit einer Zahl pro Zeile liest und Summe bzw. Maximum
in die Ausgabedatei schreibt.
```
<details><summary>Lösung</summary>

```python
import sys, getopt

def werte_aus(pfad, befehl):
    zahlen = []
    with open(pfad, "r", encoding="utf-8") as f:
        for zeile in f:
            if zeile.strip():
                zahlen.append(float(zeile))
    if befehl == "summe": return sum(zahlen)
    elif befehl == "max": return max(zahlen)

def main(argv):
    inputfile = outputfile = befehl = ""
    opts, args = getopt.getopt(argv, "i:o:b:", ["input=","output=","befehl="])
    for opt, arg in opts:
        if opt in ("-i","--input"):  inputfile = arg
        elif opt in ("-o","--output"): outputfile = arg
        elif opt in ("-b","--befehl"): befehl = arg
    ergebnis = werte_aus(inputfile, befehl)
    with open(outputfile, "w", encoding="utf-8") as f:
        f.write(f"Befehl: {befehl}\nErgebnis: {ergebnis}\n")

if __name__ == "__main__":
    main(sys.argv[1:])
```
</details>

---

# BLOCK C – Datenstruktur-Klasse (kommt IMMER)

Zwei Grund-Muster decken alles ab: **(1) verkettete Struktur (Durchlauf)** und **(2) Baum (Rekursion)**.

### Muster 1 – Durchlauf einer verketteten Struktur (auswendig)
```python
current = self.head
while current:
    # ... current.data verarbeiten ...
    current = current.next
```
Damit baust du: **Liste** (insert/print/delete/get), **Stack** (`append`/`pop`), **Queue** (`append`/`pop(0)`).

Stack/Queue-Kern:
```python
class Stack:                       class Queue:
    def __init__(self):                def __init__(self):
        self.stack = []                    self.queue = []
    def push(self, x):                 def enqueue(self, x):
        self.stack.append(x)               self.queue.append(x)
    def pop(self):                     def dequeue(self):
        return self.stack.pop()            return self.queue.pop(0)   # vorne!
```

### Muster 2 – Binärer Suchbaum (rekursiv, SS25/WS2526-Typ)
```python
class Node:
    def __init__(self, wert):
        self.wert = wert
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, wert):
        if self.root is None:
            self.root = Node(wert)
        else:
            self._insert(self.root, wert)

    def _insert(self, node, wert):          # <-- das rekursive Kernmuster
        if wert < node.wert:
            if node.left is None: node.left = Node(wert)
            else: self._insert(node.left, wert)
        else:
            if node.right is None: node.right = Node(wert)
            else: self._insert(node.right, wert)

    def _inorder(self, node):               # links -> Knoten -> rechts = sortiert
        if node is not None:
            self._inorder(node.left)
            print(node.wert)
            self._inorder(node.right)
```
> SS25 (ternärer Baum) und WS2526 (Trie) sind **Varianten** desselben rekursiven Einfüge-/Durchlauf-Musters – nur mit mehr Kindern (links/mitte/rechts bzw. dict `kinder`).

### Die 4 Klausur-Varianten (Kurz-Skelette)

**Trie (WS2526)** – Kinder als `dict`, Wortende-Markierung:
```python
class Node:
    def __init__(self):
        self.kinder = {}            # dict[str, Node]
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
    def enthaelt(self, wort):
        akt = self.wurzel
        for ch in wort:
            if ch not in akt.kinder:
                return False
            akt = akt.kinder[ch]
        return akt.ist_wortende
```

**Ternärer Suchbaum (SS25)** – Einordnung nach Wortlänge (kürzer/gleich/länger):
```python
class Node:
    def __init__(self, wort):
        self.wort = wort
        self.links = self.mitte = self.rechts = None

class TernaererSuchbaum:
    def __init__(self):
        self.wurzel = None
    def einfuegen(self, wort):
        if self.wurzel is None:
            self.wurzel = Node(wort)
        else:
            self._einfuegen(self.wurzel, wort)
    def _einfuegen(self, k, wort):
        if len(wort) < len(k.wort):
            if k.links is None: k.links = Node(wort)
            else: self._einfuegen(k.links, wort)
        elif len(wort) == len(k.wort):
            if k.mitte is None: k.mitte = Node(wort)
            else: self._einfuegen(k.mitte, wort)
        else:
            if k.rechts is None: k.rechts = Node(wort)
            else: self._einfuegen(k.rechts, wort)
    # Inorder-Ausgabe: links -> mitte -> Knoten -> rechts
```

**Zirkuläre verkettete Liste (WS2425)** – letzter Knoten zeigt auf `head`:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        neu = Node(data)
        if self.head is None:
            self.head = neu
            neu.next = self.head          # zeigt auf sich selbst
        else:
            cur = self.head
            while cur.next != self.head:  # bis zum letzten Knoten
                cur = cur.next
            cur.next = neu
            neu.next = self.head          # Kreis schließen
    def display(self):
        if self.head is None: return
        cur = self.head
        while True:
            print(cur.data)
            cur = cur.next
            if cur == self.head: break    # Abbruch bei Rückkehr zum Start
```

**Doppelt verkettete Liste + insertAfterElement (SS23)** – zusätzlich `prev`:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None                  # Rückwärts-Verweis
# insert(): wie einfach verkettet, zusätzlich  neu.prev = cur
def insertAfterElement(self, ziel, data): # neues Element NACH Knoten 'ziel'
    cur = self.head
    while cur:
        if cur.data == ziel:
            neu = Node(data)
            neu.prev = cur
            neu.next = cur.next
            if cur.next:
                cur.next.prev = neu
            cur.next = neu
            return
        cur = cur.next
```

### Übung
```
Implementiere die Methode search(wert) für den BinaryTree oben,
die True/False zurückgibt (rekursiv).
```
<details><summary>Lösung</summary>

```python
    def search(self, wert):
        return self._search(self.root, wert)

    def _search(self, node, wert):
        if node is None:            return False
        if wert == node.wert:       return True
        elif wert < node.wert:      return self._search(node.left, wert)
        else:                       return self._search(node.right, wert)
```
</details>

---

# BLOCK D – Sortierverfahren (kommt IMMER)

**Das Wichtigste:** Nimm den Standardalgorithmus und ändere **nur die Vergleichszeile**.
- Zahlen: `a > b` · Strings nach Länge: `len(a) > len(b)` · Dict nach Feld: `a["x"] > b["x"]`
- Zwei Kriterien: `(len(a), a) > (len(b), b)` · **absteigend**: `>` ↔ `<`

SS25/WS2526 sortieren **Strings nach Länge** → genau dieses Muster üben.

### Die drei „naiven" Verfahren (Skelette)
```python
def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:                 # <-- Vergleich
                a[j], a[j+1] = a[j+1], a[j]
    return a

def selection_sort(a):
    n = len(a)
    for i in range(n):
        m = i
        for j in range(i+1, n):
            if a[j] < a[m]:                   # <-- Vergleich (Minimum)
                m = j
        a[i], a[m] = a[m], a[i]
    return a

def insertion_sort(a):
    for i in range(1, len(a)):
        pivot = a[i]; j = i-1
        while j >= 0 and a[j] > pivot:        # <-- Vergleich
            a[j+1] = a[j]; j -= 1
        a[j+1] = pivot
    return a
```

### Divide-and-Conquer (Skelette)
```python
def quicksort(a):
    if len(a) <= 1: return a
    pivot = a[0]
    kleiner = [x for x in a[1:] if x <= pivot]     # <= behält Duplikate
    groesser = [x for x in a[1:] if x > pivot]
    return quicksort(kleiner) + [pivot] + quicksort(groesser)

def merge_sort(a):
    if len(a) <= 1: return a
    m = len(a)//2
    return merge(merge_sort(a[:m]), merge_sort(a[m:]))

def merge(l, r):
    erg = []; i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]: erg.append(l[i]); i += 1     # <-- Vergleich
        else:           erg.append(r[j]); j += 1
    erg.extend(l[i:]); erg.extend(r[j:])
    return erg
```

### Heapsort (SS25) – Max-Heap
```python
def heap_sort(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):    # 1) Max-Heap aufbauen
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):          # 2) Wurzel ans Ende, Heap verkleinern
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)
    return a

def heapify(a, n, i):
    largest = i
    left, right = 2 * i + 1, 2 * i + 2
    if left < n and a[left] > a[largest]:      # <-- Vergleich (bei Länge: len(...))
        largest = left
    if right < n and a[right] > a[largest]:    # <-- Vergleich
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)
```

### Komplexität (auswendig)
| Verfahren | best | mittel | schlecht |
|---|---|---|---|
| Bubble | O(n) | O(n²) | O(n²) |
| Selection | O(n²) | O(n²) | O(n²) |
| Insertion | O(n) | O(n²) | O(n²) |
| Quick | O(n·log n) | O(n·log n) | O(n²) |
| Merge | O(n·log n) | O(n·log n) | O(n·log n) |
| Heap | O(n·log n) | O(n·log n) | O(n·log n) |

### Übung (SS25/WS2526-Typ)
```
Sortiere ["Hallo","AI","Python","Zoo"] aufsteigend nach Länge mit merge_sort.
Welche Zeile musst du in merge() ändern?
```
<details><summary>Lösung</summary>

Nur die Vergleichszeile in `merge`:
```python
        if len(l[i]) < len(r[j]):     # statt l[i] < r[j]
```
Ergebnis: `['AI', 'Zoo', 'Hallo', 'Python']` (2,3,5,6).
Für „bei gleicher Länge alphabetisch": `if (len(l[i]), l[i]) < (len(r[j]), r[j]):`
</details>

---

# Deine Auswendig-Checkliste (nur Codes)

- [ ] pytest-Gerüst (`from src import ...`, `assert funktion(x) == y`) + Regeln für Äquivalenzklassen/Pfade
- [ ] Assertions (`assert isinstance(...)`) + `with pytest.raises(AssertionError)`
- [ ] Datei lesen/schreiben (`with open(...) as f`)
- [ ] getopt-Gerüst **und** argparse-Gerüst (Pflichtargumente + Befehl)
- [ ] Logdatei-Auswertung (`split(";")` + zählen + `max(..., key=...)`)
- [ ] verketteter Durchlauf (`while current: ... current = current.next`)
- [ ] Stack (`append`/`pop`) & Queue (`append`/`pop(0)`)
- [ ] BST: `_insert` (rekursiv) + `_inorder` + `_search`
- [ ] DS-Varianten: Trie (dict-Kinder), ternärer Baum, zirkuläre & doppelt verkettete Liste
- [ ] bubble / selection / insertion (Skelett + „nur Vergleichszeile ändern")
- [ ] quicksort + merge_sort/merge + **heap_sort/heapify**
- [ ] Sortieren **nach Länge** und **mit 2 Kriterien** (Tupel-Vergleich)
