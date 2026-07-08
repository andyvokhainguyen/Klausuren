# 🧩 Die Datenstrukturen erklärt (Skript 05)

Jede Struktur: **Grundidee → Code (Skript-Form) → Schritt für Schritt → Anwendung**. Das sind die im Skript behandelten Strukturen: verkettete Liste (einfach/doppelt), Queue, Stack, Binärer Suchbaum.

> Die Altklausur-Sonderfälle **Trie, Ternärer Suchbaum, Zirkuläre Liste** kamen *nicht* im Skript vor – die stehen in [`3_Alle_Codes_zum_Abtippen.md`](3_Alle_Codes_zum_Abtippen.md) (Abschnitt 5).

**Grundbaustein aller verketteten Strukturen: der Knoten (`Node`)** – ein Objekt, das **Daten** speichert und per **Zeiger** (`next`) auf das nächste Objekt verweist. Damit lassen sich Elemente verketten, ohne dass sie im Speicher hintereinander liegen müssen (anders als bei einem Array).

---

## 1) Einfach verkettete Liste (Linked List)

**Grundidee:** Eine Kette von Knoten. Jeder Knoten kennt nur **seinen Nachfolger** (`next`). Die Liste selbst merkt sich nur den **Anfang** (`head`). Das Ende erkennt man an `next == None`.

```
head -> [A|•] -> [B|•] -> [C|None]
```

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None                 # Zeiger auf den nächsten Knoten


class LinkedList:
    def __init__(self):
        self.head = None                 # leere Liste: kein Anfang

    def insert(self, data):              # neues Element am ENDE anhängen
        if not self.head:                # Liste leer -> neuer Knoten wird head
            self.head = Node(data)
        else:
            current = self.head
            while current.next:          # bis zum letzten Knoten laufen
                current = current.next
            current.next = Node(data)    # dort anhängen

    def print_list(self):
        current = self.head
        while current:                   # bis None -> alle Knoten durch
            print(current.data)
            current = current.next

    def delete(self, data):              # erstes Element mit Wert `data` entfernen
        if self.head is None:
            return
        if self.head.data == data:       # Sonderfall: head selbst löschen
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next   # Knoten „überspringen"
                return
            current = current.next
```

**Schritt für Schritt – Durchlaufen:** Man startet bei `head` und hangelt sich mit `current = current.next` von Knoten zu Knoten, bis `current` `None` ist. Das ist das Grundmuster **jeder** Listenoperation.

**Schritt für Schritt – Löschen von „B" aus `A→B→C`:** Laufe bis `current = A`. `current.next` ist B, dessen Wert passt → setze `current.next = current.next.next`, also `A.next = C`. B ist jetzt nicht mehr erreichbar → gelöscht: `A→C`.

**Anwendung (Skript):** dynamische Speicherverwaltung, Baustein für Stacks/Queues/Hash-Tabellen, Navigation vor/zurück.

---

## 2) Doppelt verkettete Liste (Doubly Linked List)

**Grundidee:** Wie oben, aber jeder Knoten kennt **beide** Nachbarn: `next` **und** `prev`. Damit kann man **vorwärts und rückwärts** laufen (z. B. Bildergalerie vor/zurück). Im Skript ist das eine **Übungserweiterung** der einfachen Liste.

```
None <- [A] <-> [B] <-> [C] -> None
```

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None                 # <<< zusätzlich: Zeiger zurück
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):              # am Ende anhängen
        neuer = Node(data)
        if self.head is None:
            self.head = neuer
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = neuer
        neuer.prev = current             # Rückwärts-Zeiger auf den Vorgänger setzen

    def print_vorwaerts(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def print_rueckwaerts(self):
        current = self.head
        if current is None:
            return
        while current.next is not None:  # erst ans Ende laufen
            current = current.next
        while current is not None:       # dann über prev zurück
            print(current.data)
            current = current.prev
```

**Der einzige echte Unterschied zur einfachen Liste:** `Node` hat zusätzlich `self.prev`, und beim Einfügen musst du diesen Rückwärts-Zeiger mitsetzen. Dafür geht Rückwärts-Laufen ohne die Liste neu zu durchsuchen.

---

## 3) Warteschlange – Queue (FIFO)

**Grundidee:** **First In, First Out** – wie die Schlange an der Kasse. Wer zuerst kommt, wird zuerst bedient. Einfügen **hinten** (`enqueue`), entfernen **vorne** (`dequeue`).

```python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):             # hinten anstellen
        self.queue.append(item)

    def dequeue(self):                   # vorderstes entnehmen (FIFO)
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)         # pop(0) = Element an Index 0 (vorne)

    def display(self):
        print(self.queue)
```

**Schritt für Schritt:** `enqueue("A"), enqueue("B"), enqueue("C")` → `['A','B','C']`. `dequeue()` gibt **`A`** zurück (das älteste) → `['B','C']`.

**Anwendung:** Druckerwarteschlange, Aufgaben-/Task-Queues, Breitensuche.

---

## 4) Stapel – Stack (LIFO)

**Grundidee:** **Last In, First Out** – wie ein Tellerstapel. Das **zuletzt** abgelegte Element wird **zuerst** wieder genommen. Einfügen und Entfernen passieren **am selben Ende** (hinten/oben).

```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):                # oben drauflegen
        self.stack.append(item)

    def pop(self):                       # oberstes entnehmen (LIFO)
        if len(self.stack) < 1:
            return None
        removed_item = self.stack[-1]    # letztes Element = oberstes
        del self.stack[-1]
        return removed_item

    def display(self):
        print(self.stack)
```

**Schritt für Schritt:** `push("A"), push("B"), push("C")` → `['A','B','C']`. `pop()` gibt **`C`** zurück (das jüngste) → `['A','B']`.

**Queue vs. Stack – der einzige Unterschied:**
| | Einfügen | Entfernen |
|---|---|---|
| **Queue** (FIFO) | `append` (hinten) | `pop(0)` (**vorne**) |
| **Stack** (LIFO) | `append` (hinten) | `pop()`/`[-1]` (**hinten**) |

**Anwendung Stack:** Undo-Funktion, Aufrufstack von Funktionen, Klammern-/Syntaxprüfung in Compilern.

---

## 5) Binärer Suchbaum (Binary Search Tree, BST)

**Grundidee:** Ein Baum, in dem jeder Knoten höchstens **zwei Kinder** hat (links/rechts). Es gilt die **Suchbaum-Eigenschaft**: alle Werte **links < Knoten**, alle Werte **rechts ≥ Knoten**. Dadurch findet/einfügt man Werte schnell (man halbiert bei jedem Schritt den Suchraum). Eine **In-order-Traversierung** (links → Knoten → rechts) liefert die Werte **automatisch sortiert**.

```
        20
       /  \
     10    30
    / \    / \
   5  15  25 35
```

```python
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):              # Wrapper: kümmert sich um leeren Baum
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):       # rekursiv den richtigen Platz suchen
        if data < node.data:             # kleiner -> nach links
            if node.left is None:
                node.left = Node(data)   # freier Platz -> einfügen
            else:
                self._insert(data, node.left)
        else:                            # größer/gleich -> nach rechts
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):         # In-order -> sortierte Ausgabe
        if node is not None:
            self._print_tree(node.left)  # 1. linker Teilbaum
            print(node.data)             # 2. aktueller Knoten
            self._print_tree(node.right) # 3. rechter Teilbaum

    def search(self, data):              # (aus Übungsblatt) True/False
        return self._search(data, self.root)

    def _search(self, data, node):
        if node is None:
            return False                 # Ast zu Ende -> nicht gefunden
        if data == node.data:
            return True
        elif data < node.data:
            return self._search(data, node.left)
        else:
            return self._search(data, node.right)

    # Löschen (Skript) – drei Fälle: Blatt/ein Kind / zwei Kinder
    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:                                   # Knoten gefunden:
            if node.left is None:               # Fall 1: kein/nur rechtes Kind
                return node.right
            elif node.right is None:            # Fall 2: nur linkes Kind
                return node.left
            temp = self._find_min(node.right)   # Fall 3: zwei Kinder ->
            node.data = temp.data               #   kleinsten im rechten Teilbaum
            node.right = self._delete(node.right, temp.data)  #   nachrücken lassen
        return node

    def _find_min(self, node):
        if node.left is None:
            return node
        return self._find_min(node.left)
```

**Schritt für Schritt – Einfügen von `[20, 10, 30, 5]`:**
1. 20 → wird `root`.
2. 10 < 20 → links von 20 (leer) → einfügen.
3. 30 ≥ 20 → rechts von 20 (leer) → einfügen.
4. 5 < 20 → links zu 10; 5 < 10 → links von 10 (leer) → einfügen.

**Schritt für Schritt – In-order-Ausgabe:** links ganz runter (5), dann dessen Elter (10), dann 15… → **5, 10, 15, 20, 25, 30, 35** (sortiert!). Das ist der Grund, warum ein BST „nebenbei" sortiert.

### Löschen aus dem BST (Skript) – die drei Fälle
Die Methoden `delete` / `_delete` / `_find_min` stehen oben mit in der Klasse. Beim Löschen unterscheidet man **drei Fälle**:
1. **Blatt oder nur rechtes Kind** → einfach das rechte Kind (oder `None`) hochziehen.
2. **Nur linkes Kind** → das linke Kind hochziehen.
3. **Zwei Kinder** → den **kleinsten Wert des rechten Teilbaums** (den „In-order-Nachfolger", via `_find_min`) an die Stelle kopieren und diesen unten dann löschen. So bleibt die Suchbaum-Eigenschaft (links < Knoten ≤ rechts) erhalten.

**Anwendung:** schnelles Suchen/Einfügen/Löschen (Ø **O(log n)** bei balanciertem Baum), sortierte Ausgabe, Grundlage vieler Such-/Datenbank-Indexstrukturen. ⚠️ Bei „entartetem" Baum (z. B. sortiert eingefügt) wird er zur Liste → **O(n)**.

---

## 📊 Überblick

| Struktur | Zugriff / Prinzip | Kernoperationen | Merksatz |
|---|---|---|---|
| Einfach verkettete Liste | vorwärts durchlaufen | insert, print, delete | `current = current.next` bis `None` |
| Doppelt verkettete Liste | vor- **und** rückwärts | + `prev` setzen | Node hat zusätzlich `self.prev` |
| Queue (FIFO) | vorne raus, hinten rein | enqueue, dequeue | `pop(0)` = vorne |
| Stack (LIFO) | oben rein, oben raus | push, pop | `pop()`/`[-1]` = hinten |
| Binärer Suchbaum | links < Knoten ≤ rechts | insert, search, delete, In-order | In-order = sortiert |
