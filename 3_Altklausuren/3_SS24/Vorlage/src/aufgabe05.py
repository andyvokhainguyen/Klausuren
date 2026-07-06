"""
Aufgabe 5 - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Fügt ein neues Element mit dem gegebenen Schlüssel ein.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rekursiv(self.root, key)
            
    def _insert_rekursiv(self, node, key):
        pass 

    def print_tree(self):
        """
        Gibt die Keys des Baums in aufsteigender Reihenfolge aus
        """
        pass

# Verwendung
bst = BinarySearchTree()
elements = [20, 10, 30, 5, 15, 25, 35]
for elem in elements:
    bst.insert(elem)

bst.print_tree()
