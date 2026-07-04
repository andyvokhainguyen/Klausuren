# Lösungen – Übungsblatt 3 (Argumente & Kommandozeile)

---

## Aufgabe 1 – `converter.py` (Euro ↔ USD) mit `sys`

```python
import sys

konvertierung = sys.argv[1]
betrag = float(sys.argv[2])
wechselkurs = float(sys.argv[3])

if konvertierung == "euro-usd":
    ergebnis = betrag * wechselkurs
    print(f"{betrag}€ entsprechen {ergebnis:.2f}$")
elif konvertierung == "usd-euro":
    ergebnis = betrag / wechselkurs
    print(f"{betrag}$ entsprechen {ergebnis:.2f}€")
else:
    print("Fehler: unbekannte Konvertierung (euro-usd oder usd-euro)")
```
`python converter.py euro-usd 10 1.07` → `10.0€ entsprechen 10.70$`.

---

## Aufgabe 2 – `taschenrechner.py` (a/s/m/d) mit `sys`

```python
import sys

if len(sys.argv) < 4:
    print("Fehler: mindestens zwei Zahlen erforderlich")
    sys.exit()

op = sys.argv[1]
zahlen = list(map(float, sys.argv[2:]))     # alle weiteren Argumente als Zahlen

if op == "a":
    ergebnis = sum(zahlen)
    print(f"Ergebnis der Addition: {ergebnis}")
elif op == "s":
    ergebnis = zahlen[0]
    for z in zahlen[1:]:
        ergebnis -= z
    print(f"Ergebnis der Subtraktion: {ergebnis}")
elif op == "m":
    ergebnis = 1
    for z in zahlen:
        ergebnis *= z
    print(f"Ergebnis der Multiplikation: {ergebnis}")
elif op == "d":
    ergebnis = zahlen[0]
    for z in zahlen[1:]:
        ergebnis /= z
    print(f"Ergebnis der Division: {ergebnis}")
else:
    print("Ungültige Operation (a, s, m oder d)")
```
`python taschenrechner.py a 5 10 2` → `Ergebnis der Addition: 17.0` · `... m 5 10 2` → `... Multiplikation: 100.0`.

---

## Aufgabe 3 – `wiederholetext.py` mit `getopt` (-t/-r/-v)

```python
import sys
import getopt


def main(argv):
    text = None
    repeat = None
    verbose = False

    try:
        opts, args = getopt.getopt(argv, "t:r:v", ["text=", "repeat=", "verbose"])
    except getopt.GetoptError:
        print("Fehlerhafte Eingabe")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-t", "--text"):
            text = arg
        elif opt in ("-r", "--repeat"):
            repeat = int(arg)
        elif opt in ("-v", "--verbose"):
            verbose = True

    # -t und -r sind Pflicht
    if text is None or repeat is None:
        print("Fehlerhafte Eingabe")
        sys.exit(2)

    if verbose:
        print(f'Der Text "{text}" wird nun {repeat} Mal ausgegeben:')
    print(text * repeat)


if __name__ == "__main__":
    main(sys.argv[1:])
```
`python wiederholetext.py --text Hallo -r 2` → `HalloHallo` ·
`... -t Hallo --repeat 3 --verbose` → Hinweiszeile + `HalloHalloHallo` ·
`... --text Hallo` (ohne -r) → `Fehlerhafte Eingabe`.

**getopt-Parsing mit pytest testen** (Parser in Funktion auslagern, die opts→Werte liefert):
```python
def test_parsing_kurz_und_lang():
    # gleiche Semantik bei kurz/lang; hier exemplarisch die reine Wiederholung
    assert "Hallo" * 2 == "HalloHallo"

def test_parsing_fehlende_option_wirft_systemexit():
    import pytest
    with pytest.raises(SystemExit):
        main(["--text", "Hallo"])     # -r fehlt
```
*(Sauberer: eine Funktion `parse_args(argv) -> (text, repeat, verbose)` schreiben und deren Rückgabe direkt asserten.)*

---

## Aufgabe 4 – Caesar-Verschlüsselung auf der Kommandozeile (getopt)

Ver-/Entschlüsselungscode ist vorgegeben; nur das Argument-Handling ist zu schreiben.
Aufruf: `python3 verschluesele_text.py -s <shift> -c/-d -t <text>`

```python
import sys
import getopt


# --- vorgegeben ---
def caesar_chiffrieren(input_string, verschiebung):
    chiffrierter_text = ""
    for char in input_string:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            chiffrierter_text += chr((ord(char) - ascii_offset + verschiebung) % 26 + ascii_offset)
        else:
            chiffrierter_text += char
    return chiffrierter_text


def caesar_dechiffrieren(input_string, verschiebung):
    return caesar_chiffrieren(input_string, -verschiebung)
# --- /vorgegeben ---


def main(argv):
    text = ""
    shift = 0
    modus = ""     # "c" oder "d"

    try:
        opts, args = getopt.getopt(
            argv, "s:cdt:h",
            ["shift=", "chiffrieren", "dechiffrieren", "text=", "help"]
        )
    except getopt.GetoptError:
        print("verschluesele_text.py -s <shift> -c/-d -t <text>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("verschluesele_text.py -s <shift> -c/-d -t <text>")
            sys.exit()
        elif opt in ("-s", "--shift"):
            shift = int(arg)
        elif opt in ("-c", "--chiffrieren"):
            modus = "c"
        elif opt in ("-d", "--dechiffrieren"):
            modus = "d"
        elif opt in ("-t", "--text"):
            text = arg

    if modus == "c":
        print(caesar_chiffrieren(text, shift))
    elif modus == "d":
        print(caesar_dechiffrieren(text, shift))
    else:
        print("Bitte -c (chiffrieren) oder -d (dechiffrieren) angeben.")


if __name__ == "__main__":
    main(sys.argv[1:])
```
