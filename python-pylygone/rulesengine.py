from record import *


class RulesEngine:
    def is_legal_polygon(self, record):
        return (
            record.sides >= record.right_angles and
            record.sides >= record.parallel_sides and
            record.sides >= record.same_length_sides and (
                record.sides != 3 or (
                    record.right_angles < 2 and
                    record.parallel_sides == 0
                )
            )
        )

    def fill(self, record):
        if not self.is_legal_polygon(record):
            return
        if record.sides == 3:
            self.three_sides(record)
        elif record.sides == 4:
            self.fourth_sides(record)
        elif record.sides == 5:
            record.set_label(Label.PENTAGON)

    def three_sides(self, record):
        if record.right_angles == 1:
            if record.same_length_sides == 2:
                record.set_label(Label.RIGHT_ISOSCELES_TRIANGLE)
            else:
                record.set_label(Label.RIGHT_TRIANGLE)
        else:
            if record.same_length_sides == 3:
                record.set_label(Label.EQUILATERAL_TRIANGLE)
            elif record.same_length_sides == 2:
                record.set_label(Label.ISOSCELES_TRIANGLE)
            else:
                record.set_label(Label.TRIANGLE)

    def fourth_sides(self, record):
        if record.sides == record.right_angles == record.parallel_sides == record.same_length_sides:
            record.set_label(Label.SQUARE)
        elif record.parallel_sides == 2:
            if record.same_length_sides == 0:
                record.set_label(Label.TRAPEZIUM)
            elif record.same_length_sides == 2:
                record.set_label(Label.ISOSCELES_TRAPEZIUM)
        elif record.parallel_sides == 4:
            if record.right_angles > 0:
                record.set_label(Label.RECTANGLE)
            elif record.same_length_sides == 4:
                record.set_label(Label.RHOMBUS)
            else:
                record.set_label(Label.PARALLELOGRAM)
        else:
            record.set_label(Label.TETRAGON)
