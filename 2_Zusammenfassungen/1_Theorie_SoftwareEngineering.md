# Theorie-Zusammenfassung (Software Engineering) – im Altklausur-Stil

Aufbau: pro Thema steht dabei, **wie der Prof es in den 6 Altklausuren gefragt hat** (Fragetyp) + die **Kernantwort**.
Ganz unten: **große Theoriethemen aus Skript 01, die noch NIE gefragt wurden** – mit Musterantwort.

---

# TEIL A – Themen, die bereits geprüft wurden

## 1. Programmierung vs. Software-Engineering
*Gefragt als:* „Erläutern Sie den Unterschied … anhand von 2 Merkmalen" (SS23, SS25).
- **Programmieren:** Code für kleine, konkrete Aufgabe; oft eine Person; Fokus Algorithmus/Syntax.
- **SE (Balzert):** „Zielorientierte Bereitstellung und systematische Verwendung von Prinzipien, Methoden und Werkzeugen für die **arbeitsteilige, ingenieurmäßige** Entwicklung **umfangreicher** Software-Systeme."
- Merkmale: **zielorientiert, systematisch, arbeitsteilig, ingenieurmäßig** (wiederholbar/messbar/dokumentiert), **umfangreiche Systeme**.

## 2. Gründe für den Einsatz von SE
*Gefragt als:* „Nennen Sie 4 Gründe" (WS2324).
| Herausforderung | Beitrag des SE |
|---|---|
| Komplexität | Strukturierung, Modularisierung, Abstraktion |
| Funktion | systematisches Erfassen der Stakeholder-Wünsche |
| Qualität | Sicherheit, Robustheit, Testbarkeit |
| Wartung | Dokumentation, langfristige Pflegbarkeit |
| Planung | Termine, Kosten, Personal, Risikomanagement |
| Organisation | Teamgröße, Standortverteilung, Zeitzonen |
| Methodik | Prozesse, Standards, Best Practices |

## 3. Magisches Dreieck des Projektmanagements
*Gefragt als:* „Erklären + Beispiel" / „Bewerten Sie die Vorgaben" (SS23, SS24, WS2425).
- Drei konkurrierende Dimensionen: **ZEIT – KOSTEN – QUALITÄT**.
- Änderung einer Dimension wirkt **zwangsläufig** auf die anderen. Man kann nicht alle drei gleichzeitig maximieren.
- Beispiel: Termin verkürzen → mehr Personal (Kosten ↑) oder weniger Features/Tests (Qualität ↓).

## 4. Softwarequalität
*Gefragt als:* „3–5 Merkmale je Sicht" / „+ Messgröße" / „Abhängigkeiten" (WS2324, SS24, Übung).
- **Benutzersicht:** Funktionserfüllung, Effizienz, Zuverlässigkeit, Benutzbarkeit, Sicherheit.
- **Entwicklersicht:** Erweiterbarkeit, Änderbarkeit, Wartbarkeit, Übertragbarkeit, Testbarkeit, Wiederverwendbarkeit.
- **Messgrößen:** Funktionserfüllung → % umgesetzte Anforderungen · Zuverlässigkeit → MTBF/Fehlerrate · Effizienz → Antwortzeit · Wartbarkeit → zyklomatische Komplexität · Testbarkeit → Testabdeckung.
- **Abhängigkeiten:** Verbesserung von Effizienz ↓ Wartbarkeit/Portabilität; Sicherheit ↓ Benutzbarkeit/Effizienz; Robustheit ↓ Effizienz.

## 5. Phasen der Softwareentwicklung
*Gefragt als:* „Ergänzen Sie die fehlenden Begriffe im Zyklus" + „Aufgabe & Ergebnis je Phase" (SS23, Übung).
Zyklus: **Analyse → Definition → Architektur → Design → Implementierung → Modultest → Integration → Systemtest → Abnahme → Einführung/Betrieb → (Analyse)**
| Phase | Ergebnis (Artefakt) | Schlüsselfrage |
|---|---|---|
| Analyse | Anforderungsdokumentation | Was will der Kunde? |
| Definition | Spezifikation, Abnahmekriterien | Was soll das System tun? |
| Architektur | Komponentenstruktur | Wie ist es aufgebaut (grob)? |
| Design | Klassen, Schnittstellen | Wie im Detail? |
| Implementierung | Code, Unit Tests | Funktioniert der Code? |
| Integration/Test | getestetes Gesamtsystem | Funktioniert alles zusammen? |
| Abnahme | Abnahmeprotokoll | Erfüllt es die Anforderungen? |
| Einführung/Betrieb | produktives System, Wartungsdoku | Läuft es zuverlässig? |

## 6. Phasenmodelle: Wasserfall / V-Modell / Scrum
*Gefragt als:* „Grundlegender Unterschied Wasserfall vs. V-Modell" + „welches Modell empfehlen Sie?" (SS23); „Scrum-Rollen + Prozess" (SS25).
- **Wasserfall:** sequenzielle Phasen (Royce 1970); Test erst am Ende → Fehler spät; geringe Flexibilität.
- **V-Modell:** jede Entwicklungsphase hat ein **Testpendant** (Anforderungsanalyse↔Abnahmetest, Systemspez.↔Systemtest, Architektur↔Integrationstest, Detailentwurf↔Modultest). QS von Anfang an. (**V-Modell XT** = „Extreme Tailoring", Pflicht für dt. Behörden-IT.)
- **Scrum (agil):** Rollen **Product Owner / Scrum Master / Entwicklungsteam**; Artefakte **Product Backlog / Sprint Backlog / Inkrement**; Events **Sprint (2–4 Wo.) / Sprint Planning / Daily Scrum (15 Min.) / Sprint Review / Retrospektive**.
- **Empfehlung:** stabile, klare Anforderungen → Wasserfall; sicherheitskritisch/komplex → V-Modell; veränderliche Anforderungen → Scrum.

## 7. Lasten- vs. Pflichtenheft
*Gefragt als:* „Unterschied" / „Kreuzen Sie an: Was gehört wohin?" (WS2324, Übung/Wiederholung).
- **Lastenheft = WAS/WOZU** (vom **Auftraggeber**): Zielbestimmung, funktionale + nicht-funktionale Anforderungen, Lieferumfang, Abnahmekriterien. Oft noch unscharf.
- **Pflichtenheft = WIE** (vom **Auftragnehmer**): konkrete Anwendungsfälle/Use Cases, Benutzungsschnittstelle (GUI-Skizzen), Glossar, technische Umsetzung/Architektur, Zeit-/Phasenplan.
- Beide bilden zusammen die **vertragliche Grundlage**.

## 8. Funktionale vs. nicht-funktionale Anforderungen
*Gefragt als:* Multiple-Choice / „3 funktionale + 3 nicht-funktionale für System X" (SS23, WS2425).
- **Funktional = WAS** das System tun soll (konkrete Funktionen).
- **Nicht-funktional = WIE GUT** (Qualität: Performanz, Zuverlässigkeit, Sicherheit, Skalierbarkeit …).

## 9. Versteckte Anforderungen
*Gefragt als:* „Was sind versteckte Anforderungen, wie erkennt man sie?" (WS2324).
Nicht explizit genannt, aber aus dem Kontext ableitbar. Erkennung durch Nachfragen:
Einsatzort→Wartungsart · Benutzungsfrequenz→Performanz · Ausfallfolgen→Robustheit · Anwenderprofil→Internationalisierung · Geschäftsplanung→Erweiterbarkeit · bestehende Probleme→kritische Anforderungen.

## 10. 4+1-Sichten nach Kruchten
*Gefragt als:* „Ergänzen Sie die 4 fehlenden Sichten in der Grafik" / „Ordnen Sie Aspekte den Sichten zu" (WS2324, SS24, WS2526).
| Sicht | Inhalt / zugeordneter Aspekt |
|---|---|
| **Logische Sicht** | Klassen/Objekte, Domänenaufteilung, Funktionalität |
| **Entwicklungs-/Implementierungs-Sicht** | Dateien, Repositories, Konfiguration |
| **Prozess-Sicht** | Prozesse/Threads, Performanz, Skalierbarkeit, Verfügbarkeit |
| **Physische Sicht** | Hardwareressourcen, Hardwaretopologie, Verteilung |
| **Szenario-/Anwendungssicht („+1")** | Akteure, Anwendungsfälle – verbindet die 4 Sichten |

## 11. Software Engineering im Projekt (Stakeholder/Rollen)
*Gefragt als:* „Skizzieren Sie die wichtigsten Rollen + Interaktionen" (WS2425, Übung).
Zentraler **Manager** (Controlling/Projektleitung) koordiniert: **Kunde** (Anforderungen/Qualitäten ↔ Termine/Kosten/Produkt), **Marketing** (Marktanforderungen/Geschäftsziele), **SW-Entwicklung** (Planung/Status), **Qualitätssicherung** (Status).

## 12. Betriebsphase & Wartung
*Gefragt als:* „Prozentualer Anteil an Gesamtkosten + Erläuterung" (WS2526).
- **~80 % der Gesamtkosten** entfallen auf den Betrieb (längste Phase).
- **Wartungsarten:** **korrektiv** (Fehlerbehebung), **adaptiv** (Anpassung an neue Rahmenbedingungen), **perfektiv** (Verbesserung bestehender Funktionen), **präventiv** (Verbesserung der Wartbarkeit).

---

# TEIL B – Große Theoriethemen aus Skript 01, die NOCH NIE gefragt wurden ⭐

*(Der Prof wiederholt selten – diese sind heiße Kandidaten.)*

## B1. Softwarekrise & CHAOS-Report ⭐ (stärkster Kandidat)
Foundational, mit konkreten Zahlen – ideal für „Nennen/Erläutern Sie".
- Begriff **„Software Engineering" 1968 auf der NATO-Konferenz in Garmisch-Partenkirchen** geprägt (Reaktion auf die „Softwarekrise": Projekte zu teuer, zu spät, mangelhafte Qualität).
- **CHAOS-Report (Standish Group)** – typische Projektergebnisse:
  - Erfolgreich: **ca. 30–35 %**
  - Herausgefordert (mit Abweichungen): **ca. 45–50 %**
  - Gescheitert (abgebrochen): **ca. 15–20 %**
- Erkenntnis: **kleinere, agil geführte Projekte** haben deutlich höhere Erfolgsquoten als große, klassisch geplante.

## B2. Brooks'sches Gesetz (1975) ⭐
Nur indirekt in der Übung vorgekommen – als direkte Frage offen.
- Zitat: **„Adding manpower to a late software project makes it later."** (F. Brooks, *The Mythical Man-Month*).
- Gründe: **Einarbeitungszeit** (Neue binden erfahrene Kollegen), **Kommunikationsaufwand** wächst mit **n·(n-1)/2** Kanälen (5 Pers. = 10, 50 Pers. = 1.225!), **nicht alle Aufgaben parallelisierbar**.

## B3. Die 1-10-100-Regel (Kosten späterer Fehlererkennung) ⭐
- Je später ein Fehler entdeckt wird, desto teurer die Behebung:
  Anforderungsanalyse **1×** → Design 3–10× → Implementierung 10–50× → Systemtest 30–100× → **nach Auslieferung 100–1000×**.
- Kernbotschaft: **Sorgfalt in frühen Phasen zahlt sich massiv aus** (Fehler in der Analysephase sind die teuersten).

## B4. Einführungsstrategien / Rollout ⭐
Klar abgrenzbare, vergleichbare Begriffe – typischer „Nennen + Risiko"-Stoff.
| Strategie | Beschreibung | Risiko |
|---|---|---|
| **Big Bang** | komplette Umstellung zum Stichtag | hoch (kein Fallback) |
| **Stufenweise** | schrittweise (z.B. Region für Region) | mittel (komplexere Koordination) |
| **Parallelbetrieb** | altes + neues System gleichzeitig | niedrig (doppelte Betriebskosten) |
| **Pilotbetrieb** | ausgewählte Anwender zuerst | niedrig (begrenzte Aussagekraft) |

## B5. Weitere bisher ungefragte Themen (kleinere Kandidaten)
- **Teststufen & Testpyramide** (Unit → Integration → System → Abnahme → Regression; „viele schnelle Unit-Tests unten"). *(Teilweise in SS24 gefragt.)*
- **Softwarearchitektur – Architekturstile** (Analogie Baukunst; Stil = Abstraktion, Rahmen für Entwurfsentscheidungen, legt Qualitätseigenschaften fest).
- **arc42-Template** (12 Abschnitte zur Architekturdokumentation: Introduction & Goals, Constraints, Context, Solution Strategy, Building Block View, Runtime View, Deployment View, Crosscutting Concepts, Architectural Decisions, Quality Requirements, Risks & Technical Debt, Glossary).
- **Make-or-Buy** (Standard-SW vs. Eigenentwicklung: Kosten, Time-to-Market, Anpassbarkeit, Vendor Lock-in, Differenzierung). Faustregel: Standardprozesse → Buy; differenzierende Prozesse → Make.
- **Häufige Fehler in IT-Projekten + Gegenmaßnahmen** (unklare Anforderungen → agil/Feedback; unrealistische Zeitpläne → Bottom-Up + Puffer; Scope Creep → Change Management; unzureichendes Testen → CI/CD).
- **Spektakuläre Fehlschläge** (Ariane-5, Boeing 737 MAX/MCAS, Lidl/SAP „Elwis", BER) – meist als Kontext/Einstieg.

---

## Prognose fürs Lernen
Wenn eine **neue** Theoriefrage kommt, sind **Softwarekrise/CHAOS-Report**, **Einführungsstrategien**, **Brooks'sches Gesetz** und die **1-10-100-Regel** die wahrscheinlichsten – die solltest du zusätzlich zu den „Klassikern" (magisches Dreieck, 4+1, Lasten-/Pflichtenheft, Phasen, Scrum) sicher können.
