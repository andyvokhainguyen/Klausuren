# Lösungsschlüssel – Übungsklausur 2 (SS26)

Gesamt: **90 Punkte**. Lösungen zu [Uebungsklausur_2.md](Uebungsklausur_2.md).

---

## Aufgabe 1 – Software Engineering (15 P)

**a) Softwarekrise & CHAOS-Report (4 P):**
- **Softwarekrise:** Seit den 1960ern viele Softwareprojekte **zu teuer, zu spät und mit mangelhafter Qualität** – die Nachfrage nach Software wuchs schneller, als man sie beherrschbar entwickeln konnte.
- Der Begriff **„Software Engineering" wurde 1968 auf der NATO-Konferenz in Garmisch-Partenkirchen** geprägt.
- **CHAOS-Report (Standish Group):** erfolgreich **ca. 30–35 %**, herausgefordert (Abweichungen) **ca. 45–50 %**, gescheitert (abgebrochen) **ca. 15–20 %**.

**b) Einführungsstrategien / Rollout (4 P):**
| Strategie | Beschreibung | Risiko |
|---|---|---|
| **Big Bang** | komplette Umstellung zum Stichtag | hoch (kein Fallback) |
| **Stufenweise** | schrittweise, z.B. Region für Region | mittel (komplexere Koordination) |
| **Parallelbetrieb** | altes + neues System gleichzeitig | niedrig (doppelte Betriebskosten) |
| **Pilotbetrieb** | ausgewählte Anwender zuerst | niedrig (begrenzte Aussagekraft) |

**c) Lasten- vs. Pflichtenheft (4 P):**
| Aussage | Lastenheft | Pflichtenheft |
|---|:---:|:---:|
| Grobe Zielbestimmung und Anforderungen des Auftraggebers | ✅ | |
| Konkrete Use Cases und GUI-Skizzen | | ✅ |
| Glossar zur einheitlichen Begriffsdefinition | | ✅ |
| Abnahmekriterien des Kunden | ✅ | |

Merksatz: **Lastenheft = WAS/WOZU (Auftraggeber)**, **Pflichtenheft = WIE (Auftragnehmer)**.

**d) 4+1-Sichten nach Kruchten (3 P):**
- **Logische Sicht** – Klassen/Objekte, Funktionalität
- **Entwicklungs-/Implementierungs-Sicht** – Dateien, Repositories
- **Prozess-Sicht** – Prozesse/Threads, Performanz, Skalierbarkeit
- **Physische Sicht** – Hardwaretopologie, Verteilung
- **Szenario-/Anwendungssicht („+1")** – Akteure, Anwendungsfälle (verbindet die 4 Sichten)

---

## Aufgabe 2 – Testen (20 P)

**a) Black-Box `rabatt` (10 P)**

| Klasse | Bereich | Wert | Erwartung |
|---|---|---|---|
| K1 ungültig | bw < 0 | -10 | "Ungültiger Wert" |
| K2 kein Rabatt | 0 ≤ bw < 50 | 20 | 0 |
| K3 mittel | 50 ≤ bw < 100 | 75 | 5 |
| K4 hoch | bw ≥ 100 | 150 | 10 |
| K5 Grenzwert | bw == 50 | 50 | 5 |

Begründung: Jede if/elif/else-Kategorie wird durch genau eine Klasse abgedeckt; K5 prüft die Grenze 50 (gehört laut Code zu 5 %). Weitere sinnvolle Grenzwerte: 0 und 100.

```python
from src import aufgabe02

def test_rabatt_ungueltig():
    assert aufgabe02.rabatt(-10) == "Ungültiger Wert"

def test_rabatt_kein():
    assert aufgabe02.rabatt(20) == 0

def test_rabatt_mittel():
    assert aufgabe02.rabatt(75) == 5

def test_rabatt_hoch():
    assert aufgabe02.rabatt(150) == 10

def test_rabatt_grenzwert_50():
    assert aufgabe02.rabatt(50) == 5
```

**b) White-Box `quersumme` (10 P)**

Empfehlung für Schleifen: **gar nicht / genau einmal / mehrfach** durchlaufen.
| Pfad | Fall | Beispiel | Erwartung |
|---|---|---|---|
| P1 | Schleife 0× (n = 0) | quersumme(0) | 0 |
| P2 | Schleife 1× (einstellig) | quersumme(7) | 7 |
| P3 | Schleife mehrfach | quersumme(123) | 6 |

```python
def test_quersumme_null():
    assert aufgabe02.quersumme(0) == 0

def test_quersumme_einstellig():
    assert aufgabe02.quersumme(7) == 7

def test_quersumme_mehrstellig():
    assert aufgabe02.quersumme(123) == 6      # 1+2+3
```

---

## Aufgabe 3 – `zahlenauswertung.py` mit getopt (20 P)

```python
import sys
import getopt


def werte_aus(pfad, befehl):
    zahlen = []
    with open(pfad, "r", encoding="utf-8") as datei:
        for zeile in datei:
            zeile = zeile.strip()
            if zeile == "":
                continue
            zahlen.append(float(zeile))

    if befehl == "summe":
        return sum(zahlen)
    elif befehl == "max":
        return max(zahlen)
    elif befehl == "schnitt":
        return round(sum(zahlen) / len(zahlen), 2)


def main(argv):
    inputfile = ""
    outputfile = ""
    befehl = ""

    try:
        opts, args = getopt.getopt(
            argv, "i:o:b:h",
            ["input=", "output=", "befehl=", "help"]
        )
    except getopt.GetoptError:
        print("zahlenauswertung.py -i <input> -o <output> -b <summe|max|schnitt>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("zahlenauswertung.py -i <input> -o <output> -b <summe|max|schnitt>")
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

    ergebnis = werte_aus(inputfile, befehl)
    with open(outputfile, "w", encoding="utf-8") as datei:
        datei.write(f"Befehl: {befehl}\n")
        datei.write(f"Ergebnis: {ergebnis}\n")


if __name__ == "__main__":
    main(sys.argv[1:])
```
Kontrolle: Datei mit 2, 4, 5, 6 → `summe` = 17.0 · `max` = 6.0 · `schnitt` = 17/4 = **4.25**.

---

## Aufgabe 4 – Einfach verkettete Liste (20 P)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    # Titel am Ende anfügen
    def insert(self, titel):
        neuer = Node(titel)
        if self.head is None:
            self.head = neuer
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = neuer

    # alle Titel ausgeben
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # ersten Knoten mit diesem Titel entfernen
    def delete(self, titel):
        if self.head is None:
            return
        if self.head.data == titel:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == titel:
                current.next = current.next.next
                return
            current = current.next

    # i-ten Titel zurückgeben (0-basiert)
    def get(self, i):
        current = self.head
        index = 0
        while current:
            if index == i:
                return current.data
            current = current.next
            index += 1
        raise IndexError("Index außerhalb der Liste")

    # Anzahl der Titel
    def size(self):
        anzahl = 0
        current = self.head
        while current:
            anzahl += 1
            current = current.next
        return anzahl


# Anwendungsbeispiel
pl = Playlist()
pl.insert("Song A")
pl.insert("Song B")
pl.insert("Song C")
pl.print_list()          # Song A, Song B, Song C
print("Größe:", pl.size())   # 3
pl.delete("Song B")
pl.print_list()          # Song A, Song C
print("get(0):", pl.get(0))  # Song A
```

**Zusatzfrage:** Bei einer verketteten Liste sind die Knoten nur über `next`-Verweise verbunden und liegen **nicht zusammenhängend** im Speicher – man muss die Liste vom Kopf an durchlaufen; es gibt **keinen Direktzugriff** über einen Index wie beim Array.

---

## Aufgabe 5 – Selection-Sort (15 P)

**a) (10 P)**
```python
def selection_sort_laenge(woerter):
    n = len(woerter)
    for i in range(n):
        # Minimum (kürzestes Wort) im unsortierten Rest suchen
        min_index = i
        for j in range(i + 1, n):
            if len(woerter[j]) < len(woerter[min_index]):
                min_index = j
        # kürzestes Wort nach vorne tauschen
        woerter[i], woerter[min_index] = woerter[min_index], woerter[i]
    return woerter


woerter = ["Hallo", "Python", "Wirtschaftsinformatiker", "Aufgabe", "Sortieren"]
print(selection_sort_laenge(woerter))
# ['Hallo', 'Python', 'Aufgabe', 'Sortieren', 'Wirtschaftsinformatiker']
#   Längen:  5         6          7            9              23
```

**b) (5 P)**
1. Selection-Sort: **bester Fall O(n²)** und **schlechtester Fall O(n²)** – es wird immer der komplette unsortierte Rest durchsucht, unabhängig von der Vorsortierung.
2. Unterschied Selection vs. Bubble (einer genügt):
   - **Selection** sucht das Minimum und macht nur **einen** Tausch pro Durchlauf; **Bubble** vergleicht/tauscht **benachbarte** Elemente (viele Tausche).
   - **Bubble** kann bei sortierter Eingabe früh abbrechen (O(n)); **Selection** ist **immer** O(n²).
   - **Bubble ist stabil**, **Selection nicht**.

---

## Punkteverteilung
| Aufgabe | Thema | Punkte |
|---|---|---|
| 1 | Software Engineering (inkl. Softwarekrise, Rollout) | 15 |
| 2 | Testen (Black-/White-Box + pytest) | 20 |
| 3 | Kommandozeile & Datei-IO (getopt) | 20 |
| 4 | Einfach verkettete Liste | 20 |
| 5 | Selection-Sort | 15 |
| **Summe** | | **90** |
