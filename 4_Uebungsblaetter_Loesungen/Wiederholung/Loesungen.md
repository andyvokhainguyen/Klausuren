# Lösungen – Übungsaufgaben zur Wiederholung Prog SS26

Musterlösungen zu allen 9 Aufgaben aus `Übungsaufgaben_Wiederholung_Prog_26.pdf`.

---

## Aufgabe 1 – Qualitätsmerkmale

**a) Drei Merkmale aus Benutzersicht (+ warum relevant):**
- **Funktionserfüllung** – der geplante Funktionsumfang ist realisiert; der Benutzer kann alle erwarteten Aufgaben erledigen.
- **Zuverlässigkeit** – das System bleibt bei Fehlern/Ausfällen stabil (z.B. kein Datenverlust); der Benutzer kann sich darauf verlassen.
- **Benutzbarkeit** – intuitiv bedienbar, geringe Einarbeitungszeit; der Benutzer arbeitet effizient ohne Frust.
  *(weitere möglich: Effizienz, Sicherheit)*

**b) Drei Merkmale aus Entwicklersicht (+ warum relevant):**
- **Wartbarkeit** – übersichtlicher, gut dokumentierter Code; Fehlerbehebung/Pflege ist einfach (Betrieb ≈ 80 % der Kosten).
- **Testbarkeit** – isoliert testbare Module ermöglichen hohe Testabdeckung und frühe Fehlererkennung.
- **Übertragbarkeit/Portabilität** – Code lässt sich auf andere Plattformen übertragen.
  *(weitere möglich: Änderbarkeit, Wiederverwendbarkeit)*

**c) Merkmal für Benutzer UND Entwickler:**
- **Effizienz** (Performanz): Für den Benutzer = kurze Antwortzeiten; für den Entwickler = ressourcenschonende, gut optimierbare Umsetzung. *(auch vertretbar: Sicherheit oder Zuverlässigkeit.)*

---

## Aufgabe 2 – Vier fehlende Begriffe im Phasenzyklus

Gegeben: Analyse, Architektur, Design, Implementierung, Integration, Abnahme.
**Fehlende vier Begriffe (in Zyklus-Reihenfolge):**

| Position im Bild | fehlender Begriff | Aufgabe der Phase | Ergebnis |
|---|---|---|---|
| zwischen Analyse und Architektur | **Definition** (Spezifikation) | Festlegen, *was* das System tun soll; Anforderungen + Abnahmekriterien | Spezifikation / Pflichtenheft |
| zwischen Implementierung und Integration | **Modultest** | einzelne Module isoliert testen | getestete Einzelmodule |
| zwischen Integration und Abnahme | **Systemtest** | Gesamtsystem gegen die Spezifikation prüfen | getestetes Gesamtsystem |
| oben (zwischen Abnahme und Analyse) | **Einführung/Betrieb** (Wartung) | produktive Nutzung, Wartung (korrektiv/adaptiv/perfektiv/präventiv) | laufendes System + Wartungsdoku |

Vollständiger Zyklus: *Einführung/Betrieb → Analyse → Definition → Architektur → Design → Implementierung → Modultest → Integration → Systemtest → Abnahme → (Einführung/Betrieb)*.

Kurz zu den vorgegebenen Phasen: **Analyse** (verstehen, was der Kunde will → Anforderungsdok.), **Architektur** (Grobentwurf, Komponenten/Schnittstellen), **Design** (Feinentwurf, Klassen im Detail), **Implementierung** (Code + Unit-Tests), **Integration** (Module zusammenfügen), **Abnahme** (Abnahmeprotokoll).

---

## Aufgabe 3 – Lastenheft vs. Pflichtenheft (ankreuzen)

| Aussage | Lastenheft | Pflichtenheft |
|---|:---:|:---:|
| Beschreibung der allgemeinen Zielsetzung des Projekts | ✅ | |
| Detaillierte technische Spezifikationen für die Softwarelösung | | ✅ |
| Fristen für die Fertigstellung der verschiedenen Projektphasen | | ✅ |
| Liste von Funktionen, die der Kunde von der Software erwartet | ✅ | |
| Informationen zur Softwarearchitektur und den zu verwendenden Technologien | | ✅ |

Merksatz: **Lastenheft = WAS/WOZU** (vom *Auftraggeber*, Ziele + Kundenanforderungen). **Pflichtenheft = WIE** (vom *Auftragnehmer*, technische Umsetzung, Architektur, konkreter Zeit-/Phasenplan).
*(Die „Fristen der Projektphasen" sind der einzige Grenzfall: der detaillierte Phasenplan gehört zur Umsetzungsplanung des Auftragnehmers → Pflichtenheft.)*

---

## Aufgabe 4a – berechne_ticketpreis (Black-Box)

```python
def berechne_ticketpreis(alter):
    if alter < 0:
        return "Ungültiges Alter"
    elif alter <= 12:
        return 5.0
    elif alter <= 65:
        return 10.0
    else:
        return 7.5
```

**1) Äquivalenzklassen** (je Kategorie eine Klasse + Grenzwert):
| Klasse | Bereich | repräsentativ | erwartet |
|---|---|---|---|
| K1 ungültig | alter < 0 | -5 | "Ungültiges Alter" |
| K2 Kind | 0 ≤ alter ≤ 12 | 8 | 5.0 |
| K3 Erwachsen | 13 ≤ alter ≤ 65 | 30 | 10.0 |
| K4 Senior | alter > 65 | 70 | 7.5 |
| K5 Grenzwert | alter == 12 | 12 | 5.0 |

Begründung: Jede if/elif/else-Kategorie wird durch genau eine Klasse abgedeckt (überschneidungsfrei); K5 prüft zusätzlich die kritische Grenze 12 (gehört laut Code noch zu 5.0). Sinnvolle weitere Grenzwerte: 0, 65, 66.

**2) pytest:**
```python
from src import aufgabe04   # Pfad ggf. anpassen

def test_ticket_ungueltig():
    assert aufgabe04.berechne_ticketpreis(-5) == "Ungültiges Alter"

def test_ticket_kind():
    assert aufgabe04.berechne_ticketpreis(8) == 5.0

def test_ticket_erwachsen():
    assert aufgabe04.berechne_ticketpreis(30) == 10.0

def test_ticket_senior():
    assert aufgabe04.berechne_ticketpreis(70) == 7.5

def test_ticket_grenzwert_12():
    assert aufgabe04.berechne_ticketpreis(12) == 5.0
```

---

## Aufgabe 4b – fakultaet (White-Box)

```python
def fakultaet(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * fakultaet(n - 1)
```

**1) White-Box-Pfade** (Empfehlung Rekursion: Basisfall / einmal / mehrfach + alle Zweige):
| Pfad | Fall | Beispiel | erwartet |
|---|---|---|---|
| P1 | n < 0 (ungültig) | fakultaet(-1) | None |
| P2 | Basisfall n == 0 | fakultaet(0) | 1 |
| P3 | genau 1× rekursiv | fakultaet(1) → 1·fakultaet(0) | 1 |
| P4 | mehrfach rekursiv | fakultaet(5) | 120 |

**2) pytest:**
```python
from src import aufgabe04

def test_fakultaet_negativ():
    assert aufgabe04.fakultaet(-1) is None

def test_fakultaet_basisfall():
    assert aufgabe04.fakultaet(0) == 1

def test_fakultaet_eine_rekursion():
    assert aufgabe04.fakultaet(1) == 1

def test_fakultaet_mehrfach():
    assert aufgabe04.fakultaet(5) == 120
```

---

## Aufgabe 5 – getopt-Taschenrechner

```python
import sys
import getopt


def hilfe():
    print("Verwendung:")
    print("  python myscript.py --add -x <zahl> -y <zahl>       # Summe")
    print("  python myscript.py --multiply -x <zahl> -y <zahl>  # Produkt")
    print("  python myscript.py -h                              # diese Hilfe")


def main(argv):
    operation = ""
    x = None
    y = None

    try:
        # kurze Flags: h,a,m ohne Argument; x:,y: mit Argument
        opts, args = getopt.getopt(
            argv, "hamx:y:",
            ["help", "add", "multiply", "zahlx=", "zahly="]
        )
    except getopt.GetoptError:
        print("Fehler: ungültige Option oder ungültiges Argument.")
        hilfe()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            hilfe()
            sys.exit()
        elif opt in ("-a", "--add"):
            operation = "add"
        elif opt in ("-m", "--multiply"):
            operation = "multiply"
        elif opt in ("-x", "--zahlx"):
            x = int(arg)
        elif opt in ("-y", "--zahly"):
            y = int(arg)

    # Fehlerbehandlung: fehlende Angaben
    if operation == "" or x is None or y is None:
        print("Fehler: Operation (--add/--multiply) sowie -x und -y erforderlich.")
        hilfe()
        sys.exit(2)

    if operation == "add":
        print(x + y)
    elif operation == "multiply":
        print(x * y)


if __name__ == "__main__":
    main(sys.argv[1:])
```
Test: `python myscript.py --add -x 5 -y 10` → `15` · `python myscript.py -m --zahlx 3 --zahly 7` → `21` · `python myscript.py -h` → Hilfe.

---

## Aufgabe 6 – Wörter zählen + in Datei schreiben

```python
def analysiere_datei(eingabe="textdata.txt", ausgabe="ergebnisse.txt"):
    with open(eingabe, "r", encoding="utf-8") as f:
        text = f.read()

    # 1) Satzzeichen entfernen, dann in Wörter zerlegen
    for zeichen in [".", ",", "!", "?", ";", ":"]:
        text = text.replace(zeichen, "")
    woerter = text.split()

    # 2) Wörter zählen (Häufigkeitswörterbuch)
    anzahl = len(woerter)
    haeufigkeit = {}
    for wort in woerter:
        if wort in haeufigkeit:
            haeufigkeit[wort] += 1
        else:
            haeufigkeit[wort] = 1

    # 3) häufigstes Wort (max nach Dictionary-Wert)
    haeufigstes = max(haeufigkeit, key=haeufigkeit.get)
    max_anzahl = haeufigkeit[haeufigstes]

    print("Anzahl der Wörter:", anzahl)
    print("Häufigkeit der Wörter:", haeufigkeit)
    print(f"Am häufigsten vorkommendes Wort: '{haeufigstes}' ({max_anzahl} Mal)")

    # 4) Ergebnis in Datei schreiben
    with open(ausgabe, "w", encoding="utf-8") as f:
        f.write(f"Anzahl der Wörter: {anzahl}\n")
        f.write(f"Häufigkeit der Wörter: {haeufigkeit}\n")
        f.write(f"Am häufigsten vorkommendes Wort: '{haeufigstes}' ({max_anzahl} Mal)\n")


analysiere_datei()
```
Für `Das ist ein Test. Dieser Test ist nur ein Beispiel.`:
```
Anzahl der Wörter: 10
Häufigkeit der Wörter: {'Das': 1, 'ist': 2, 'ein': 2, 'Test': 2, 'Dieser': 1, 'nur': 1, 'Beispiel': 1}
Am häufigsten vorkommendes Wort: 'ist' (2 Mal)
```
*(`max(..., key=haeufigkeit.get)` liefert bei Gleichstand das zuerst eingefügte Wort → 'ist'.)*

---

## Aufgabe 7 – Aufgabenverwaltung als doppelt verkettete Liste (mit Insertion Sort)

```python
class Aufgabe:
    def __init__(self, beschreibung, prioritaet):
        self.beschreibung = beschreibung
        self.prioritaet = prioritaet


class Node:
    def __init__(self, aufgabe):
        self.aufgabe = aufgabe
        self.next = None
        self.prev = None          # doppelt verkettet


class Aufgabenverwaltung:
    def __init__(self):
        self.head = None

    # Aufgabe mit Beschreibung + Priorität am Ende hinzufügen
    def hinzufuegen(self, beschreibung, prioritaet):
        neuer = Node(Aufgabe(beschreibung, prioritaet))
        if self.head is None:
            self.head = neuer
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = neuer
        neuer.prev = current

    # neue Aufgabe direkt NACH der Aufgabe mit gegebener Beschreibung einfügen
    def einfuegen_nach(self, ziel_beschreibung, beschreibung, prioritaet):
        current = self.head
        while current:
            if current.aufgabe.beschreibung == ziel_beschreibung:
                neuer = Node(Aufgabe(beschreibung, prioritaet))
                neuer.prev = current
                neuer.next = current.next
                if current.next:                 # nicht am Ende
                    current.next.prev = neuer
                current.next = neuer
                return
            current = current.next
        raise ValueError("Zielaufgabe nicht gefunden")

    # Liste aller Aufgaben zurückgeben
    def liste(self):
        ergebnis = []
        current = self.head
        while current:
            ergebnis.append((current.aufgabe.beschreibung, current.aufgabe.prioritaet))
            current = current.next
        return ergebnis

    # Sortierung nach Priorität mit Insertion Sort
    # (die Datenwerte der Knoten werden umsortiert, die Knotenstruktur bleibt)
    def sortiere(self):
        if self.head is None:
            return
        current = self.head.next               # ab dem zweiten Knoten
        while current is not None:
            schluessel = current.aufgabe        # zu platzierende Aufgabe
            lauf = current.prev
            # Knoten mit größerer Priorität nach rechts schieben
            while lauf is not None and lauf.aufgabe.prioritaet > schluessel.prioritaet:
                lauf.next.aufgabe = lauf.aufgabe
                lauf = lauf.prev
            if lauf is None:
                self.head.aufgabe = schluessel
            else:
                lauf.next.aufgabe = schluessel
            current = current.next


# Anwendungsbeispiel
av = Aufgabenverwaltung()
av.hinzufuegen("Einkaufen", 3)
av.hinzufuegen("Lernen", 1)
av.hinzufuegen("Sport", 2)
av.einfuegen_nach("Lernen", "Kochen", 5)   # Kochen nach Lernen einfügen
print(av.liste())      # [('Einkaufen', 3), ('Lernen', 1), ('Kochen', 5), ('Sport', 2)]
av.sortiere()
print(av.liste())      # nach Priorität: [('Lernen',1),('Sport',2),('Einkaufen',3),('Kochen',5)]
```
*(Alternative für die Sortierung: Werte in eine Python-Liste auslesen, `insertion_sort` darauf anwenden, neu aufbauen – funktional gleichwertig, aber weniger „echte" Listen-Operation.)*

---

## Aufgabe 8 – Binärer Suchbaum vervollständigen

```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rekursiv(self.root, key)

    # a) rekursives Einfügen (BST-Regel: kleiner links, größer/gleich rechts)
    def _insert_rekursiv(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_rekursiv(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_rekursiv(node.right, key)

    # b) In-order-Ausgabe (links → Knoten → rechts) = aufsteigend sortiert
    def print_tree(self):
        self._print_rekursiv(self.root)

    def _print_rekursiv(self, node):
        if node is not None:
            self._print_rekursiv(node.left)
            print(node.val)
            self._print_rekursiv(node.right)


bst = BinarySearchTree()
for elem in [20, 10, 30, 5, 15, 25, 35]:
    bst.insert(elem)
bst.print_tree()      # 5 10 15 20 25 30 35
```

---

## Aufgabe 9 – Mitarbeiter nach Gehalt sortieren (Mergesort)

```python
def mergesort(mitarbeiter):
    if len(mitarbeiter) <= 1:
        return mitarbeiter

    mitte = len(mitarbeiter) // 2
    links = mergesort(mitarbeiter[:mitte])
    rechts = mergesort(mitarbeiter[mitte:])
    return merge(links, rechts)


def merge(links, rechts):
    ergebnis = []
    i = 0
    j = 0
    while i < len(links) and j < len(rechts):
        # Vergleich über den Schlüssel 'gehalt'
        if links[i]["gehalt"] <= rechts[j]["gehalt"]:
            ergebnis.append(links[i])
            i += 1
        else:
            ergebnis.append(rechts[j])
            j += 1
    ergebnis.extend(links[i:])
    ergebnis.extend(rechts[j:])
    return ergebnis


mitarbeitergehaelter = [
    {"name": "Klaus", "gehalt": 270000},
    {"name": "Peter", "gehalt": 150000},
    {"name": "Markus", "gehalt": 350000},
    {"name": "Patrick", "gehalt": 500000},
    {"name": "Johannes", "gehalt": 100000},
]
print(mergesort(mitarbeitergehaelter))
# [Johannes 100000, Peter 150000, Klaus 270000, Markus 350000, Patrick 500000]
```

> Muster für **alle** Sortier-Aufgaben des Profs: Standardalgorithmus nehmen und nur die **Vergleichszeile** an den Schlüssel anpassen – hier `["gehalt"]`, bei Strings `len(...)`, bei Tupeln `(len(s), s)`.
