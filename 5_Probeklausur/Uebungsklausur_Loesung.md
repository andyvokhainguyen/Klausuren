# Lösungsschlüssel – Übungsklausur Programmierung (SS26)

Gesamt: **90 Punkte**. Lösungen zu [Uebungsklausur.md](Uebungsklausur.md).

---

## Aufgabe 1 – Software Engineering (15 P)

**a) Programmieren vs. Software-Engineering (4 P)** — zwei unterscheidende Merkmale, z.B.:
- **Systematik:** Programmieren = ad-hoc-Schreiben von Code für eine kleine, konkrete Aufgabe (oft eine Person, Fokus Algorithmus/Syntax). Software-Engineering = systematisches Vorgehen nach **Phasenmodellen** (Wasserfall, V-Modell, Scrum) für umfangreiche Systeme.
- **Umfang/Lebenszyklus:** SE umfasst den **gesamten Lebenszyklus** inkl. Betrieb/Wartung (~80 % der Kosten), Qualitätssicherung, Dokumentation und **arbeitsteilige Teamarbeit**; reines Programmieren endet meist, wenn „der Code läuft".

**b) Wasserfall vs. V-Modell (4 P):**
- **Wasserfall:** rein **sequenzielle** Phasen; getestet wird erst **am Ende** → Fehler werden spät entdeckt.
- **V-Modell:** ordnet **jeder** Entwicklungsphase eine **Teststufe** zu (Anforderungen↔Abnahmetest, Systemspezifikation↔Systemtest, Architektur↔Integrationstest, Detailentwurf↔Modultest).
- **Kernunterschied:** Das V-Modell **verzahnt Entwicklung und Test** (Qualitätssicherung von Anfang an, jede Phase hat ein Testpendant), Wasserfall testet erst nach der Realisierung.

**c) Drei Qualitätsmerkmale (Benutzersicht) + Messgröße (4 P):**
| Merkmal | Messgröße |
|---|---|
| Funktionserfüllung | Anteil umgesetzter Anforderungen (%) |
| Zuverlässigkeit | mittlere Betriebsdauer zwischen Ausfällen (MTBF) / Fehlerrate |
| Benutzbarkeit | Einarbeitungszeit / Anzahl Klicks pro Vorgang |
*(auch gültig: Effizienz → Antwortzeit in ms; Sicherheit → Anzahl Schwachstellen)*

**d) Drei Scrum-Rollen (3 P):**
- **Product Owner:** pflegt und priorisiert das Product Backlog, vertritt den Kunden.
- **Scrum Master:** Prozess-Coach, sorgt für die Einhaltung von Scrum und beseitigt Hindernisse.
- **Entwicklungsteam:** selbstorganisiert und cross-funktional, liefert das Produkt-Inkrement.

---

## Aufgabe 2 – Testen (20 P)

**a) Black-Box `versandkosten` (10 P)**

Äquivalenzklassen (überschneidungsfrei + Grenzwert):
| Klasse | Bereich | Wert | Erwartung |
|---|---|---|---|
| K1 ungültig | gewicht ≤ 0 | 0 | "Ungültiges Gewicht" |
| K2 leicht | 0 < g ≤ 2 | 1 | 3.0 |
| K3 mittel | 2 < g ≤ 10 | 5 | 5.0 |
| K4 schwer | g > 10 | 15 | 9.0 |
| K5 Grenzwert | g == 2 | 2 | 3.0 |

Begründung: Jede if/elif/else-Kategorie wird durch genau eine Klasse abgedeckt; K5 prüft die kritische Grenze 2 (gehört laut Code noch zu 3.0). Weitere sinnvolle Grenzwerte: 0 und 10.

```python
from src import aufgabe02

def test_versand_ungueltig():
    assert aufgabe02.versandkosten(0) == "Ungültiges Gewicht"

def test_versand_leicht():
    assert aufgabe02.versandkosten(1) == 3.0

def test_versand_mittel():
    assert aufgabe02.versandkosten(5) == 5.0

def test_versand_schwer():
    assert aufgabe02.versandkosten(15) == 9.0

def test_versand_grenzwert_2():
    assert aufgabe02.versandkosten(2) == 3.0
```

**b) White-Box `summe_bis` (10 P)**

Pfade (Empfehlung Rekursion: Basisfall / einmal / mehrfach):
| Pfad | Fall | Beispiel | Erwartung |
|---|---|---|---|
| P1 | Basisfall n ≤ 0 | summe_bis(0) | 0 |
| P1b | Randfall negativ | summe_bis(-3) | 0 |
| P2 | genau 1× rekursiv | summe_bis(1) → 1 + summe_bis(0) | 1 |
| P3 | mehrfach rekursiv | summe_bis(4) | 10 |

```python
def test_summe_basisfall():
    assert aufgabe02.summe_bis(0) == 0

def test_summe_negativ():
    assert aufgabe02.summe_bis(-3) == 0

def test_summe_eine_rekursion():
    assert aufgabe02.summe_bis(1) == 1

def test_summe_mehrfach():
    assert aufgabe02.summe_bis(4) == 10   # 4+3+2+1
```

---

## Aufgabe 3 – `notenauswertung.py` (20 P)

```python
import argparse


def werte_aus(pfad, befehl):
    noten = []
    with open(pfad, "r", encoding="utf-8") as datei:
        for zeile in datei:
            zeile = zeile.strip()
            if zeile == "":
                continue
            matrikel, note = zeile.split(";")
            noten.append(float(note))

    if befehl == "anzahl":
        return len(noten)
    elif befehl == "bestanden":
        return sum(1 for n in noten if n < 5.0)
    elif befehl == "schnitt":
        return round(sum(noten) / len(noten), 2)


def schreibe_ergebnis(pfad, befehl, ergebnis):
    with open(pfad, "w", encoding="utf-8") as datei:
        datei.write(f"Befehl: {befehl}\n")
        datei.write(f"Ergebnis: {ergebnis}\n")


def main():
    parser = argparse.ArgumentParser(description="Auswertung von Klausurnoten.")
    parser.add_argument("--input", "-i", required=True, help="Eingabedatei")
    parser.add_argument("--output", "-o", required=True, help="Ausgabedatei")
    parser.add_argument("--befehl", "-b", required=True,
                        choices=["anzahl", "bestanden", "schnitt"])
    args = parser.parse_args()

    ergebnis = werte_aus(args.input, args.befehl)
    schreibe_ergebnis(args.output, args.befehl, ergebnis)


if __name__ == "__main__":
    main()
```
Kontrolle mit der Beispieldatei: Noten 2.3, 5.0, 1.7, 4.0, 5.0 →
`anzahl` = 5 · `bestanden` = 3 (2.3, 1.7, 4.0) · `schnitt` = 18.0/5 = **3.6**.

---

## Aufgabe 4 – Warteschlange / Queue (20 P)

```python
class Warteschlange:
    def __init__(self):
        self.queue = []

    def enqueue(self, ticket):          # hinten anfügen
        self.queue.append(ticket)

    def dequeue(self):                  # vorne entfernen (FIFO)
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):                     # vorne ansehen, nicht entfernen
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def get(self, i):                   # i-tes Ticket (0-basiert)
        if i < 0 or i >= len(self.queue):
            raise IndexError("Index außerhalb der Warteschlange")
        return self.queue[i]


# Anwendungsbeispiel
w = Warteschlange()
w.enqueue("A")
w.enqueue("B")
w.enqueue("C")
print("Größe:", w.size())        # 3
print("dequeue:", w.dequeue())   # A
print("peek:", w.peek())         # B
print("Größe:", w.size())        # 2
print("leer?", w.is_empty())     # False
```

**Zusatzfrage:** Eine **Queue** entfernt vorne = das **zuerst** eingefügte Element (**FIFO**); ein **Stack** entfernt hinten = das **zuletzt** eingefügte Element (**LIFO**).

---

## Aufgabe 5 – Bubble-Sort (15 P)

**a) (10 P)**
```python
def bubble_sort_studierende(studierende):
    n = len(studierende)
    for i in range(n - 1):
        getauscht = False
        for j in range(0, n - i - 1):
            # Vergleich über den Schlüssel "note" (aufsteigend)
            if studierende[j]["note"] > studierende[j + 1]["note"]:
                studierende[j], studierende[j + 1] = studierende[j + 1], studierende[j]
                getauscht = True
        if not getauscht:          # nichts getauscht -> fertig
            break
    return studierende


studierende = [
    {"name": "Anna",  "note": 2.3},
    {"name": "Ben",   "note": 1.0},
    {"name": "Clara", "note": 3.7},
    {"name": "David", "note": 1.7},
]
bubble_sort_studierende(studierende)
for s in studierende:
    print(s)
# Ben (1.0), David (1.7), Anna (2.3), Clara (3.7)
```

**b) (5 P)**
1. Bubble-Sort: **bester Fall O(n)** (bereits sortiert, mit `getauscht`-Abbruch), **schlechtester Fall O(n²)**.
2. Unterschied Bubble vs. Selection (einer genügt):
   - **Bubble** vergleicht/tauscht **benachbarte** Elemente (viele Vertauschungen); **Selection** sucht das **Minimum** und macht nur **einen** Tausch pro Durchlauf.
   - **Bubble ist stabil**, **Selection nicht**.
   - Bubble kann bei sortierter Eingabe früh abbrechen (O(n)); Selection ist immer O(n²).

---

## Punkteverteilung
| Aufgabe | Thema | Punkte |
|---|---|---|
| 1 | Software Engineering | 15 |
| 2 | Testen (Black-/White-Box + pytest) | 20 |
| 3 | Kommandozeile & Datei-IO (argparse) | 20 |
| 4 | Queue | 20 |
| 5 | Bubble-Sort | 15 |
| **Summe** | | **90** |
