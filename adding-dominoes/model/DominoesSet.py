
"""
Class representing a set of dominoes. It has:
    - domino: tuple containing the upper and lower value of the domino. (UPPER, LOWER)
    - upper
    - lower
    - weight: sum of the upper and lower value of the domino. UPPER + LOWER
    - diff: diff from the upper and lower value of the domino. |UPPER - LOWER|
"""
from typing import List, Optional

from model.Domino import Domino


class DominoesSet:
    dominoes: List[Domino]
    size: int
    upper: int
    lower: int
    weight: int
    diff: int

    def __init__(self, dominoes: List[Domino] = None):
        if dominoes is None:
            dominoes = []
            upper = 0
            lower = 0
            weight = 0
        else:
            upper = sum(domino.upper for domino in dominoes)
            lower = sum(domino.lower for domino in dominoes)
            weight = sum(domino.weight for domino in dominoes)

        self.dominoes = dominoes
        self.size = len(dominoes)
        self.upper = upper
        self.lower = lower
        self.weight = weight
        self.diff = lower - upper

    def append_domino(self, domino: Domino):
        self.dominoes.append(domino)
        self.size += 1
        self.upper += domino.upper
        self.lower += domino.lower
        self.weight += domino.weight
        self.diff = self.lower - self.upper

    def remove_domino(self, index=None) -> Optional[Domino]:
        if index is None:
            index = -1
        elif index >= len(self.dominoes):
            return None

        removed_domino = self.dominoes.pop(index)
        self.upper -= removed_domino.upper
        self.lower -= removed_domino.lower
        self.weight -= removed_domino.weight
        self.diff = self.lower - self.upper

        return removed_domino

    def sort_by_weight(self):
        self.dominoes.sort(key=lambda domino: domino.weight)

    def sort_by_diff(self):
        self.dominoes.sort(key=lambda domino: domino.diff)

    def __repr__(self):
        return f"""S: {self.size} U: {self.upper} L: {self.lower} W: {self.weight} D: {self.diff}"""
