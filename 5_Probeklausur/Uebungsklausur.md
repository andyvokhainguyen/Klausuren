# Übungsklausur – Programmierung (SS26)

**Hochschule Trier – Prof. Dr. Andreas Biesdorf**
Bearbeitungszeit: ca. 90 Minuten · Erreichbare Punkte: **90**
Hilfsmittel: nur Python-Syntax-Blatt (keine fertigen Implementierungen).

> Diese Übungsklausur bildet das wiederkehrende Klausurmuster ab und gewichtet die bisher **nie geprüften, aber aktuell geübten** Themen (Queue, Bubble-Sort). Eine eigenständige Exception-Aufgabe ist – wie in der letzten Altklausur – **nicht** enthalten.
> Versuche die Aufgaben zuerst selbst. Schreib mir deine Lösungen, oder sag **„Lösung"**, dann gebe ich dir den kompletten Lösungsschlüssel.

---

## Aufgabe 1 – Software Engineering (15 Punkte)

**a) (4 P)** Erklären Sie den Unterschied zwischen *Programmieren* und *Software-Engineering* anhand von **zwei** unterscheidenden Merkmalen.

**b) (4 P)** Erläutern Sie den **grundlegenden Unterschied** zwischen dem **Wasserfallmodell** und dem **V-Modell**.

**c) (4 P)** Nennen Sie **drei Qualitätsmerkmale aus Benutzersicht** und geben Sie zu jedem **eine Messgröße** an, mit der sich der Grad der Erfüllung bestimmen lässt.

**d) (3 P)** Nennen Sie die **drei Hauptrollen in Scrum** und beschreiben Sie je in einem Satz ihre Aufgabe.

---

## Aufgabe 2 – Testen (20 Punkte)

**a) Black-Box (10 P)** — Gegeben ist folgende Funktion:
```python
def versandkosten(gewicht):
    """ gewicht: Zahl in kg. Gibt die Versandkosten (float) oder einen
        Fehlerstring zurück. """
    if gewicht <= 0:
        return "Ungültiges Gewicht"
    elif gewicht <= 2:
        return 3.0
    elif gewicht <= 10:
        return 5.0
    else:
        return 9.0
```
1. Bestimmen Sie **sinnvolle, überschneidungsfreie Äquivalenzklassen** (inkl. mindestens eines **Grenzwerts**) und begründen Sie kurz.
2. Schreiben Sie zu jeder Klasse einen **pytest**-Test mit einem repräsentativen Wert.

**b) White-Box (10 P)** — Gegeben ist folgende rekursive Funktion:
```python
def summe_bis(n):
    """ n: nicht-negative Ganzzahl. Gibt die Summe 0+1+...+n zurück. """
    if n <= 0:
        return 0
    return n + summe_bis(n - 1)
```
1. Welche **Pfade** sollten für eine „path-complete" Prüfung getestet werden? Benennen und begründen Sie sie kurz.
2. Schreiben Sie die zugehörigen **pytest**-Tests.

---

## Aufgabe 3 – Kommandozeile & Datei-IO (20 Punkte)

Schreiben Sie ein Programm `notenauswertung.py`, das eine Textdatei mit Klausurergebnissen einliest. Jede Zeile hat das Format:
```
matrikelnummer;note
```
Beispiel `noten.txt`:
```
12345;2.3
23456;5.0
34567;1.7
45678;4.0
56789;5.0
```

Verwenden Sie das **argparse**-Modul. Das Programm soll folgende Argumente unterstützen:
- `--input` / `-i` : Name der Eingabedatei (Pflicht)
- `--output` / `-o` : Name der Ausgabedatei (Pflicht)
- `--befehl` / `-b` : einer von `anzahl`, `bestanden`, `schnitt` (Pflicht)

Bedeutung der Befehle:
- `anzahl` : Anzahl der Zeilen/Studierenden in der Datei
- `bestanden` : Anzahl der Noten, die **besser als 5.0** sind (also `note < 5.0`)
- `schnitt` : Notendurchschnitt (auf 2 Nachkommastellen gerundet)

Das Ergebnis soll in die Ausgabedatei geschrieben werden, z.B.:
```
Befehl: schnitt
Ergebnis: 3.6
```
Beispielaufruf: `python3 notenauswertung.py -i noten.txt -o ergebnis.txt -b schnitt`

---

## Aufgabe 4 – Datenstruktur: Warteschlange (20 Punkte)

Ein Support-System verwaltet Tickets nach dem **FIFO-Prinzip**. Implementieren Sie eine Klasse `Warteschlange` (Queue) mit folgenden Methoden:

- `enqueue(ticket)` : fügt ein Ticket **hinten** an
- `dequeue()` : entfernt das **vorderste** Ticket und gibt es zurück (bei leerer Schlange `None`)
- `peek()` : gibt das vorderste Ticket zurück, **ohne** es zu entfernen (bei leer `None`)
- `is_empty()` : `True`, wenn die Schlange leer ist
- `size()` : Anzahl der Tickets
- `get(i)` : gibt das `i`-te Ticket (0-basiert) zurück; bei ungültigem Index eine `IndexError`-Ausnahme

Demonstrieren Sie die korrekte Funktion mit einem kleinen Anwendungsbeispiel (Ticket „A", „B", „C" einfügen, einmal `dequeue`, Zustand ausgeben).

**Zusatzfrage (schriftlich):** Worin unterscheidet sich die Entnahme bei einer **Queue** von der bei einem **Stack**? (1 Satz)

---

## Aufgabe 5 – Sortierverfahren: Bubble-Sort (15 Punkte)

Gegeben ist eine Liste von Studierenden als Dictionaries:
```python
studierende = [
    {"name": "Anna",  "note": 2.3},
    {"name": "Ben",   "note": 1.0},
    {"name": "Clara", "note": 3.7},
    {"name": "David", "note": 1.7},
]
```

**a) (10 P)** Implementieren Sie eine Funktion `bubble_sort_studierende(studierende)`, die die Liste mithilfe des **Bubble-Sort-Algorithmus** aufsteigend nach der **Note** sortiert. Geben Sie anschließend die sortierte Liste aus.

**b) (5 P)** Beantworten Sie schriftlich:
1. Wie lautet die Zeitkomplexität von Bubble-Sort im **besten** und im **schlechtesten** Fall?
2. Nennen Sie **einen** Unterschied zwischen **Bubble-Sort** und **Selection-Sort**.

---

*Viel Erfolg!* — Wenn du fertig bist: schick mir deine Lösungen zum Korrigieren oder sag **„Lösung"** für den Lösungsschlüssel.
