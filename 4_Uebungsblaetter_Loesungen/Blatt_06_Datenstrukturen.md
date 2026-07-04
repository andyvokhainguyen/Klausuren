# Lösungen – Übungsblatt 6 (Queue, Stack, BST)

Datenstruktur-Aufgaben im Klausurformat. **Queue** ist ein heißer Klausurkandidat (nie in einer Altklausur, aber hier geübt).

---

## Aufgabe 1 – Druckerwarteschlange als Queue (FIFO)

```python
class PrintQueue:
    def __init__(self):
        self.queue = []

    # Druckauftrag hinten anfügen
    def enqueue(self, print_job):
        self.queue.append(print_job)

    # ersten Druckauftrag entfernen und zurückgeben (FIFO)
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)          # pop(0) = vorne!

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# Nutzung
pq = PrintQueue()
pq.enqueue("Dokument1")
pq.enqueue("Dokument2")
print(f"Größe der Warteschlange nach dem Hinzufügen: {pq.size()}")   # 2
removed = pq.dequeue()
print(f"Entfernt: {removed}, Größe der Warteschlange: {pq.size()}")  # Dokument1, 1
print(f"Ist die Warteschlange leer? {pq.is_empty()}")               # False
pq.dequeue()
print(f"Ist die Warteschlange leer nach dem Entfernen? {pq.is_empty()}")  # True
```

---

## Aufgabe 2 – Klammer-Check mit Stack

```python
def ist_korrekt_geklammert(ausdruck):
    stack = []                                   # Liste als Stack (append/pop)
    paare = {")": "(", "]": "[", "}": "{"}       # schließend -> passend öffnend
    oeffnend = set(paare.values())               # {'(', '[', '{'}

    for zeichen in ausdruck:
        if zeichen in oeffnend:
            stack.append(zeichen)                # Öffnungsklammer merken (push)
        elif zeichen in paare:                   # Schließklammer
            # kein passendes Gegenstück offen? -> falsch
            if not stack or stack.pop() != paare[zeichen]:
                return False
    return len(stack) == 0                        # alle geöffneten wieder geschlossen?


# Nutzung
while True:
    ausdruck = input("Geben Sie einen mathematischen Ausdruck ein oder 'exit': ")
    if ausdruck == "exit":
        break
    if ist_korrekt_geklammert(ausdruck):
        print("Der Ausdruck ist korrekt geklammert.")
    else:
        print("Der Ausdruck ist nicht korrekt geklammert.")
```
Beispiele: `{[()]}` → korrekt · `{[()}` → nicht korrekt · `((3+2)*5-(7*12))/15` → korrekt.

**Warum ein Stack?** Die zuletzt geöffnete Klammer muss zuerst geschlossen werden = **LIFO**.

---

## Aufgabe 3 – Netzwerksimulation: Router mit Queue (eingehend) + Stack (ausgehend)

```python
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return None if self.is_empty() else self.items.pop(0)
    def is_empty(self):
        return len(self.items) == 0


class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return None if self.is_empty() else self.items.pop()   # letztes Element
    def is_empty(self):
        return len(self.items) == 0


class Packet:
    def __init__(self, packet_id, ziel_id):
        self.packet_id = packet_id
        self.ziel_id = ziel_id


class Router:
    def __init__(self, router_id):
        self.router_id = router_id
        self.incoming = Queue()   # eingehende Pakete: FIFO
        self.outgoing = Stack()   # ausgehende Pakete: LIFO

    # Paket empfangen -> in die Eingangs-Queue
    def receive_packet(self, packet):
        print(f"Router {self.router_id}: Paket {packet.packet_id} empfangen")
        self.incoming.enqueue(packet)

    # eingehende Queue in den ausgehenden Stack umkopieren
    def process_incoming_packets(self):
        while not self.incoming.is_empty():
            paket = self.incoming.dequeue()
            self.outgoing.push(paket)

    # zuletzt angekommenes Paket zuerst weitersenden (LIFO)
    def send_packet(self, ziel_router):
        paket = self.outgoing.pop()
        if paket is None:
            print(f"Router {self.router_id}: keine Pakete zum Senden")
            return
        print(f"Router {self.router_id} sendet Paket {paket.packet_id} "
              f"an Router {ziel_router.router_id}")
        ziel_router.receive_packet(paket)


# Kleines Netzwerk
router_a = Router("A")
router_b = Router("B")
router_c = Router("C")

packet1 = Packet(1, "C")
packet2 = Packet(2, "C")

router_a.receive_packet(packet1)
router_b.receive_packet(packet2)

router_a.process_incoming_packets()
router_a.send_packet(router_b)

router_b.process_incoming_packets()
router_b.send_packet(router_c)
```

---

## Aufgabe 4 – Bücherverwaltung mit Binärem Suchbaum (Ordnung nach ISBN)

```python
class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author


class Node:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # (1) Buch sortiert nach ISBN einfügen
    def insert(self, book):
        if self.root is None:
            self.root = Node(book)
        else:
            self._insert(self.root, book)

    def _insert(self, node, book):
        if book.isbn < node.book.isbn:
            if node.left is None:
                node.left = Node(book)
            else:
                self._insert(node.left, book)
        else:
            if node.right is None:
                node.right = Node(book)
            else:
                self._insert(node.right, book)

    # (2) Buch nach ISBN suchen -> Book oder None
    def search(self, isbn):
        return self._search(self.root, isbn)

    def _search(self, node, isbn):
        if node is None:
            return None
        if isbn == node.book.isbn:
            return node.book
        elif isbn < node.book.isbn:
            return self._search(node.left, isbn)
        else:
            return self._search(node.right, isbn)

    # (3) Buch nach ISBN entfernen
    def delete(self, isbn):
        self.root = self._delete(self.root, isbn)

    def _delete(self, node, isbn):
        if node is None:
            return None
        if isbn < node.book.isbn:
            node.left = self._delete(node.left, isbn)
        elif isbn > node.book.isbn:
            node.right = self._delete(node.right, isbn)
        else:
            # Knoten gefunden
            if node.left is None:
                return node.right          # 0/1 Kind
            elif node.right is None:
                return node.left
            # zwei Kinder: kleinsten Knoten im rechten Teilbaum als Ersatz
            min_node = self._find_min(node.right)
            node.book = min_node.book
            node.right = self._delete(node.right, min_node.book.isbn)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node


# (4) Bücher nach ISBN sortiert ausgeben (In-order) — eigenständige Funktion
def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(f"ISBN: {node.book.isbn}, Titel: {node.book.title}, Autor: {node.book.author}")
        in_order_traversal(node.right)


# Beispieldaten
book1 = Book("123", "Harry Potter", "J.K. Rowling")
book2 = Book("789", "The Hobbit", "J.R.R. Tolkien")
book3 = Book("456", "The Da Vinci Code", "Dan Brown")

bst = BinarySearchTree()
bst.insert(book1)
bst.insert(book2)
bst.insert(book3)

print("Bücher in sortierter Reihenfolge:")
in_order_traversal(bst.root)        # 123, 456, 789

isbn_to_search = "789"
book = bst.search(isbn_to_search)
if book:
    print(f"Buch gefunden: ISBN: {book.isbn}, Titel: {book.title}, Autor: {book.author}")
else:
    print("Buch nicht gefunden")
```
> ISBN sind hier **Strings** → sie werden lexikografisch verglichen (`"123" < "456" < "789"`).

---

## Aufgabe 5 – Performance: sortierte doppelt verkettete Liste vs. BST

Idee: beide Strukturen mit z.B. `n = 10000` Zufallszahlen füllen und **Einfügen / Löschen / Suchen** mit `time` messen.

```python
import time
import random

zahlen = random.sample(range(1, 1000000), 10000)

start = time.time()
# ... Operation auf Struktur A (sortierte Liste) ...
dauer_a = time.time() - start

start = time.time()
# ... Operation auf Struktur B (BST) ...
dauer_b = time.time() - start
```

**Erwartetes Ergebnis (Begründung):**
| Operation | sortierte (doppelt) verkettete Liste | Binärer Suchbaum |
|---|---|---|
| Suchen | O(n) – kein Direktzugriff, muss durchlaufen | O(log n) (ausgeglichen) |
| Einfügen (sortiert) | O(n) – Position suchen | O(log n) |
| Löschen | O(n) | O(log n) |

➡️ Der **BST ist bei großen Datenmengen deutlich schneller**, weil er bei jedem Schritt den halben Suchraum verwirft (logarithmisch). Die verkettete Liste muss dagegen im Schnitt die halbe Liste durchlaufen (linear). *Achtung:* ein **unausgeglichener** BST kann im schlechtesten Fall auf O(n) entarten.

---

## Merksatz Datenstrukturen
| Struktur | Prinzip | Einfügen | Entfernen |
|---|---|---|---|
| **Queue** | FIFO | `append` (hinten) | `pop(0)` (vorne) |
| **Stack** | LIFO | `append`/`push` | `pop()`/`[-1]` (hinten) |
| **BST** | links < Knoten ≤ rechts | rekursiv per `_insert` | `_delete` + `_find_min` |
