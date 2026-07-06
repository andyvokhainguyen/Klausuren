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

    def pop(self):
        """Entfernt und gibt das oberste Element des Stacks zurück."""
        raise NotImplementedError

    def peek(self):
        """Gibt das oberste Element des Stacks zurück, ohne es zu entfernen."""
        raise NotImplementedError

    def is_empty(self):
        """Gibt True zurück, wenn der Stack leer ist, sonst False."""
        raise NotImplementedError

    def display(self):
        """Zeigt alle Elemente im Stack an."""
        raise NotImplementedError
