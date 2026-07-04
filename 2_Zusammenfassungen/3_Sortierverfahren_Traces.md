# Sortierverfahren – Schritt-für-Schritt-Traces

Alle Verfahren mit derselben Eingabe: **`[55, 7, 78, 12, 42]`** → sortiert **`[7, 12, 42, 55, 78]`**.
Gedanklich zum Nachrechnen/Üben. (Fett/→ markiert Vertauschungen.)

---

## 1) Bubble-Sort
Regel: benachbarte Paare vergleichen, bei `links > rechts` tauschen. Nach Durchlauf `i` steht die `i`-größte Zahl hinten fest.

**Durchlauf i=0** (vergleiche j=0..3):
| Schritt | Liste | Aktion |
|---|---|---|
| j=0 | [**55,7**,78,12,42] | 55>7 → tausche → [7,55,78,12,42] |
| j=1 | [7,**55,78**,12,42] | 55>78? nein |
| j=2 | [7,55,**78,12**,42] | 78>12 → tausche → [7,55,12,78,42] |
| j=3 | [7,55,12,**78,42**] | 78>42 → tausche → [7,55,12,42,**78**] |

**Durchlauf i=1** (j=0..2): [7,55,12,42,78]
| j=0 | 7>55? nein |
| j=1 | 55>12 → tausche → [7,12,55,42,78] |
| j=2 | 55>42 → tausche → [7,12,42,**55**,78] |

**Durchlauf i=2** (j=0..1): [7,12,42,55,78]
- 7>12? nein · 12>42? nein → **kein Tausch → `list_sorted=True` → return** (vorzeitiger Abbruch!)

**Ergebnis:** `[7, 12, 42, 55, 78]`

---

## 2) Selection-Sort
Regel: im unsortierten Rest das Minimum suchen und an die vorderste freie Stelle tauschen.

| i | Liste vorher | Minimum im Rest [i..] | Aktion | Liste nachher |
|---|---|---|---|---|
| 0 | [55,7,78,12,42] | 7 (Idx 1) | tausche 7 ↔ 55 | [**7**,55,78,12,42] |
| 1 | [7,55,78,12,42] | 12 (Idx 3) | tausche 12 ↔ 55 | [7,**12**,78,55,42] |
| 2 | [7,12,78,55,42] | 42 (Idx 4) | tausche 42 ↔ 78 | [7,12,**42**,55,78] |
| 3 | [7,12,42,55,78] | 55 (Idx 3) | tausche 55 ↔ 55 (nichts) | [7,12,42,**55**,78] |
| 4 | [7,12,42,55,78] | 78 (Idx 4) | tausche 78 ↔ 78 (nichts) | [7,12,42,55,**78**] |

**Ergebnis:** `[7, 12, 42, 55, 78]`

---

## 3) Insertion-Sort
Regel: `pivot = numbers[i]`; solange links größer → nach rechts schieben; dann pivot einsetzen.

| i | pivot | Vorgang (Verschieben) | Liste nachher |
|---|---|---|---|
| 1 | 7 | 55>7 → 55 nach rechts; einfügen vor 55 | [7,55,78,12,42] |
| 2 | 78 | 55>78? nein → bleibt stehen | [7,55,78,12,42] |
| 3 | 12 | 78>12→schieben; 55>12→schieben; 7>12? nein → einfügen | [7,12,55,78,42] |
| 4 | 42 | 78>42→schieben; 55>42→schieben; 12>42? nein → einfügen | [7,12,42,55,78] |

**Ergebnis:** `[7, 12, 42, 55, 78]`

---

## 4) Quicksort (Teile-und-Herrsche, pivot = erstes Element)
`less = Elemente < pivot`, `greater = Elemente > pivot`, dann `quicksort(less) + [pivot] + quicksort(greater)`.

```
quicksort([55,7,78,12,42])            pivot=55  less=[7,12,42]  greater=[78]
├─ quicksort([7,12,42])               pivot=7   less=[]         greater=[12,42]
│  ├─ quicksort([])            = []
│  └─ quicksort([12,42])              pivot=12  less=[]         greater=[42]
│     ├─ quicksort([])         = []
│     └─ quicksort([42])       = [42]
│     └──────────────► [] + [12] + [42]      = [12,42]
│  └──────────────────► [] + [7]  + [12,42]  = [7,12,42]
└─ quicksort([78])              = [78]
└─────────────────────► [7,12,42] + [55] + [78] = [7,12,42,55,78]
```
**Ergebnis:** `[7, 12, 42, 55, 78]`
> Hinweis: mit `<` / `>` gingen Duplikate verloren – für Duplikate einen Vergleich auf `<=` ändern.

---

## 5) Mergesort (Teile-und-Herrsche, Mitte teilen)
Teilen bis Einzelelemente, dann sortiert zusammenführen (`merge`).

**Teilen (rekursiv):**
```
              [55,7,78,12,42]
              /             \
         [55,7]           [78,12,42]
         /    \            /       \
      [55]   [7]        [78]     [12,42]
                                  /    \
                               [12]   [42]
```
**Zusammenführen (merge, jeweils kleinstes zuerst):**
```
[55] + [7]        -> [7,55]
[12] + [42]       -> [12,42]
[78] + [12,42]    -> [12,42,78]
[7,55] + [12,42,78] -> [7,12,42,55,78]
```
Detail des letzten Merges `[7,55]` & `[12,42,78]`:
| Vergleich | genommen | Ergebnis bisher |
|---|---|---|
| 7 < 12 | 7 | [7] |
| 55 < 12? nein | 12 | [7,12] |
| 55 < 42? nein | 42 | [7,12,42] |
| 55 < 78? ja | 55 | [7,12,42,55] |
| links leer → Rest anhängen | 78 | [7,12,42,55,78] |

**Ergebnis:** `[7, 12, 42, 55, 78]`

---

## 6) Heapsort (Max-Heap)
Indexregel (0-basiert wie im Code): Kinder von `i` sind `2i+1` und `2i+2`.

### Phase A – Max-Heap aufbauen
`for i in range(n//2 - 1, -1, -1)` → n=5 → i = 1, dann 0.

| heapify | Liste vorher | Vorgang | Liste nachher |
|---|---|---|---|
| i=1 | [55,7,78,12,42] | Kinder von 7: 12, 42 → größtes 42 > 7 → tausche | [55,**42**,78,12,**7**] |
| i=0 | [55,42,78,12,7] | Kinder von 55: 42, 78 → 78 > 55 → tausche | [**78**,42,**55**,12,7] |

**Max-Heap:** `[78, 42, 55, 12, 7]`
```
        78
       /  \
     42    55
    /  \
  12    7
```

### Phase B – Elemente entnehmen
`for i in range(n-1, 0, -1)` → i = 4,3,2,1. Jeweils: Wurzel ↔ letztes freies Element tauschen, dann `heapify` auf den verbleibenden vorderen Teil (Größe = i).

| i | tausche Wurzel↔arr[i] | nach Tausch | heapify(Größe=i) | Liste (sortierter Teil **fett**) |
|---|---|---|---|---|
| 4 | 78 ↔ 7 | [7,42,55,12,**78**] | versickere 7: →55→ [55,42,7,12] | [55,42,7,12,**78**] |
| 3 | 55 ↔ 12 | [12,42,7,**55,78**] | versickere 12: →42→ [42,12,7] | [42,12,7,**55,78**] |
| 2 | 42 ↔ 7 | [7,12,**42,55,78**] | versickere 7: →12→ [12,7] | [12,7,**42,55,78**] |
| 1 | 12 ↔ 7 | [7,**12,42,55,78**] | Rest Größe 1 → fertig | [**7,12,42,55,78**] |

**Ergebnis:** `[7, 12, 42, 55, 78]`

---

## Merk-Vergleich der Ideen
| Verfahren | Kernidee in einem Satz |
|---|---|
| Bubble | größte Zahl "blubbert" durch Nachbartausch nach hinten |
| Selection | immer das Minimum des Rests nach vorne holen |
| Insertion | jedes Element an die richtige Stelle im sortierten Teil einsortieren |
| Quicksort | Pivot wählen, in kleiner/größer teilen, rekursiv |
| Mergesort | in der Mitte halbieren, rekursiv, sortiert mischen |
| Heapsort | Max-Heap bauen, Wurzel (Maximum) entnehmen, Heap reparieren |
