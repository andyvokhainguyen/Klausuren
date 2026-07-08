"""
Aufgabe 5 - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999

Hinweis: In der Original-Klausur war das Node-Geruest mit `key`/`self.val`
vorgegeben. Hier zur einheitlichen Uebersicht auf `data`/`self.data` umgestellt
(gleiche Datenstruktur, nur andere Bezeichner). In der echten Klausur die
vorgegebenen Namen verwenden!
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
        # a) BST-Regel: kleinere Werte nach links, groessere nach rechts.
        if data < node.data:
            if node.left is None:
                node.left = Node(data)          # freier Platz -> hier einfuegen
            else:
                self._insert_rekursiv(node.left, data)   # sonst links weiter
        else:
            if node.right is None:
                node.right = Node(data)         # freier Platz -> hier einfuegen
            else:
                self._insert_rekursiv(node.right, data)  # sonst rechts weiter

    def print_tree(self):
        """
        Gibt die Werte des Baums in aufsteigender Reihenfolge aus
        """
        # b) In-order-Traversierung (links -> Knoten -> rechts) liefert die
        #    Werte eines BST automatisch in aufsteigender Reihenfolge.
        self._print_rekursiv(self.root)

    def _print_rekursiv(self, node):
        if node is not None:
            self._print_rekursiv(node.left)    # 1. linker Teilbaum
            print(node.data)                   # 2. aktueller Knoten
            self._print_rekursiv(node.right)   # 3. rechter Teilbaum

# Verwendung
bst = BinarySearchTree()
elements = [20, 10, 30, 5, 15, 25, 35]
for elem in elements:
    bst.insert(elem)

bst.print_tree()
