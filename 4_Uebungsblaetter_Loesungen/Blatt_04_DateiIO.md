# Lösungen – Übungsblatt 4 (Datei-Handling und IO)

---

## Aufgabe 1 – Caesar: Textdatei zeilenweise ver-/entschlüsseln (Datei → Datei)

Aufruf: `python3 verschluesele_text.py -i <infile> -o <outfile> -s <shift> -c/-d`

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
    infile = outfile = ""
    shift = 0
    modus = ""

    try:
        opts, args = getopt.getopt(
            argv, "i:o:s:cdh",
            ["infile=", "outfile=", "shift=", "chiffrieren", "dechiffrieren", "help"]
        )
    except getopt.GetoptError:
        print("verschluesele_text.py -i <infile> -o <outfile> -s <shift> -c/-d")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("verschluesele_text.py -i <infile> -o <outfile> -s <shift> -c/-d")
            sys.exit()
        elif opt in ("-i", "--infile"):
            infile = arg
        elif opt in ("-o", "--outfile"):
            outfile = arg
        elif opt in ("-s", "--shift"):
            shift = int(arg)
        elif opt in ("-c", "--chiffrieren"):
            modus = "c"
        elif opt in ("-d", "--dechiffrieren"):
            modus = "d"

    with open(infile, "r", encoding="utf-8") as ein, \
         open(outfile, "w", encoding="utf-8") as aus:
        for zeile in ein:
            if modus == "c":
                aus.write(caesar_chiffrieren(zeile, shift))
            elif modus == "d":
                aus.write(caesar_dechiffrieren(zeile, shift))


if __name__ == "__main__":
    main(sys.argv[1:])
```

---

## Aufgabe 2 – Ausgabe der Code-Snippets erklären (Dateien sind Streams!)

Kernprinzip: Eine geöffnete Datei ist ein **Stream mit Lesezeiger**. Jeder Lesevorgang bewegt den Zeiger weiter; ein erneutes Lesen beginnt **dort, wo der letzte aufhörte** (nicht von vorne).

**Snippet 1**
```python
f = open("morgenstern.txt", "r")
print(f.read())        # gibt den GESAMTEN Inhalt aus; Zeiger steht danach am ENDE
print("Kürzere Ausgabe, nur erste Zeile:")
print(f.read(12))      # Zeiger ist schon am Ende -> liefert "" (leere Zeile!)
f.close()
```
→ Ganzer Text, dann die Zwischenzeile, dann eine **leere Zeile**. Der beschriftete „nur erste Zeile" ist irreführend – es kommt nichts mehr.

**Snippet 2**
```python
f = open("morgenstern.txt", "r")
print(f.readline())    # nur die ERSTE Zeile (inkl. Zeilenumbruch)
print("Stopp!")
print(f.read(4))       # die nächsten 4 Zeichen ab Position hinter Zeile 1
print("Stopp!")
print(f.read())        # der komplette RESTliche Inhalt
f.close()
```
→ Erste Zeile, „Stopp!", 4 Zeichen, „Stopp!", Rest der Datei. Der Zeiger wandert kontinuierlich weiter.

**Snippet 3**
```python
f = open("morgenstern.txt", "r")
print(f.read(12))      # die ersten 12 Zeichen
print("Stopp!")
print(f.read())        # der Rest ab Zeichen 13 bis zum Ende
f.close()
```
→ Erste 12 Zeichen, „Stopp!", dann der restliche Text.

---

## Aufgabe 3 – `textstatistik.py` (getopt, -w/-z/-l/-h + Ausgabedatei)

Achtung: `-h` bedeutet hier **häufigstes Wort** (nicht Hilfe!).

```python
import sys
import getopt


def main(argv):
    inputfile = ""
    outputfile = ""
    zeige_wort = zeige_zeichen = zeige_zeilen = zeige_haeufig = False

    try:
        opts, args = getopt.getopt(
            argv, "wzlh",
            ["inputfile=", "outputfile=", "wortanzahl", "zeichenanzahl",
             "zeilenanzahl", "haeufigsteswort"]
        )
    except getopt.GetoptError:
        print("Fehlerhafte Eingabe")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "--inputfile":
            inputfile = arg
        elif opt == "--outputfile":
            outputfile = arg
        elif opt in ("-w", "--wortanzahl"):
            zeige_wort = True
        elif opt in ("-z", "--zeichenanzahl"):
            zeige_zeichen = True
        elif opt in ("-l", "--zeilenanzahl"):
            zeige_zeilen = True
        elif opt in ("-h", "--haeufigsteswort"):
            zeige_haeufig = True

    with open(inputfile, "r", encoding="utf-8") as f:
        inhalt = f.read()

    woerter = inhalt.split()
    zeilen = inhalt.splitlines()

    ausgaben = []
    if zeige_wort:
        ausgaben.append(f"Wortanzahl: {len(woerter)}")
    if zeige_zeichen:
        ausgaben.append(f"Zeichenanzahl: {len(inhalt)}")
    if zeige_zeilen:
        ausgaben.append(f"Zeilenanzahl: {len(zeilen)}")
    if zeige_haeufig:
        haeufigkeit = {}
        for w in woerter:
            haeufigkeit[w] = haeufigkeit.get(w, 0) + 1
        haeufigstes = max(haeufigkeit, key=haeufigkeit.get)
        ausgaben.append(f"Häufigstes Wort: {haeufigstes} ({haeufigkeit[haeufigstes]}x)")

    text = "\n".join(ausgaben)
    print(text)

    if outputfile:
        with open(outputfile, "w", encoding="utf-8") as f:
            f.write(text + "\n")


if __name__ == "__main__":
    main(sys.argv[1:])
```
Aufruf z.B.: `python3 textstatistik.py --inputfile textdatei.txt --outputfile textstatistik.txt -w -z -l -h`

---

## Aufgabe 4 – `combinefiles.py` (getopt, and/or/xor/weave)

```python
import sys
import getopt


def combine_images(image1, image2, funktion):
    ergebnis = ""
    for i in range(len(image1)):
        c1 = image1[i]
        c2 = image2[i]
        if c1 == "\n" or c2 == "\n":
            ergebnis += "\n"
            continue
        if funktion == "and":                       # nur wenn BEIDE '*'
            ergebnis += "*" if (c1 == "*" and c2 == "*") else " "
        elif funktion == "or":                      # wenn MINDESTENS einer '*'
            ergebnis += "*" if (c1 == "*" or c2 == "*") else " "
        elif funktion == "xor":                     # wenn GENAU einer '*'
            ergebnis += "*" if (c1 == "*") != (c2 == "*") else " "
        elif funktion == "weave":                   # abwechselnd Bild1/Bild2
            ergebnis += c1 if i % 2 == 0 else c2
    return ergebnis


def main(argv):
    bild1 = bild2 = funktion = output = ""

    try:
        opts, args = getopt.getopt(argv, "h", ["bild1=", "bild2=", "funktion=", "output=", "help"])
    except getopt.GetoptError:
        print("combinefiles.py --bild1 <n1> --bild2 <n2> --funktion <and|or|xor|weave> --output <n3>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("combinefiles.py --bild1 <n1> --bild2 <n2> --funktion <and|or|xor|weave> --output <n3>")
            sys.exit()
        elif opt == "--bild1":
            bild1 = arg
        elif opt == "--bild2":
            bild2 = arg
        elif opt == "--funktion":
            funktion = arg
        elif opt == "--output":
            output = arg

    with open(bild1, "r", encoding="utf-8") as f:
        image1 = f.read()
    with open(bild2, "r", encoding="utf-8") as f:
        image2 = f.read()

    ergebnis = combine_images(image1, image2, funktion)

    # ohne --output: Ergebnis in die Datei von Bild 1 schreiben
    ziel = output if output else bild1
    with open(ziel, "w", encoding="utf-8") as f:
        f.write(ergebnis)


if __name__ == "__main__":
    main(sys.argv[1:])
```
