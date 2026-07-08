"""
Übung 11: Doppelt verkettete Liste (Skript-Übung)

Aus der einfach verketteten Liste ableiten: Node bekommt zusätzlich .prev.
"""


class Node:
    def __init__(self, data):
        self.data = data
        # ✍️ SELBST: zusätzlich self.prev = None   (das ist der Unterschied!)
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        # ✍️ SELBST: am Ende anhängen UND neuer.prev = letzter Knoten setzen
        neuer = Node(data)
        if self.head is None:
            self.head = neuer
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = neuer
        neuer.prev = current

    def print_vorwaerts(self):
        # ✍️ SELBST: von head über .next bis None ausgeben
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def print_rueckwaerts(self):
        # ✍️ SELBST: bis ans Ende laufen, dann über .prev rückwärts ausgeben
        current = self.head
        if current is None:
            return
        while current.next is not None:
            current = current.next
        while current is not None:
            print(current.data)
            current = current.prev


# Testaufruf
dll = DoublyLinkedList()
for x in ["A", "B", "C"]:
    dll.insert(x)
print("vorwaerts:")
dll.print_vorwaerts()        # erwartet: A B C
print("rueckwaerts:")
dll.print_rueckwaerts()      # erwartet: C B A
