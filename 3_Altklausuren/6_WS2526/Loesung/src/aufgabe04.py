"""
Aufgabe 4 - Klausur Programmierung WS2025/26
"""


class Node:
    def __init__(self):
        self.kinder = {}  # dict[str, Node]
        self.ist_wortende = False


class Trie:
    def __init__(self):
        self.wurzel = Node()

    def einfuegen(self, wort):
        """
        Fuegt ein Wort in den Trie ein.
        """
        aktueller = self.wurzel
        for ch in wort:
            if ch not in aktueller.kinder:
                aktueller.kinder[ch] = Node()
            aktueller = aktueller.kinder[ch]
        aktueller.ist_wortende = True

    def enthaelt(self, wort):
        """
        True, wenn wort vollstaendig enthalten ist (ist_wortende am Ende).
        """
        aktueller = self.wurzel
        for ch in wort:
            if ch not in aktueller.kinder:
                return False
            aktueller = aktueller.kinder[ch]
        return aktueller.ist_wortende

    def woerter_mit_praefix(self, praefix):
        """
        Liefert alle Woerter, die mit praefix beginnen, alphabetisch sortiert.

        Teilaufgabe b): Ist praefix leer, wird die for-Schleife unten kein
        einziges Mal durchlaufen, sodass `aktueller` unveraendert auf
        self.wurzel bleibt. _sammle_woerter wird dann direkt ab der Wurzel
        aufgerufen und sammelt dadurch bereits alle Woerter im gesamten
        Trie ein - alphabetisch sortiert, da _sammle_woerter die Kinder
        jedes Knotens ueber sorted(...) durchlaeuft. Es ist daher keine
        Sonderbehandlung fuer den leeren Praefix noetig.
        """
        aktueller = self.wurzel
        for ch in praefix:
            if ch not in aktueller.kinder:
                return []
            aktueller = aktueller.kinder[ch]

        ergebnis = []
        self._sammle_woerter(aktueller, praefix, ergebnis)
        return ergebnis

    def _sammle_woerter(self, knoten, gebaut, ergebnis):
        """
        Hilfsfunktion: sammelt ab knoten alle Woerter ein.
        gebaut ist das bisher aufgebaute Wort.
        """
        if knoten.ist_wortende:
            ergebnis.append(gebaut)
        for ch in sorted(knoten.kinder.keys()):
            self._sammle_woerter(knoten.kinder[ch], gebaut + ch, ergebnis)


trie = Trie()
woerter = ["cat", "car", "cart", "dog", "dot", "dove"]
for w in woerter:
    trie.einfuegen(w)

print(trie.woerter_mit_praefix("ca"))
print(trie.woerter_mit_praefix("do"))
print(trie.enthaelt("car"), trie.enthaelt("care"))
