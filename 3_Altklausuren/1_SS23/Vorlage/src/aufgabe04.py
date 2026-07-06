"""
Aufgabe 4 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

# Aufruf des Tests in der Kommandozeile mit folgendem Befehl: python -m pytest -v
# Alternativ links in Visual Studio Code die Test-Umgebung öffnen (Klick auf das Reagenzglas)

def bmi_klassifizierung(gewicht, groesse):
    
    bmi = gewicht / (groesse**2)

    if bmi < 18.5:
        return "Untergewicht"
    elif bmi < 25:
        return "Normalgewicht"
    elif bmi < 30:
        return "Übergewicht"
    else:
        return "Adipositas"


def addiere_positive_zahlen(zahlenliste):
    summe = 0
    for zahl in zahlenliste:
        if zahl > 0:
            summe += zahl
    return summe
