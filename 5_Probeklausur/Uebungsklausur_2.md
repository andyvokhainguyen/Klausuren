# Übungsklausur 2 – Programmierung (SS26)

**Hochschule Trier – Prof. Dr. Andreas Biesdorf**
Bearbeitungszeit: ca. 90 Minuten · Erreichbare Punkte: **90**
Hilfsmittel: nur Python-Syntax-Blatt (keine fertigen Implementierungen).

> Zweite Übungsklausur – bewusst mit den **anderen** wahrscheinlichen Varianten: **getopt** statt argparse, **verkettete Liste** statt Queue, **Selection-Sort** statt Bubble, und Theoriethemen, die in Altklausuren **noch nie** gefragt wurden.
> Versuche es zuerst selbst. Danach: Lösung in `Uebungsklausur_2_Loesung.md` oder sag **„Lösung 2"**.

---

## Aufgabe 1 – Software Engineering (15 Punkte)

**a) (4 P)** Die **Softwarekrise**: Erklären Sie kurz, was damit gemeint ist. Wann und wo wurde der Begriff „Software Engineering" geprägt? Nennen Sie außerdem die grobe Verteilung der Projektergebnisse laut **CHAOS-Report** (erfolgreich / herausgefordert / gescheitert).

**b) (4 P)** Nennen Sie **vier Einführungsstrategien (Rollout)** und geben Sie zu jeder eine kurze Beschreibung sowie das jeweilige **Risiko** an.

**c) (4 P)** Kreuzen Sie an: Was gehört ins **Lastenheft**, was ins **Pflichtenheft**?

| Aussage | Lastenheft | Pflichtenheft |
|---|---|---|
| Grobe Zielbestimmung und Anforderungen des Auftraggebers | ☐ | ☐ |
| Konkrete Use Cases und GUI-Skizzen | ☐ | ☐ |
| Glossar zur einheitlichen Begriffsdefinition | ☐ | ☐ |
| Abnahmekriterien des Kunden | ☐ | ☐ |

**d) (3 P)** Nennen Sie die **fünf Sichten des 4+1-Modells nach Kruchten** und geben Sie zu jeder ein Stichwort.

---

## Aufgabe 2 – Testen (20 Punkte)

**a) Black-Box (10 P)** — Gegeben ist folgende Funktion:
```python
def rabatt(bestellwert):
    """ bestellwert: Zahl in Euro. Gibt den Rabatt in Prozent (int)
        oder einen Fehlerstring zurück. """
    if bestellwert < 0:
        return "Ungültiger Wert"
    elif bestellwert < 50:
        return 0
    elif bestellwert < 100:
        return 5
    else:
        return 10
```
1. Bestimmen Sie sinnvolle, überschneidungsfreie **Äquivalenzklassen** (inkl. mindestens eines **Grenzwerts**) und begründen Sie kurz.
2. Schreiben Sie zu jeder Klasse einen **pytest**-Test.

**b) White-Box (10 P)** — Gegeben ist folgende Funktion mit einer **while-Schleife**:
```python
def quersumme(n):
    """ n: nicht-negative Ganzzahl. Gibt die Quersumme der Ziffern zurück. """
    summe = 0
    while n > 0:
        summe += n % 10
        n = n // 10
    return summe
```
1. Welche **Pfade** sollten für eine „path-complete" Prüfung getestet werden (Empfehlung für Schleifen)? Benennen und begründen Sie sie.
2. Schreiben Sie die zugehörigen **pytest**-Tests.

---

## Aufgabe 3 – Kommandozeile & Datei-IO mit **getopt** (20 Punkte)

Schreiben Sie ein Programm `zahlenauswertung.py`, das eine Textdatei mit **einer Zahl pro Zeile** einliest. Verwenden Sie das **getopt**-Modul.

Unterstützte Optionen:
- `-i` / `--input` : Eingabedatei (Pflicht)
- `-o` / `--output` : Ausgabedatei (Pflicht)
- `-b` / `--befehl` : einer von `summe`, `max`, `schnitt` (Pflicht)
- `-h` / `--help` : Hilfetext ausgeben

Bedeutung: `summe` = Summe aller Zahlen · `max` = größte Zahl · `schnitt` = Durchschnitt (auf 2 Nachkommastellen gerundet).
Das Ergebnis wird in die Ausgabedatei geschrieben:
```
Befehl: schnitt
Ergebnis: 4.25
```
Bei fehlerhaften/fehlenden Argumenten soll eine Fehlermeldung ausgegeben werden.
Beispielaufruf: `python3 zahlenauswertung.py -i zahlen.txt -o ergebnis.txt -b summe`

---

## Aufgabe 4 – Datenstruktur: Einfach verkettete Liste (20 Punkte)

Implementieren Sie eine **einfach verkettete Liste** als Klasse `Playlist`, die Songtitel (Strings) verwaltet. Verwenden Sie eine Hilfsklasse `Node` mit den Attributen `data` und `next`.

Methoden:
- `insert(titel)` : fügt einen Titel **am Ende** an
- `print_list()` : gibt alle Titel der Reihe nach aus
- `delete(titel)` : entfernt den ersten Knoten mit diesem Titel
- `get(i)` : gibt den Titel an Position `i` (0-basiert) zurück; bei ungültigem Index eine `IndexError`-Ausnahme
- `size()` : Anzahl der Titel

Demonstrieren Sie die Funktion mit einem kleinen Beispiel (drei Titel einfügen, einen löschen, Liste ausgeben).

**Zusatzfrage (schriftlich):** Warum kann man bei einer verketteten Liste **nicht** direkt über einen Index zugreifen (wie bei einem Array)? (1 Satz)

---

## Aufgabe 5 – Sortierverfahren: Selection-Sort (15 Punkte)

Gegeben ist eine Liste von Wörtern:
```python
woerter = ["Hallo", "Python", "Wirtschaftsinformatiker", "Aufgabe", "Sortieren"]
```

**a) (10 P)** Implementieren Sie eine Funktion `selection_sort_laenge(woerter)`, die die Liste mit dem **Selection-Sort-Algorithmus** aufsteigend nach der **Wortlänge** sortiert. Geben Sie die sortierte Liste aus.

**b) (5 P)** Beantworten Sie schriftlich:
1. Wie lautet die Zeitkomplexität von Selection-Sort im **besten** und im **schlechtesten** Fall?
2. Nennen Sie **einen** Unterschied zwischen **Selection-Sort** und **Bubble-Sort**.

---

*Viel Erfolg!* — Lösung: `Uebungsklausur_2_Loesung.md` oder sag **„Lösung 2"**.
