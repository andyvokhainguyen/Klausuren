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
        pass

    def inorder_ausgabe(self):
        """
        Gibt alle Wörter in der Inorder-Reihenfolge der Längen aus:
        links → mitte → aktueller Knoten → rechts
        """
        self._inorder_ausgabe_rekursiv(self.wurzel)

    def _inorder_ausgabe_rekursiv(self, knoten):
        if knoten is not None:
            pass



baum = TernaererSuchbaum()
woerter = ["Cat", "Hello", "Hi", "Dog", "World", "Python"]

for wort in woerter:
    baum.einfuegen(wort)

print("Inorder-Ausgabe der Wörter:")
baum.inorder_ausgabe()