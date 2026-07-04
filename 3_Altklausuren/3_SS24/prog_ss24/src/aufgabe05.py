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
        # a) BST-Regel: kleinere Schluessel nach links, groessere nach rechts.
        if key < node.val:
            if node.left is None:
                node.left = Node(key)          # freier Platz -> hier einfuegen
            else:
                self._insert_rekursiv(node.left, key)   # sonst links weiter
        else:
            if node.right is None:
                node.right = Node(key)         # freier Platz -> hier einfuegen
            else:
                self._insert_rekursiv(node.right, key)  # sonst rechts weiter

    def print_tree(self):
        """
        Gibt die Keys des Baums in aufsteigender Reihenfolge aus
        """
        # b) In-order-Traversierung (links -> Knoten -> rechts) liefert die
        #    Schluessel eines BST automatisch in aufsteigender Reihenfolge.
        self._print_rekursiv(self.root)

    def _print_rekursiv(self, node):
        if node is not None:
            self._print_rekursiv(node.left)    # 1. linker Teilbaum
            print(node.val)                    # 2. aktueller Knoten
            self._print_rekursiv(node.right)   # 3. rechter Teilbaum

# Verwendung
bst = BinarySearchTree()
elements = [20, 10, 30, 5, 15, 25, 35]
for elem in elements:
    bst.insert(elem)

bst.print_tree()
