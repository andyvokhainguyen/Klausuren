"""
Übung 03: Datei lesen & schreiben (Datei-IO, Skript 04)

Übe beide Grundformen: Datei schreiben ("w") und zeilenweise lesen ("r").
"""


def lies_datei_zeilenweise(dateiname):
    # ✍️ SELBST: mit `with open(dateiname, "r", encoding="utf-8") as f:`
    #   for zeile in f:  leere Zeilen überspringen, sonst print(zeile.strip())
    with open(dateiname, "r", encoding="utf-8") as f:
        for zeile in f:
            if zeile.strip() == "":
                continue
            print(zeile.strip())
    

def schreibe_datei(dateiname):
    # ✍️ SELBST: mit `with open(dateiname, "w", encoding="utf-8") as f:`
    #   drei Zeilen schreiben, z.B. "Apfel\n", "Banane\n", "Kirsche\n"
    #   (Denk dran: \n selbst anhängen!)
    with open(dateiname, "w", encoding="utf-8") as f:
        f.write("Apfel\n")
        f.write("Banane\n")
        f.write("Kirsche\n")





# Zum Nachschlagen – die "kurze" Skript-Form ohne with:
#   f = open("datei.txt", "r"); print(f.read()); f.close()
#   f = open("datei.txt", "w"); f.write("Text"); f.close()


# Testaufruf
schreibe_datei("demo.txt")
lies_datei_zeilenweise("demo.txt")     # erwartet: Apfel / Banane / Kirsche (untereinander)
