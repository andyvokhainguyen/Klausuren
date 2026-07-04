"""
Aufgabe 5 - Klausur Programmierung

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # a) Neues Element am Ende einfuegen; letzter Knoten zeigt wieder auf head.
    def insert(self, key):
        neuer_knoten = Node(key)
        if self.head is None:
            self.head = neuer_knoten
            neuer_knoten.next = self.head       # einziger Knoten zeigt auf sich selbst
        else:
            current = self.head
            while current.next != self.head:    # bis zum letzten Knoten laufen
                current = current.next
            current.next = neuer_knoten
            neuer_knoten.next = self.head        # Kreis wieder schliessen

    # b) Element mit dem Wert key entfernen (Kreis bleibt erhalten).
    def delete(self, key):
        if self.head is None:
            return

        # Fall 1: der head-Knoten enthaelt den Wert
        if self.head.data == key:
            if self.head.next == self.head:      # nur ein einziges Element
                self.head = None
                return
            # letzten Knoten suchen (der auf head zeigt) und umhaengen
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = self.head.next
            last.next = self.head
            return

        # Fall 2: Wert liegt in der Mitte/am Ende
        current = self.head
        while current.next != self.head:
            if current.next.data == key:
                current.next = current.next.next  # Knoten ueberspringen
                return
            current = current.next

    # c) Liste einmal komplett ausgeben, ohne Endlosschleife.
    def display(self):
        if self.head is None:
            print("Liste ist leer")
            return
        current = self.head
        while True:
            print(current.data)
            current = current.next
            if current == self.head:             # wieder am Anfang -> Abbruch
                break


# Anwendungsbeispiel
cll = CircularLinkedList()
for wert in ["A", "B", "C", "D"]:
    cll.insert(wert)
cll.display()          # A B C D
print("--- nach delete('B') ---")
cll.delete("B")
cll.display()          # A C D
