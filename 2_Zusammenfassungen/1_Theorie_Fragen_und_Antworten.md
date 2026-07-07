# 📝 Theorie: Fragen & Antworten (Software Engineering)

Alle Theoriefragen aus den 6 Altklausuren + mögliche weitere – jeweils mit **kurzer, vollständiger Antwort**.
Zum Selbsttesten: Antwort abdecken, Frage beantworten, vergleichen.

---

# TEIL A – Kam schon dran

## 1. Programmierung vs. Software-Engineering *(SS23, SS25)*
**F:** Unterschied Programmierung vs. Software-Engineering (2 Merkmale)?
**A:** *Programmieren* = Code für eine kleine, konkrete Aufgabe, oft eine Person, Fokus Algorithmus/Syntax. *SE* (Balzert) = zielorientierte, **systematische, arbeitsteilige, ingenieurmäßige** Entwicklung **umfangreicher** Systeme. Unterscheidend: (1) systematisches Vorgehen nach **Phasenmodellen** statt ad hoc; (2) **gesamter Lebenszyklus** inkl. Wartung, Qualitätssicherung, Teamarbeit – nicht nur bis „Code läuft".

## 2. Gründe für Software-Engineering *(WS2324)*
**F:** Vier Gründe für SE in größeren Projekten?
**A:** **Komplexität** (Strukturierung/Modularisierung/Abstraktion), **Qualität** (Sicherheit/Robustheit/Testbarkeit), **Wartung** (Dokumentation, ~80 % der Kosten), **Planung/Organisation** (Termine, Kosten, Personal, Teamkommunikation). *(auch: Methodik/Best Practices)*

## 3. Magisches Dreieck *(SS23, SS24, WS2425)*
**F:** Erklären + Beispiel?
**A:** Drei konkurrierende Dimensionen **Zeit – Kosten – Qualität**; die Änderung einer wirkt **zwangsläufig** auf die anderen, man kann nicht alle gleichzeitig optimieren. Beispiel: Termin verkürzen → entweder mehr Personal (**Kosten ↑**) oder Features/Tests weglassen (**Qualität ↓**).

## 4. Softwarequalität *(WS2324, SS24)*
**F:** Je 3 Qualitätsmerkmale aus Benutzer- und Entwicklersicht (+ Messgröße)?
**A:** *Benutzer:* Funktionserfüllung, Zuverlässigkeit, Benutzbarkeit (auch Effizienz, Sicherheit). *Entwickler:* Wartbarkeit, Testbarkeit, Übertragbarkeit (auch Änderbarkeit, Wiederverwendbarkeit). *Messgrößen:* Funktionserfüllung → % umgesetzte Anforderungen · Zuverlässigkeit → MTBF/Fehlerrate · Effizienz → Antwortzeit · Wartbarkeit → zyklomatische Komplexität · Testbarkeit → Testabdeckung.
**F:** Abhängigkeiten zwischen Merkmalen?
**A:** Verbesserung von **Effizienz** kann Wartbarkeit/Portabilität senken; **Sicherheit** kann Benutzbarkeit/Effizienz senken; **Robustheit** kostet Effizienz. → Qualitätsanforderungen bewusst festlegen/priorisieren.

## 5. Funktionale vs. nicht-funktionale Anforderungen *(SS23, WS2425)*
**F:** Unterschied + je ein Beispiel?
**A:** **Funktional = WAS** das System tun soll (konkrete Funktionen, z.B. „Produkt in Warenkorb legen"). **Nicht-funktional = WIE GUT** (Qualitätseigenschaften: Performanz, Zuverlässigkeit, Sicherheit, Skalierbarkeit, z.B. „Antwortzeit < 2 s").

## 6. Versteckte Anforderungen *(WS2324)*
**F:** Was sind sie, wie erkennt man sie?
**A:** Anforderungen, die der Kunde **nicht explizit nennt**, die sich aber aus dem Kontext ergeben; erkennbar durch **gezieltes Nachfragen**. Bsp.: Einsatzort → Wartungsart (Remote), Benutzungsfrequenz → Performanz, Ausfallfolgen → Robustheit, Anwenderprofil → Internationalisierung, Geschäftsplanung → Erweiterbarkeit.

## 7. Lasten- vs. Pflichtenheft *(WS2324)*
**F:** Unterschied?
**A:** **Lastenheft = WAS/WOZU**, vom **Auftraggeber** (Zielbestimmung, Anforderungen, Abnahmekriterien; oft noch unscharf). **Pflichtenheft = WIE**, vom **Auftragnehmer** (Use Cases, GUI-Skizzen, Glossar, technische Umsetzung/Architektur). Beide bilden zusammen die **vertragliche Grundlage**.

## 8. Phasen der Softwareentwicklung *(SS23)*
**F:** Phasen in Reihenfolge + Ergebnis (Artefakt)?
**A:** **Analyse** (Anforderungsdok.) → **Definition** (Spezifikation + Abnahmekriterien) → **Architektur** (Komponentenstruktur) → **Design** (Klassen/Schnittstellen) → **Implementierung** (Code + Unit-Tests) → **Modultest** → **Integration** (getestetes Gesamtsystem) → **Systemtest** → **Abnahme** (Abnahmeprotokoll) → **Einführung/Betrieb** (produktives System, Wartungsdoku).

## 9. Phasenmodelle: Wasserfall / V-Modell / Scrum *(SS23, SS25)*
**F:** Grundlegender Unterschied Wasserfall vs. V-Modell?
**A:** **Wasserfall** = rein sequenzielle Phasen, getestet erst am Ende → Fehler spät. **V-Modell** = jede Entwicklungsphase hat ein **Testpendant** (Anforderungsanalyse↔Abnahmetest, Systemspez.↔Systemtest, Architektur↔Integrationstest, Detailentwurf↔Modultest) → QS von Anfang an.
**F:** Scrum – Rollen + Prozess?
**A:** *Rollen:* **Product Owner** (pflegt/priorisiert Backlog, vertritt Kunde), **Scrum Master** (Prozess-Coach, beseitigt Hindernisse), **Entwicklungsteam** (selbstorganisiert, liefert Inkrement). *Prozess:* Sprint Planning → **Sprint** (2–4 Wochen, tägl. Daily Scrum 15 min) → Sprint Review → Retrospektive. *Artefakte:* Product Backlog, Sprint Backlog, Inkrement.
**F:** Welches Modell wann?
**A:** Stabile, klare Anforderungen → **Wasserfall**; sicherheitskritisch/komplex → **V-Modell**; veränderliche Anforderungen → **Scrum**.

## 10. 4+1-Sichten nach Kruchten *(WS2324, SS24, WS2526)*
**F:** Die fünf Sichten + je ein Stichwort?
**A:** **Logische Sicht** (Klassen/Funktionalität), **Entwicklungs-/Implementierungssicht** (Dateien/Repositories), **Prozess-Sicht** (Prozesse/Threads, Performanz/Skalierbarkeit), **Physische Sicht** (Hardwaretopologie/Verteilung), **Szenario-/Anwendungssicht ("+1")** (Akteure/Use Cases, verbindet die vier Sichten).

## 11. Software Engineering im Projekt / Stakeholder *(WS2425)*
**F:** Zentrale Rollen + Beziehungen?
**A:** Zentraler **Manager** (Controlling/Projektleitung) koordiniert: **Kunde** (Anforderungen/Qualitäten ↔ Termine/Kosten/Produkt), **Marketing** (Marktanforderungen/Geschäftsziele), **SW-Entwicklung** (Planung/Status), **Qualitätssicherung** (Status).

## 12. Betriebsphase & Wartung *(WS2526)*
**F:** Anteil an Gesamtkosten + Wartungsarten?
**A:** **~80 %** der Gesamtkosten entfallen auf den Betrieb (längste Phase). **Wartungsarten:** korrektiv (Fehlerbehebung), adaptiv (Anpassung an neue Rahmenbedingungen), perfektiv (Verbesserung bestehender Funktionen), präventiv (Verbesserung der Wartbarkeit).

## 13. Testen (Theorie) *(SS24, WS2425, SS25, WS2526)*
**F:** Testpyramide?
**A:** **Unit-Tests** (viele, schnell) → **Integrationstests** → **System-/E2E-Tests** (wenige, aufwändig); **Regressionstests** begleitend. Idee: breite Basis schneller Unit-Tests, wenige teure E2E-Tests.
**F:** Black-Box vs. White-Box?
**A:** **Black-Box** = Testentwurf **ohne** Codekenntnis, nur nach Spezifikation (Äquivalenzklassen, Randwerte). **White-Box** = **mit** Codekenntnis, Pfade durch den Code.
**F:** Was heißt „path-complete"?
**A:** Jeder mögliche **Pfad** im Code wird mind. einmal durchlaufen (White-Box). Empfehlung: Verzweigungen → beide Zweige, Schleifen → 0/1/mehrfach, Rekursion → Basisfall/1×/mehrfach.
**F:** Defensive Programmierung – Beitrag + Maßnahmen?
**A:** Fehler früh vermeiden/erkennen → robusterer, testbarer Code. Maßnahmen: klare **Spezifikationen** (Docstrings), **Modularisierung**, **Assertions** (Typ-/Constraint-Prüfung), bewusste Ausnahmebehandlung.

## 14. Programmiersprachen-Zuordnung *(SS23, WS2324)*
**F:** Welche Sprache wofür?
**A:** iOS → **Swift** · Android → **Kotlin** · interaktive Website → **JavaScript** · Webanwendung Backend+DB → **Java** · Server-Backend hohe Netzleistung → **Golang** · massiv-paralleles numerisches Rechnen → **Julia** · Echtzeit/verteilt/nebenläufig → **Erlang** · Web-Automatisierung/Skripte → **Ruby** · automatisiertes Web-Testen → **Selenium** · Windows-Desktop → **Visual Basic** · Blog-CMS → **WordPress**.

---

# TEIL B – Kam NIE dran (heiße Kandidaten)

## 15. Softwarekrise & CHAOS-Report
**F:** Was war die Softwarekrise? Wann/wo wurde „Software Engineering" geprägt? Erfolgsverteilung?
**A:** **Softwarekrise** = seit den 1960ern Projekte zu teuer, zu spät, mangelhafte Qualität. Begriff **1968 auf der NATO-Konferenz in Garmisch-Partenkirchen** geprägt. **CHAOS-Report** (Standish Group): erfolgreich **~30–35 %**, herausgefordert **~45–50 %**, gescheitert **~15–20 %**.

## 16. Brooks'sches Gesetz
**F:** Wie lautet es, warum gilt es?
**A:** **„Adding manpower to a late software project makes it later."** Gründe: **Einarbeitungszeit** (Neue binden Erfahrene), **Kommunikationsaufwand** wächst mit **n·(n-1)/2** Kanälen (5 Pers. = 10, 50 = 1225), **nicht alle Aufgaben parallelisierbar**.

## 17. 1-10-100-Regel
**F:** Was besagt sie?
**A:** Die **Fehlerkosten steigen drastisch**, je später ein Fehler entdeckt wird: Anforderungsanalyse **1×** → Implementierung ~10× → **nach Auslieferung 100–1000×**. → Sorgfalt in frühen Phasen zahlt sich massiv aus.

## 18. Einführungsstrategien (Rollout)
**F:** Vier Strategien + Risiko?
**A:** **Big Bang** (komplett zum Stichtag – Risiko hoch, kein Fallback), **Stufenweise** (Region für Region – mittel), **Parallelbetrieb** (alt + neu gleichzeitig – niedrig, doppelte Kosten), **Pilotbetrieb** (ausgewählte Anwender – niedrig, begrenzte Aussagekraft).

## 19. Make-or-Buy
**F:** Standard-Software vs. Eigenentwicklung?
**A:** **Buy** (Standard-SW): schneller, aber begrenzt anpassbar, Vendor Lock-in, keine Differenzierung. **Make** (Eigenentwicklung): flexibel, Wettbewerbsvorteil, aber teurer/langsamer. **Faustregel:** Standardprozesse (HR, Buchhaltung) → Buy; differenzierende Prozesse → Make.

## 20. Architekturstile & arc42
**F:** Was ist ein Architekturstil? Wozu arc42?
**A:** **Architekturstil** = Abstraktion/Leitlinie für Art der Komponenten und ihrer Beziehungen; gibt Rahmen für Entwurfsentscheidungen und legt Qualitätseigenschaften fest. **arc42** = Template mit **12 Abschnitten** zur Architekturdokumentation (Ziele, Constraints, Kontext, Lösungsstrategie, Bausteinsicht, Laufzeit, Verteilung, Querschnittskonzepte, Entscheidungen, Qualität, Risiken, Glossar).

## 21. Häufige Fehler in IT-Projekten
**F:** Fehler + Gegenmaßnahme?
**A:** Unklare Anforderungen → agile Methoden/Feedback · unrealistische Zeitpläne → Bottom-Up-Schätzung + Puffer · Scope Creep → Change Management · unzureichendes Testen → Testautomatisierung/CI-CD · mangelnde Stakeholder-Einbindung → Sprint Reviews/Demos.
