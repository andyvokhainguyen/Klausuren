"""
Aufgabe 4 - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

import sys
import getopt


def combine_images(image1, image2, function):
    combined_image = ""

    if function == "and":
        for i in range(len(image1)):
            if image1[i] == "*" and image2[i] == "*":
                combined_image += "*"
            elif image1[i] == "\n" and image2[i] == "\n":
                combined_image += "\n"
            else:
                combined_image += " "
    elif function == "or":
        for i in range(len(image1)):
            if image1[i] == "*" or image2[i] == "*":
                combined_image += "*"
            elif image1[i] == "\n" and image2[i] == "\n":
                combined_image += "\n"
            else:
                combined_image += " "

    return combined_image + "\n"


def main(argv):
    bild1 = ""
    bild2 = ""
    funktion = ""
    output = ""

    # Kommandozeilenargumente mit getopt einlesen (wie in der Aufgabe gefordert)
    try:
        opts, args = getopt.getopt(
            argv,
            "h",
            ["bild1=", "bild2=", "funktion=", "output=", "help"],
        )
    except getopt.GetoptError:
        print("aufgabe04.py --bild1 <name1> --bild2 <name2> "
              "--funktion <and|or> --output <name3>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("aufgabe04.py --bild1 <name1> --bild2 <name2> "
                  "--funktion <and|or> --output <name3>")
            sys.exit()
        elif opt == "--bild1":
            bild1 = arg
        elif opt == "--bild2":
            bild2 = arg
        elif opt == "--funktion":
            funktion = arg
        elif opt == "--output":
            output = arg

    # Beide Eingabebilder einlesen
    with open(bild1, "r", encoding="utf-8") as f1:
        image1 = f1.read()
    with open(bild2, "r", encoding="utf-8") as f2:
        image2 = f2.read()

    # Bilder verknuepfen und Ergebnis in die Ausgabedatei schreiben
    ergebnis = combine_images(image1, image2, funktion)
    with open(output, "w", encoding="utf-8") as f_out:
        f_out.write(ergebnis)


if __name__ == "__main__":
    main(sys.argv[1:])
