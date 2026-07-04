# Lösungen – Übungsblatt 1 (Software-Engineering-Theorie)

Fallstudie: Scheitern der Entwicklung einer SAP-basierten Warenwirtschaftslösung für einen führenden deutschen Discounter (bekanntes Beispiel: das ~2018 eingestellte Projekt „eLWIS"/SAP bei Lidl).
*Hinweis: Die Antworten stützen sich auf allgemeine SE-Prinzipien und den bekannten Fall; die genaue Punktvergabe hängt vom Artikel ab.*

---

## Aufgabe 1 – Analyse des gescheiterten Projekts

**1) Fünf besonders herausfordernde Randbedingungen (aus SW-Entwicklungssicht):**
- **Anpassung von Standardsoftware an bestehende Prozesse:** Statt Prozesse an die Standardsoftware anzupassen, sollte die Software an gewachsene (z.B. einkaufspreisbasierte) Sonderprozesse angepasst werden → enorme Customizing-/Anpassungstiefe.
- **Migration von Altsystemen:** Ablösung eines langjährig gewachsenen Legacy-Systems mit riesigem Datenbestand und undokumentierten Sonderfällen.
- **Große Systemkomplexität & Skalierung:** Warenwirtschaft über tausende Filialen/Länder mit hohen Performance- und Verfügbarkeitsanforderungen.
- **Sich ändernde/unklare Anforderungen:** Viele versteckte und im Laufe des Projekts wechselnde Anforderungen (Requirements Creep).
- **Organisatorische Randbedingungen:** Verteilte Teams, Abhängigkeit von externem Dienstleister, Termindruck, hohe Kosten (dreistelliger Millionenbereich).

**2) Wichtigste beteiligte Rollen + Interaktionen (aus Sicht des Anbieters/SAP):**
```
        Kunde (Discounter)  <---- Anforderungen/Abnahme ---->  Projektleitung/Manager
                                                                     |  (koordiniert)
     Marketing/Vertrieb ----\                                       |
                             \--->  Manager  <----> SW-Entwicklung (Berater/Entwickler)
     Qualitätssicherung <-----------/    \----> Betrieb/Support
```
- **Kunde** liefert Anforderungen, nimmt ab. **Projektleitung/Manager** (zentral) koordiniert Termine/Kosten/Ressourcen. **SW-Entwicklung/Consulting** setzt um. **QS** sichert Qualität. **Betrieb/Support** übernimmt später.

**3) Fünf „Learnings" für zukünftige Projekte:**
- Prozesse möglichst an den **Standard** anpassen statt die Software massiv zu individualisieren.
- **Anforderungen früh und klar** erheben (Lasten-/Pflichtenheft), versteckte Anforderungen aktiv aufdecken.
- **Iterativ/agil** vorgehen mit früher, kontinuierlicher Lieferung statt Big-Bang.
- **Realistische Planung** (Zeit/Kosten/Qualität = magisches Dreieck) und Risikomanagement mit Puffern.
- **Frühzeitig testen** (V-Modell-Denke), Qualitätssicherung von Anfang an.

**4) Konkrete Maßnahmen für das neu startende Wawi-Projekt:**
Klare Anforderungsdokumentation, MVP/Scope-Priorisierung, Standard-nahe Umsetzung, agile Sprints mit Kundenfeedback, durchgehende Testautomatisierung, erfahrenes Kernteam (nicht spät aufblähen), regelmäßige Reviews.

---

## Aufgabe 2 – Qualitätsmerkmale (als Chief-Requirements-Engineer)

**1) Je 3–5 Merkmale + Erläuterung**
Benutzersicht: **Funktionserfüllung** (alle Warenwirtschaftsfunktionen vorhanden), **Zuverlässigkeit** (kein Ausfall/Datenverlust im Filialbetrieb), **Benutzbarkeit** (schnelle Einarbeitung der Mitarbeitenden), **Effizienz** (kurze Antwortzeiten an der Kasse).
Entwicklersicht: **Wartbarkeit** (Pflege über Jahre), **Testbarkeit** (isolierte Module), **Änderbarkeit/Erweiterbarkeit** (neue Länder/Filialen), **Portabilität**.

**2) Grad der Erfüllung messen (je eine Messgröße):**
| Merkmal | Messgröße |
|---|---|
| Funktionserfüllung | Anteil umgesetzter Anforderungen (%) |
| Zuverlässigkeit | mittlere Betriebsdauer zwischen Ausfällen (MTBF), Fehlerrate |
| Benutzbarkeit | durchschnittliche Einarbeitungszeit / Klicks pro Vorgang |
| Effizienz | durchschnittliche Antwortzeit (ms), Durchsatz |
| Wartbarkeit | Zeit für Fehlerbehebung, zyklomatische Komplexität |
| Testbarkeit | Testabdeckung (%) |

**3) Abhängigkeiten:**
Die Merkmale stehen in **Wechselwirkung** (magisches Dreieck): Steigt z.B. die Anforderung an **Effizienz** stark, kann das die **Wartbarkeit** senken (hochoptimierter, komplexer Code) und die **Kosten/Zeit** erhöhen. Mehr **Sicherheit/Zuverlässigkeit** kostet ebenfalls Zeit/Budget. Ändert sich eine Anforderung stark, müssen die anderen neu balanciert werden.

---

## Aufgabe 3 – CIO-Gespräch (Phasen & Personalplanung)

**1) Antwort an den CIO (mit Phasen der SW-Entwicklung):**
„Zwei Jahre reine Implementierung inkl. Architektur/Design sind für ein System dieser Größe **sehr optimistisch**." Begründung über die **Phasen**: Nach Analyse und Definition folgen Architektur, Design, Implementierung und – entscheidend – **Modultest, Integration, Systemtest, Abnahme** sowie Einführung/Betrieb. Gerade Test-, Integrations- und Einführungsphasen werden oft unterschätzt; ein fixer Jubiläumstermin ist riskant, wenn Qualität nicht leiden soll.

**2) Wie viele Programmierer? (Brooks' Law + magisches Dreieck):**
Personal lässt sich **nicht beliebig** hochskalieren. **Brooks' Gesetz:** „Adding manpower to a late software project makes it later." Mehr Leute erhöhen den **Kommunikationsaufwand** (wächst ~quadratisch mit der Teamgröße) und die Einarbeitungszeit. Offshore/Nearshore bringen zusätzlich Sprach-, Zeitzonen- und Abstimmungskosten. → Man kann **nicht** über reine Personalzahl den Termin retten; besser: **Scope reduzieren**, Prioritäten setzen, erfahrenes, angemessen großes Team. Im magischen Dreieck (Zeit/Kosten/Qualität) lässt sich nicht alles gleichzeitig maximieren.
