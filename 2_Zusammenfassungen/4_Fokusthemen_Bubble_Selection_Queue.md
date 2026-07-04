# Übung: Wahrscheinliche Lücken-Themen (Bubble-Sort, Selection-Sort, Queue)

Diese drei Themen kamen in **keiner** Altklausur dran, das Umfeld (andere Sortierverfahren, Stack) aber schon.
Format wie beim Prof: **Sortierung auf Strings nach Länge** bzw. **Objekte nach Schlüssel**, Datenstruktur als **Klasse mit Erweiterungen**.

---

## 1) Bubble-Sort

### 1a) Grundform (Zahlen) — auswendig können
```python
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        sortiert = True                       # Optimierung: Abbruch, wenn nichts getauscht
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                sortiert = False
        if sortiert:
            return numbers
    return numbers
```

### 1b) Klausur-Variante: Strings **aufsteigend nach Länge**
Nur die **Vergleichszeile** ändern (`len(...)` statt direktem Vergleich):
```python
def bubble_sort(strings):
    n = len(strings)
    for i in range(n - 1):
        sortiert = True
        for j in range(0, n - i - 1):
            if len(strings[j]) > len(strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
                sortiert = False
        if sortiert:
            return strings
    return strings


wort_liste = ["Hallo", "Python", "Wirtschaftsinformatiker", "Aufgabe", "Sortieren"]
print(bubble_sort(wort_liste))
# -> ['Hallo', 'Python', 'Aufgabe', 'Sortieren', 'Wirtschaftsinformatiker']
```

### 1c) Zusatz: bei gleicher Länge zusätzlich alphabetisch (wie WS2526)
Tupel-Trick — vergleicht erst Länge, dann den String selbst:
```python
if (len(strings[j]), strings[j]) > (len(strings[j + 1]), strings[j + 1]):
```

**Idee in einem Satz:** größtes Element „blubbert" durch Nachbartausch nach hinten; nach Durchlauf `i` steht das `i`-größte fest.

---

## 2) Selection-Sort

### 2a) Grundform (Zahlen) — auswendig können
```python
def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_index = i                          # Minimum im unsortierten Rest suchen
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers
```

### 2b) Klausur-Variante: Strings **aufsteigend nach Länge**
```python
def selection_sort(strings):
    n = len(strings)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if len(strings[j]) < len(strings[min_index]):
                min_index = j
        strings[i], strings[min_index] = strings[min_index], strings[i]
    return strings


wort_liste = ["Hallo", "Python", "Wirtschaftsinformatiker", "Aufgabe", "Sortieren"]
print(selection_sort(wort_liste))
# -> ['Hallo', 'Python', 'Aufgabe', 'Sortieren', 'Wirtschaftsinformatiker']
```

**Idee in einem Satz:** immer das Minimum des unsortierten Rests suchen und an die vorderste freie Stelle tauschen.

> Merke Unterschied: **Bubble** vergleicht/tauscht Nachbarn; **Selection** sucht das Minimum und macht nur **einen** Tausch pro Runde.
> Bubble ist **stabil**, Selection **nicht** (relevant nur, wenn Zweitkriterium wichtig ist).

---

## 3) Queue / Warteschlange (FIFO) — als Klasse mit Erweiterungen

Aufbau analog zum Stack (WS2324), aber **FIFO** statt LIFO: `enqueue` hinten anfügen, `dequeue` **vorne** entfernen.

```python
class Queue:
    def __init__(self):
        self.queue = []

    # Element hinten in die Schlange stellen
    def enqueue(self, item):
        self.queue.append(item)

    # a) vorderstes Element entfernen und zurueckgeben (FIFO)
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)          # pop(0) = vorne! (beim Stack: pop() = hinten)

    # b) vorderstes Element ansehen, ohne es zu entfernen
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]              # vorne (beim Stack: self.stack[-1])

    def is_empty(self):
        return len(self.queue) == 0

    # c) i-tes Element zurueckgeben (0-basiert)
    def get(self, i):
        if i < 0 or i >= len(self.queue):
            raise IndexError("Index liegt ausserhalb der Queue")
        return self.queue[i]

    # d) i-tes Element entfernen (0-basiert)
    def delete(self, i):
        if i < 0 or i >= len(self.queue):
            raise IndexError("Index liegt ausserhalb der Queue")
        del self.queue[i]

    def display(self):
        print(self.queue)


# Anwendungsbeispiel
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.display()               # ['A', 'B', 'C']
print("peek:", q.peek())  # A   (vorderstes)
print("dequeue:", q.dequeue())  # A
q.display()               # ['B', 'C']
print("get(1):", q.get(1))      # C
q.delete(0)               # entfernt B
q.display()               # ['C']
print("is_empty:", q.is_empty())  # False
```

**FIFO vs. LIFO auf einen Blick:**
| | Einfügen | Entfernen | peek |
|---|---|---|---|
| **Queue** (FIFO) | `append` (hinten) | `pop(0)` (vorne) | `[0]` |
| **Stack** (LIFO) | `append` (hinten) | `pop()`/`[-1]`+`del` (hinten) | `[-1]` |

---

## Selbsttest (ohne nachschauen schreiben können)
- [ ] `bubble_sort` (Zahlen) inkl. `sortiert`-Abbruch
- [ ] dieselbe Funktion auf **Strings nach Länge** umstellen (welche Zeile?)
- [ ] `selection_sort` (Zahlen) + auf Länge umstellen
- [ ] `Queue`-Klasse mit `enqueue`, `dequeue`, `peek`, `is_empty`, `get`, `delete`, `display`
- [ ] erklären: Warum `pop(0)` bei Queue, aber `pop()`/`[-1]` bei Stack?
