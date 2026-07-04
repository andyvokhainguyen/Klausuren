# Lösungen – Übungsblatt 2 (Testen)

---

## Aufgabe 1 – Minimales Testset für `dritteWurzel(x, epsilon)`

Spezifikation: `x, epsilon` floats, `epsilon > 0`; Ergebnis erfüllt `x-epsilon <= ergebnis**3 <= x+epsilon`.
Anders als bei der Quadratwurzel ist die **dritte Wurzel auch für negative x** definiert → negative Werte mit testen (Black-Box, natürliche Partitionen + Randwerte).

| Testfall | x | epsilon | Erwartung |
|---|---|---|---|
| Randwert 0 | 0 | 0.0001 | ≈ 0 |
| perfekte dritte Wurzel | 27 | 0.0001 | ≈ 3 |
| 0 < x < 1 | 0.125 | 0.0001 | ≈ 0.5 |
| negatives x | -8 | 0.0001 | ≈ -2 |
| großes x (Extremwert) | 1e9 | 0.001 | ≈ 1000 |
| kleines epsilon (Genauigkeit) | 2 | 1e-9 | ≈ 1.2599 |

Begründung: deckt Null, exakte Wurzel, Bereich <1, negatives Vorzeichen sowie Extrem-/Genauigkeitsränder ab.

---

## Aufgabe 2 – Minimales Testset für `ersetzeUmlauteInText(text)`

Spezifikation: ersetzt Umlaute (ä→ae, ö→oe, ü→ue, Ä/Ö/Ü, ß→ss) und **entfernt** zusätzlich alle Sonderzeichen.

| Testfall | Eingabe | Erwartung |
|---|---|---|
| leerer String (Randfall) | `""` | `""` |
| ohne Umlaute/Sonderzeichen | `"Hallo"` | `"Hallo"` |
| nur Umlaute | `"äöüÄÖÜß"` | `"aeoeueAeOeUess"` |
| nur Sonderzeichen | `"!?.,"` | `""` |
| gemischt | `"Müller & Söhne!"` | `"MuellerSoehne"` |

*(Annahme: Leerzeichen zählt als Sonderzeichen und wird entfernt – ggf. mit Prof abklären.)*

---

## Aufgabe 3 – Bestes Test-Set für `foo(x, a)`

```python
def foo(x, a):        # while x >= a: count += 1; x = x - a  ->  return count
```
White-Box-Empfehlung für Schleifen: **gar nicht / genau einmal / mehrfach** durchlaufen.

- **Test-Set A:** foo(2,5)=0, foo(5,6)=0, foo(9,7)=1 → nur **0×** und **1×** (mehrfach fehlt).
- **Test-Set B:** foo(10,3)=3, foo(1,4)=0, foo(10,6)=1 → **mehrfach**, **0×**, **1×** ✅ alle drei Fälle.
- **Test-Set C:** foo(100,5)=20, foo(96,5)=19, foo(22,5)=4 → nur **mehrfach** (0× und 1× fehlen).

**➡️ Test-Set B ist das beste**, weil es als einziges alle drei Schleifen-Durchlauf-Fälle (0, 1, mehrfach) abdeckt = path-complete für die Schleife.

---

## Aufgabe 4 – `lies_zahl_ein()` + Taschenrechner-Funktion

**Black-Box-Äquivalenzklassen für `lies_zahl_ein()`:**
| Klasse | Eingabe | Erwartung |
|---|---|---|
| gültige Ganzzahl | `"5"` | 5.0 |
| gültige Kommazahl | `"3.14"` | 3.14 |
| negative Zahl | `"-2"` | -2.0 |
| ungültige Eingabe | `"abc"` | erneute Abfrage / Fehler |

**Robuste Implementierung:**
```python
def lies_zahl_ein():
    """Fragt den Nutzer nach einer Zahl; wiederholt bei ungültiger Eingabe."""
    while True:
        eingabe = input("Bitte eine Zahl eingeben: ")
        try:
            return float(eingabe)
        except ValueError:
            print("Ungültige Eingabe – bitte eine Zahl eingeben.")
```

**Robuste Taschenrechner-Funktion** (nan bei nicht definierten Ergebnissen):
```python
import math

def alle_funktionen_auf_meinem_taschenrechner(x):
    """returns: Liste mit sqrt(x), log(x), asin(x), acos(x), atan(x);
    nicht definierte Ergebnisse werden durch 'nan' ersetzt (mit Hinweis)."""
    funktionen = [("sqrt", math.sqrt), ("log", math.log),
                  ("asin", math.asin), ("acos", math.acos), ("atan", math.atan)]
    ergebnis = []
    for name, func in funktionen:
        try:
            ergebnis.append(func(x))
        except ValueError:
            print(f"Hinweis: {name}({x}) ist nicht definiert -> 'nan'")
            ergebnis.append("nan")
    return ergebnis
```

**White-Box-Tests** (jeder Zweig „definiert" / „nicht definiert" pro Funktion):
| x | sqrt | log | asin/acos | atan | Bemerkung |
|---|---|---|---|---|---|
| 0.5 | ok | ok | ok (∈[-1,1]) | ok | alle definiert |
| 2 | ok | ok | **nan** (>1) | ok | asin/acos außerhalb Definitionsbereich |
| -1 | **nan** | **nan** | ok (=-1) | ok | sqrt/log für negative undefiniert |
| 0 | ok | **nan** | ok | ok | log(0) nicht definiert |

```python
def test_x_negativ_liefert_nan():
    erg = alle_funktionen_auf_meinem_taschenrechner(-1)
    assert erg[0] == "nan" and erg[1] == "nan"   # sqrt, log

def test_x_groesser_eins_liefert_nan_bei_asin_acos():
    erg = alle_funktionen_auf_meinem_taschenrechner(2)
    assert erg[2] == "nan" and erg[3] == "nan"   # asin, acos

def test_x_gueltig_alle_definiert():
    erg = alle_funktionen_auf_meinem_taschenrechner(0.5)
    assert "nan" not in erg
```
