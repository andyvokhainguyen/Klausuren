"""
Aufgabe 3 - Klausur Prog

Author:
Vorname Nachname

Matrikelnummer:
999.999
"""


def get_ratio_at_position(list_a, list_b, pos_in_list):
    """Assumes: list_a and list_b are lists of equal length of numbers
    Returns: List_a[pos_in_list]/List_b[pos_in_list]"""

    if (
        not isinstance(list_a, list)
        or not isinstance(list_b, list)
        or not isinstance(pos_in_list, int)
    ):
        raise TypeError

    return float(list_a[pos_in_list]) / float(list_b[pos_in_list])


# Beispielaufruf und Überprüfung
assert get_ratio_at_position([2, 3, 6, 9], [1, 2, 3, 4], 2) == 2

assert not get_ratio_at_position([2, 3, 6, 9], [1, 2, 3, 4], 3) == 3
