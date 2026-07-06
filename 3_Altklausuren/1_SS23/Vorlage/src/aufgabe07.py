"""
Aufgabe 7 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


# Nutzungsbeispie der verlinkten Liste
linked_list = LinkedList()
linked_list.insert("A")
linked_list.insert("B")
linked_list.insert("C")
linked_list.print_list()
