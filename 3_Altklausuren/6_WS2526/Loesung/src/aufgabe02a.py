"""
Aufgabe 2a - Klausur Programmierung WS2025/26
"""


def normalize_and_pack(values, limit):
    """
    Alle negativen Werte werden verworfen. Alle verbleibenden Werte werden auf ganze
    Zahlen gerundet (Standardrundung von Python). Falls nach dem Verwerfen nichts
    übrig bleibt, ist das Ergebnis die leere Liste. Anschließend werden die Werte in
    der ursprünglichen Reihenfolge zu „Paketen“ zusammengefasst, sodass die Summe
    eines Pakets jeweils kleiner oder gleich limit ist. Sobald der nächste Wert
    nicht mehr in das aktuelle Paket passt, beginnt ein neues Paket. Ist limit <= 0,
    soll eine Exception geworfen werden.

    :param values: ist eine Liste von Zahlen (int oder float) und darf leer sein
    :param limit: ist eine ganze Zahl
    """
    assert type(values) == list
    # Zusaetzliche defensive Assertions (Aufgabe 2e):
    # 1) limit muss eine ganze Zahl sein, da mit ihr Groessenvergleiche gegen
    #    gerundete int-Werte durchgefuehrt werden. Ein falscher Typ (z.B. str)
    #    wuerde sonst erst spaeter bei "sum(...) + x < limit" zu einer
    #    schwer nachvollziehbaren TypeError-Ausnahme fuehren.
    assert isinstance(limit, int), "limit muss eine ganze Zahl sein"
    # 2) alle Elemente von values muessen numerisch sein, da sonst round(v)
    #    bzw. der Vergleich "v >= 0" mit einer TypeError-Ausnahme abbricht.
    assert all(isinstance(v, (int, float)) for v in values), \
        "alle Elemente von values muessen int oder float sein"

    if limit < 0:
        raise ValueError("limit must be positive")

    cleaned = []
    for v in values:
        if v >= 0:
            cleaned.append(round(v))

    packs = [[]]
    for x in cleaned:
        if sum(packs[-1]) + x < limit:
            packs[-1].append(x)
        else:
            packs.append([x])

    if packs == [[]]:
        return []
    return packs
