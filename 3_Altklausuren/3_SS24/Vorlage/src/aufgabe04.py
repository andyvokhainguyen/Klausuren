"""
Aufgabe 4 - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""


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


# Beispielaufruf
string1 = "***\n * \n   "
string2 = "   \n * \n***"

print(combine_images(string1, string2, "or"))
