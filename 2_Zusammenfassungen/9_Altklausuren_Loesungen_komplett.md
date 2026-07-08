# 📚 Alle Altklausur-Lösungen komplett (SS23 – WS2526)

Vollständige Musterlösungen **aller 6 Altklausuren**, chronologisch, Aufgabe für Aufgabe – genau so, wie der Professor sie erwartet. **Die gesonderten Exception-Aufgaben (try/except/else/finally) sind ausgelassen** (in deiner Klausur nicht direkt gefragt); an ihrer Stelle steht ein kurzer Hinweis.

> Theorie-Antworten sind hier kompakt gehalten – ausführlich in [`1_Theorie_Fragen_und_Antworten.md`](1_Theorie_Fragen_und_Antworten.md). Code-Lösungen sind vollständig.

**Inhalt:** [SS23](#ss23) · [WS2324](#ws2324) · [SS24](#ss24) · [WS2425](#ws2425) · [SS25](#ss25) · [WS2526](#ws2526)

Wiederkehrendes Muster jeder Klausur: **Theorie · Testen · Kommandozeile+Datei · Datenstruktur · Sortieren** (+ früher eine Exception-Aufgabe).

---

## SS23

### Aufgabe 1 – Theorie
- **Programmierung vs. Software-Engineering:** Programmieren = Code für kleine Aufgabe, oft eine Person. SE (Balzert) = systematische, arbeitsteilige, ingenieurmäßige Entwicklung **umfangreicher** Systeme; Phasenmodelle, ganzer Lebenszyklus inkl. Wartung (~80 %), QS.
- **Magisches Dreieck:** Zeit – Kosten – Qualität; eine Ecke ändern wirkt zwangsläufig auf die anderen (Zeit ↓ → Kosten ↑ oder Qualität ↓).
- **Funktional vs. nicht-funktional (MC):** *Funktional = WAS* das System tut, *nicht-funktional = WIE GUT*.

### Aufgabe 2 – Theorie: Phasenzyklus (4 fehlende Begriffe)
**Analyse** (→ Anforderungsdok.) → **Architektur/Grobentwurf** (→ Komponentenstruktur) → **Implementierung** (→ Code + Unit-Tests) → **Integration** (→ getestetes Gesamtsystem).

### Aufgabe 3 – Theorie: Wasserfall vs. V-Modell
- **Wasserfall:** rein sequenziell, Test erst am Ende → Fehler spät.
- **V-Modell:** jede Entwicklungsphase hat ein **Testpendant** (Anforderung↔Abnahmetest, Systemspez.↔Systemtest, Architektur↔Integrationstest, Detailentwurf↔Modultest).
- **Empfehlung:** einfaches Spiel/stabile Anforderungen → Wasserfall; sicherheitskritisch/komplex/änderungswahrscheinlich → V-Modell.

### Aufgabe 4 – Testen: BMI + positive Zahlen (Black-Box + pytest)
```python
def bmi_klassifizierung(gewicht, groesse):
    bmi = gewicht / (groesse**2)
    if bmi < 18.5:
        return "Untergewicht"
    elif bmi < 25:
        return "Normalgewicht"
    elif bmi < 30:
        return "Übergewicht"
    else:
        return "Adipositas"


def addiere_positive_zahlen(zahlenliste):
    summe = 0
    for zahl in zahlenliste:
        if zahl > 0:
            summe += zahl
    return summe
```
```python
# test/test_aufgabe04.py  (je Äquivalenzklasse ein Test, inkl. Grenzwert 18.5 bzw. 0)
from src import aufgabe04

def test_bmi_untergewicht():   assert aufgabe04.bmi_klassifizierung(50, 1.75) == "Untergewicht"
def test_bmi_normalgewicht():  assert aufgabe04.bmi_klassifizierung(70, 1.75) == "Normalgewicht"
def test_bmi_uebergewicht():   assert aufgabe04.bmi_klassifizierung(80, 1.70) == "Übergewicht"
def test_bmi_adipositas():     assert aufgabe04.bmi_klassifizierung(100, 1.70) == "Adipositas"
def test_bmi_grenzwert_18_5(): assert aufgabe04.bmi_klassifizierung(74, 2.0) == "Normalgewicht"  # 74/2² = 18.5

def test_addiere_leere_liste():  assert aufgabe04.addiere_positive_zahlen([]) == 0
def test_addiere_nur_positive(): assert aufgabe04.addiere_positive_zahlen([2, 4, 6]) == 12
def test_addiere_nur_negative(): assert aufgabe04.addiere_positive_zahlen([-1, -2, -3]) == 0
def test_addiere_gemischt():     assert aufgabe04.addiere_positive_zahlen([2, 4, 6, -8, 10]) == 22
def test_addiere_grenzwert_null(): assert aufgabe04.addiere_positive_zahlen([0, 5]) == 5   # 0 zählt nicht (>0)
```

### Aufgabe 5 – *(Exception-Aufgabe `string_operations` – ausgelassen)*

### Aufgabe 6 – Kommandozeile + Datei: Caesar-Chiffre (argparse)
```python
import argparse

def caesar_chiffrieren(input_string, verschiebung):
    chiffrierter_text = ""
    for char in input_string:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            chiffrierter_text += chr((ord(char) - ascii_offset + verschiebung) % 26 + ascii_offset)
        else:
            chiffrierter_text += char
    return chiffrierter_text

def caesar_dechiffrieren(input_string, verschiebung):
    return caesar_chiffrieren(input_string, -verschiebung)

def main():
    parser = argparse.ArgumentParser(description="Caesar-Ver-/Entschluesselung zeilenweise.")
    parser.add_argument("--infile", "-i", required=True)
    parser.add_argument("--outfile", "-o", required=True)
    parser.add_argument("--shift", "-s", type=int, required=True)
    parser.add_argument("--chiffrieren", "-c", action="store_true")
    parser.add_argument("--dechiffrieren", "-d", action="store_true")
    args = parser.parse_args()

    # genau eins von -c/-d muss gesetzt sein (ohne mutually_exclusive_group)
    if args.chiffrieren == args.dechiffrieren:
        parser.error("Bitte genau eine Option angeben: -c ODER -d.")

    with open(args.infile, "r", encoding="utf-8") as ein, \
         open(args.outfile, "w", encoding="utf-8") as aus:
        for zeile in ein:
            if args.chiffrieren:
                aus.write(caesar_chiffrieren(zeile, args.shift))
            else:
                aus.write(caesar_dechiffrieren(zeile, args.shift))

if __name__ == "__main__":
    main()
```

### Aufgabe 7 – Datenstruktur: Einfach verkettete Liste
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
```

### Aufgabe 8 – Sortieren: Quicksort (String)
```python
def quicksort(input_text):
    if len(input_text) <= 1:
        return input_text
    pivot = input_text[0]
    kleiner  = [z for z in input_text[1:] if z <= pivot]   # <= behält Duplikate
    groesser = [z for z in input_text[1:] if z > pivot]
    return quicksort("".join(kleiner)) + pivot + quicksort("".join(groesser))
```

### Aufgabe 9 – Theorie: Sprachen-Zuordnung
iOS → **Swift** · interaktive Website → **JavaScript** · Android → **Kotlin** · Webserver-Automatisierung → **Ruby** · massiv-parallel numerisch → **Julia** · Blog-CMS → **WordPress** · Echtzeit-Nachrichten → **Erlang** · Windows-Desktop → **Visual Basic** · Webanwendung Backend+DB → **Java** · Server-Backend hohe Netzleistung → **Golang**.

---

## WS2324

### Aufgabe 1 – Theorie
- **4 Gründe für SE:** Komplexität, Qualität, Wartung (~80 % Kosten), Planung/Organisation.
- **Qualitätsmerkmale** – Benutzer: Funktionserfüllung, Zuverlässigkeit, Benutzbarkeit; Entwickler: Wartbarkeit, Testbarkeit, Übertragbarkeit.
- **Lasten- vs. Pflichtenheft:** Lastenheft = WAS/WOZU (Auftraggeber); Pflichtenheft = WIE (Auftragnehmer).
- **Versteckte Anforderungen:** nicht explizit genannt, aus Kontext; durch Nachfragen erkennen.
- **4+1-Sichten:** Logisch, Entwicklung, Prozess, Physisch + Szenarien.

### Aufgabe 2 – Testen: Blutdruck + erste negative Zahl (Black-Box + pytest)
```python
def blutdruck_klassifizierung(systolisch, diastolisch):
    if systolisch < 120 and diastolisch < 80:
        return "Normal"
    elif 120 <= systolisch < 130 and diastolisch < 80:
        return "Erhöht"
    elif 130 <= systolisch < 140 or 80 <= diastolisch < 90:
        return "Bluthochdruck (Stufe 1)"
    elif systolisch >= 140 or diastolisch >= 90:
        return "Bluthochdruck (Stufe 2)"
    else:
        return "Hypertensiver Krisenzustand"

def finde_erste_negative_zahl(zahlenliste):
    index = 0
    while index < len(zahlenliste):
        if zahlenliste[index] < 0:
            return zahlenliste[index]
        index += 1
    return "Keine negative Zahl gefunden"
```
```python
from src import aufgabe02

def test_blutdruck_normal():        assert aufgabe02.blutdruck_klassifizierung(100, 70) == "Normal"
def test_blutdruck_erhoeht():       assert aufgabe02.blutdruck_klassifizierung(125, 70) == "Erhöht"
def test_blutdruck_stufe1():        assert aufgabe02.blutdruck_klassifizierung(135, 75) == "Bluthochdruck (Stufe 1)"
def test_blutdruck_stufe2():        assert aufgabe02.blutdruck_klassifizierung(145, 95) == "Bluthochdruck (Stufe 2)"
def test_blutdruck_grenzwert_120(): assert aufgabe02.blutdruck_klassifizierung(120, 70) == "Erhöht"

def test_negative_leere_liste(): assert aufgabe02.finde_erste_negative_zahl([]) == "Keine negative Zahl gefunden"
def test_negative_nur_positive(): assert aufgabe02.finde_erste_negative_zahl([1, 2, 3]) == "Keine negative Zahl gefunden"
def test_negative_am_anfang():   assert aufgabe02.finde_erste_negative_zahl([-5, 2, 3]) == -5
def test_negative_am_ende():     assert aufgabe02.finde_erste_negative_zahl([2, 4, -8]) == -8
def test_negative_mehrere():     assert aufgabe02.finde_erste_negative_zahl([3, -1, -2]) == -1
```
> Hinweis: Der `else`-Zweig „Hypertensiver Krisenzustand" ist mit diesen Bedingungen nicht erreichbar (toter Code) – im Testkommentar erwähnen.

### Aufgabe 3 – *(Exception-Aufgabe `get_ratio_at_position` – ausgelassen)*

### Aufgabe 4 – Kommandozeile + Datei: Atbash-Chiffre (argparse)
```python
import argparse

def atbash_chiffrieren(input_string):
    chiffrierter_text = ""
    for char in input_string:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            chiffrierter_text += chr(25 - (ord(char) - ascii_offset) + ascii_offset)
        else:
            chiffrierter_text += char
    return chiffrierter_text

def atbash_dechiffrieren(input_string):
    return atbash_chiffrieren(input_string)   # Atbash ist selbstinvers

def main():
    parser = argparse.ArgumentParser(description="Atbash zeilenweise.")
    parser.add_argument("--infile", "-i", required=True)
    parser.add_argument("--outfile", "-o", required=True)
    parser.add_argument("--chiffrieren", "-c", action="store_true")
    parser.add_argument("--dechiffrieren", "-d", action="store_true")
    args = parser.parse_args()

    # genau eins von -c/-d muss gesetzt sein (ohne mutually_exclusive_group)
    if args.chiffrieren == args.dechiffrieren:
        parser.error("Bitte genau eine Option angeben: -c ODER -d.")

    with open(args.infile, "r", encoding="utf-8") as ein, \
         open(args.outfile, "w", encoding="utf-8") as aus:
        for zeile in ein:
            if args.chiffrieren:
                aus.write(atbash_chiffrieren(zeile))
            else:
                aus.write(atbash_dechiffrieren(zeile))

if __name__ == "__main__":
    main()
```

### Aufgabe 5 – Datenstruktur: Stack (LIFO)
```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()          # oberstes = letztes

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)

    def get(self, i):
        if i < 0 or i >= len(self.stack):
            raise IndexError("Index liegt ausserhalb des Stacks")
        return self.stack[i]

    def delete(self, i):                 # 'del' ist reserviert -> 'delete'
        if i < 0 or i >= len(self.stack):
            raise IndexError("Index liegt ausserhalb des Stacks")
        del self.stack[i]
```

### Aufgabe 6 – Sortieren: Insertion-Sort (String)
```python
def insertionsort(input_text):
    zeichen = list(input_text)           # String -> Liste (unveränderlich)
    n = len(zeichen)
    for i in range(1, n):
        pivot = zeichen[i]
        j = i - 1
        while j >= 0 and zeichen[j] > pivot:
            zeichen[j + 1] = zeichen[j]
            j -= 1
        zeichen[j + 1] = pivot
    return "".join(zeichen)
```

### Aufgabe 7 – Theorie: Sprachen & Zweck
Kotlin → Android · Erlang → hochverfügbar/nebenläufig (Telko) · Swift → iOS/macOS · Selenium → automatisiertes Web-Testen · Ruby → Web/Skripte (Rails).

---

## SS24

### Aufgabe 1 – Theorie
- **4+1-Sichten (Stud.IP-Beispiel):** Logisch (Klassen Veranstaltung/Nutzer …), Prozess (gleichzeitige Zugriffe), Entwicklung (Module/Repos), Physisch (Web-/App-/DB-Server), Szenarien (Use Cases „Anmelden" …).
- **Magisches Dreieck:** Einfluss auf Planung + Balancierung (Scope/MVP, Prioritäten).

### Aufgabe 2 – Testen: `foo` (Schleife) + `vereinigung` (Rekursion) (White-Box + pytest)
```python
def foo(x, a):
    zaehler = 0
    while x >= a:
        zaehler += 1
        x = x - a
    return zaehler

def vereinigung(menge1, menge2):
    if len(menge1) == 0:
        return menge2
    elif menge1[0] in menge2:
        return vereinigung(menge1[1:], menge2)
    else:
        return [menge1[0]] + vereinigung(menge1[1:], menge2)
```
```python
from src import aufgabe02

# foo: Schleife 0x / 1x / mehrfach
def test_foo_null():     assert aufgabe02.foo(1, 2) == 0
def test_foo_eins():     assert aufgabe02.foo(3, 2) == 1
def test_foo_mehrfach(): assert aufgabe02.foo(10, 3) == 3

# vereinigung: Basisfall / elif-Treffer / else / gemischt
def test_ver_basis():    assert aufgabe02.vereinigung([], [1, 2]) == [1, 2]
def test_ver_enthalten(): assert aufgabe02.vereinigung([1], [1, 2]) == [1, 2]
def test_ver_neu():      assert aufgabe02.vereinigung([3], [1, 2]) == [3, 1, 2]
def test_ver_gemischt(): assert aufgabe02.vereinigung([1, 2, 3], [1, 2]) == [3, 1, 2]
```

### Aufgabe 3 – *(Exception-Aufgabe `calculate_difference_at_index` – ausgelassen)*

### Aufgabe 4 – Kommandozeile + Datei: Bilder verknüpfen (getopt)
```python
import sys
import getopt

def combine_images(image1, image2, function):
    combined_image = ""
    if function == "and":
        for i in range(len(image1)):
            if image1[i] == "*" and image2[i] == "*":
                combined_image += "*"
            elif image1[i] == "\n" and image2[i] == "\n":
                combined_image += "\n"
            else:
                combined_image += " "
    elif function == "or":
        for i in range(len(image1)):
            if image1[i] == "*" or image2[i] == "*":
                combined_image += "*"
            elif image1[i] == "\n" and image2[i] == "\n":
                combined_image += "\n"
            else:
                combined_image += " "
    return combined_image + "\n"

def main(argv):
    bild1 = bild2 = funktion = output = ""
    try:
        opts, args = getopt.getopt(argv, "h",
                                   ["bild1=", "bild2=", "funktion=", "output=", "help"])
    except getopt.GetoptError:
        print("--bild1 <n1> --bild2 <n2> --funktion <and|or> --output <n3>")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("--bild1 <n1> --bild2 <n2> --funktion <and|or> --output <n3>"); sys.exit()
        elif opt == "--bild1":    bild1 = arg
        elif opt == "--bild2":    bild2 = arg
        elif opt == "--funktion": funktion = arg
        elif opt == "--output":   output = arg

    with open(bild1, "r", encoding="utf-8") as f1:
        image1 = f1.read()
    with open(bild2, "r", encoding="utf-8") as f2:
        image2 = f2.read()
    ergebnis = combine_images(image1, image2, funktion)
    with open(output, "w", encoding="utf-8") as f_out:
        f_out.write(ergebnis)

if __name__ == "__main__":
    main(sys.argv[1:])
```

### Aufgabe 5 – Datenstruktur: Binärer Suchbaum
> Original-Klausur gab `key`/`self.val` vor; hier zur Einheitlichkeit auf `data`/`self.data` umgestellt (gleiche Struktur). In der echten Klausur die vorgegebenen Namen nehmen.
```python
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_rekursiv(self.root, data)

    def _insert_rekursiv(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_rekursiv(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_rekursiv(node.right, data)

    def print_tree(self):
        self._print_rekursiv(self.root)

    def _print_rekursiv(self, node):
        if node is not None:
            self._print_rekursiv(node.left)    # links
            print(node.data)                   # Knoten
            self._print_rekursiv(node.right)   # rechts  -> In-order = sortiert
```

### Aufgabe 6 – Sortieren: Mergesort nach Länge (merge vorgegeben)
```python
def mergesort(input_liste):
    if len(input_liste) <= 1:
        return input_liste
    mitte = len(input_liste) // 2
    links = mergesort(input_liste[:mitte])
    rechts = mergesort(input_liste[mitte:])
    return merge(links, rechts)

def merge(left, right):                  # 🟩 war vorgegeben
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if len(left[i]) < len(right[j]):
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

---

## WS2425

### Aufgabe 1 – Theorie
- **Stakeholder:** zentraler **Manager** koordiniert Kunde, Marketing, SW-Entwicklung, QS.
- **Magisches Dreieck:** alle drei Ecken gleichzeitig maximal = unmöglich → Scope/MVP, Brooks.
- **Funktional vs. nicht-funktional** (Hochfrequenzhandel): funktional = Echtzeit-Analyse/Handel; nicht-funktional = Latenz (ms), Verfügbarkeit, Skalierbarkeit.

### Aufgabe 2 – Testen: `minOfThree` + `ggt` (White-Box + pytest)
```python
def minOfThree(a, b, c):
    if a < b:
        kleiner = a
    else:
        kleiner = b
    if c < kleiner:
        kleiner = c
    return kleiner

def ggt(a, b):
    if b == 0:
        return a
    else:
        return ggt(b, a % b)
```
```python
from src import aufgabe02

# minOfThree: 2 if -> 4 Pfade
def test_min_p1(): assert aufgabe02.minOfThree(2, 3, 1) == 1
def test_min_p2(): assert aufgabe02.minOfThree(1, 3, 2) == 1
def test_min_p3(): assert aufgabe02.minOfThree(3, 2, 1) == 1
def test_min_p4(): assert aufgabe02.minOfThree(3, 1, 2) == 1

# ggt (rekursiv): Basisfall / 1x / mehrfach
def test_ggt_basis():    assert aufgabe02.ggt(5, 0) == 5
def test_ggt_eine():     assert aufgabe02.ggt(4, 2) == 2
def test_ggt_mehrfach(): assert aufgabe02.ggt(18, 27) == 9
```

### Aufgabe 3 – *(Exception-Aufgabe `fehlerhafte_berechnung` – ausgelassen)*

### Aufgabe 4 – Kommandozeile + Datei: Rechner (getopt)
```python
import sys
import getopt

def zahl_einlesen(text):
    try:
        return int(text)
    except ValueError:
        return float(text)

def berechne(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        if b == 0:
            raise ZeroDivisionError
        return a / b
    else:
        raise ValueError("Unbekannte Operation: " + str(operation))

def main(argv):
    a = b = None
    operation = ""
    dateiname = ""
    try:
        opts, args = getopt.getopt(argv, "a:b:o:f:h", ["help"])
    except getopt.GetoptError:
        print("-a <zahl> -b <zahl> -o <add|sub|mul|div> -f <datei>"); sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("-a <zahl> -b <zahl> -o <add|sub|mul|div> -f <datei>"); sys.exit()
        elif opt == "-a": a = zahl_einlesen(arg)
        elif opt == "-b": b = zahl_einlesen(arg)
        elif opt == "-o": operation = arg
        elif opt == "-f": dateiname = arg

    if a is None or b is None or operation == "" or dateiname == "":
        print("Fehler: Es fehlen Argumente. Erforderlich: -a, -b, -o, -f"); sys.exit(2)

    try:
        ergebnis = berechne(a, b, operation)
    except ZeroDivisionError:
        print("Fehler: Division durch Null ist nicht erlaubt."); sys.exit(1)
    except ValueError as fehler:
        print("Fehler:", fehler); sys.exit(1)

    with open(dateiname, "w", encoding="utf-8") as datei:
        datei.write("Ergebnis: " + str(ergebnis) + "\n")

if __name__ == "__main__":
    main(sys.argv[1:])
```

### Aufgabe 5 – Datenstruktur: Zirkuläre verkettete Liste
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key):
        neuer_knoten = Node(key)
        if self.head is None:
            self.head = neuer_knoten
            neuer_knoten.next = self.head        # zeigt auf sich selbst
        else:
            current = self.head
            while current.next != self.head:     # bis zum letzten Knoten
                current = current.next
            current.next = neuer_knoten
            neuer_knoten.next = self.head         # Kreis schließen

    def delete(self, key):
        if self.head is None:
            return
        if self.head.data == key:                # head-Fall
            if self.head.next == self.head:      # nur ein Element
                self.head = None
                return
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = self.head.next
            last.next = self.head
            return
        current = self.head                      # Mitte/Ende
        while current.next != self.head:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        if self.head is None:
            print("Liste ist leer")
            return
        current = self.head
        while True:
            print(current.data)
            current = current.next
            if current == self.head:
                break
```

### Aufgabe 6 – Sortieren: Quicksort für Dokumente (nach Inhaltslänge, dann Titel)
```python
def quicksort_documents(documents):
    if len(documents) <= 1:
        return documents

    def schluessel(dokument):
        titel, inhalt = dokument
        return (len(inhalt), titel)          # primär Länge, sekundär Titel

    pivot = documents[0]
    pivot_key = schluessel(pivot)
    kleiner = [d for d in documents[1:] if schluessel(d) < pivot_key]
    groesser_gleich = [d for d in documents[1:] if schluessel(d) >= pivot_key]
    return quicksort_documents(kleiner) + [pivot] + quicksort_documents(groesser_gleich)
```

---

## SS25

### Aufgabe 1 – Theorie
- **Softwaretechnik vs. Programmieren:** siehe SS23 A1 (Balzert; systematisch, Lebenszyklus, QS).
- **Scrum:** Rollen **Product Owner / Scrum Master / Entwicklungsteam**; Events Sprint Planning → Sprint (+ Daily) → Review → Retrospektive; Artefakte Product/Sprint Backlog, Inkrement.

### Aufgabe 2a – Testen: größte gerade Zahl (Black-Box + pytest)
```python
def finde_groesste_gerade_zahl(zahlenliste):
    groesste = None
    for zahl in zahlenliste:
        if zahl % 2 == 0:
            if groesste is None or zahl > groesste:
                groesste = zahl
    if groesste is None:
        return "Keine gerade Zahl gefunden"
    return groesste
```
```python
from src import aufgabe02a
def test_leer():     assert aufgabe02a.finde_groesste_gerade_zahl([]) == "Keine gerade Zahl gefunden"
def test_ungerade(): assert aufgabe02a.finde_groesste_gerade_zahl([1, 3, 5, 7]) == "Keine gerade Zahl gefunden"
def test_gemischt(): assert aufgabe02a.finde_groesste_gerade_zahl([3, 7, 8, 2, 10, 5]) == 10
def test_negativ():  assert aufgabe02a.finde_groesste_gerade_zahl([-4, -2, -10, 3]) == -2
def test_mehrfach(): assert aufgabe02a.finde_groesste_gerade_zahl([4, 8, 8, 2]) == 8
```

### Aufgabe 2b – Testen: Schnittmenge (White-Box, rekursiv + pytest)
```python
def schnittmenge(menge1, menge2):
    if not menge1:
        return []
    elif menge1[0] in menge2:
        return [menge1[0]] + schnittmenge(menge1[1:], menge2)
    else:
        return schnittmenge(menge1[1:], menge2)
```
```python
from src import aufgabe02b
def test_p1_basis():    assert aufgabe02b.schnittmenge([], [1, 2, 3]) == []
def test_p2_treffer():  assert aufgabe02b.schnittmenge([1, 2], [1, 2]) == [1, 2]
def test_p3_kein():     assert aufgabe02b.schnittmenge([1, 2, 3], [4, 5]) == []
def test_p4_gemischt(): assert aufgabe02b.schnittmenge([1, 2, 3], [2, 4]) == [2]
def test_p5_leer2():    assert aufgabe02b.schnittmenge([1, 2, 3], []) == []
```

### Aufgabe 3 – Kommandozeile + Datei: Log-Analyse (getopt)
```python
import sys
import getopt

def zaehle(dateiname, befehl):
    anzahl = 0
    with open(dateiname, "r", encoding="utf-8") as datei:
        for zeile in datei:
            if zeile.strip() == "":
                continue
            if befehl == "count":
                anzahl += 1
            elif befehl == "errors":
                if "ERROR" in zeile:
                    anzahl += 1
            elif befehl == "warnings":
                if "WARNING" in zeile:
                    anzahl += 1
    return anzahl

def schreibe_ergebnis(dateiname, befehl, ergebnis):
    with open(dateiname, "w", encoding="utf-8") as datei:
        datei.write(f"Befehl: {befehl}\n")
        datei.write(f"Ergebnis: {ergebnis}\n")

def main(argv):
    eingabe = ausgabe = befehl = None
    try:
        opts, args = getopt.getopt(argv, "i:o:b:h", ["input=", "output=", "befehl=", "help"])
    except getopt.GetoptError as fehler:
        print("Fehler:", fehler); sys.exit(2)
    for opt, wert in opts:
        if opt in ("-h", "--help"):
            print("-i <log> -o <out> -b <count|errors|warnings>"); sys.exit()
        elif opt in ("-i", "--input"):  eingabe = wert
        elif opt in ("-o", "--output"): ausgabe = wert
        elif opt in ("-b", "--befehl"): befehl = wert
    if eingabe is None or befehl is None:
        print("Fehler: -i und -b sind Pflicht."); sys.exit(2)
    if befehl not in ("count", "errors", "warnings"):
        print("Fehler: -b muss count, errors oder warnings sein."); sys.exit(2)
    ergebnis = zaehle(eingabe, befehl)
    if ausgabe:
        schreibe_ergebnis(ausgabe, befehl, ergebnis)
    else:
        print(f"Befehl: {befehl}"); print(f"Ergebnis: {ergebnis}")

if __name__ == "__main__":
    main(sys.argv[1:])
```
> Original mit argparse gelöst; hier die getopt-Variante (Klausur-erlaubt). Log-Format: `... [LEVEL] Nachricht`, gezählt per Substring `"ERROR"`/`"WARNING"`.

### Aufgabe 4 – Datenstruktur: Ternärer Suchbaum (nach Wortlänge)
```python
class Node:
    def __init__(self, wort):
        self.wort = wort
        self.links = None
        self.mitte = None
        self.rechts = None

class TernaererSuchbaum:
    def __init__(self):
        self.wurzel = None

    def einfuegen(self, wort):
        if self.wurzel is None:
            self.wurzel = Node(wort)
        else:
            self._einfuegen_rekursiv(self.wurzel, wort)

    def _einfuegen_rekursiv(self, knoten, wort):
        if len(wort) < len(knoten.wort):
            if knoten.links is None:
                knoten.links = Node(wort)
            else:
                self._einfuegen_rekursiv(knoten.links, wort)
        elif len(wort) == len(knoten.wort):
            if knoten.mitte is None:
                knoten.mitte = Node(wort)
            else:
                self._einfuegen_rekursiv(knoten.mitte, wort)
        else:
            if knoten.rechts is None:
                knoten.rechts = Node(wort)
            else:
                self._einfuegen_rekursiv(knoten.rechts, wort)

    def inorder_ausgabe(self):
        self._gesammelt = []
        self._inorder(self.wurzel)
        print(", ".join(self._gesammelt))

    def _inorder(self, knoten):
        if knoten is not None:
            self._inorder(knoten.links)
            self._inorder(knoten.mitte)
            self._gesammelt.append(knoten.wort)
            self._inorder(knoten.rechts)
```

### Aufgabe 5 – Sortieren: Heapsort nach Länge (heapify vorgegeben)
```python
def heapsort(input_liste):
    liste = list(input_liste)
    n = len(liste)
    for i in range(n // 2 - 1, -1, -1):      # Max-Heap aufbauen
        heapify(liste, n, i)
    for i in range(n - 1, 0, -1):            # größtes ans Ende
        liste[0], liste[i] = liste[i], liste[0]
        heapify(liste, i, 0)
    return liste

def heapify(liste, n, i):                    # 🟩 war vorgegeben
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
```

---

## WS2526

### Aufgabe 1 – Theorie
- **4+1-Sichten zuordnen:** Klassen→Logisch, Akteure/Use Cases→Szenarien, Performanz/Skalierbarkeit→Prozess, Hardware-Topologie→Physisch, Dateien/Repos→Entwicklung.
- **Betrieb & Wartung:** ~80 % der Kosten; 4 Wartungsarten: korrektiv, adaptiv, perfektiv, präventiv.

### Aufgabe 2 – Testen: Buggy Code analysieren + Assertions + pytest
**c) Die 3 eingebauten Fehler** in `normalize_and_pack`:
1. `if limit < 0` → muss `<= 0` sein (Spec: Exception bei `limit <= 0`).
2. `sum(packs[-1]) + x < limit` → muss `<=` sein (Summe == limit passt noch rein).
3. Startwert `packs = [[]]` erzeugt bei sofortigem neuen Paket ein leeres erstes Paket.

**e) Funktion mit ergänzten Assertions:**
```python
def normalize_and_pack(values, limit):
    assert type(values) == list                              # 🟩 vorgegeben
    assert isinstance(limit, int), "limit muss eine ganze Zahl sein"          # 🟨
    assert all(isinstance(v, (int, float)) for v in values), \
        "alle Elemente von values muessen int oder float sein"                # 🟨
    if limit < 0:                                            # (Korrektur: <= 0)
        raise ValueError("limit must be positive")
    cleaned = []
    for v in values:
        if v >= 0:
            cleaned.append(round(v))
    packs = [[]]
    for x in cleaned:
        if sum(packs[-1]) + x < limit:                       # (Korrektur: <=)
            packs[-1].append(x)
        else:
            packs.append([x])
    if packs == [[]]:
        return []
    return packs
```
```python
import pytest
from src import aufgabe02a

def test_verwirft_negative(): assert aufgabe02a.normalize_and_pack([-3, -1], 10) == []
def test_leere_liste():       assert aufgabe02a.normalize_and_pack([], 10) == []
def test_einfaches_paket():   assert aufgabe02a.normalize_and_pack([1, 2, 3], 10) == [[1, 2, 3]]
def test_rundet():            assert aufgabe02a.normalize_and_pack([2.5, 3.5], 100) == [[2, 4]]
def test_mehrere_pakete():    assert aufgabe02a.normalize_and_pack([3, 4], 5) == [[3], [4]]
def test_negatives_limit():
    with pytest.raises(ValueError):
        aufgabe02a.normalize_and_pack([1, 2], -1)

@pytest.mark.xfail(reason="Bug 2c: '<' statt '<=', Summe==limit wird aufgeteilt")
def test_summe_gleich_limit():
    assert aufgabe02a.normalize_and_pack([5], 5) == [[5]]

@pytest.mark.xfail(reason="Bug 2c: prüft nur limit<0 statt limit<=0")
def test_limit_null():
    with pytest.raises(ValueError):
        aufgabe02a.normalize_and_pack([1, 2], 0)

def test_falscher_typ_values():
    with pytest.raises(AssertionError):
        aufgabe02a.normalize_and_pack(["text"], 10)
def test_falscher_typ_limit():
    with pytest.raises(AssertionError):
        aufgabe02a.normalize_and_pack([1, 2], 10.5)
```

### Aufgabe 3 – Kommandozeile + Datei: Log-Analyse (getopt)
```python
import sys
import getopt
from collections import Counter

def parse_zeile(zeile):
    teile = zeile.strip().split(";")
    if len(teile) != 4:
        return None
    zeit, level, user, action = teile
    return {"zeit": zeit, "level": level, "user": user, "action": action}

def werte_logdatei_aus(pfad, befehl):
    zaehler = Counter()
    with open(pfad, "r", encoding="utf-8") as f:
        for zeile in f:
            eintrag = parse_zeile(zeile)
            if eintrag is None:
                continue
            zaehler[eintrag[befehl]] += 1     # befehl = "action"|"user"|"level"
    return zaehler

def schreibe_ergebnis(zaehler, ausgabe):
    zeilen = [f"{k}:{v}" for k, v in zaehler.items()]
    text = "\n".join(zeilen)
    if ausgabe:
        with open(ausgabe, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    else:
        print(text)

def main(argv):
    eingabe = ausgabe = befehl = None
    try:
        opts, args = getopt.getopt(argv, "i:o:b:h", ["input=", "output=", "befehl=", "help"])
    except getopt.GetoptError as e:
        print("Fehler:", e); sys.exit(1)
    for opt, wert in opts:
        if opt in ("-h", "--help"):
            print("-i <log> -b <actions|user|level> [-o <out>]"); sys.exit(0)
        elif opt in ("-i", "--input"):  eingabe = wert
        elif opt in ("-o", "--output"): ausgabe = wert
        elif opt in ("-b", "--befehl"): befehl = wert
    if eingabe is None or befehl is None:
        print("Fehler: -i und -b sind Pflicht."); sys.exit(1)
    umbenennung = {"actions": "action", "user": "user", "level": "level"}
    if befehl not in umbenennung:
        print("Fehler: -b muss actions, user oder level sein."); sys.exit(1)
    zaehler = werte_logdatei_aus(eingabe, umbenennung[befehl])
    schreibe_ergebnis(zaehler, ausgabe)

if __name__ == "__main__":
    main(sys.argv[1:])
```
> Log-Format hier: `zeit;LEVEL;USER;ACTION` (per `;` gesplittet). Original argparse → hier getopt.

### Aufgabe 4 – Datenstruktur: Trie / Präfixbaum
```python
class Node:
    def __init__(self):
        self.kinder = {}
        self.ist_wortende = False

class Trie:
    def __init__(self):
        self.wurzel = Node()

    def einfuegen(self, wort):
        aktueller = self.wurzel
        for ch in wort:
            if ch not in aktueller.kinder:
                aktueller.kinder[ch] = Node()
            aktueller = aktueller.kinder[ch]
        aktueller.ist_wortende = True

    def enthaelt(self, wort):
        aktueller = self.wurzel
        for ch in wort:
            if ch not in aktueller.kinder:
                return False
            aktueller = aktueller.kinder[ch]
        return aktueller.ist_wortende

    def woerter_mit_praefix(self, praefix):
        aktueller = self.wurzel
        for ch in praefix:
            if ch not in aktueller.kinder:
                return []
            aktueller = aktueller.kinder[ch]
        ergebnis = []
        self._sammle_woerter(aktueller, praefix, ergebnis)
        return ergebnis

    def _sammle_woerter(self, knoten, gebaut, ergebnis):
        if knoten.ist_wortende:
            ergebnis.append(gebaut)
        for ch in sorted(knoten.kinder.keys()):
            self._sammle_woerter(knoten.kinder[ch], gebaut + ch, ergebnis)
```

### Aufgabe 5 – Sortieren: Mergesort (Länge, dann alphabetisch; merge vorgegeben)
```python
def mergesort(input_liste):
    if len(input_liste) <= 1:
        return input_liste
    mitte = len(input_liste) // 2
    links = mergesort(input_liste[:mitte])
    rechts = mergesort(input_liste[mitte:])
    return merge(links, rechts)

def merge(left, right):                  # 🟩 war vorgegeben
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if (len(left[i]), left[i]) <= (len(right[j]), right[j]):   # Länge, dann Alphabet
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

---

## 🗺️ Quer-Übersicht: was war wo?

| Klausur | Testen | Kommandozeile | Datenstruktur | Sortieren |
|---|---|---|---|---|
| **SS23** | BMI + pos. Zahlen | Caesar (argparse) | LinkedList | Quicksort (String) |
| **WS2324** | Blutdruck + neg. Zahl | Atbash (argparse) | **Stack** | **Insertion-Sort** |
| **SS24** | foo + vereinigung (White-Box) | combine_images (getopt) | BST | Mergesort |
| **WS2425** | minOfThree + ggt (White-Box) | Rechner (getopt) | **Zirkuläre Liste** | Quicksort (Dokumente) |
| **SS25** | größte gerade + schnittmenge | Log (getopt) | **Ternärer Suchbaum** | **Heapsort** |
| **WS2526** | Buggy-Code + Assertions | Log (getopt) | **Trie** | Mergesort (Länge+Alpha) |

**Nie drangekommen** (→ heiße Kandidaten): **Queue**, **Bubble-Sort**, **Selection-Sort** – siehe [`5_Lueckenanalyse.md`](5_Lueckenanalyse.md) und [`6_Fokusthemen_Bubble_Selection_Queue.md`](6_Fokusthemen_Bubble_Selection_Queue.md).
