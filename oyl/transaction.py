from enum import Enum, auto


class Transaction:

    class InOrOut(Enum):
        IN = auto()
        OUT = auto()

    def __init__(self, date, name, number, unit):
        self.date = date
        self.in_or_out = None
        self.name = name
        self.number = number
        self.unit = unit