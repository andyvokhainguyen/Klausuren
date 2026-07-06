"""
Aufgabe 5 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    # a) --------------------------------------------------------------------
    def pop(self):
        """Entfernt und gibt das oberste Element des Stacks zurück."""
        if self.is_empty():
            return None
        # oberstes Element = letztes Listenelement (LIFO)
        return self.stack.pop()

    def peek(self):
        """Gibt das oberste Element des Stacks zurück, ohne es zu entfernen."""
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        """Gibt True zurück, wenn der Stack leer ist, sonst False."""
        return len(self.stack) == 0

    def display(self):
        """Zeigt alle Elemente im Stack an."""
        print(self.stack)

    # b) --------------------------------------------------------------------
    def get(self, i):
        """Gibt das i-te Element des Stacks zurück (0-basiert)."""
        if i < 0 or i >= len(self.stack):
            raise IndexError("Index liegt ausserhalb des Stacks")
        return self.stack[i]

    # c) 'del' ist ein reserviertes Python-Schluesselwort und kann nicht als
    #    Methodenname verwendet werden -> Methode heisst hier 'delete'.
    def delete(self, i):
        """Entfernt das i-te Element des Stacks (0-basiert)."""
        if i < 0 or i >= len(self.stack):
            raise IndexError("Index liegt ausserhalb des Stacks")
        del self.stack[i]


# Anwendungsbeispiel
s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.display()              # ['A', 'B', 'C']
print("peek:", s.peek())  # C
print("pop:", s.pop())    # C
print("get(0):", s.get(0))  # A
s.delete(0)              # entfernt A
s.display()              # ['B']
print("is_empty:", s.is_empty())  # False
