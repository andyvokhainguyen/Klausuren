# 🎯 2-Tage-Lernplan: Diese Codes MUSST du können

Jeder Code hat eine **Eselsbrücke** (die Idee in einem Satz), **Zeilen-Erklärungen** und **typische Fehler**. Lerne nicht die Zeichen auswendig, sondern die **Idee** – dann kannst du den Code jederzeit neu herleiten.
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

## CODE 1: Datei lesen & schreiben
**Eselsbrücke:** *„with open – r zum Lesen, w zum Schreiben, für jede Zeile strip."*

```python
# LESEN – Zeile für Zeile
with open("daten.txt", "r", encoding="utf-8") as f:
    for zeile in f:                # gibt jede Zeile MIT \n am Ende
        zeile = zeile.strip()      # \n und Leerzeichen entfernen
        if zeile == "":            # leere Zeilen überspringen
            continue
        print(zeile)

# SCHREIBEN
with open("ergebnis.txt", "w", encoding="utf-8") as f:
    f.write("Erste Zeile\n")       # \n selbst anhängen!
```
**Warum so?** `with` schließt die Datei automatisch (kein `close()` nötig). `"r"` = read, `"w"` = write (überschreibt!), `"a"` = anhängen.
**Typische Fehler:** `\n` beim Schreiben vergessen · `strip()` vergessen (dann hängt `\n` an jedem Wort).

---

## CODE 2: getopt-Gerüst (WICHTIGSTER CODE! steht so ähnlich in JEDER Klausur)
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
        print("prog.py -i <in> -o <out> -b <befehl>")
        sys.exit(2)

    # 3) ZUORDNEN: jedes (Flag, Wert)-Paar in die richtige Variable
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

    # 4) PRÜFEN: getopt kennt kein "required" -> selbst checken
    if inputfile == "" or outputfile == "" or befehl == "":
        print("Fehler: -i, -o und -b sind erforderlich.")
        sys.exit(2)

    # 5) ... hier die eigentliche Arbeit (Code 3) ...


if __name__ == "__main__":
    main(sys.argv[1:])        # [1:] = ohne den Skriptnamen!
```
**Merke die Magie-Zeichen:** kurzes Flag mit Wert = **Doppelpunkt** (`"i:"`), langes Flag mit Wert = **Gleichheitszeichen** (`"input="`).
**Typische Fehler:** `sys.argv[1:]` vergessen (dann ist der Skriptname das erste „Argument") · Doppelpunkte vergessen · `opts, args =` (es kommen ZWEI Rückgaben).

---

## CODE 3: Logdatei auswerten (das SS25/WS2526-Herzstück)
**Eselsbrücke:** *„split, zählen im dict, max mit key."*

```python
def werte_aus(pfad, befehl):
    zaehler = {}                                   # leeres Zähl-Dictionary
    with open(pfad, "r", encoding="utf-8") as f:
        for zeile in f:
            teile = zeile.strip().split(";")       # "2025-05-10 ...;INFO;alice;login"
            if len(teile) != 4:                    # kaputte/leere Zeile überspringen
                continue
            _zeit, level, user, action = teile     # auspacken (4 Variablen!)

            if befehl == "level":
                schluessel = level
            elif befehl == "user":
                schluessel = user
            else:
                schluessel = action

            # zählen: get(x, 0) liefert 0, wenn Schlüssel noch nicht existiert
            zaehler[schluessel] = zaehler.get(schluessel, 0) + 1
    return zaehler


def schreibe_ergebnis(pfad, befehl, zaehler):
    with open(pfad, "w", encoding="utf-8") as f:
        f.write(f"Befehl: {befehl}\n")
        for schluessel, anzahl in zaehler.items():
            f.write(f"{schluessel}: {anzahl}\n")
```
**Bonus (NICHT auf dem Hilfsmittelblatt → merken!):**
```python
haeufigstes = max(zaehler, key=zaehler.get)    # Schlüssel mit größtem Wert
```
**Typische Fehler:** vergessen, dass `split(";")` eine **Liste** liefert · `.items()` beim Iterieren über dict-Paare vergessen.

---

## CODE 4: pytest + Testfälle finden
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

**Assertions in Funktionen prüfen (WS2526-Stil, merken):**
```python
def funktion(werte, limit):
    assert isinstance(limit, int), "limit muss int sein"
# und im Test:
with pytest.raises(AssertionError):
    funktion([1], "zehn")
```

---

# TAG 1 (Nachmittag + Abend) – Datenstrukturen & naive Sortierverfahren

## CODE 5: Stack & Queue (heißer Kandidat – kam noch NIE dran!)
**Eselsbrücke:** *„Beide sind eine Liste. Stack nimmt hinten (Stapel Teller), Queue nimmt vorne (Warteschlange Kasse)."*

```python
class Stack:                          # LIFO - Last In, First Out
    def __init__(self):
        self.stack = []

    def push(self, item):             # drauflegen
        self.stack.append(item)

    def pop(self):                    # OBERSTES nehmen = hinten
        if self.is_empty():
            return None
        return self.stack.pop()       # pop() ohne Zahl = letztes Element

    def peek(self):                   # nur angucken
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


class Queue:                          # FIFO - First In, First Out
    def __init__(self):
        self.queue = []

    def enqueue(self, item):          # hinten anstellen
        self.queue.append(item)

    def dequeue(self):                # VORDERSTES nehmen = vorne!
        if self.is_empty():
            return None
        return self.queue.pop(0)      # pop(0) = erstes Element  <<< DER Unterschied!

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]          # vorne angucken

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
```
**DER eine Unterschied:** Stack = `pop()` / `[-1]` (hinten) · Queue = `pop(0)` / `[0]` (vorne). Alles andere ist identisch!

---

## CODE 6: Einfach verkettete Liste
**Eselsbrücke:** *„Eine Schatzsuche: jeder Zettel (Node) zeigt zum nächsten. Laufen = `while current: current = current.next`."*

```python
class Node:
    def __init__(self, data):
        self.data = data              # der Wert
        self.next = None              # Zeiger auf den nächsten Knoten


class LinkedList:
    def __init__(self):
        self.head = None              # Anfang der Liste (erst mal leer)

    def insert(self, data):           # am ENDE anfügen
        neuer = Node(data)
        if self.head is None:         # Liste leer -> neuer Knoten ist der Kopf
            self.head = neuer
            return
        current = self.head
        while current.next:           # bis zum LETZTEN Knoten laufen
            current = current.next    #   (der hat next == None)
        current.next = neuer          # anhängen

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
        while current.next:
            if current.next.data == data:
                current.next = current.next.next   # Knoten überspringen
                return
            current = current.next
```
**Typische Fehler:** Sonderfall „Kopf löschen" vergessen · `while current.next` vs. `while current` verwechseln (insert braucht `.next`, print braucht `current`).

---

## CODE 7: Binärer Suchbaum (insert + inorder + search)
**Eselsbrücke:** *„Kleiner links, größer rechts. Platz frei? Einfügen! Sonst weiterfragen (Rekursion). Inorder = links-ich-rechts = sortiert."*

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

    def _insert(self, node, wert):            # das rekursive Kernmuster
        if wert < node.wert:                  # kleiner -> nach links
            if node.left is None:             #   Platz frei? einfügen
                node.left = Node(wert)
            else:                             #   sonst: dort weiterfragen
                self._insert(node.left, wert)
        else:                                 # größer/gleich -> nach rechts
            if node.right is None:
                node.right = Node(wert)
            else:
                self._insert(node.right, wert)

    def print_inorder(self):                  # gibt Werte SORTIERT aus
        self._inorder(self.root)

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)          # 1. links (alles Kleinere)
            print(node.wert)                  # 2. ich selbst
            self._inorder(node.right)         # 3. rechts (alles Größere)

    def search(self, wert):
        return self._search(self.root, wert)

    def _search(self, node, wert):
        if node is None:                      # unten angekommen: nicht da
            return False
        if wert == node.wert:
            return True
        elif wert < node.wert:
            return self._search(node.left, wert)
        else:
            return self._search(node.right, wert)
```
**Typische Fehler:** In `_inorder` die Reihenfolge (links → print → rechts) vertauschen · `is None`-Prüfung vergessen (Absturz).

---

## CODE 8: Bubble, Selection, Insertion – EIN Skelett, 3 Varianten
**Eselsbrücken:**
- **Bubble:** *„Blubberblasen: Nachbarn vergleichen, Größere blubbern nach hinten."*
- **Selection:** *„Casting-Show: such das Minimum, hol es nach vorne. Ein Tausch pro Runde."*
- **Insertion:** *„Kartenspiel: nimm die nächste Karte, schiebe Größere nach rechts, steck sie rein."*

```python
def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):                    # n-1 Runden
        for j in range(n - i - 1):            # hinten ist schon fertig (-i)
            if a[j] > a[j + 1]:               # Nachbarn falsch herum?
                a[j], a[j + 1] = a[j + 1], a[j]   # tauschen (steht auf Hilfsblatt!)
    return a


def selection_sort(a):
    n = len(a)
    for i in range(n):
        m = i                                 # Annahme: i ist das Minimum
        for j in range(i + 1, n):             # im Rest nach Kleinerem suchen
            if a[j] < a[m]:
                m = j                         # neues Minimum gemerkt (Index!)
        a[i], a[m] = a[m], a[i]               # EIN Tausch pro Runde
    return a


def insertion_sort(a):
    n = len(a)
    for i in range(1, n):                      # ab dem 2. Element
        pivot = a[i]                           # die "neue Karte"
        j = i - 1
        while j >= 0 and a[j] > pivot:         # alle Größeren...
            a[j + 1] = a[j]                    # ...nach rechts schieben
            j -= 1
        a[j + 1] = pivot                       # Karte in die Lücke
    return a
```

**🔑 DER Klausur-Trick – nur die Vergleichszeile ändern:**
| Aufgabe | Vergleich |
|---|---|
| Zahlen aufsteigend | `a[j] > a[j+1]` |
| **Strings nach Länge** (SS25/WS2526-Typ!) | `len(a[j]) > len(a[j+1])` |
| Dicts nach Feld | `a[j]["gehalt"] > a[j+1]["gehalt"]` |
| 2 Kriterien (Länge, dann ABC) | `(len(a[j]), a[j]) > (len(a[j+1]), a[j+1])` |
| absteigend | `>` durch `<` ersetzen |

---

# TAG 2 – Divide & Conquer + Generalprobe

## CODE 9: Quicksort & Mergesort
**Eselsbrücken:**
- **Quicksort:** *„Pivot wählen, Rest in kleiner/größer teilen, beide Hälften wieder quicksorten, zusammenkleben."*
- **Mergesort:** *„Halbieren bis einzeln, dann sortiert zusammenreißverschlussen."*

```python
def quicksort(a):
    if len(a) <= 1:                            # Basisfall: nichts zu tun
        return a
    pivot = a[0]
    kleiner  = [x for x in a[1:] if x <= pivot]    # <= behält Duplikate!
    groesser = [x for x in a[1:] if x > pivot]
    return quicksort(kleiner) + [pivot] + quicksort(groesser)


def merge_sort(a):
    if len(a) <= 1:                            # Basisfall
        return a
    mitte = len(a) // 2
    links = merge_sort(a[:mitte])              # linke Hälfte sortieren
    rechts = merge_sort(a[mitte:])             # rechte Hälfte sortieren
    return merge(links, rechts)                # zusammenführen


def merge(l, r):
    ergebnis = []
    i = j = 0
    while i < len(l) and j < len(r):           # Reißverschluss:
        if l[i] <= r[j]:                       #   das Kleinere zuerst
            ergebnis.append(l[i]); i += 1
        else:
            ergebnis.append(r[j]); j += 1
    ergebnis.extend(l[i:])                     # Reste anhängen
    ergebnis.extend(r[j:])
    return ergebnis
```
**Typische Fehler:** Basisfall vergessen (Endlos-Rekursion!) · bei quicksort `a[1:]` vergessen (Pivot doppelt) · nur `<` statt `<=` (Duplikate verschwinden).

**Komplexität (2 Zeilen merken):**
- Bubble/Selection/Insertion: **O(n²)** — Quick/Merge/Heap: **O(n·log n)**
- Ausnahmen: Bubble/Insertion best case **O(n)**; Quicksort worst case **O(n²)** (bei sortierter Liste + erstem Element als Pivot); Selection immer O(n²).

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
- [ ] Logdatei: `split(";")` → dict zählen → `max(d, key=d.get)`
- [ ] pytest-Gerüst + Testregeln (Grenzwert! leer! 0/1/mehrfach!)
- [ ] Stack (`pop()`) vs. Queue (`pop(0)`) — der EINE Unterschied
- [ ] Liste: Durchlauf-Muster + insert + delete (Kopf-Sonderfall!)
- [ ] BST: `_insert` + `_inorder` (links-ich-rechts) + `_search`
- [ ] Bubble + Selection + Insertion + „nur Vergleichszeile ändern"

**Tag 2:**
- [ ] Quicksort (`<=`!) + Mergesort/merge
- [ ] Sortieren nach `len()` und mit Tupel-Vergleich
- [ ] Probeklausur unter Realbedingungen bestanden
- [ ] Theorie 1× durchgelesen (`1_Theorie_SoftwareEngineering.md`)

**Notfall-Minimum** (wenn die Zeit knapp wird, DAS zuerst): getopt-Gerüst + Logdatei-Auswertung + ein Baum (`_insert`/`_inorder`) + ein Sortierverfahren nach Länge + pytest. Das ist das SS25/WS2526-Muster = wahrscheinlichste Klausur.
