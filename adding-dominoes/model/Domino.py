
"""
Class describing a domino piece. It has:
    - domino: tuple containing the upper and lower value of the domino. (UPPER, LOWER)
    - upper
    - lower
    - weight: sum of the upper and lower value of the domino. UPPER + LOWER
    - diff: diff from the upper and lower value of the domino. |UPPER - LOWER|
"""


class Domino:
    domino: tuple
    upper: int
    lower: int
    weight: int
    diff: int

    def __init__(self, upper: int, lower: int):
        self.domino = (upper, lower)
        self.upper = upper
        self.lower = lower
        self.weight = upper + lower
        self.diff = lower - upper

    # Method to flip the upper and lower value from domino piece.
    def flip(self) -> None:
        self.domino = (self.domino[1], self.domino[0])

    def __repr__(self):
        return f"""Domino: {self.domino} U: {self.upper} L: {self.lower} W: {self.weight} D: {self.diff}"""
