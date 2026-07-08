# 🔢 Die 6 Sortierverfahren erklärt (Skript 06)

Jedes Verfahren: **Grundidee → Code (Skript-Form) → Schritt für Schritt → Komplexität**. Detaillierte Zahlen-Durchläufe mit `[55, 7, 78, 12, 42]` stehen in [`4_Sortierverfahren_Traces.md`](4_Sortierverfahren_Traces.md).

**Zwei Gruppen:**
- **„Naive" Verfahren – O(n²):** Bubble, Selection, Insertion (einfach, aber langsam bei großen Listen).
- **Teile-und-Herrsche – O(n·log n):** Quicksort, Mergesort, Heapsort (effizient).

---

## 1) Bubble-Sort

**Grundidee:** Vergleiche immer **benachbarte** Elemente und tausche sie, wenn sie in falscher Reihenfolge sind. Das größte Element „blubbert" pro Durchlauf ganz nach hinten. Nach Durchlauf `i` steht das `i`-größte Element endgültig richtig.

```python
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        list_sorted = True                         # Optimierung: Früh-Abbruch
        for j in range(0, n - i - 1):              # -i: hinten steht schon Sortiertes
            if numbers[j] > numbers[j + 1]:        # Nachbarn in falscher Reihenfolge?
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]   # tauschen
                list_sorted = False
        if list_sorted:                            # nichts getauscht -> fertig
            return
```

**Schritt für Schritt** (`[5, 3, 8, 1]`):
1. Durchlauf i=0: (5,3)→tausch `[3,5,8,1]`; (5,8)→ok; (8,1)→tausch `[3,5,1,8]`. **8 sitzt hinten.**
2. Durchlauf i=1: (3,5)→ok; (5,1)→tausch `[3,1,5,8]`. **5 sitzt.**
3. Durchlauf i=2: (3,1)→tausch `[1,3,5,8]`. Fertig.

**Merkmale:** `list_sorted`-Flag bricht ab, sobald ein Durchlauf ohne Tausch bleibt → **Best Case O(n)** (schon sortiert). Sonst **O(n²)**. **Stabil** (gleiche Elemente behalten Reihenfolge, da nur bei `>` getauscht wird).

---

## 2) Selection-Sort

**Grundidee:** Der vordere Teil der Liste ist immer sortiert. Suche im **unsortierten Rest** das **Minimum** und tausche es an die vorderste freie Stelle. Pro Runde genau **ein** Tausch.

```python
def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_index = i                              # Annahme: vorderstes ist Minimum
        for j in range(i + 1, n):                  # Rest durchsuchen
            if numbers[j] < numbers[min_index]:
                min_index = j                      # kleineres gefunden
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]   # 1 Tausch
```

**Schritt für Schritt** (`[5, 3, 8, 1]`):
1. i=0: Minimum im ganzen Array = 1 (Index 3) → tausch mit Index 0 → `[1, 3, 8, 5]`.
2. i=1: Minimum in `[3,8,5]` = 3 (steht schon) → kein echter Tausch → `[1, 3, 8, 5]`.
3. i=2: Minimum in `[8,5]` = 5 → tausch → `[1, 3, 5, 8]`. Fertig.

**Merkmale:** Immer **O(n²)** – auch bei bereits sortierter Liste wird der Rest komplett durchsucht (kein Früh-Abbruch). Macht aber **wenige Tausche** (genau n). **Nicht stabil**.

---

## 3) Insertion-Sort

**Grundidee:** Wie beim Karten-Sortieren. Nimm das nächste Element (`pivot`) und **schiebe** es im bereits sortierten linken Teil so weit nach links, bis es an der richtigen Stelle sitzt.

```python
def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):                          # ab dem 2. Element
        pivot = numbers[i]                         # das einzusortierende Element
        j = i - 1
        while j >= 0 and numbers[j] > pivot:       # größere nach rechts schieben
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = pivot                     # Lücke mit pivot füllen
```

**Schritt für Schritt** (`[5, 3, 8, 1]`):
1. i=1: pivot=3; 5>3 → 5 nach rechts `[5,5,8,1]`, dann pivot rein → `[3, 5, 8, 1]`.
2. i=2: pivot=8; 5>8? nein → bleibt `[3, 5, 8, 1]`.
3. i=3: pivot=1; 8>1→schieben, 5>1→schieben, 3>1→schieben → `[1, 3, 5, 8]`. Fertig.

**Merkmale:** **Best Case O(n)** (fast sortiert – die `while` läuft kaum), sonst **O(n²)**. **Stabil**. Gut für kleine oder fast sortierte Listen.

---

## 4) Quicksort (Teile-und-Herrsche)

**Grundidee:** Wähle ein **Pivot** (hier das erste Element). Teile den Rest in „kleiner-gleich Pivot" und „größer Pivot". Sortiere beide Teile **rekursiv** und setze zusammen: `kleiner + [pivot] + größer`.

```python
def quicksort(numbers):
    if len(numbers) <= 1:                          # Basisfall: 0/1 Element = sortiert
        return numbers
    pivot = numbers[0]
    kleiner  = [x for x in numbers[1:] if x <= pivot]   # <= behält Duplikate!
    groesser = [x for x in numbers[1:] if x > pivot]
    return quicksort(kleiner) + [pivot] + quicksort(groesser)
```

**Schritt für Schritt** (`[5, 3, 8, 1]`):
1. pivot=5 → kleiner=`[3,1]`, größer=`[8]`.
2. quicksort(`[3,1]`): pivot=3 → kleiner=`[1]`, größer=`[]` → `[1,3]`.
3. Zusammen: `[1,3]` + `[5]` + `[8]` = `[1, 3, 5, 8]`.

**Merkmale:** Schnitt **O(n·log n)**, **Worst Case O(n²)** (schon sortiert + erstes Element als Pivot → sehr unbalanciert). ⚠️ **Wichtig:** Im Skript steht `< pivot` / `> pivot` – das **verliert Elemente, die gleich dem Pivot sind** (Duplikate)! Deshalb in der Klausur `<=` verwenden, wie oben.

---

## 5) Mergesort (Teile-und-Herrsche)

**Grundidee:** Teile die Liste stur in der **Mitte**, bis nur noch Einzelelemente übrig sind (die sind „sortiert"). Führe dann die sortierten Hälften mit `merge` **sortiert zusammen**.

```python
def merge_sort(numbers):
    if len(numbers) <= 1:                          # Basisfall
        return numbers
    mid = len(numbers) // 2
    left_half  = merge_sort(numbers[:mid])         # linke Hälfte rekursiv
    right_half = merge_sort(numbers[mid:])         # rechte Hälfte rekursiv
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:  # kleineres zuerst übernehmen
            merged.append(left[left_index]); left_index += 1
        else:
            merged.append(right[right_index]); right_index += 1
    merged.extend(left[left_index:])               # Rest anhängen
    merged.extend(right[right_index:])
    return merged
```

**Schritt für Schritt** (`[5, 3, 8, 1]`):
1. **Teilen:** `[5,3,8,1]` → `[5,3]` und `[8,1]` → `[5],[3]` und `[8],[1]`.
2. **Mergen:** `merge([5],[3])=[3,5]`, `merge([8],[1])=[1,8]`.
3. **Mergen:** `merge([3,5],[1,8])`: 3vs1→1, 3vs8→3, 5vs8→5, Rest 8 → `[1, 3, 5, 8]`.

**Merkmale:** **immer O(n·log n)** (auch im Worst Case – Vorteil ggü. Quicksort). **Stabil** (bei `<`). Braucht **zusätzlichen Speicher** (nicht in-place). In der Klausur ist `merge` oft **vorgegeben** – du schreibst nur `merge_sort`.

---

## 6) Heapsort (Max-Heap)

**Grundidee:** Ordne die Liste als **Max-Heap** an (Elternknoten ≥ Kinder, also größtes Element an der Wurzel = Index 0). Dann wiederhole: **Wurzel** (größtes) ans **Ende** tauschen, Heap um 1 verkleinern, Heap wiederherstellen (`heapify`).

Die Liste wird als Baum gelesen: Kind-Indizes von `i` sind `2*i+1` (links) und `2*i+2` (rechts).

```python
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):            # Phase A: Max-Heap aufbauen
        heapify(arr, n, i)                         #   ab letztem inneren Knoten rückwärts
    for i in range(n - 1, 0, -1):                  # Phase B: entnehmen
        arr[i], arr[0] = arr[0], arr[i]            #   größtes (Wurzel) ans Ende
        heapify(arr, i, 0)                         #   Rest-Heap (Größe i) reparieren


def heapify(arr, n, i):                            # Max-Heap-Eigenschaft ab Index i
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:      # größtes von i, links, rechts finden
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:                               # größtes Kind war größer -> tauschen
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)                   # nach unten weiter reparieren
```

**Schritt für Schritt (grob)** (`[5, 3, 8, 1]`):
1. **Phase A (Heap bauen):** ab Index `n//2-1 = 1` rückwärts heapify → Max-Heap `[8, 3, 5, 1]` (8 an der Wurzel).
2. **Phase B:** 8↔letztes tauschen → `[1,3,5,|8]`, Rest reparieren → `[5,3,1,|8]`; dann 5 ans Ende → `[1,3,|5,8]`, reparieren → `[3,1,|5,8]`; dann 3 → `[1,|3,5,8]`. Ergebnis `[1, 3, 5, 8]`.

**Merkmale:** **immer O(n·log n)**, sortiert **in-place** (kein Extraspeicher wie Mergesort). **Nicht stabil**. In der Klausur ist `heapify` oft **vorgegeben** – du schreibst nur `heap_sort` (die zwei Schleifen).

---

## 🔑 Das Sortierkriterium – nur EINE Zeile

Das Gerüst bleibt immer gleich; nur der Vergleich entscheidet, *wonach* sortiert wird:

| Sortiere nach … | Vergleich (Beispiel Bubble) |
|---|---|
| Zahl aufsteigend | `numbers[j] > numbers[j+1]` |
| String-Länge | `len(a[j]) > len(a[j+1])` |
| Länge, dann Alphabet | `(len(a[j]), a[j]) > (len(a[j+1]), a[j+1])` |
| Dict/Objekt nach Feld | `a[j]["gehalt"] > a[j+1]["gehalt"]` |
| absteigend | `>` durch `<` ersetzen |

## 📊 Vergleich auf einen Blick

| Verfahren | Best | Mittel | Worst | stabil? | in-place? | Prinzip |
|---|---|---|---|---|---|---|
| Bubble | O(n) | O(n²) | O(n²) | ✅ | ✅ | Nachbarn tauschen |
| Selection | O(n²) | O(n²) | O(n²) | ❌ | ✅ | Minimum suchen |
| Insertion | O(n) | O(n²) | O(n²) | ✅ | ✅ | einsortieren/schieben |
| Quicksort | O(n·log n) | O(n·log n) | O(n²) | ❌ | ✅ | Pivot + partitionieren |
| Mergesort | O(n·log n) | O(n·log n) | O(n·log n) | ✅ | ❌ | teilen + mergen |
| Heapsort | O(n·log n) | O(n·log n) | O(n·log n) | ❌ | ✅ | Max-Heap entnehmen |
