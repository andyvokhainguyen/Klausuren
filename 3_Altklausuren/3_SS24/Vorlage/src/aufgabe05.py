"""
Aufgabe 5 - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999

Hinweis: Original-Klausur gab `key`/`self.val` vor - hier zur einheitlichen
Uebersicht auf `data`/`self.data` umgestellt.
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        Fügt ein neues Element mit dem gegebenen Wert ein.
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_rekursiv(self.root, data)

    def _insert_rekursiv(self, node, data):
        pass

    def print_tree(self):
        """
        Gibt die Werte des Baums in aufsteigender Reihenfolge aus
        """
        pass

# Verwendung
bst = BinarySearchTree()
elements = [20, 10, 30, 5, 15, 25, 35]
for elem in elements:
    bst.insert(elem)

bst.print_tree()
