"""
Aufgabe 7 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""

# Teilaufgabe c) Erweiterung auf eine DOPPELT verkettete Liste:
# Der Node bekommt zusaetzlich einen Verweis auf das vorherige Element (prev),
# und beim Einfuegen werden die prev-Zeiger mitgepflegt. Die Loesungen fuer
# a) get(i) und b) insertAfterElement sind hier bereits enthalten.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None          # c) Rueckwaerts-Verweis (doppelt verkettet)


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        # am Ende anfuegen und dabei prev setzen (c)
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            neuer_knoten = Node(data)
            neuer_knoten.prev = current      # c) Rueckwaerts-Verweis
            current.next = neuer_knoten

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # a) Gibt das i-te Element (0-basiert) der Liste zurueck.
    def get(self, i):
        current = self.head
        zaehler = 0
        while current:
            if zaehler == i:
                return current.data
            current = current.next
            zaehler += 1
        # Index ausserhalb der Liste
        raise IndexError("Index liegt ausserhalb der Liste")

    # b) Fuegt 'data' als neues Element direkt NACH dem Knoten mit Wert
    #    'element' ein. prev/next werden korrekt umgehaengt (c).
    def insertAfterElement(self, element, data):
        current = self.head
        while current:
            if current.data == element:
                neuer_knoten = Node(data)
                neuer_knoten.prev = current
                neuer_knoten.next = current.next
                if current.next is not None:     # nicht am Ende der Liste
                    current.next.prev = neuer_knoten
                current.next = neuer_knoten
                return
            current = current.next
        raise ValueError("Element nicht in der Liste enthalten")


# Nutzungsbeispiel der verlinkten Liste
linked_list = LinkedList()
linked_list.insert("A")
linked_list.insert("B")
linked_list.insert("C")
linked_list.print_list()

print("get(1):", linked_list.get(1))          # -> B
linked_list.insertAfterElement("A", "X")       # X zwischen A und B einfuegen
linked_list.print_list()                       # -> A X B C
