from enum import Enum, auto


class Orientation(Enum):
    TOP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()


class CellState(Enum):
    UNKNOWN = '?'
    EMPTY = '_'
    FULL = 'O'
    AGENT = 'X'

    def __str__(self):
        return self.value
