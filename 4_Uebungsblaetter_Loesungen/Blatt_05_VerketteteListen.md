# Lösungen – Übungsblatt 5 (Array-Operationen, verkettete Listen, Texteditor)

---

## Aufgabe 1 – Automarken einfügen/löschen ohne `remove()`/`insert()`

```python
def einfuegen_marke(automarken, marke, i):
    """Fügt marke an Position i ein und gibt die neue Liste zurück."""
    return automarken[:i] + [marke] + automarken[i:]


def loeschen_marke(automarken, i):
    """Löscht das Element an Position i und gibt die neue Liste zurück."""
    return automarken[:i] + automarken[i + 1:]
```
**pytest:**
```python
from src import aufgabe01   # Pfad ggf. anpassen

def test_einfuegen_am_anfang():
    assert aufgabe01.einfuegen_marke(["A", "B"], "X", 0) == ["X", "A", "B"]

def test_einfuegen_in_der_mitte():
    assert aufgabe01.einfuegen_marke(["A", "B", "C"], "X", 1) == ["A", "X", "B", "C"]

def test_einfuegen_am_ende():
    assert aufgabe01.einfuegen_marke(["A", "B"], "X", 2) == ["A", "B", "X"]

def test_loeschen_erstes():
    assert aufgabe01.loeschen_marke(["A", "B", "C"], 0) == ["B", "C"]

def test_loeschen_mitte():
    assert aufgabe01.loeschen_marke(["A", "B", "C"], 1) == ["A", "C"]
```

---

## Aufgabe 2 – ToDo-Liste als einfach verkettete Liste

```python
class ToDoItem:
    def __init__(self, taskdescr, priority):
        self.taskdescr = taskdescr
        self.priority = priority


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class ToDoList:
    def __init__(self):
        self.head = None

    # ToDo mit Beschreibung + Priorität hinzufügen (am Ende)
    def add(self, taskdescr, priority):
        neuer = Node(ToDoItem(taskdescr, priority))
        if self.head is None:
            self.head = neuer
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = neuer

    # i-tes ToDo-Item zurückgeben (0-basiert)
    def get(self, i):
        current = self.head
        index = 0
        while current:
            if index == i:
                return current.item
            current = current.next
            index += 1
        raise IndexError("Index außerhalb der Liste")

    # i-tes ToDo-Item entfernen
    def delete(self, i):
        if self.head is None:
            return
        if i == 0:
            self.head = self.head.next
            return
        current = self.head
        index = 0
        while current.next and index < i - 1:
            current = current.next
            index += 1
        if current.next:
            current.next = current.next.next

    # Anzahl der ToDo-Items
    def count(self):
        anzahl = 0
        current = self.head
        while current:
            anzahl += 1
            current = current.next
        return anzahl

    # Liste aller ToDo-Items zurückgeben
    def list_all(self):
        ergebnis = []
        current = self.head
        while current:
            ergebnis.append((current.item.taskdescr, current.item.priority))
            current = current.next
        return ergebnis


# Nutzung
todo = ToDoList()
todo.add("Einkaufen", 2)
todo.add("Lernen", 1)
todo.add("Sport", 3)
print(todo.list_all())     # [('Einkaufen', 2), ('Lernen', 1), ('Sport', 3)]
print(todo.count())        # 3
print(todo.get(1).taskdescr)  # Lernen
todo.delete(0)
print(todo.list_all())     # [('Lernen', 1), ('Sport', 3)]
```
**pytest (Auszug):**
```python
def test_add_und_count():
    t = ToDoList(); t.add("A", 1); t.add("B", 2)
    assert t.count() == 2

def test_get():
    t = ToDoList(); t.add("A", 1); t.add("B", 2)
    assert t.get(1).taskdescr == "B"

def test_delete():
    t = ToDoList(); t.add("A", 1); t.add("B", 2); t.delete(0)
    assert t.list_all() == [("B", 2)]
```

---

## Aufgabe 3 – Aus einfach → doppelt verkettete Liste

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None            # NEU: Rückwärts-Verweis


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):         # am Ende anfügen, prev mitpflegen
        neuer = Node(data)
        if not self.head:
            self.head = neuer
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = neuer
            neuer.prev = current    # Rückwärts-Verweis setzen

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:               # war der Kopf
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def print_vorwaerts(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def print_rueckwaerts(self):
        # bis zum letzten Knoten laufen, dann über prev zurück
        current = self.head
        if current is None:
            return
        while current.next:
            current = current.next
        while current:
            print(current.data)
            current = current.prev
```

---

## Aufgabe 4 – Texteditor mit doppelt verketteter Liste

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):                     # Wort am Ende anfügen
        neuer = Node(data)
        if self.head is None:
            self.head = self.tail = neuer
        else:
            neuer.prev = self.tail
            self.tail.next = neuer
            self.tail = neuer
        return neuer

    def remove(self, node):                  # Knoten entfernen
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def insert(self, node, data):            # neues Wort NACH node einfügen
        neuer = Node(data)
        neuer.prev = node
        neuer.next = node.next
        if node.next:
            node.next.prev = neuer
        else:
            self.tail = neuer
        node.next = neuer
        return neuer

    def get_next(self, node):
        return node.next if node else None

    def get_prev(self, node):
        return node.prev if node else None

    def move(self, node, richtung):          # zu Nachbarknoten wechseln
        if richtung == "next":
            return self.get_next(node)
        if richtung == "prev":
            return self.get_prev(node)
        return node

    def print_sentence(self):
        woerter = []
        current = self.head
        while current:
            woerter.append(current.data)
            current = current.next
        print(" ".join(woerter))


class TextEditor:
    def __init__(self, satz):
        self.liste = DoublyLinkedList()
        for wort in satz.split():
            self.liste.add(wort)
        self.current_word = self.liste.head       # zeigt auf aktuelles Wort

    def next_word(self):
        naechster = self.liste.get_next(self.current_word)
        if naechster:
            self.current_word = naechster
        return self.current_word

    def previous_word(self):
        vorheriger = self.liste.get_prev(self.current_word)
        if vorheriger:
            self.current_word = vorheriger
        return self.current_word

    def add_word_here(self, wort):                # Wort nach aktueller Position einfügen
        return self.liste.insert(self.current_word, wort)

    def print_sentence(self):
        self.liste.print_sentence()


# Nutzung
editor = TextEditor("Dies ist ein Satz")
editor.print_sentence()                 # Dies ist ein Satz
print("aktuell:", editor.current_word.data)   # Dies
editor.next_word()
print("aktuell:", editor.current_word.data)   # ist
editor.add_word_here("wirklich")        # nach "ist" einfügen
editor.print_sentence()                 # Dies ist wirklich ein Satz
```
