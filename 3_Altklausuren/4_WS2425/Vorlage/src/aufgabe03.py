"""
Aufgabe 3 - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

def fehlerhafte_berechnung(liste, index):
    """
    Nimmt an: liste ist eine Liste von Zahlen, index ist die Position des zu teilenden Werts.
    Gibt zurück: Den Wert an der gegebenen Indexposition, geteilt durch eine Benutzereingabe.
    """
    wert = liste[index] 

    eingabe = input("Geben Sie eine Zahl zum Dividieren ein: ")  
    zahl = int(eingabe) 
    
    ergebnis = wert / zahl

    print("Ergebnis:", ergebnis)

    return ergebnis

# Beispielaufruf
liste = [10, 20, 30, 40]
index = int(input("Geben Sie den Index ein: "))  
fehlerhafte_berechnung(liste, index)