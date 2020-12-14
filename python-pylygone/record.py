from enum import Enum, unique


class Record:
    def __init__(self, sides, right_angles, parallel_sides, same_length_sides):
        self.sides = sides
        self.right_angles = right_angles
        self.parallel_sides = parallel_sides
        self.same_length_sides = same_length_sides
        self.label = None

    def set_label(self, label):
        self.label = label

    def is_filled(self):
        return self.label is not None

    def export(self):
        export = self.__dict__
        if self.label:
            export['label'] = str(self.label)
        return export

    def __eq__(self, other):
        a, b = self.__dict__.copy(), other.__dict__.copy()
        a.pop('label')
        b.pop('label')
        return a == b

    def __str__(self):
        return str(self.label) if self.label else "STRANGE ONE"


@unique
class Label(Enum):
    TRIANGLE = 1
    RIGHT_TRIANGLE = 2
    EQUILATERAL_TRIANGLE = 3
    ISOSCELES_TRIANGLE = 4
    RIGHT_ISOSCELES_TRIANGLE = 5
    TETRAGON = 6
    SQUARE = 7
    RECTANGLE = 8
    TRAPEZIUM = 9
    ISOSCELES_TRAPEZIUM = 10
    PARALLELOGRAM = 11
    RHOMBUS = 12
    PENTAGON = 13
    EQUILATERAL_PENTAGON = 14
    # Not implemented after that
    HEXAGON = 15
    REGULAR_HEXAGON = 16
    HEPTAGON = 17
    OCTAGON = 18
    REGULAR_OCTAGON = 19
    NONAGON = 20
    DECAGON = 21
    REGULAR_DECAGON = 22

    def __str__(self):
        return self.name
