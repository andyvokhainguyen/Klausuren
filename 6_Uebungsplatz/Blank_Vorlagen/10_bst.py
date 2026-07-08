"""
Übung 10: Binärer Suchbaum (SS24-Stil, + delete aus Skript 05)

Gegeben: Node, __init__, insert-Wrapper.
Selbst:  _insert, print_tree (+ _print_tree), search, delete.
"""


class Node:                                  # 🟩
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:                            # 🟩
    def __init__(self):                      # 🟩
        self.root = None

    def insert(self, data):                  # 🟩 Wrapper vorgegeben
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        # ✍️ SELBST: rekursiv - data < node.data -> links, sonst rechts;
        #            Platz None -> Node(data), sonst rekursiv weiter
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)

        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def print_tree(self):
        # ✍️ SELBST: Wrapper -> self._print_tree(self.root), falls root vorhanden
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        # ✍️ SELBST: In-order: links -> print(node.data) -> rechts (= sortiert)
        if node is not None:
            self._print_tree(node.left)
            print(node.data)
            self._print_tree(node.right)

    def search(self, data):
        # ✍️ SELBST: True/False - rekursiv links/rechts absteigen
        return self._search(data, self.root)
    
    def _search(self, data, node):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search(data, node.left)
        else:
            return self._search(data, node.right)

    def delete(self, data):
        # ✍️ SELBST (schwieriger, aus Skript): self.root = self._delete(self.root, data)
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        # ✍️ SELBST: 3 Fälle - Blatt / ein Kind / zwei Kinder (kleinsten rechts holen)
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._find_min(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)
        return node

    def _find_min(self, node):
        if node.left is None:
            return node
        return self._find_min(node.left)


# Testaufruf
bst = BinaryTree()
for x in [20, 10, 30, 5, 15, 25, 35]:
    bst.insert(x)
bst.print_tree()             # erwartet: 5 10 15 20 25 30 35 (aufsteigend)
