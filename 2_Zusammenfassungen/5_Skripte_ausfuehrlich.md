# Programmierung 2 – Vollständige Lern-Zusammenfassung

> Erstellt ausschließlich aus den sechs Vorlesungsskripten (Ordner `01_-_Skript`) von Prof. Dr. Andreas Biesdorf, Hochschule Trier.
> Ziel: Diese Zusammenfassung enthält alle prüfungsrelevanten Inhalte der Skripte – du kannst damit lernen, ohne die Foliensätze zu öffnen.

## Inhaltsverzeichnis
0. [Code selbst reproduzieren – universelle Muster](#0-code-selbst-reproduzieren--universelle-muster)
1. [Software Engineering](#1-software-engineering)
2. [Testen und Debuggen](#2-testen-und-debuggen)
3. [Argumente und Kommandozeilenbefehle](#3-argumente-und-kommandozeilenbefehle)
4. [Datei-Handling und IO](#4-datei-handling-und-io)
5. [Datenstrukturen](#5-datenstrukturen)
6. [Sortierverfahren](#6-sortierverfahren)

> **Hinweis zur Nutzung:** Bei den Code-Kapiteln (5 und 6) steht jeweils ein **🔧 Bauplan** (in welcher Reihenfolge du den Code aus dem Kopf aufschreibst), der **Code** und **⚠️ Stolperfallen** (die typischen Fehler). Ziel: Du kannst jeden Algorithmus **frei reproduzieren**, nicht nur wiedererkennen. Lerne zuerst die **fünf Muster in Kapitel 0** – fast jeder Code der Vorlesung ist eine Kombination daraus.

---

# 0. Code selbst reproduzieren – universelle Muster

Fast der gesamte Klausur-Code ist aus **fünf wiederkehrenden Bausteinen** zusammengesetzt. Wenn du diese Muster beherrschst, musst du dir die einzelnen Funktionen nicht auswendig merken – du **leitest sie ab**.

### Muster A – Tausch zweier Werte (Swap)
In Python **ohne** Hilfsvariable:
```python
a, b = b, a                       # vertauscht a und b
liste[i], liste[j] = liste[j], liste[i]   # vertauscht zwei Listenelemente
```
Kommt in **jedem** In-place-Sortierverfahren vor (Bubble, Selection, Heapsort).

### Muster B – Öffentliche Methode + private Rekursions-Hilfsmethode
Klassen mit Bäumen/Listen folgen fast immer diesem Aufbau: eine **öffentliche** Methode fängt den Sonderfall „leer" ab und startet dann eine **private** rekursive Hilfsmethode (`_name`), die einen Knoten als Parameter bekommt.
```python
def operation(self, wert):            # ÖFFENTLICH: Sonderfall + Start
    if self.wurzel is None:
        # Sonderfall behandeln (z.B. Wurzel neu setzen)
        ...
    else:
        self._operation_rekursiv(self.wurzel, wert)

def _operation_rekursiv(self, knoten, wert):   # PRIVAT: eigentliche Rekursion
    ...
```
> Merksatz: **„Öffentlich prüft die Wurzel, privat macht die Rekursion."** Gilt für BST-`insert`, Baum-Ausgabe, Trie usw.

### Muster C – Rekursion (immer gleiche 2 Bestandteile)
Jede Rekursion braucht:
1. **Basisfall** (Abbruchbedingung) – wann hört es auf? (leere Liste/`None`-Knoten/Länge ≤ 1)
2. **Rekursiver Fall** – Problem verkleinern und sich selbst aufrufen.
```python
def f(daten):
    if <basisfall>:          # 1. Abbruch
        return <trivialwert>
    ...                      # 2. verkleinern + f(...) erneut aufrufen
```
Prüfe beim Reproduzieren immer: **Habe ich einen Basisfall? Wird das Problem kleiner?** (sonst Endlosschleife).

### Muster D – Liste linear durchlaufen (mit Zeiger `current`)
Für verkettete Listen: mit einer Laufvariable `current` von Element zu Element hangeln, bis `None`.
```python
current = self.head
while current:                # bis zum Ende
    ...                       # etwas mit current.data tun
    current = current.next    # einen Schritt weiter
```

### Muster E – Zwei-Zeiger-Verschmelzen (Merge)
Zwei bereits sortierte Listen mit zwei Indizes `i`, `j` gleichzeitig durchlaufen, jeweils das kleinere Element übernehmen, am Ende den Rest anhängen. (Kern von Mergesort.)
```python
i = j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i]); i += 1
    else:
        result.append(b[j]); j += 1
result.extend(a[i:]); result.extend(b[j:])   # Rest anhängen
```

### Das musst du dir merken (Kapitel 0)
- **Swap:** `x, y = y, x` – keine Hilfsvariable nötig.
- **Klassen-Muster:** öffentliche Methode prüft Wurzel/Sonderfall → private `_rekursiv`-Methode macht die Arbeit.
- **Rekursion = Basisfall + kleiner werdender Selbstaufruf.**
- **Listen-Durchlauf:** `while current: … current = current.next`.
- **Merge:** zwei Zeiger, kleineres zuerst, Rest anhängen.

---

# 1. Software Engineering

## 1.1 Warum Software Engineering? (Motivation)

**Kernaussage:** Programmierung allein reicht nicht aus. Sobald ein Projekt über ein einfaches Skript hinausgeht, werden **Planung, Struktur und systematisches Vorgehen** unverzichtbar. Als Wirtschaftsinformatiker bildet man später die **Brücke zwischen Fachbereich und IT**.

**Gedankenexperiment** (typisches Softwareprojekt): 15 Mio. € Entwicklungsaufwand, 500 Mio. € geplanter Umsatz, 10 Jahre Wartung. Die zu lösenden Probleme betreffen nicht nur die Entwicklung (System in handhabbare Teile zerlegen), sondern auch **Management** (Termine, Budget), **Qualität** (Doku für 10 Jahre Wartung) und **Stakeholder** (Kundenwünsche korrekt erfassen).

### Gründe für den Einsatz von Software Engineering
| Herausforderung | Beitrag des Software Engineerings |
|---|---|
| Komplexität | Strukturierung, Modularisierung, Abstraktion |
| Funktion | Systematisches Erfassen der Stakeholder-Wünsche |
| Qualität | Sicherheit, Robustheit, Testbarkeit |
| Wartung | Dokumentation, langfristige Pflegbarkeit |
| Planung | Termine, Kosten, Personal, Risikomanagement |
| Organisation | Teamgröße, Standortverteilung, Zeitzonenmanagement |
| Methodik | Arbeitstechniken, Prozesse, Standards, Best Practices |

> Die Erstellung großer Softwaresysteme in hoher Qualität erfordert den systematischen Einsatz von **Modellen, Methoden und Techniken** → ein strukturiertes Software Engineering.

## 1.2 Softwarekrise und historische Fehlschläge

- Der Begriff **„Software Engineering"** wurde **1968 auf der NATO-Konferenz in Garmisch-Partenkirchen** geprägt.
- **CHAOS Report (Standish Group)** – typische Projektergebnisse:

| Projektergebnis | Anteil |
|---|---|
| Erfolgreich | ca. 30–35 % |
| Herausgefordert (Abweichungen) | ca. 45–50 % |
| Gescheitert (Abgebrochen) | ca. 15–20 % |

  *Erkenntnis:* Kleinere, **agil** geführte Projekte haben deutlich höhere Erfolgsquoten als große, klassisch geplante Vorhaben.

**Spektakuläre Fehlschläge** (zeigen: SE ist wirtschaftliche/gesellschaftliche Notwendigkeit):
| Projekt | Problem | Folgen |
|---|---|---|
| Ariane-5 (1996) | 64-Bit-Überlauf in 16-Bit-Integer | Explosion, ~370 Mio. USD |
| Healthcare.gov (2013) | Mangelhaftes Projektmanagement | Wochen Nicht-Verfügbarkeit |
| Boeing 737 MAX (2018) | Software-Designfehler MCAS | 346 Tote, Milliarden-Verluste |
| Lidl/SAP Elwis (2018) | Fehlende Strategie, zu viele Anpassungen | über 500 Mio. €, Abbruch |
| BER Flughafen | IT-Steuerungssysteme mangelhaft | Jahre Verzögerung, Milliarden Mehrkosten |

### Brooks'sches Gesetz (1975)
> „**Adding manpower to a late software project makes it later.**" – Frederick Brooks, *The Mythical Man-Month*

Begründung:
- **Einarbeitungszeit:** Neue Teammitglieder binden erfahrene Kollegen.
- **Kommunikationsaufwand:** wächst mit `n × (n-1) / 2` Kanälen (5 Personen = 10 Kanäle, 50 Personen = 1.225 Kanäle!).
- **Aufteilungsgrenzen:** Nicht alle Aufgaben sind parallelisierbar.

## 1.3 Definition und Grundkonzepte

**Definition nach Balzert:**
> „Zielorientierte Bereitstellung und systematische Verwendung von Prinzipien, Methoden und Werkzeugen für die arbeitsteilige, ingenieurmäßige Entwicklung und Anwendung von umfangreichen Software-Systemen."

Die fünf Bestandteile der Definition:
- **Zielorientiert:** Jede Aktivität dient einem konkreten Projektziel.
- **Systematisch:** Nach definierten Methoden, nicht ad hoc.
- **Arbeitsteilig:** Team-Koordination und Kommunikation.
- **Ingenieurmäßig:** Wiederholbar, messbar, dokumentiert.
- **Umfangreiche Systeme:** Zu komplex für einen einzelnen Entwickler.

### Das magische Dreieck des Projektmanagements
Die drei Dimensionen **Zeit – Kosten – Qualität** stehen im Spannungsverhältnis. **Die Veränderung einer Dimension hat unweigerlich Auswirkungen auf die anderen** (z. B. Zeit verkürzen → Kosten steigen oder Qualität sinkt).

## 1.4 Softwarequalität

Qualitätsmerkmale werden aus zwei Perspektiven betrachtet.

### Qualitätsmerkmale aus Benutzersicht
| Qualitätsmerkmal | Beschreibung | Beispiel |
|---|---|---|
| Funktionserfüllung | Geplanter Funktionsumfang realisiert | Alle Lastenheft-Funktionen verfügbar |
| Zuverlässigkeit | Stabil bei Fehlern/Ausfällen | Kein Datenverlust bei Netzwerkausfall |
| Effizienz | Schnell, ressourcenschonend | Suchergebnisse in < 2 Sekunden |
| Benutzbarkeit | Intuitiv, geringe Einarbeitung | Neue Mitarbeiter nach 1 Tag produktiv |
| Sicherheit | Schutz vor unberechtigtem Zugriff | Verschlüsselung, Zugriffskontrollen |

*(Untergliederungen laut Skript: Effizienz → HW-Effizienz + SW-Effizienz/Performance; Benutzbarkeit → Robustheit + Fehlertoleranz.)*

### Qualitätsmerkmale aus Entwicklersicht
| Qualitätsmerkmal | Beschreibung | Messgröße |
|---|---|---|
| Wartbarkeit | Übersichtlicher Code, gute Doku | Zyklomatische Komplexität |
| Änderbarkeit | Neue Anforderungen umsetzbar | Durchschn. Dauer Änderungsanforderung |
| Übertragbarkeit | Portierbar auf andere Plattformen | Anteil plattformabhängigen Codes |
| Testbarkeit | Isoliert testbare Komponenten | Testabdeckung, Anzahl Unit Tests |
| Wiederverwendbarkeit | In anderen Projekten einsetzbar | Anzahl generischer Module |

*(Weitere im Baumdiagramm genannte Entwickler-Merkmale: Erweiterbarkeit → Änderbarkeit; Wartbarkeit → Verständlichkeit + Testbarkeit.)*

### Abhängigkeiten (Zielkonflikte) zwischen Qualitätsmerkmalen
| Verbesserung von… | wirkt negativ auf… | Warum? |
|---|---|---|
| Effizienz | Wartbarkeit, Portabilität | Hardwarenahe Optimierungen schwer lesbar |
| Sicherheit | Benutzbarkeit, Effizienz | Zusätzliche Verschlüsselung verlangsamt |
| Flexibilität | Einfachheit, Effizienz | Generische Lösungen komplexer |
| Robustheit | Effizienz | Fehlerbehandlung kostet Rechenzeit |

> Die Festlegung der geforderten **Qualitätseigenschaften** ist genauso wichtig wie die Festlegung der **Funktionalität**.

## 1.5 Phasen der Softwareentwicklung

### Die 1-10-100-Regel (Kosten späterer Fehlererkennung)
Je später ein Fehler entdeckt wird, desto teurer seine Behebung.
| Phase der Fehlererkennung | Relative Kosten |
|---|---|
| Anforderungsanalyse | 1× (Referenz) |
| Design/Architektur | 3–10× |
| Implementierung | 10–50× |
| Systemtest | 30–100× |
| Nach Auslieferung (Betrieb) | 100–1000× |

> **Kernbotschaft:** Fehler aus der Analysephase, die erst im Betrieb gefunden werden, kosten bis zu **1000×** mehr. Sorgfältige Arbeit in frühen Phasen zahlt sich massiv aus.

### Übersicht: Phasen und ihre Ergebnisse (Artefakte)
| Phase | Ergebnis (Artefakt) | Schlüsselfrage |
|---|---|---|
| Analyse | Anforderungsdokumentation | Was will der Kunde? |
| Definition | Spezifikation, Abnahmekriterien | Was soll das System tun? |
| Architektur | Komponentenstruktur | Wie ist es aufgebaut? |
| Design | Klassen, Schnittstellen | Wie im Detail? |
| Implementierung | Code, Unit Tests | Funktioniert der Code? |
| Integration/Test | Getestetes Gesamtsystem | Funktioniert alles zusammen? |
| Abnahme | Abnahmeprotokoll | Erfüllt es die Anforderungen? |
| Einführung | Produktives System | Ist es einsatzbereit? |
| Betrieb | Wartungsdokumentation | Läuft es zuverlässig? |

**Analysephase:** Anwendungsgebiet verstehen, Ist-Ablauf aufnehmen, begreifen was der Kunde wirklich will, Schwachstellen analysieren → Ergebnis: **Anforderungsdokumentation**.
**Definitionsphase:** informelle Anforderungen → formale **Spezifikation**, beschreibt das **„Was"**, implementierungsunabhängig → Ergebnis: **Spezifikation + Abnahmekriterien**.
> Fehler in der Analysephase sind die teuersten – sie wirken sich auf alle folgenden Phasen aus.

**Architektur (Grobentwurf):** IT-Lösung auf hoher Abstraktionsebene, Systembestandteile & Schnittstellen, grundlegende Umsetzungsart → beschreibt grob das **„Wie"**.
**Design (Feinentwurf):** Lösung nah am Zielsystem (Betriebssystem, Sprache, Hardware, Design Patterns, Datenbank) → beschreibt das **„Wie" im Detail**.

### Einführungsstrategien (Rollout)
| Strategie | Beschreibung | Risiko |
|---|---|---|
| Big Bang | Komplette Umstellung zum Stichtag | Hoch – kein Fallback |
| Stufenweise | Schrittweise (z. B. Region für Region) | Mittel – komplexere Koordination |
| Parallelbetrieb | Altes + neues System gleichzeitig | Niedrig – doppelte Betriebskosten |
| Pilotbetrieb | Ausgewählte Anwender zuerst | Niedrig – begrenzte Aussagekraft |

### Betriebsphase: ~80 % der Gesamtkosten
**Etwa 80 % der Gesamtkosten** eines Softwareprojekts entfallen auf den **Betrieb (Wartung)** – die zeitlich mit Abstand längste Phase.

**Die vier Wartungsarten:**
- **Korrektiv:** Fehlerbehebung
- **Adaptiv:** Anpassung an veränderte Rahmenbedingungen
- **Perfektiv:** Verbesserung bestehender Funktionen
- **Präventiv:** Verbesserung der Wartbarkeit

### Teststufen und Testpyramide
| Teststufe | Ziel | Werkzeuge |
|---|---|---|
| Unit Test | Einzelne Funktionen/Klassen | pytest, JUnit, Jest |
| Integrationstest | Zusammenspiel Module | Testcontainers, Selenium |
| Systemtest | Gesamtsystem vs. Spezifikation | Cypress, Playwright |
| Abnahmetest | System vs. Kundenanforderungen | Manuelle Tests, UAT |
| Regressionstest | Änderungen brechen nichts | CI/CD-Pipeline |

> **Testpyramide:** Viele schnelle Unit Tests, weniger Integrationstests, wenige aufwändige E2E-Tests. Testabdeckung > 80 % ist ein guter Indikator, **garantiert aber nicht Fehlerfreiheit**.

## 1.6 Phasenmodelle

### Wasserfallmodell
- Sequenzielle Phasen (Royce, 1970): Anforderungen → Analyse → Systementwurf → Realisierung → Test → Systemintegration → Systemabnahme.
- Einfach verständlich, klare Meilensteine.
- **Geringe Flexibilität** bei Änderungen; **Fehler werden spät entdeckt**.

### V-Modell
Ordnet jeder Entwicklungsphase eine Teststufe zu:
| Entwicklung | Test |
|---|---|
| Anforderungsanalyse | Abnahmetest |
| Systemspezifikation | Systemtest |
| Architektur | Integrationstest |
| Detailentwurf | Modultest |

- **V-Modell XT:** vom deutschen Bund für IT-Projekte der öffentlichen Verwaltung vorgeschrieben. „XT" = **„Extreme Tailoring"** – erlaubt projektspezifische Anpassung.

### Scrum (agiles Vorgehensmodell)
**Agiles Manifest (2001) – Wertepaare** („Wir schätzen … mehr als …"):
| Wir schätzen… | …mehr als |
|---|---|
| Individuen und Interaktionen | Prozesse und Werkzeuge |
| Funktionierende Software | Umfassende Dokumentation |
| Zusammenarbeit mit dem Kunden | Vertragsverhandlung |
| Änderungen willkommen heißen | Befolgen eines Plans |

**Rollen:**
| Rolle | Verantwortung |
|---|---|
| Product Owner | Product Backlog, Priorisierung, Kundenvertretung |
| Scrum Master | Prozess-Coach, beseitigt Hindernisse |
| Entwicklungsteam | Selbstorganisiert, cross-funktional (3–9 Personen) |

**Artefakte:**
| Artefakt | Beschreibung |
|---|---|
| Product Backlog | Priorisierte Liste aller Anforderungen |
| Sprint Backlog | Ausgewählte Items für aktuellen Sprint |
| Produkt-Inkrement | Funktionsfähige Software am Sprint-Ende |

**Ereignisse (Events):**
| Ereignis | Dauer | Zweck |
|---|---|---|
| Sprint | 2–4 Wochen | Zeitrahmen für Inkrement-Erstellung |
| Sprint Planning | max. 8 h | Planung der Sprint-Arbeit |
| Daily Scrum | 15 Min. | Tägliche Synchronisation |
| Sprint Review | max. 4 h | Präsentation, Feedback |
| Sprint Retrospektive | max. 3 h | Reflexion, Prozessverbesserung |

*Praxis:* Oft **hybride Ansätze** (V-Modell-Rahmen + agile Sprints), **SAFe** (Scaled Agile Framework) für Großprojekte, **Kanban** als leichtgewichtige Alternative für Wartungsteams.

### Vergleich der Phasenmodelle
| Kriterium | Wasserfall | V-Modell | Scrum |
|---|---|---|---|
| Anforderungen | Stabil | Stabil | Veränderlich |
| Kundenfeedback | Spät (Abnahme) | Spät (Tests) | Früh (jeder Sprint) |
| Dokumentation | Umfangreich | Sehr umfangreich | Bedarfsgerecht |
| Flexibilität | Gering | Gering | Hoch |
| Teamgröße | Beliebig | Beliebig | Klein (3–9) |
| Risikomanagement | Reaktiv | Proaktiv | Kontinuierlich |

## 1.7 Lasten- und Pflichtenheft

Auftraggeber und Auftragnehmer sind **zwei Welten** (Auftraggeber hat ein Problem/Budget, denkt in Geschäftsprozessen; Auftragnehmer soll Lösung liefern, denkt in technischen Lösungen). **Lasten- und Pflichtenheft schaffen die gemeinsame Verständigungsbasis und bilden die vertragliche Grundlage.**

**Inhalte des Lastenheftes** (vom Auftraggeber, das „Was" und „Wozu"):
- Titel (Systemname, Datum, Autor)
- I. Zielbestimmung und Zielgruppen (Produktperspektive, Einsatzkontext)
- II. Funktionale Anforderungen (Produktfunktionen, -daten, -schnittstellen, Anwenderprofile)
- III. Nichtfunktionale Anforderungen (Qualitäts- und technische Anforderungen)
- IV. Lieferumfang
- V. Abnahmekriterien (Minimalkriterien für die Akzeptanz), Anhänge

**Inhalte des Pflichtenheftes** (vom Auftragnehmer, das „Wie"):
- Funktionale Anforderungen: konkrete Anwendungsfälle/Abläufe (evtl. Use Cases, Sequenzdiagramme), Benutzer/Akteure.
- Nicht-funktionale Anforderungen: systematische Betrachtung + Priorisierung der Qualitätseigenschaften.
- Benutzungsschnittstelle (GUI/HMI): Skizzen, Snapshots, Navigationskonzepte, Dialogführung.
- **Glossar:** zentrale Sammlung aller Definitionen; den Auftraggeber nicht mit neuen Begriffen „beglücken"; Universalausdrücke (System, Komponente …) vermeiden bzw. genau spezifizieren.
- Sonstiges (z. B. Datenmodellierung des Realweltausschnitts).

### Versteckte Anforderungen erkennen
| Information | Hinweis auf… | Beispiel |
|---|---|---|
| Einsatzort | Wartungsart | Remote-Zugang nötig |
| Benutzungsfrequenz | Performanz | 1000 gleichzeitige Nutzer |
| Folgen bei Ausfall | Robustheit | Max. 1 h Ausfallzeit |
| Anwenderprofil | Internationalisierung | 26 Länder, Mehrsprachigkeit |
| Geschäftsplanung | Erweiterbarkeit | 5 neue Länder geplant |
| Bestehende Probleme | Kritische Anforderungen | Datenverluste im Altsystem |

## 1.8 Softwarearchitektur

**Architekturstil** (Analogie: eine Kirche „gotisch" oder „romanisch" bauen – beides eine Kirche, aber andere Eigenschaften):
- ist eine **Abstraktion** von den Spezifika einer konkreten Architektur,
- liefert eine **Leitlinie** für Art der Komponenten und Beziehungen,
- gibt einen **Rahmen für Entwurfsentscheidungen**,
- legt **Qualitätseigenschaften** fest (kann Qualitätsanforderungen erleichtern oder praktisch unmöglich machen),
- In einer Architektur werden meist **mehrere** Architekturstile verwendet.

### 4+1-Sichten nach Kruchten
Vier Sichten plus die verbindende **Szenariosicht („+1")**, die die anderen vier prüft/verbindet.

| Sicht | Elemente | Inhalt | Stakeholder | UML-Umsetzung |
|---|---|---|---|---|
| **Logische Sicht** | Komponenten (Klassen), Verantwortlichkeiten, Kollaborationen | Aufteilung der Domäne, Zuständigkeiten, Funktionalität | Anwender, Analytiker, Designer, Domänenexperte | Komponenten-, Klassen-, Sequenzdiagramm |
| **Implementierungs-/Entwicklungs-Sicht** | Dateien, Repositories | Systembestandteile, Konfiguration | Designer, Entwickler, Konfigurationsmanager | Komponenten-, Zustandsdiagramm |
| **Prozess-Sicht** | Prozesse, Threads | Performanz, Skalierbarkeit, Verfügbarkeit | Designer, Tester, Deployer | Kommunikations-, Timing-, Sequenzdiagramm |
| **Physische Sicht** | Hardwareressourcen | Hardwaretopologie | Hardwareingenieur, Logistik | Verteilungs-, Kompositionsstruktur-, Komponentendiagramm |
| **Anwendungs-/Szenariosicht („+1")** | Akteure, Anwendungsfälle | Verhalten des Systems | Anwender, Analytiker, Tester | Sequenz-, Kommunikationsdiagramm |

**Merkhilfe für die typische Zuordnung von Aspekten:**
- Klassen und Objekte → **Logische Sicht**
- Akteure und Anwendungsfälle → **Anwendungs-/Szenariosicht („+1")**
- Performanz und Skalierbarkeit → **Prozess-Sicht**
- Hardware-Topologie → **Physische Sicht**
- Dateien und Repositories → **Implementierungs-/Entwicklungs-Sicht**

### arc42-Template (Architekturdokumentation)
12 Gliederungspunkte: 1. Introduction & Goals, 2. Constraints, 3. Context & Scope, 4. Solution Strategy, 5. Building Block View, 6. Runtime View, 7. Deployment View, 8. Crosscutting Concepts, 9. Architectural Decisions, 10. Quality Requirements, 11. Risks & Technical Debt, 12. Glossary („ubiquitous language").

## 1.9 Make-or-Buy und häufige Projektfehler

### Make-or-Buy: Standard-SW vs. Eigenentwicklung
| Kriterium | Buy (Standard-SW) | Make (Eigenentwicklung) |
|---|---|---|
| Kosten initial | Lizenz + Implementierung | Entwicklung + Personal |
| Time-to-Market | Schneller (wenn Standard passt) | Langsamer, aber flexibler |
| Anpassbarkeit | Begrenzt, oft teuer | Unbegrenzt, eigene Verantwortung |
| Risiko | Vendor Lock-in | Abhängig vom eigenen Know-how |
| Differenzierung | Gleiche SW wie Wettbewerber | Wettbewerbsvorteil möglich |

> **Faustregel:** Standardprozesse (Finanzbuchhaltung, HR) → Standard-SW. Differenzierende Geschäftsprozesse (z. B. Warenwirtschaft bei Discounter) → Eigenentwicklung oder gezielte Anpassung.

### Häufige Fehler in IT-Projekten
| Fehler | Gegenmaßnahme |
|---|---|
| Unklare Anforderungen | Agile Methoden, regelmäßiges Feedback |
| Unrealistische Zeitpläne | Bottom-Up-Schätzung, Puffer einplanen |
| Mangelnde Stakeholder-Einbindung | Sprint Reviews, regelmäßige Demos |
| Fehlende Architektur | Frühzeitige Workshops, Prototypen |
| Unzureichendes Testen | Testautomatisierung, CI/CD |
| Scope Creep | Change Management, Product Backlog |
| Überschätzung Standard-SW | Proof of Concept vor Kauf |
| Ignorieren techn. Schulden | Regelmäßiges Refactoring, Code Reviews |

### Das musst du dir merken (Kapitel 1)
- **~80 % der Gesamtkosten = Betrieb/Wartung**; 4 Wartungsarten: korrektiv, adaptiv, perfektiv, präventiv.
- **1-10-100-Regel:** späte Fehler kosten bis 1000× mehr; Fehler in der Analysephase sind die teuersten.
- **Kruchten 4+1:** Logisch (Klassen), Prozess (Performanz/Skalierbarkeit), Physisch (Hardware), Implementierung (Dateien/Repositories), Szenario „+1" (Akteure/Use Cases).
- **Phasenmodelle:** Wasserfall (sequenziell, unflexibel), V-Modell (Phase↔Teststufe, XT = Extreme Tailoring), Scrum (agil, veränderliche Anforderungen).
- **Scrum:** 3 Rollen (Product Owner, Scrum Master, Entwicklungsteam), 3 Artefakte (Product/Sprint Backlog, Inkrement), Events (Sprint, Planning, Daily, Review, Retrospektive).
- **Lastenheft = „Was" (Auftraggeber), Pflichtenheft = „Wie" (Auftragnehmer).**
- **Magisches Dreieck:** Zeit–Kosten–Qualität, Änderung einer Dimension beeinflusst die anderen.

---

# 2. Testen und Debuggen

## 2.1 Drei Grundbegriffe (Analogie „Brot machen")
Während man ein Brot zubereitet, krabbeln Insekten auf den Teller:
- **Testen:** *Prüfen*, ob wieder ein Insekt auf dem Brot ist.
- **Defensive Programmierung:** *Schützen* der Lebensmittel, damit kein Insekt herankommt.
- **Debugging:** *Grundreinigung* der Küche, um die **Ursache** zu eliminieren.

### Defensive Programmierung vs. Testen vs. Debugging
- **Defensive Programmierung:** Formulieren **klarer Spezifikationen** für Funktionen; systematische **Modularisierung**; Prüfung von **Bedingungen (Conditions)** bzgl. Inputs/Outputs (**Assertions**).
- **Testen:** Input/Output auf Basis der **Spezifikation** vergleichen; systematisch **Test Cases** erzeugen und prüfen.
- **Debuggen:** **Analyse der Events**, die zu einem Fehler führen; **verstehen, warum** ein Programm nicht korrekt funktioniert.

## 2.2 Clean Code & Startbedingungen des Testens

**Clean Code – Vorbereitungen für einfaches Testen:**
- Code **von Anfang an** mit dem Ziel entwickeln, strukturiert zu testen.
- Code in **mehrere Module** aufbrechen (Funktionen/Klassen), die individuelles Testen/Debuggen erlauben.
- **Randbedingungen** explizit dokumentieren (Wie sieht Input/Output aus?) via **Docstring**.
- **Annahmen** und **Lösungsansätze** (welche Lösungsmuster?) dokumentieren.

**Startbedingungen fürs Testen:**
- Der Code **„läuft"** (Syntaxfehler eliminiert, statische Semantik-Fehler entfernt).
- **Zu erwartende Ergebnisse sind bekannt** (Input-Daten verfügbar, für jeden Input-Datensatz ist das erwartete Ergebnis bekannt).

## 2.3 Testpyramide
- **Unit Tests:** Testen einzelner Funktionen und Module.
- **Integrationstests:** Prüfen, dass das **gesamte** Programm funktioniert.
- **Regressionstests:** Sicherstellen, dass **keine neuen Fehler** durch Weiterentwicklung entstanden sind.

## 2.4 Testansätze
| Ansatz | Idee |
|---|---|
| **Intuitives Testen** | Basiert auf Wissen über frühere Fehlerwirkungen / allgemeinem Wissen (Beispiel: natürliche Partitionen). |
| **Zufallsbasiertes Testen** | Wenn keine Partitionen bildbar sind, werden zufällige Werte zum Testen verwendet. |
| **Black-Box Testen** | Exploration des Pfads **auf Basis der Spezifikation**. |
| **White-Box Testen** | Exploration des Programmpfads **durch den Code**. |

### Black-Box Testen
- Entwurf von Tests, **ohne den Code zu inspizieren** (Tester ≠ Entwickler; die Interna sind irrelevant).
- Idee: Ableitung von Tests **auf Basis der Spezifikation**:
  - Suche nach **natürlichen Partitionen** (Äquivalenzklassen).
  - Testen von **Randbedingungen** (leere Listen, sehr große Zahlen, sehr kleine Zahlen, negative Zahlen).

**Beispiel (Äquivalenzklassen für `sqrt(x, epsilon)`):** Randwert (x=0), perfekte Wurzel (x=25), Wert < 1.0, sowie diverse **Extremwerte** (sehr kleine/große x und epsilon, z. B. `1.0/2.0**64.0` und `2.0**64.0`).

**Nützliche Übungs-Partitionen (Black-Box):**
- Für `size(aSet)`: leeres Set, Set der Länge 1, ungerade Länge, gerade Länge, Länge > 1, Primzahl-Länge.
- Für `union(set1, set2)`: beide leer; eins leer/eins gefüllt (beide Richtungen); beide gefüllt ohne Duplikate; beide gefüllt mit gemeinsamen Objekten. Bei Listen zusätzlich: **Reihenfolge/Duplikate** beachten.

### White-Box Testen
- **Direkte Prüfung** des Codes.
- **„Path-complete"**: wenn **jeder mögliche Pfad im Code mindestens einmal** geprüft wird.
- **Nachteil:** Aufwand/Komplexität der Tests; Gefahr, wichtige Pfade zu übersehen.
- **Empfehlungen zur Testkonstruktion:**
  - **Verzweigungen:** alle Bedingungen prüfen (jeden Zweig).
  - **For-Schleifen:** Schleife gar nicht / genau einmal / mehrfach durchlaufen.
  - **While-Schleifen:** analog zur For-Schleife; zusätzlich **alle Wege, die Schleife zu verlassen**, testen.
  - **Rekursion:** (1) **Basisfall**, (2) **einmal rekursiv**, (3) **mehrmals rekursiv**.

> **Achtung:** „Path-complete" allein genügt manchmal nicht, um Fehler zu finden – zusätzlich müssen **Randwerte** getestet werden (Beispiel `my_abs` mit `if x < -1:` – der Grenzwert x = -1 offenbart erst den Fehler).

**White-Box-Übung (rekursives `union`):** Die beste Test Suite deckt **sowohl alle Pfade als auch die verschiedenen Rekursionstiefen (0/1/n)** ab.

## 2.5 Bugs und Debugging

**Drei Schritte zum Handling von Bugs:**
1. **Isolation**
2. **Korrektur**
3. **Regressions-Tests**, bis das Programm das korrekte Verhalten zeigt.

*(Historie: Admiral Grace Murray Hopper; der erste dokumentierte „Bug" war 1947 eine Motte im Relais des Mark II Aiken Relay Computers.)*

### Typen von Laufzeitfehlern
Zwei Dimensionen kombiniert:
| | **Offen** (klare Ursache) | **Verborgen** (keine klare Ursache) |
|---|---|---|
| **Persistent** (stabil reproduzierbar) | Leicht zu entdecken; defensive Programmierung hilft | Sehr problematisch – fallen oft erst nach langer Laufzeit auf |
| **Intermittierend** (tritt nur manchmal auf, selbst bei identischem Input) | Schwieriger als persistente Fehler; Ursache durch systematisches Testen isolieren | Albtraum eines jeden Programmierers |

### Debugging-Werkzeuge und -Systematik
- **Tools:** Debugger in der IDE; `print`-Statements (Eingang in Funktion, Parameter, Ergebnisse).
- **Systematik:** analog zu Tests in der Mathematik; **Teile und Herrsche** – Problem strukturiert zerlegen.

### Typische Exceptions (einfach zu korrigieren)
| Code | Exception |
|---|---|
| `test = [1,2,3]; test[4]` (Zugriff jenseits der Größe) | `IndexError` |
| `int(test)` (Konvertierung inkompatibler Typen) | `TypeError` |
| `a` (Referenz nicht existierender Variablen) | `NameError` |
| `'3'/4` (Vermischung von Datentypen) | `TypeError` |
| `a = len([1,2,3]` + `print a` (Klammern/Syntax) | `SyntaxError` |

### Logische Fehler (schwer zu korrigieren)
Empfehlungen: (1) Erst überlegen, dann implementieren; (2) konzeptuelles Design visuell erstellen; (3) Code erklären / Code Review.
**Debugging-Ansatz:** Aufbau eines **wiederholbaren Experiments**; Ziel: möglichst **einfache Reproduktion** des Fehlers.

**Debugging als Suchproblem:**
- Analyse verfügbarer Daten – **sowohl „korrekte" als auch „inkorrekte" Test-Cases**.
- Formulierung einer **Hypothese**.
- Design/Implementierung eines wiederholbaren **Experiments** zur Prüfung.
- **Dokumentation** der Tests.
- Systematische **Reduktion** möglicher Fehlerquellen.
- Tests, die auch **Zwischenergebnisse** sichtbar machen.

**Pragmatische Hinweise:** Nach Standard-Fehlern suchen; fragen, **warum der Code tut, was er tut** (nicht, warum er nicht tut, was man will); Fehler ist oft nicht dort, wo man ihn vermutet; Code einer anderen Person erklären; **der Dokumentation nicht blind trauen**.

## 2.6 Assertions (defensive Programmierung)
- Weiteres Stilmittel des **defensiven Programmierens**.
- Sichern zu, dass der **Vertrag** beim Aufruf einer Funktion eingehalten wird.
- Eine Verletzung des Assert-Statements wirft eine **`AssertionError`**-Exception (→ **sofortige Terminierung** der Funktion).

```python
def avg(grades):
    assert not len(grades) == 0, 'no grades data'   # prüft Vorbedingung
    return sum(grades) / len(grades)
```

**Einsatz von Assertions:** üblicherweise zur **Prüfung der Eingaben** – kritische Funktionen sollten immer mit Assertions starten:
- Prüfung des **Typs** von Argumenten/Werten.
- Prüfung von **Violations** (z. B. Duplikate in einer Liste).
- Prüfung von **Constraints** bzgl. Rückgaben.
- Prinzipiell auch zur Prüfung von **Ergebnissen** nutzbar.
- Hilft, **Fehlerquellen zu reduzieren** bzw. Fehler einzugrenzen.

## 2.7 pytest (Kombination Testen + Ausnahmen + Asserts)
- **`pytest`** ist das Standard-Unit-Test-Framework in Python; gut mit git/GitHub integrierbar.
- **Notwendige Strukturen:**
  - Leere Datei **`__init__.py`** im Ordner anlegen.
  - **`src`- und `test`-Ordner trennen.**
  - `pytest` aufrufen.

```python
"""Test uebungsblatt03_03.py"""
from Uebungsblatt_03.src import uebungsblatt03_05

def test_foo():
    """Test cases für rekursive Addition"""
    assert uebungsblatt03_05.foo(10, 3) == 3
    assert uebungsblatt03_05.foo(1, 4) == 0
    assert uebungsblatt03_05.foo(10, 6) == 1
```
Testfunktionen beginnen mit `test_`, prüfen mit `assert`.

### Das musst du dir merken (Kapitel 2)
- **Testen** = Ist/Soll gegen Spezifikation; **Debuggen** = Ursache verstehen; **Defensive Programmierung** = Spezifikationen/Modularisierung/Assertions.
- **Black-Box:** natürliche Partitionen + Randbedingungen, **ohne** Codekenntnis, aus der Spezifikation.
- **White-Box:** „Path-complete", jede Verzweigung, Schleifen **0/1/mehrfach**, Rekursion **Basisfall/1×/mehrfach**. Path-complete allein reicht nicht → **Randwerte** testen.
- **Bugs:** Isolation → Korrektur → Regressionstests.
- **Fehlertypen:** offen/verborgen × persistent/intermittierend (verborgen+intermittierend am schlimmsten).
- **Assertions** werfen `AssertionError`, prüfen den **Vertrag** (Typ, Violations, Constraints) und terminieren sofort.
- **pytest:** `__init__.py`, `src`/`test` trennen, Testfunktionen `test_*` mit `assert`.

---

# 3. Argumente und Kommandozeilenbefehle

## 3.1 Motivation
Programme bisher: Eingabe per `input()`, Ausgabe per `print()`.
**Nachteile:**
- `input()`: Schwierigkeiten bei **großen Datenmengen** (Bilder, Log-Files); **blockierend** bei Skripten.
- `print()`: nur **einmalige Ausgabe** auf der Kommandozeile; „**Piping**" in Datei möglich, aber umständlich.

→ Lösung: **Argumente/Kommandozeilenbefehle** und **Datei-Handling**.

## 3.2 Argumente – einfacher Fall (`sys`-Modul)
Argumente werden durch **Leerzeichen getrennt** an den Python-Interpreter übergeben und im Code über **`sys.argv`** ausgewertet.

```python
import sys

if len(sys.argv) > 1:
    for arg in range(len(sys.argv)):
        print('Argument ' + str(arg) + ':', sys.argv[arg])
else:
    print('Keine Argumente angegeben')
```
`sys.argv[0]` ist der Skriptname, ab `sys.argv[1]` folgen die übergebenen Argumente (als Strings).

**Nachteile des einfachen Falls:**
- Reihenfolge der Argumente nicht immer gleich.
- Lang-/Kurzversionen von Argumenten gewünscht.
- **Manuelles Parsing** ist sehr fehleranfällig.
- Schwierig in Integrations-Tests einzubinden.

→ **Wunsch:** Systematische Angabe von Parametern in Lang-/Kurzversionen und in beliebiger Reihenfolge, z. B. `python test.py -l de -t g -name Andreas`.

## 3.3 Flags
- Ein **Flag** ist ein speziell ausgezeichnetes Argument.
- **Kurzes Flag** beginnt mit `-`, **langes Flag** mit `--`:
  ```
  python test.py -f ./dateiname.txt
  python test.py --filename ./dateiname.txt
  ```
- Fehlt ein Flag, wird der **Standardwert** verwendet.

## 3.4 `getopt` (Parser für Kommandozeileneingaben)
`getopt.getopt(args, shortopt, longopts)`:
- **args:** zu verarbeitende Argumente, typischerweise `sys.argv[1:]`.
- **shortopt:** unterstützte kurze Varianten (String).
- **longopts:** unterstützte lange Varianten (Liste).

**Shortopts (kurze Argumente):**
- Benennt mögliche Flags, z. B. `'hab'` → `python test.py -h -a -b`.
- Erfordert ein Flag ein **Argument**, wird ein **Doppelpunkt** ergänzt: `'ha:b'` → `python test.py -h -a argument1 -b`.

**Longopts (lange Argumente):**
- Benennt Flags als Worte, z. B. `['help', 'simplex']` → `python test.py --help`.
- Erfordert ein Flag ein Argument, wird ein **Gleichheitszeichen** ergänzt: `['help', 'simplex', 'option=']` → `python test.py --simplex --option=argument1`.

**Rückgabe von `getopt`:**
- **opts:** Liste von Flags mit zugeordneten Argumenten.
- **args:** Argumente ohne Flags.

```python
import sys, getopt

args = sys.argv[1:]
inputfile = ''
outputfile = ''
try:
    opts, args = getopt.getopt(args, "hi:o:", ["infile=", "outfile="])
except getopt.GetoptError:
    print('test.py -i <inputfile> -o <outputfile>')
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print('args.py -i <inputfile> -o <outputfile>')
        sys.exit()
    elif opt in ("-i", "--infile"):
        inputfile = arg
    elif opt in ("-o", "--outfile"):
        outputfile = arg

print('Input file is "', inputfile)
print('Output file is "', outputfile)
```

## 3.5 `argparse` (aktueller Ansatz)
Modernes, komfortables Modul zum Parsen von Kommandozeilenargumenten.

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Ein kleines Beispiel")
    parser.add_argument('zahl', type=int, help="Eine ganze Zahl eingeben")   # Positionsargument
    parser.add_argument('--verbose', action='store_true', help="Mehr Details ausgeben")  # optionales Flag
    args = parser.parse_args()

    ergebnis = args.zahl ** 2
    if args.verbose:
        print(f"Das Quadrat von {args.zahl} ist {ergebnis}.")
    else:
        print(ergebnis)

if __name__ == "__main__":
    main()
```
- `ArgumentParser(description=...)` erzeugt den Parser.
- `add_argument(...)`: Positionsargumente (z. B. `'zahl'`, `type=int`) und Optionen (`--verbose`, `action='store_true'` = Boolean-Flag).
- `parse_args()` liefert ein Objekt, dessen Attribute die Werte enthalten (`args.zahl`, `args.verbose`).
- `argparse` erzeugt automatisch Hilfe (`-h`/`--help`) und Fehlermeldungen.

### Das musst du dir merken (Kapitel 3)
- `input()`/`print()` sind für große Daten/Skripte ungeeignet → Argumente + Dateien.
- **`sys.argv`**: einfachster Weg, Argumente (Strings, durch Leerzeichen getrennt) zu lesen; `argv[0]` = Skriptname; manuelles Parsing fehleranfällig.
- **Flag:** kurz `-x`, lang `--xyz`; fehlt es → Standardwert.
- **`getopt`:** `shortopt` als String (`:` = Argument erforderlich), `longopts` als Liste (`=` = Argument erforderlich); Rückgabe `opts` (Flags+Argumente) und `args` (Rest).
- **`argparse`:** moderner Standard mit `ArgumentParser`, `add_argument`, `parse_args`; `action='store_true'` für Boolean-Flags; automatische Hilfe.

---

# 4. Datei-Handling und IO

## 4.1 Rechte auf Dateien (Unix/Bash)
Drei Rechte: **Lesen (r)**, **Schreiben (w)**, **Ausführen (x)**.
- Rechte **überprüfen:** Befehl `ls`.
- Rechte **ändern:** Befehl `chmod`.
- Gruppen eines Nutzers **anzeigen:** Befehl `id`.

Die Rechte werden für drei Gruppen angezeigt (`ls -l`, 9 Zeichen), ein führendes `d` markiert ein Verzeichnis:
| | Eigentümer | Gruppe | Sonstige/Public |
|---|---|---|---|
| Leserecht (r) | r | r | r |
| Schreibrecht (w) | w | w | w |
| Ausführungsrecht (x) | x | x | x |

### Der Befehl `chmod`
| Zeichen | Bedeutung |
|---|---|
| `u` | user (Nutzer) |
| `g` | group (Gruppe) |
| `o` | other (andere) |
| `a` | all (alle) |
| `r` | read (lesen) |
| `w` | write (schreiben und löschen) |
| `x` | execute (ausführen bzw. bei Verzeichnissen: zugreifen) |
| `+` | Recht hinzufügen |
| `-` | Recht entfernen |

Beispiele:
```bash
chmod a+rw test.txt   # Lese- und Schreibrechte für alle hinzufügen
chmod a-rw test.txt   # diese Rechte für alle entfernen
```

**Wichtig bei Verzeichnissen:** Das **x-Recht auf einem Ordner** bedeutet „zugreifen/betreten". Ohne r-Recht am Ordner kann man dessen Inhalt nicht auflisten; ohne x-Recht kann man nicht auf enthaltene Dateien/Unterordner durchgreifen (relevant für die Übungen zu `testfolder`).

## 4.2 Nützliche Bash-Befehle
| Befehl | Bedeutung |
|---|---|
| `cd` | Change Directory – Arbeitsverzeichnis wechseln |
| `ls` | List – Verzeichnisinhalt anzeigen |
| `pwd` | Print Working Directory – aktuellen Pfad ausgeben |
| `mkdir` | Make Directory – neues Verzeichnis erstellen |
| `rm` | Remove – Dateien/Verzeichnisse löschen |
| `cp` | Copy – Dateien/Verzeichnisse kopieren |
| `mv` | Move – verschieben oder umbenennen |
| `touch` | neue leere Datei erstellen bzw. Änderungsdatum aktualisieren |
| `echo` | Text oder Variablen auf der Standardausgabe ausgeben |

## 4.3 Die „Shebang"
Enthält eine Datei interpretierbaren Code, kann der Interpreter als **Kommentar in der ersten Zeile** angegeben werden:
```python
#!/usr/local/bin/python3
print("hello, world!")
```
```bash
#!/bin/bash
echo "hello, world!"
```
> **Achtung:** Die Datei muss **ausführbar** sein (`+x`).

## 4.4 Dateien lesen in Python
Dateien werden mit **`open`** geöffnet. **Achtung:** Python geht vom **aktuellen Verzeichnis** aus, in dem das Programm aufgerufen wird.

```python
f = open("morgenstern.txt", "r")   # Datei zum Lesen öffnen
print(f.read())                    # gesamten Inhalt einlesen und ausgeben
f.close()                          # Datei schließen
```

**Methoden zum Lesen:**
| Methode | Bedeutung |
|---|---|
| `read()` | gesamter Inhalt |
| `read(x)` | x Zeichen der Datei |
| `readline()` | einzelne (nächste) Zeile |
| `readlines()` | Liste aller Zeilen |

Beispiel „Datei mit Zeilennummern ausgeben":
```python
f = open("morgenstern.txt", "r")
zeilennummer = 1
for zeile in f.readlines():
    print(zeilennummer, zeile, end='')
    zeilennummer += 1
f.close()
```

### Dateien sind Streams!
Sehr wichtig: Eine Datei ist ein **Stream**. `open` liefert eine **Referenz** zur Datei; jeder Lesebefehl (`read`, `readline`) liest **ab der aktuellen Position weiter** – der „Lesezeiger" wandert vorwärts.
- Ein zweites `f.read()` nach einem ersten `f.read()` liefert daher **einen leeren String** (es ist schon alles gelesen).
- `readline()` gibt jeweils die **nächste** Zeile; `read(4)` gibt die **nächsten 4 Zeichen** ab aktueller Position.
- Genau darauf zielen die Übungs-Snippets „Welche Ausgabe erzeugen folgende Snippets?": Das Ergebnis hängt von der bereits gelesenen Position ab.

## 4.5 Dateien schreiben in Python
| Methode | Bedeutung |
|---|---|
| `write()` | gesamter Text als **ein String** |
| `writelines()` | schreibt eine **Liste von Strings** |

```python
f = open("meinWitz.txt", 'w')
f.write("Treffen sich zwei Jäger.\nBeide tot.")
f.close()
```
```python
f = open("meinWitz.txt", 'w')
f.writelines(["Treffen sich zwei Jäger.", "\nBeide tot."])
f.close()
```
Zeilenumbrüche müssen selbst als `\n` gesetzt werden.

## 4.6 open-Modi
| Character | Meaning |
|---|---|
| `'r'` | open for reading (default) |
| `'w'` | open for writing, **truncating the file first** (überschreibt!) |
| `'x'` | open for exclusive creation, failing if the file already exists |
| `'a'` | open for writing, **appending** to the end of file if it exists |
| `'b'` | binary mode |
| `'t'` | text mode (default) |
| `'+'` | open for updating (reading and writing) |

> Merke: `'w'` **leert die Datei zuerst** (truncate), `'a'` **hängt an**, `'x'` schlägt fehl, wenn die Datei existiert.

## 4.7 Dateiinhalte verändern
Idee: Zeilen **auslesen**, in der Liste **verändern**, dann wieder **zurückschreiben**:
```python
f = open("meinWitz.txt", "r")
l = f.readlines()          # Liste aller Zeilen
f.close()
print(l)
l.insert(3, "tralala\n")   # neue Zeile an Index 3 einfügen
print(l)
f = open("meinWitz.txt", "w")
f.writelines(l)            # veränderte Liste zurückschreiben
f.close()
```

## 4.8 Pfad-Hilfsfunktionen: `os.path`
| Funktion | Bedeutung |
|---|---|
| `exists()` | Existiert die Datei? |
| `getsize()` | Größe der Datei (Bytes) |
| `isabs()` | Absoluter Pfad? |
| `isfile()` | Ist es eine Datei? |
| `isdir()` | Ist es ein Verzeichnis? |
| `realpath()` | absoluter Pfad |
| `split()` | trennt in (Verzeichnis, Datei) |

```python
import os.path
os.path.exists("morgenstern.txt")     # True
os.path.getsize("morgenstern.txt")    # 199
os.path.isabs("./")                   # False
os.path.isfile("morgenstern.txt")     # True
os.path.isdir("morgenstern.txt")      # False
os.path.split("./morgenstern.txt")    # ('.', 'morgenstern.txt')
```

### Das musst du dir merken (Kapitel 4)
- **Rechte:** r/w/x für Eigentümer/Gruppe/Sonstige; `ls` prüfen, `chmod` ändern (`a+rw`, `a-rw`), `id` für Gruppen. Bei Ordnern = x zum „Betreten", r zum „Auflisten".
- **Shebang** `#!/…` in Zeile 1 gibt den Interpreter an; Datei muss `+x` sein.
- **Lesen:** `read()` (alles), `read(x)` (x Zeichen), `readline()` (nächste Zeile), `readlines()` (Liste). **Dateien sind Streams** – der Lesezeiger wandert; ein zweites `read()` gibt "".
- **Schreiben:** `write()` (ein String), `writelines()` (Liste). Immer `f.close()`.
- **open-Modi:** `r` lesen, `w` **überschreiben (truncate)**, `a` anhängen, `x` exklusiv erstellen, `b`/`t` binär/text, `+` lesen+schreiben.
- **Ändern:** readlines → Liste bearbeiten → writelines. `os.path` für Existenz/Größe/Typ/Pfad.

---

# 5. Datenstrukturen

## 5.1 Grundlagen
- **Algorithmen** manipulieren **dynamische Mengen von Elementen** (Suchen, Einfügen, Löschen, Min/Max finden, kleiner/größer als …).
- **Datenstrukturen** repräsentieren diese Mengen; verschiedene Strukturen haben **unterschiedliche Effizienz** bei verschiedenen Operationen.
- Die Wahl der Datenstruktur sollte auf der **Effizienz** für die **konkret benötigten Operationen** basieren.

**Element:** Jedes Element besteht aus **Attributen**; ein spezielles Attribut, der **Schlüssel (key)**, identifiziert es eindeutig.
```python
class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
```

### Typische Operationen auf einer Menge D
| Operation | Bedeutung |
|---|---|
| `INSERT(D, x)` / `DELETE(D, x)` | Element mit Schlüssel x einfügen / löschen |
| `SEARCH(D, x)` | Element mit Schlüssel x suchen |
| `SIZE(D)` | Anzahl der Elemente in D |
| `MAX(D)` / `MIN(D)` | Element mit größtem / kleinstem Schlüssel |
| `SUCC(D, x)` / `PRED(D, x)` | Nachfolger / Vorgänger (nächstgrößerer / nächstkleinerer Schlüssel) |

### Beispiele für Datenstrukturen
- **Feld (Array):** Zugriff über den Index.
- **Verkettete Liste (Linked List):** Element besitzt Verweis auf das folgende Element.
- **Warteschlange (Queue):** Lesen/Löschen nur in **gleicher** Reihenfolge des Einfügens.
- **Stapel (Stack):** Lesen/Löschen nur in **umgekehrter** Reihenfolge des Einfügens.
- **Graphen und Bäume:** variable Anzahl von Verweisen auf weitere Elemente.

**Motivation Liste vs. Binärbaum** (Zahlen 3,18,7,24,1):
- **Einfügen** ist **einfacher für die unsortierte Liste** (einfach anhängen).
- **Suchen** ist **effizienter für den Binärbaum** (nicht alle Elemente durchlaufen).

## 5.2 Feld / Array
- Feld hat (klassisch) eine **feste Anzahl** von Elementen. In Python arbeitet man mit **Listen**, daher Erweiterung einfach per `append`; in anderen Sprachen ist Verlängerung deutlich aufwändiger.
```python
def insert_element(array, index, element):
    return array[:index] + [element] + array[index:]   # Einfügen an Position

def delete_element(array, index):
    return array[:index] + array[index + 1:]           # Löschen an Position
```
Alternativen in Python: `insert()`, `pop()`, `del`. **Suchen:** Komplexität hängt davon ab, ob die Daten sortiert sind.

## 5.3 Verkettete Liste
- **Dynamische** Datenstruktur; Zahl der Elemente zur **Laufzeit frei wählbar**.
- Elemente sind über **Zeiger/Referenzen** auf das folgende Element verbunden; letzter Zeiger auf `NIL/NULL`.
- **Typen:** einfach oder doppelt verkettet.

**Eigenschaften:**
- Geringer Mehrbedarf an Speicher.
- Einfügen/Löschen **ohne Umkopieren** anderer Elemente.
- Zahl der Elemente beliebig veränderbar.
- **Kein direkter Zugriff** auf Elemente (Liste muss durchlaufen werden).

**🔧 Bauplan (Muster D – Durchlauf mit `current`):**
- `Node`: `data` + `next = None`.
- `LinkedList`: nur ein Attribut `head = None`.
- `insert`: ist `head` leer → `head = Node(data)`; sonst mit `current` **bis zum letzten** Knoten laufen (`while current.next`) und dort `current.next = Node(data)` anhängen.
- `print_list`: `current = self.head`, dann `while current: … current = current.next`.
- `delete`: drei Fälle – (1) Liste leer → `return`; (2) **head** enthält den Wert → `head = head.next`; (3) sonst mit `while current.next` vorlaufen und beim Treffer den Zwischenknoten **überspringen**: `current.next = current.next.next`.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):                 # am Ende anhängen
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):                   # von head bis Ende durchlaufen
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def delete(self, data):                 # erstes Vorkommen entfernen
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
```

> **⚠️ Stolperfallen verkettete Liste:** Beim Löschen des ersten Elements muss man **`head` umbiegen** (Sonderfall!). Beim Anhängen bis zum **letzten** Knoten laufen (`while current.next`, nicht `while current` – sonst läuft `current` bis `None` und `current.next` crasht).

**Anwendungen verketteter Listen:** dynamische Speicherverwaltung; Baustein für Stacks/Queues/Hash-Tabellen/Graphen; Listen in Datenbanken; Vorwärts-/Rückwärts-Navigation (doppelt verkettet); speicher­effizient bei großen, sich häufig ändernden Datensätzen.

## 5.4 Warteschlange (Queue)
- Dynamische Menge mit **speziellen Zugriffsoperationen**.
- **FIFO-Prinzip – First In / First Out**: das am längsten wartende Element wird als nächstes entfernt.
- Realisierung als verkettete Liste oder Array; **Anfang und Ende sind immer bekannt**.

```python
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):      # Element hinten hinzufügen
        self.queue.append(item)
    def dequeue(self):            # Element vorne entnehmen
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    def display(self):
        print(self.queue)
```

**Anwendungen von Queues:** Datenpuffer zwischen Prozessen, Druckaufträge, CPU-Scheduling, Webserver-Anfragen, Message Queuing Service, Tastatureingaben.

## 5.5 Stapel (Stack / Kellerspeicher)
- Dynamische Menge mit speziellen Zugriffsoperationen.
- **LIFO-Prinzip – Last In / First Out**: das am kürzesten wartende Element wird als nächstes entfernt.
- Realisierung als verkettete Liste oder Array; **nur das oberste Element ist bekannt**.

```python
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):          # oben auflegen
        self.stack.append(item)
    def pop(self):                 # oberstes Element entnehmen
        if len(self.stack) < 1:
            return None
        removed_item = self.stack[-1]
        del self.stack[-1]
        return removed_item
    def display(self):
        print(self.stack)
```

**Anwendungen von Stacks:** Rückgängig/Wiederholen (Undo/Redo), Aufrufstack in Programmiersprachen, Kontrollflüsse (Schleifen/Bedingungen), Syntaxprüfung in Compilern (Klammern/Tags), Speicherverwaltung in Betriebssystemen.

> **🔧 Bauplan Queue vs. Stack (beide = dünne Hülle um eine Python-Liste):** Hinzufügen ist bei beiden `self.liste.append(item)`. Der **einzige Unterschied ist das Entnehmen**:
> - **Queue (FIFO):** vorne entnehmen → `self.queue.pop(0)`.
> - **Stack (LIFO):** hinten/oben entnehmen → `self.stack[-1]` merken und `del self.stack[-1]` (bzw. `self.stack.pop()`).
>
> Beide prüfen vor dem Entnehmen `if len(...) < 1: return None` (leere Struktur). Merke: **FIFO = pop(0), LIFO = pop() / [-1]**.

## 5.6 Bäume und Binäre Suchbäume

### Bäume in der Informatik
- Ein **Baum** ist eine Menge von **Knoten und Kanten** mit hierarchischer Struktur.
- Besitzt immer einen speziellen Knoten, die **Wurzel (root)** (außer beim leeren Baum).
- Jeder Knoten außer der Wurzel ist über genau eine Kante mit seinem **Elternknoten (parent)** verbunden; er ist dessen **Kind (child)**.
- **Blatt (leaf):** Knoten ohne Kinder. **Innerer Knoten:** hat mindestens ein Kind.
- Jeder Knoten hat **höchstens einen Elternknoten**, aber ggf. mehrere Kindknoten.
- **Binärbaum:** jeder Knoten hat **höchstens zwei Kinder**. Allgemein: **n-äre Bäume** (bis zu n Kinder).

### Binärer Suchbaum (BST)
Eigenschaften (**gelten für jeden Knoten**, nicht nur die Wurzel):
- Jeder Knoten hat höchstens zwei Kinder (linkes/rechtes Kind).
- **Alle Werte im linken Teilbaum sind kleiner**, **alle Werte im rechten Teilbaum sind größer** als der Wert des Knotens.

Nutzen: effizientes Suchen/Sortieren. **Eine In-order-Traversierung liefert eine sortierte Liste** der Elemente.
> Zu beachten: BSTs sollten **ausgeglichen** sein; ein unausgewogener Baum kann im schlimmsten Fall **linear** statt **logarithmisch** skalieren.

**🔧 Bauplan (Muster B – öffentlich prüft Wurzel, privat rekursiv):**
- `Node`: drei Attribute `left`, `right` (beide `None`), `data`.
- `insert(data)`: ist `root` leer → `root = Node(data)`; sonst private `_insert(data, root)`.
- `_insert(data, node)`: **kleiner → links, sonst → rechts**. Pro Richtung immer dasselbe 2-Fall-Schema: *Kind leer?* → dort neuen `Node` einhängen; *sonst* → rekursiv in dieses Kind absteigen.
- `print_tree()` (In-order): startet private `_print_tree(root)`.
- `_print_tree(node)`: **wenn `node` nicht `None`**: erst **links**, dann **Knoten ausgeben**, dann **rechts** → das ergibt automatisch die **sortierte Reihenfolge**. (Merke die Reihenfolge L → N → R.)

```python
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):        # kleiner -> links, sonst -> rechts
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def print_tree(self):                 # In-order: gibt sortiert aus
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)   # 1. links
            print(str(node.data))         # 2. Knoten
            self._print_tree(node.right)  # 3. rechts
```

> **Reproduktions-Trick für alle Traversierungen:** Es sind immer dieselben drei Zeilen (links / Knoten / rechts), nur die **Reihenfolge** ändert sich: **In-order** = L, N, R (sortiert); **Pre-order** = N, L, R; **Post-order** = L, R, N.
>
> **⚠️ Stolperfallen BST:** In `_insert` in **jeder** Richtung beide Fälle abdecken (Kind leer → einhängen, sonst → Rekursion); der `None`-Check `if node is not None` in `_print_tree` ist der **Basisfall**, ohne ihn crasht die Rekursion an den Blättern.

**BST löschen** (drei Fälle): Blatt / ein Kind / zwei Kinder. Bei zwei Kindern wird der Knoten durch das **Minimum des rechten Teilbaums** ersetzt.
```python
def delete(self, data):
    self.root = self._delete(self.root, data)

def _delete(self, node, data):
    if node is None:
        return node
    if data < node.data:
        node.left = self._delete(node.left, data)
    elif data > node.data:
        node.right = self._delete(node.right, data)
    else:
        if node.left is None:
            temp = node.right; node = None; return temp
        elif node.right is None:
            temp = node.left; node = None; return temp
        temp = self._find_min(node.right)   # Minimum im rechten Teilbaum
        node.data = temp.data
        node.right = self._delete(node.right, temp.data)
    return node

def _find_min(self, node):
    if node.left is None:
        return node
    else:
        return self._find_min(node.left)
```

**Anwendungen von BSTs:** Suchalgorithmen, dynamisches Sortieren, Datenbanken (B-/T-Bäume), Dateisysteme, Speicherbelegung, Computergrafik (BSP-Bäume).

### Das musst du dir merken (Kapitel 5)
- Wahl der Datenstruktur nach **Effizienz** für die benötigten Operationen; **Element = Attribute + Schlüssel (key)**.
- **Queue = FIFO** (Anfang+Ende bekannt), **Stack = LIFO** (nur oberstes Element bekannt).
- **Verkettete Liste:** dynamisch, Einfügen/Löschen ohne Umkopieren, aber **kein direkter Indexzugriff**; einfach/doppelt verkettet.
- **BST-Eigenschaft:** links < Knoten < rechts, **für jeden Knoten**; **In-order-Traversierung = sortierte Ausgabe** (links → Knoten → rechts).
- BST sollte **ausgeglichen** sein (sonst O(n) statt O(log n)); Löschen mit zwei Kindern → Minimum des rechten Teilbaums.
- Einfügen einfacher in unsortierter Liste, Suchen effizienter im Binärbaum.

---

# 6. Sortierverfahren

## 6.1 Das Sortierproblem
- **Eingabe:** Folge von Zahlen `<a1, a2, …, an>`.
- **Ausgabe:** sortierte Folge `<a'1, a'2, …, a'n>` mit `a'1 ≤ a'2 ≤ … ≤ a'n`.
- **Aufgabe:** möglichst **effizienten** Weg zur Sortierung finden.

**Einteilung der Verfahren:**
- **„Naive" Sortierverfahren:** Bubble-Sort, Selection-Sort, Insertion-Sort – durchschnittliche Zeitkomplexität **O(n²)**.
- **Divide-and-Conquer:** Quicksort, Mergesort, Heapsort – Mergesort/Quicksort mit durchschnittlich **O(n log n)** gehören zu den effizientesten.

## 6.2 Bubble-Sort
**Idee:** die größten Zahlen „aufsteigen" lassen.
- Menge durchlaufen, jeweils zwei benachbarte Zahlen vergleichen.
- Falls `a_n > a_{n+1}`: die beiden vertauschen.
- Nach dem ersten Durchlauf ist die **letzte Zahl garantiert die größte**; dann von vorn wiederholen.

**🔧 Bauplan (so schreibst du es aus dem Kopf):**
1. `n = len(numbers)`.
2. **Äußere Schleife** `for i in range(n-1)`: so oft wie nötig komplett durchlaufen.
3. Flag `list_sorted = True` **am Anfang jedes äußeren Durchlaufs** setzen.
4. **Innere Schleife** `for j in range(0, n-i-1)`: benachbarte Paare vergleichen. Das `-i` spart die schon sortierten letzten `i` Elemente, das `-1` verhindert Zugriff auf `numbers[j+1]` außerhalb der Liste.
5. Bei `numbers[j] > numbers[j+1]`: **Swap (Muster A)** + `list_sorted = False`.
6. Nach der inneren Schleife: `if list_sorted: return` (früher Abbruch).

```python
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        list_sorted = True
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]  # tauschen
                list_sorted = False
        if list_sorted:            # kein Tausch nötig gewesen -> fertig
            return
```
Das `list_sorted`-Flag erlaubt frühen Abbruch (daher **bester Fall O(n)** bei bereits sortierter Eingabe).

**Durchgerechnetes Beispiel** `[55, 7, 78, 12, 42]` (erste 3 Iterationen; „größte steigt nach rechts"):
```
Iteration 1: 55 7 78 12 42 → swap 55/7 → 7 55 78 12 42
             → swap 78/12 → 7 55 12 78 42 → swap 78/42 → 7 55 12 42 [78]  (78 sitzt)
Iteration 2: 7 55 12 42 78 → swap 55/12 → 7 12 55 42 78 → swap 55/42 → 7 12 42 [55] 78
Iteration 3: 7 12 42 55 78 → keine Vertauschung mehr → list_sorted bleibt True → fertig
Ergebnis:    7 12 42 55 78
```

**⚠️ Stolperfallen:**
- Innere Grenze ist `n - i - 1` (nicht `n`), sonst `IndexError` bei `numbers[j+1]`.
- `list_sorted = True` gehört **in** die äußere Schleife (bei jedem Durchlauf neu), nicht davor.

## 6.3 Selection-Sort
**Idee:** iterativ das **kleinste** Element suchen und nach vorne legen.
- Kleinstes Element finden, mit dem ersten tauschen.
- Vorderer Teil ist sortiert (k Elemente nach Durchlauf k), hinterer Teil unsortiert; im unsortierten Teil das nächstkleinste Element suchen und tauschen.

**🔧 Bauplan:**
1. Äußere Schleife `for i in range(n)`: `i` ist die Position, die als Nächstes richtig befüllt wird.
2. `min_index = i` annehmen (das aktuelle Element ist erstmal das kleinste).
3. Innere Schleife `for j in range(i+1, n)`: **nur den unsortierten Rest** durchsuchen; wenn `numbers[j] < numbers[min_index]`, `min_index = j` merken.
4. Nach der inneren Schleife **einmal** tauschen: `numbers[i] ↔ numbers[min_index]` (Muster A).

```python
def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):                 # Minimum im unsortierten Teil
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]  # tauschen
```

**Durchgerechnetes Beispiel** `[55, 7, 78, 12, 42]`:
```
i=0: Minimum ist 7  → tausche 7 mit 55  → 7 55 78 12 42
i=1: Minimum ist 12 → tausche 12 mit 55 → 7 12 78 55 42
i=2: Minimum ist 42 → tausche 42 mit 78 → 7 12 42 55 78
i=3: Minimum ist 55 → tausche 55 mit 55 → 7 12 42 55 78 (unverändert)
Ergebnis: 7 12 42 55 78
```

**⚠️ Stolperfallen:**
- Die innere Schleife startet bei `i+1`, nicht bei `0` (sonst vergleicht man mit schon Sortiertem).
- Der **Tausch steht außerhalb** der inneren Schleife – man tauscht nur **einmal pro Durchlauf**, nicht bei jedem Vergleich (Unterschied zu Bubble-Sort).

## 6.4 Insertion-Sort
**Idee:** Menge in **sortierten** und **unsortierten** Bereich teilen; Element aus dem unsortierten Bereich an der korrekten Stelle im sortierten Bereich einfügen; bis unsortierte Menge leer.

**🔧 Bauplan:**
1. Äußere Schleife **ab `i=1`** (`numbers[0]` gilt allein als sortiert).
2. `pivot = numbers[i]` (das einzufügende Element) merken; `j = i - 1` (letzter Index des sortierten Teils).
3. **While-Schleife** `while j >= 0 and numbers[j] > pivot`: alle Elemente, die größer als `pivot` sind, **um eins nach rechts schieben** (`numbers[j+1] = numbers[j]`), dabei `j -= 1`.
4. Nach der Schleife: `pivot` an die gefundene Lücke setzen: `numbers[j+1] = pivot`.

```python
def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):
        pivot = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > pivot:      # größere Elemente nach rechts schieben
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = pivot                    # Pivot an korrekter Stelle einfügen
```

**Durchgerechnetes Beispiel** `[55, 7, 78, 12, 42]` (| trennt sortiert | unsortiert):
```
Start:      55 | 7 78 12 42
pivot=7:    füge 7 vor 55 ein   → 7 55 | 78 12 42
pivot=78:   bleibt hinter 55    → 7 55 78 | 12 42
pivot=12:   füge 12 vor 55 ein  → 7 12 55 78 | 42
pivot=42:   füge 42 vor 55 ein  → 7 12 42 55 78 |
Ergebnis:   7 12 42 55 78
```

**⚠️ Stolperfallen:**
- Reihenfolge in der `while`-Bedingung: **erst `j >= 0`**, dann `numbers[j] > pivot` (sonst `IndexError` bei `numbers[-1]`).
- Am Ende `numbers[j+1] = pivot` (nicht `numbers[j]`), weil `j` nach der Schleife eins zu weit links steht.

## 6.5 Quicksort (Divide-and-Conquer)
**Idee: Teile-und-Herrsche.**
- **Pivot wählen:** ein Element als Pivot bestimmen.
- **Partitionierung:** Liste mit Hilfe des Pivots in zwei Teile teilen (kleiner / größer).
- **Rekursive Sortierung** der Teillisten links und rechts des Pivots (bis Teillisten nur noch ein Element haben).
- **Kombinieren:** kleiner-Teil + Pivot + größer-Teil zusammenfügen.

**🔧 Bauplan (Muster C – Rekursion):**
1. **Basisfall:** `if len(numbers) <= 1: return numbers` (0 oder 1 Element ist schon sortiert).
2. **Pivot** wählen: `pivot = numbers[0]`.
3. **Partitionieren** mit List-Comprehensions über `numbers[1:]` (Pivot selbst auslassen): `less` = alle `< pivot`, `greater` = alle `> pivot`.
4. **Kombinieren:** `return quicksort(less) + [pivot] + quicksort(greater)`.

```python
def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers[0]
        less    = [x for x in numbers[1:] if x < pivot]
        greater = [x for x in numbers[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
```
**Durchgerechnetes Beispiel** `[55, 7, 78, 12, 42]` (Pivot = erstes Element, fett):
```
[55,7,78,12,42]  pivot 55 → less=[7,12,42]           greater=[78]
  [7,12,42]      pivot 7  → less=[]                  greater=[12,42]
    [12,42]      pivot 12 → less=[]                  greater=[42]
Zusammensetzen: [] + 7 + ([]+12+[42]) = [7,12,42]; dann [7,12,42]+55+[78]
Ergebnis: [7,12,42,55,78]
```
> **⚠️ Achtung (Klausur-Klassiker):** Vergleich nur auf `<` bzw. `>` **eliminiert Duplikate** (ein zweites `55` würde weder in `less` noch in `greater` landen). Sollen Duplikate erhalten bleiben, muss **einer der beiden Vergleiche `<=`** sein (z. B. `less = [x … if x <= pivot]`).

**⚠️ Weitere Stolperfallen:**
- `numbers[1:]` (nicht `numbers`) durchsuchen – sonst kommt der Pivot doppelt vor.
- Basisfall nicht vergessen → sonst Endlos-Rekursion.

## 6.6 Mergesort (Divide-and-Conquer)
**Idee: Teile-und-Herrsche.**
- **Teilen:** Liste rekursiv in der Mitte in zwei etwa gleich große Teillisten teilen, bis jede nur noch **ein Element** enthält.
- **Sortieren:** Teilliste mit einem Element gilt als sortiert; sonst Mergesort rekursiv.
- **Merge:** sortierte Teillisten schrittweise zusammenführen (Elemente vergleichen, **kleinste zuerst** in die Ergebnisliste).

**🔧 Bauplan – zwei Funktionen:**
- `merge_sort` (Muster C – Rekursion): 1. Basisfall `len <= 1`; 2. Mitte `mid = len // 2`; 3. beide Hälften **rekursiv** sortieren; 4. mit `merge` zusammenführen.
- `merge` (Muster E – zwei Zeiger): `result`-Liste + Indizes `i`, `j` = 0; solange **beide** Listen noch Elemente haben, das **kleinere** anhängen und dessen Index erhöhen; danach den **Rest beider** Listen anhängen.

```python
def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2                 # in der Mitte teilen
    left_half  = merge_sort(numbers[:mid])  # rekursiv sortieren
    right_half = merge_sort(numbers[mid:])
    return merge(left_half, right_half)     # sortierte Hälften zusammenführen

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:      # kleineres zuerst
            merged.append(left[left_index]); left_index += 1
        else:
            merged.append(right[right_index]); right_index += 1
    merged.extend(left[left_index:])       # Rest anhängen
    merged.extend(right[right_index:])
    return merged
```
**Durchgerechnetes Beispiel** `[55, 7, 78, 12, 42]`:
```
Teilen:  [55,7,78,12,42] → [55,7] | [78,12,42]
         [55,7] → [55] | [7]        [78,12,42] → [78] | [12,42] → [12] | [42]
Mergen (kleinere zuerst):
         merge([55],[7])   = [7,55]
         merge([12],[42])  = [12,42];  merge([78],[12,42]) = [12,42,78]
         merge([7,55],[12,42,78]) = [7,12,42,55,78]
Ergebnis: [7,12,42,55,78]
```

**⚠️ Stolperfallen:**
- In `merge` nach der `while`-Schleife **beide** `extend`-Zeilen nicht vergessen – eine der Listen hat noch einen Rest.
- Nur **einen** Index pro Schritt erhöhen (den der übernommenen Seite).
- `mid = len(numbers) // 2` mit Ganzzahl-Division `//`.

## 6.7 Heapsort (Max-Heap)
**Prinzip:** Daten als **Max-Heap** repräsentieren.
- **Max-Heap:** Binärbaum, in dem der Schlüssel eines Knotens **immer ≥ die Schlüssel der beiden Nachfolgeknoten** ist → der **Wurzelknoten enthält das größte Element**.
- **Feld-Darstellung:** Elemente eines Feldes können als Binärbaum angeordnet werden; die **Nachfolger von Knoten k** stehen an den Indizes **2k und 2k+1** (bei 0-basierten Indizes im Code: `2*i+1` und `2*i+2`).

**Ablauf:**
1. **Initialisierung:** Max-Heap für das Feld aufbauen.
2. **N Iterationen:** größtes Element (Wurzel) **entnehmen** (mit letztem Element tauschen → ans Ende in den sortierten Teil), dann Max-Heap aus den verbleibenden Elementen **wiederherstellen** (**„versickern"/percolate**).

**Versickern (percolate):** Wurzel mit dem **Maximum ihrer beiden Nachfolger** vergleichen und tauschen; das versickernde Element wandert nach unten, bis die Heap-Eigenschaft wiederhergestellt ist – **maximal log n** Versickerungs-Schritte.

**Motivation der Komplexität:** n Elemente müssen entnommen werden (n Iterationen), Wiederherstellung des Heaps je in log(n) → insgesamt **O(n log n)**.

**🔧 Bauplan – zwei Funktionen:**
- `heapify(arr, n, i)` = **Versickern** eines Knotens `i` in einem Heap der Größe `n`:
  1. `largest = i` annehmen; Kinder berechnen: `left = 2*i+1`, `right = 2*i+2`.
  2. Wenn linkes Kind existiert (`left < n`) **und** größer als `largest` → `largest = left`.
  3. Analog für rechtes Kind.
  4. Wenn `largest != i` (ein Kind war größer): **tauschen** (Muster A) und **rekursiv** `heapify(arr, n, largest)` (versickert weiter nach unten).
- `heap_sort(arr)`:
  1. **Max-Heap aufbauen:** `for i in range(n//2 - 1, -1, -1)` (von unten nach oben, nur innere Knoten) je `heapify`.
  2. **Extrahieren:** `for i in range(n-1, 0, -1)`: Wurzel `arr[0]` mit `arr[i]` **tauschen** (größtes ans Ende in den sortierten Teil), dann `heapify(arr, i, 0)` – wichtig: **Heapgröße `i`**, damit der schon sortierte Teil hinten unangetastet bleibt.

```python
def heap_sort(arr):
    n = len(arr)
    # 1. Max-Heap aufbauen
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # 2. Elemente extrahieren
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # größtes (Wurzel) ans Ende tauschen
        heapify(arr, i, 0)                # Heap für Rest wiederherstellen (Größe i!)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left  < n and arr[left]  > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]   # mit größtem Kind tauschen
        heapify(arr, n, largest)                       # rekursiv weiter versickern
```

**Durchgerechnetes Beispiel** (Feld-Darstellung, Skript-Beispiel; Max-Heap `[7,6,5,2,3,4,1]`; gelb = schon sortiert am Ende):
```
Heap:            7 6 5 2 3 4 1
entnehme 7 → tausche mit letztem 1:   1 6 5 2 3 4 |7   → versickere 1:   6 3 5 2 1 4 |7
entnehme 6 → tausche mit 4:           4 3 5 2 1 |6 7   → versickere 4:   5 3 4 2 1 |6 7
entnehme 5 → tausche mit 1:           1 3 4 2 |5 6 7   → versickere 1:   4 3 1 2 |5 6 7
entnehme 4 → tausche mit 2:           2 3 1 |4 5 6 7   → versickere 2:   3 2 1 |4 5 6 7
… weiter bis:                         1 2 3 4 5 6 7
```
Kern jeder Iteration: **Wurzel (=Maximum) nach hinten tauschen → Heap um 1 verkleinern → Wurzel versickern.**

**⚠️ Stolperfallen:**
- Beim Extrahieren `heapify(arr, i, 0)` mit **`i`** (der schrumpfenden Heapgröße), **nicht** `n` – sonst wird der bereits sortierte Teil zerstört.
- Kinder-Indizes (0-basiert): `2*i+1` (links) und `2*i+2` (rechts). *(Das Skript nennt die Formel für 1-basierte Indizes als `2k`/`2k+1`.)*
- Heap-Aufbau läuft **rückwärts** (`range(n//2 - 1, -1, -1)`), damit man von unten nach oben versickert.
- Immer **Max-Heap** (größtes oben), weil wir aufsteigend sortieren und das Maximum nach hinten schieben.

## 6.8 Zusammenfassung: Zeitkomplexitäten
| Verfahren | bester Fall | mittlerer Fall | schlechtester Fall |
|---|---|---|---|
| **Bubble** | O(n) | O(n²) | O(n²) |
| **Selection** | O(n²) | O(n²) | O(n²) |
| **Insertion** | O(n) | O(n²) | O(n²) |
| **Heap** | O(n·log n) | O(n·log n) | O(n·log n) |
| **Quick** | O(n·log n) | O(n·log n) | **O(n²)** |
| **Merge** | O(n·log n) | O(n·log n) | O(n·log n) |
| **Counting** | O(n) | O(n) | O(n) |

### Das musst du dir merken (Kapitel 6)
- **Naive Verfahren (Bubble, Selection, Insertion): im Schnitt O(n²).** Bubble/Insertion bester Fall O(n), Selection immer O(n²).
- **Divide-and-Conquer:** Quicksort, Mergesort, Heapsort.
- **Quicksort:** Pivot + Partition + Rekursion; **O(n log n)** im Schnitt, aber **O(n²)** im schlechtesten Fall; nur `<`/`>` **entfernt Duplikate** (einen Vergleich auf `<=` setzen, um sie zu behalten).
- **Mergesort:** in der Mitte teilen, rekursiv, dann `merge` (kleinste zuerst); **immer O(n log n)**.
- **Heapsort:** **Max-Heap** (Wurzel = Maximum); Kinder an `2i+1`/`2i+2`; Wurzel entnehmen + **versickern** (max. log n Schritte); **immer O(n log n)**.
- **In-order-Traversierung eines BST** liefert ebenfalls eine sortierte Ausgabe (Bezug zu Kapitel 5).

---

*Ende der Zusammenfassung – erstellt ausschließlich aus den sechs Vorlesungsskripten. Titelfolien und rein bildliche Folien wurden übersprungen; wo Skriptangaben knapp/uneindeutig waren (z. B. konkrete Ausgaben der IO-Snippet-Übungen), ist dies im Text als solches gekennzeichnet.*

*Alle durchgerechneten Sortier-Beispiele (Heapsort inkl. jedem Versickern-Schritt, Quicksort, Mergesort) wurden mit echtem Python ausgeführt und geben nachweislich das gezeigte Ergebnis. Die 🔧-Baupläne und ⚠️-Stolperfallen sollen dir ermöglichen, den Code in der Klausur frei zu reproduzieren.*
