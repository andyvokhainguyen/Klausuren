# Programmierung 2 – Klausurvorbereitung

Zentrale Übersicht über alle Lernmaterialien. **Wichtigstes zuerst:** in der Klausur ist nur ein Syntax-Blatt erlaubt (`Hilfsmittel_erlaubt.pdf`) – die kompletten Code-Strukturen musst du **auswendig** können.

## 📂 Ordnerstruktur

| Ordner / Datei | Inhalt |
|---|---|
| **`Hilfsmittel_erlaubt.pdf`** | Das in der Klausur **erlaubte** Syntax-Blatt (nur Syntax, keine fertigen Lösungen). |
| **`1_Skripte/`** | Die 6 Vorlesungsskripte (PDF) als Wissensgrundlage. |
| **`2_Zusammenfassungen/`** | Meine Lern-Zusammenfassungen – das **Kernmaterial** zum Auswendiglernen. |
| **`3_Altklausuren/`** | Die 6 Original-Altklausuren (SS23–WS2526) mit vollständigen Musterlösungen (`prog_*/src` + `test`). |
| **`4_Uebungsblaetter_Loesungen/`** | Meine Lösungen zu den Übungsblättern 1–7 + der Wiederholungsaufgaben. |
| **`5_Probeklausur/`** | Eine selbst erstellte Übungsklausur mit Lösungsschlüssel. |

### `2_Zusammenfassungen/` im Detail
1. **`1_Theorie_SoftwareEngineering.md`** – alle Theoriethemen im Altklausur-Frage-Stil (+ noch nie gefragte Themen).
2. **`2_Code_Uebersicht.md`** – alle prüfungsrelevanten Codes (Skript 02–06) mit Erklärungen.
3. **`3_Sortierverfahren_Traces.md`** – alle 6 Sortierverfahren Schritt für Schritt durchgerechnet.
4. **`4_Fokusthemen_Bubble_Selection_Queue.md`** – die wahrscheinlichsten „neuen" Aufgaben (Lückenanalyse).
5. **`5_Skripte_ausfuehrlich.md`** – die ausführliche Gesamt-Zusammenfassung der Skripte.

## 🎯 Empfohlener Lernpfad (Schritt für Schritt)

**Grundprinzip:** Nicht 20 Programme auswendig lernen, sondern **~6 Grundmuster** verstehen und anpassen. Pro Struktur: verstehen → Skelett erkennen → abschreiben → **aus dem Kopf aufschreiben** → mit Abstand wiederholen.

1. **Stack & Queue** → `2_Zusammenfassungen/2_Code_Uebersicht.md` + `4_Fokusthemen…`
2. **Sortieren (Bubble → Selection → Insertion)** → `2_Code_Uebersicht.md` + `3_Sortierverfahren_Traces.md`
3. **Rekursion (BST-insert, Quicksort, Mergesort)** → `2_Code_Uebersicht.md`
4. **Testen (Äquivalenzklassen + pytest)** → `2_Code_Uebersicht.md` + `4_Uebungsblaetter_Loesungen/Blatt_02_Testen.md`
5. **Kommandozeile + Datei-IO (argparse/getopt)** → `Blatt_03…` + `Blatt_04…`
6. **Theorie wiederholen** → `1_Theorie_SoftwareEngineering.md`
7. **Testlauf:** `5_Probeklausur/Uebungsklausur.md` selbst lösen, dann mit der Lösung vergleichen.

## 🔥 Wahrscheinliche Schwerpunkte (Lückenanalyse)
Diese Themen kamen in **keiner** Altklausur dran, werden aber aktuell geübt → gut vorbereiten:
- **Bubble-Sort** und **Selection-Sort** (auf Strings/Dicts angewandt)
- **Queue / Warteschlange** (FIFO)
- Theorie: **Softwarekrise/CHAOS-Report**, **Einführungsstrategien (Rollout)**, **Brooks'sches Gesetz**, **1-10-100-Regel**
