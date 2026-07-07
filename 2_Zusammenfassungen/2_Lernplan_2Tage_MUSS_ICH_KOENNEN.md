# 🎯 2-Tage-Lernplan: Diese Codes MUSST du können

Jeder Code ist **originalgetreu aus Skript bzw. Altklausur** übernommen (gleiche Struktur, gleiche Variablennamen) – du lernst also exakt die Form, die der Prof verwendet und erwartet. Dazu: **Eselsbrücke** (die Idee in einem Satz), Erklärungen und typische Fehler.
**Tempo-Regel bei 2 Tagen:** Was du schon sicher kannst, hakst du per Schnelltest ab (einmal fehlerfrei aus dem Kopf schreiben = fertig, weiter) – die volle Lernschleife nur für Unsicheres.

**So lernst du jeden unsicheren Code (4 Schritte):**
1. Code **lesen** + Erklärung verstehen
2. **Abtippen** in VSCode und **ausführen** (er muss laufen!)
3. Datei zuklappen → **aus dem Kopf neu schreiben** (Blank-Page!)
4. Vergleichen, Fehler markieren → am nächsten Block nur Schritt 3 wiederholen

> ⚠️ Aufs Hilfsmittelblatt (1 Seite) kannst du nur Syntax schreiben. **NICHT drauf** (auswendig!): `max(d, key=d.get)`, `sorted(key=len)`, `if __name__ == "__main__":`, argparse.

---

# 📅 DER PLAN (2 Tage)

| Tag | Vormittag (~2,5h) | Nachmittag (~2,5h) | Abend (~1,5h) |
|---|---|---|---|
| **Tag 1** | Code 1–4: Datei-IO, getopt, Logdatei-Tool, pytest | Code 5–7: Stack/Queue, verkettete Liste, BST | Code 8: die 3 naiven Sorts + Blank-Page über ALLES von heute |
| **Tag 2** | Code 9: Quick/Merge + „nach Länge" + Blank-Page-Wdh. Tag 1 | **Probeklausur real schreiben** (90 min, nur Hilfsmittelblatt!) | Fehler nacharbeiten + Theorie 1× lesen |

Empfehlung Tag 2 nachmittags: `5_Probeklausur/2_Probeklausur` (getopt + Liste + Selection = wahrscheinlichste Mischung). Theorie abends: `1_Theorie_SoftwareEngineering.md`.
**Priorität, falls die Zeit nicht reicht:** Code 2+3 (getopt+Logdatei) > Code 8 (Sorts nach Länge) > Code 7 (BST) > Code 4 (pytest) > Rest. Das ist das SS25/WS2526-Muster.

---

# TAG 1 (Vormittag) – Datei, Kommandozeile, Testen

## CODE 1: Datei lesen & schreiben *(Quelle: Skript 04 + Altklausuren)*
**Eselsbrücke:** *„open – lesen/schreiben – close. Oder with, dann schließt es sich selbst."*

```python
# Skript-Form (Skript 04):
f = open("morgenstern.txt", "r")
print(f.read())                    # gesamter Inhalt; f.readline() = eine Zeile
f.close()

f = open("meinWitz.txt", "w")
f.write("Treffen sich zwei Jäger.\nBeide tot.")   # \n selbst anhängen!
f.close()

# Altklausur-Form (SS23-WS2526) - zeilenweise mit with:
with open("log.txt", "r", encoding="utf-8") as datei:
    for zeile in datei:            # jede Zeile MIT \n am Ende
        if zeile.strip() == "":    # leere Zeilen überspringen (SS25-Stil)
            continue
        print(zeile.strip())

with open("ergebnis.txt", "w", encoding="utf-8") as datei:
    datei.write("Erste Zeile\n")
```
**Merke:** `"r"` = lesen, `"w"` = schreiben (überschreibt!), `"a"` = anhängen. `with` schließt automatisch (kein `close()` nötig) – so machen es alle Klausurlösungen ab SS23.
**Typische Fehler:** `\n` beim Schreiben vergessen · `strip()` vergessen (dann hängt `\n` an jedem Wort).

---

## CODE 2: getopt-Gerüst *(Quelle: Altklausuren SS24 + WS2425, Original-Struktur)*
**Eselsbrücke:** *„try getopt – for opt – if fehlt: Fehler"* (3 Abschnitte: parsen, zuordnen, prüfen)

```python
import sys
import getopt


def main(argv):
    # 1) Variablen mit leeren Startwerten
    inputfile = ""
    outputfile = ""
    befehl = ""

    # 2) PARSEN: "i:o:b:h" -> i,o,b erwarten einen WERT (Doppelpunkt!), h nicht
    try:
        opts, args = getopt.getopt(argv, "i:o:b:h",
                                   ["input=", "output=", "befehl=", "help"])
    except getopt.GetoptError:                      # unbekannte Option
        print("prog.py -i <inputfile> -o <outputfile> -b <befehl>")
        sys.exit(2)

    # 3) ZUORDNEN: jedes (Flag, Wert)-Paar in die richtige Variable
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("prog.py -i <inputfile> -o <outputfile> -b <befehl>")
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg
        elif opt in ("-b", "--befehl"):
            befehl = arg

    # 4) PRÜFEN: getopt kennt kein "required" -> selbst checken (WS2425-Stil)
    if inputfile == "" or outputfile == "" or befehl == "":
        print("Fehler: Es fehlen Argumente. Erforderlich: -i, -o, -b")
        sys.exit(2)

    # 5) ... hier die eigentliche Arbeit (Code 3) ...


if __name__ == "__main__":
    main(sys.argv[1:])        # [1:] = ohne den Skriptnamen!
```
**Merke die Magie-Zeichen:** kurzes Flag mit Wert = **Doppelpunkt** (`"i:"`), langes Flag mit Wert = **Gleichheitszeichen** (`"input="`). Genau so auf dem Hilfsmittelblatt: `getopt.getopt(args, shortopts, longopts)`.
**Typische Fehler:** `sys.argv[1:]` vergessen · Doppelpunkte vergessen · `opts, args =` (es kommen ZWEI Rückgaben).

---

## CODE 3: Logdatei auswerten *(Quelle: SS25 + WS2526, die letzten beiden Klausuren!)*
**Eselsbrücke:** *„split, im dict zählen, ausgeben."*

```python
def werte_logdatei_aus(pfad, befehl):
    zaehler = {}                                   # Zähl-Dictionary
    with open(pfad, "r", encoding="utf-8") as datei:
        for zeile in datei:
            teile = zeile.strip().split(";")       # "2025-05-10 ...;INFO;alice;login"
            if len(teile) != 4:                    # kaputte/leere Zeile überspringen
                continue
            _zeitstempel, level, user, action = teile   # auspacken (4 Variablen!)

            if befehl == "level":
                schluessel = level
            elif befehl == "user":
                schluessel = user
            else:
                schluessel = action

            # Zählen im Dictionary (Form wie in der Blatt-0-Musterlösung):
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
```
**Einfachere SS25-Variante** (nur zählen, wenn ein Wort in der Zeile steht):
```python
def zaehle(pfad, befehl):
    anzahl = 0
    with open(pfad, "r", encoding="utf-8") as datei:
        for zeile in datei:
            if zeile.strip() == "":
                continue
            if befehl == "count":
                anzahl += 1
            elif befehl == "errors":
                if "ERROR" in zeile:
                    anzahl += 1
    return anzahl
```
**Häufigstes Wort/Element** (stand auf dem alten Hilfsmittelblatt, auf dem neuen NICHT mehr → merken!):
```python
haeufigstes = max(zaehler, key=zaehler.get)    # Schlüssel mit größtem Wert
```
**Typische Fehler:** `split(";")` liefert eine **Liste** · `.items()` beim Iterieren über dict-Paare vergessen.

---

## CODE 4: pytest + Testfälle finden *(Quelle: Altklausur-Testdateien, Original-Form)*
**Eselsbrücke:** *„from src import – def test_ – assert."* Und für die Fälle: *„Grenzen, leer, normal."*

```python
from src import aufgabe02        # Datei aufgabe02.py im Ordner src/

import pytest


def test_normalfall():
    assert aufgabe02.note(80) == 1

def test_grenzwert_50():
    assert aufgabe02.note(50) == 4      # genau AUF der Grenze testen!

def test_ungueltig():
    assert aufgabe02.note(-1) == "ungültig"
```

**Regeln zum Testfälle-Finden (auswendig – gibt sichere Punkte):**
| Situation | Testfälle |
|---|---|
| if/elif/else-Kategorien | je Kategorie 1 Wert **+ 1 Grenzwert** (genau auf der Grenze) |
| Liste als Eingabe | leer `[]`, ein Element, mehrere, (mit/ohne Duplikate) |
| Schleife (White-Box) | 0× / 1× / mehrfach durchlaufen |
| Rekursion (White-Box) | Basisfall / 1× rekursiv / mehrfach rekursiv |

**Assertions prüfen (WS2526-Klausur, Aufgabe 2e):**
```python
# In der Funktion (WS2526-Original):
assert type(values) == list
assert isinstance(limit, int), "limit muss eine ganze Zahl sein"

# Im Test prüfen, dass die Assertion anschlägt:
def test_falscher_typ():
    with pytest.raises(AssertionError):
        aufgabe02a.normalize_and_pack([1, 2], 10.5)
```

---

# TAG 1 (Nachmittag + Abend) – Datenstrukturen & naive Sortierverfahren

## CODE 5: Stack & Queue *(Quelle: Skript 05, Original-Form + WS2324-Erweiterung)*
**Eselsbrücke:** *„Beide sind eine Liste. Stack nimmt hinten (Stapel Teller), Queue nimmt vorne (Warteschlange Kasse)."*

```python
# Skript-Form (Skript 05):
class Stack:
    def __init__(self):
        self.stack = []

    # Add an element
    def push(self, item):
        self.stack.append(item)

    # Remove an element
    def pop(self):
        if len(self.stack) < 1:
            return None
        removed_item = self.stack[-1]      # oberstes = letztes Element
        del self.stack[-1]
        return removed_item

    # Display the stack
    def display(self):
        print(self.stack)


class Queue:
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)           # vorderstes Element!  <<< DER Unterschied

    # Display the queue
    def display(self):
        print(self.queue)
```
**Erweiterung aus der WS2324-Klausur** (dort für den Stack gefordert – für die Queue analog):
```python
    def peek(self):
        """Gibt das oberste Element zurück, ohne es zu entfernen."""
        if self.is_empty():
            return None
        return self.stack[-1]              # bei Queue: self.queue[0]

    def is_empty(self):
        """Gibt True zurück, wenn der Stack leer ist, sonst False."""
        return len(self.stack) == 0
```
**DER eine Unterschied:** Stack entnimmt **hinten** (`[-1]`/`pop()`), Queue entnimmt **vorne** (`pop(0)`/`[0]`). Alles andere ist identisch!

---

## CODE 6: Einfach verkettete Liste *(Quelle: Skript 05, Original-Form)*
**Eselsbrücke:** *„Schatzsuche: jeder Zettel (Node) zeigt zum nächsten. Laufen = `while current: current = current.next`."*

```python
class Node:
    def __init__(self, data):
        self.data = data              # der Wert
        self.next = None              # Zeiger auf den nächsten Knoten


class LinkedList:
    def __init__(self):
        self.head = None              # Anfang der Liste (erst mal leer)

    def insert(self, data):           # am ENDE anfügen
        if not self.head:             # Liste leer -> neuer Knoten ist der Kopf
            self.head = Node(data)
        else:
            current = self.head
            while current.next:       # bis zum LETZTEN Knoten laufen
                current = current.next
            current.next = Node(data) # anhängen

    def print_list(self):
        current = self.head
        while current:                # DAS Durchlauf-Muster (auswendig!)
            print(current.data)
            current = current.next

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:    # Sonderfall: Kopf löschen
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next   # Knoten überspringen
                return
            current = current.next
```
**Typische Fehler:** Sonderfall „Kopf löschen" vergessen · `while current.next` vs. `while current` verwechseln (insert braucht `.next`, print braucht `current`).

---

## CODE 7: Binärer Suchbaum *(Quelle: Skript 05, Original-Form; search aus Übungsblatt 6)*
**Eselsbrücke:** *„Kleiner links, größer rechts. Platz frei? Einfügen! Sonst weiterfragen (Rekursion). Inorder = links-ich-rechts = sortiert."*

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

    def _insert(self, data, node):            # Skript-Signatur: (data, node)!
        if data < node.data:                  # kleiner -> nach links
            if node.left is None:             #   Platz frei? einfügen
                node.left = Node(data)
            else:                             #   sonst: dort weiterfragen
                self._insert(data, node.left)
        else:                                 # größer/gleich -> nach rechts
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def print_tree(self):                     # gibt Werte SORTIERT aus (In-order)
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)       # 1. links (alles Kleinere)
            print(str(node.data))             # 2. ich selbst
            self._print_tree(node.right)      # 3. rechts (alles Größere)

    # search wie in Übungsblatt 6 (Bücherverwaltung) gefordert:
    def search(self, data):
        return self._search(data, self.root)

    def _search(self, data, node):
        if node is None:                      # unten angekommen: nicht da
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search(data, node.left)
        else:
            return self._search(data, node.right)
```
**Typische Fehler:** In `_print_tree` die Reihenfolge (links → print → rechts) vertauschen · `is None`-Prüfung vergessen (Absturz) · Skript-Signatur ist `_insert(data, node)` – **data zuerst**.

---

## CODE 8: Bubble, Selection, Insertion *(Quelle: Skript 06, Original-Form)*
**Eselsbrücken:**
- **Bubble:** *„Blubberblasen: Nachbarn vergleichen, Größere blubbern nach hinten."*
- **Selection:** *„Casting-Show: such das Minimum, hol es nach vorne. Ein Tausch pro Runde."*
- **Insertion:** *„Kartenspiel: nimm die nächste Karte, schiebe Größere nach rechts, steck sie rein."*

```python
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        list_sorted = True                    # Skript-Optimierung!
        for j in range(0, n - i - 1):         # hinten ist schon fertig (-i)
            if numbers[j] > numbers[j + 1]:   # Nachbarn falsch herum?
                # Tausche die Positionen (Swap steht auf dem Hilfsblatt!)
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                list_sorted = False
        if list_sorted:
            # kein Vertauschen erforderlich gewesen -> fertig
            return


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


def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):                     # ab dem 2. Element
        pivot = numbers[i]                    # die "neue Karte"
        j = i - 1
        while j >= 0 and numbers[j] > pivot:  # alle Größeren...
            numbers[j + 1] = numbers[j]       # ...nach rechts schieben
            j -= 1
        numbers[j + 1] = pivot                # Karte in die Lücke
```
**Hinweis:** Die Skript-Versionen sortieren **in-place** (kein `return numbers` nötig – die Liste ist danach sortiert).

**🔑 DER Klausur-Trick – nur die Vergleichszeile ändern** (so in den Altklausuren angewandt):
| Aufgabe (Klausur) | Vergleich |
|---|---|
| Zahlen aufsteigend (Skript) | `numbers[j] > numbers[j + 1]` |
| **Strings nach Länge** (SS25 heapsort) | `len(liste[links]) > len(liste[groesster])` |
| Zeichen eines Strings (WS2324 insertionsort) | vorher `zeichen = list(input_text)`, am Ende `"".join(zeichen)` |
| Dokumente/Dicts nach Schlüssel (WS2425) | Schlüssel `(len(inhalt), titel)` bilden, Tupel vergleichen |
| **Länge, dann alphabetisch** (WS2526 merge) | `(len(left[i]), left[i]) <= (len(right[j]), right[j])` |

---

# TAG 2 – Divide & Conquer + Generalprobe

## CODE 9: Quicksort & Mergesort *(Quelle: Skript 06 + SS23/WS2526-Klausuren, Original-Form)*
**Eselsbrücken:**
- **Quicksort:** *„Pivot wählen, Rest in kleiner/größer teilen, beide Hälften wieder quicksorten, zusammenkleben."*
- **Mergesort:** *„Halbieren bis einzeln, dann sortiert zusammenführen (Reißverschluss)."*

```python
# Quicksort in der SS23-Klausur-Form (mit <= für Duplikate):
def quicksort(numbers):
    # Basisfall: 0 oder 1 Element ist bereits sortiert
    if len(numbers) <= 1:
        return numbers

    # Pivot = erstes Element; '<=' behält Duplikate (sonst gehen sie verloren!)
    pivot = numbers[0]
    kleiner = [x for x in numbers[1:] if x <= pivot]
    groesser = [x for x in numbers[1:] if x > pivot]

    # Rekursiv sortieren und zusammensetzen
    return quicksort(kleiner) + [pivot] + quicksort(groesser)
```

```python
# Mergesort in der Skript-Form (Skript 06):
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
**WS2526-Klausur-Variante** (Strings: erst Länge, bei Gleichstand alphabetisch) – nur die Vergleichszeile in `merge`:
```python
        if (len(left[left_index]), left[left_index]) <= (len(right[right_index]), right[right_index]):
```
**Typische Fehler:** Basisfall vergessen (Endlos-Rekursion!) · bei quicksort `numbers[1:]` vergessen (Pivot doppelt) · nur `<` statt `<=` (Duplikate verschwinden).

**Komplexität (2 Zeilen merken):**
- Bubble/Selection/Insertion: **O(n²)** — Quick/Merge/Heap: **O(n·log n)**
- Ausnahmen: Bubble/Insertion best case **O(n)**; Quicksort worst case **O(n²)**; Selection immer O(n²).

---

## Tag 2 Nachmittag: GENERALPROBE
1. `5_Probeklausur/2_Probeklausur/Aufgaben.md` öffnen
2. **90 Minuten Timer**, nur `Hilfsmittel_Klausur_Prog_25.pdf` daneben
3. Alles in VSCode schreiben und **ausführen**
4. Mit `Loesung.md` vergleichen, Fehler auf einen Zettel → die abends nochmal als Blank-Page

---

# ✅ FINALE CHECKLISTE (vor der Klausur alle Haken?)

**Tag 1:**
- [ ] Datei lesen (`with open`, `strip`) & schreiben (`\n`!)
- [ ] getopt-Gerüst komplett aus dem Kopf (parsen → zuordnen → prüfen)
- [ ] Logdatei: `split(";")` → dict zählen (`if x in d: ... else: ...`) → `max(d, key=d.get)`
- [ ] pytest-Gerüst + Testregeln (Grenzwert! leer! 0/1/mehrfach!)
- [ ] Stack (hinten: `[-1]`/`del`) vs. Queue (vorne: `pop(0)`) — der EINE Unterschied
- [ ] Liste: Durchlauf-Muster + insert (`if not self.head`) + delete (Kopf-Sonderfall!)
- [ ] BST: `_insert(data, node)` + `_print_tree` (links-ich-rechts) + `_search`
- [ ] Bubble (mit `list_sorted`) + Selection (`min_index`) + Insertion (`pivot`)

**Tag 2:**
- [ ] Quicksort (`<=` für Duplikate!) + merge_sort/merge (Skript-Namen!)
- [ ] Vergleichszeile umbauen: nach `len()` / Tupel `(len(s), s)`
- [ ] Probeklausur unter Realbedingungen bestanden
- [ ] Theorie 1× durchgelesen (`1_Theorie_SoftwareEngineering.md`)

**Notfall-Minimum** (wenn die Zeit knapp wird, DAS zuerst): getopt-Gerüst + Logdatei-Auswertung + BST (`_insert`/`_print_tree`) + ein Sortierverfahren nach Länge + pytest. Das ist das SS25/WS2526-Muster = wahrscheinlichste Klausur.
