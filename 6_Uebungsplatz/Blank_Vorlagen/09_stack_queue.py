"""
Übung 09: Stack (LIFO) & Queue (FIFO) (WS2324-Stil)

Gegeben: __init__, push/enqueue.   Selbst: der Rest.
Einziger Unterschied: entfernen hinten (Stack) vs. vorne (Queue).
"""


class Stack:                                 # 🟩
    def __init__(self):                      # 🟩
        self.stack = []

    def push(self, item):                    # 🟩 vorgegeben
        self.stack.append(item)

    def pop(self):
        # ✍️ SELBST: oberstes (LETZTES) Element entfernen + zurückgeben; leer -> None
        if self.is_empty():
            return None
        removed = self.stack[-1]
        del self.stack[-1]
        return removed

    def peek(self):
        # ✍️ SELBST: oberstes Element ansehen (self.stack[-1]); leer -> None
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        # ✍️ SELBST: True, wenn len == 0
        return len(self.stack) == 0

    def display(self):
        # ✍️ SELBST: print(self.stack)
        print(self.stack)


class Queue:                                 # 🟩
    def __init__(self):                      # 🟩
        self.queue = []

    def enqueue(self, item):                 # 🟩 vorgegeben
        self.queue.append(item)

    def dequeue(self):
        # ✍️ SELBST: VORDERSTES Element entfernen -> self.queue.pop(0); leer -> None
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        # ✍️ SELBST: print(self.queue)
        print(self.queue)


# Testaufruf
s = Stack()
for x in ["A", "B", "C"]:
    s.push(x)
print("pop:", s.pop())       # erwartet: C
s.display()                  # erwartet: ['A', 'B']

q = Queue()
for x in ["A", "B", "C"]:
    q.enqueue(x)
print("dequeue:", q.dequeue())   # erwartet: A
q.display()                      # erwartet: ['B', 'C']
