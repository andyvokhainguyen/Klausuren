"""
Aufgabe 4 - Klausur Programmierung
"""
class Node:
    def __init__(self, wort):
        self.wort = wort
        self.links = None
        self.mitte = None
        self.rechts = None


class TernaererSuchbaum:
    def __init__(self):
        self.wurzel = None

    def einfuegen(self, wort):
        """
        Fügt ein Wort entsprechend seiner Länge in den ternären Suchbaum ein.
        - kürzer -> links
        - gleich lang -> mitte
        - länger -> rechts
        """
        if self.wurzel is None:
            self.wurzel = Node(wort)
        else:
            self._einfuegen_rekursiv(self.wurzel, wort)

    def _einfuegen_rekursiv(self, aktueller_knoten, wort):
        if len(wort) < len(aktueller_knoten.wort):
            if aktueller_knoten.links is None:
                aktueller_knoten.links = Node(wort)
            else:
                self._einfuegen_rekursiv(aktueller_knoten.links, wort)
        elif len(wort) == len(aktueller_knoten.wort):
            if aktueller_knoten.mitte is None:
                aktueller_knoten.mitte = Node(wort)
            else:
                self._einfuegen_rekursiv(aktueller_knoten.mitte, wort)
        else:
            if aktueller_knoten.rechts is None:
                aktueller_knoten.rechts = Node(wort)
            else:
                self._einfuegen_rekursiv(aktueller_knoten.rechts, wort)

    def inorder_ausgabe(self):
        """
        Gibt alle Wörter in der Inorder-Reihenfolge der Längen aus:
        links → mitte → aktueller Knoten → rechts
        """
        self._gesammelte_woerter = []
        self._inorder_ausgabe_rekursiv(self.wurzel)
        print(", ".join(self._gesammelte_woerter))

    def _inorder_ausgabe_rekursiv(self, knoten):
        if knoten is not None:
            self._inorder_ausgabe_rekursiv(knoten.links)
            self._inorder_ausgabe_rekursiv(knoten.mitte)
            self._gesammelte_woerter.append(knoten.wort)
            self._inorder_ausgabe_rekursiv(knoten.rechts)



baum = TernaererSuchbaum()
woerter = ["Cat", "Hello", "Hi", "Dog", "World", "Python"]

for wort in woerter:
    baum.einfuegen(wort)

print("Inorder-Ausgabe der Wörter:")
baum.inorder_ausgabe()