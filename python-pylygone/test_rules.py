import unittest
from rulesengine import *
from record import *


class TestRulesEngine(unittest.TestCase):
    def setUp(self):
        self.re = RulesEngine()

    def test_filling_a_possible_polygon(self):
        record = Record(3, 0, 0, 0)
        self.re.fill(record)
        self.assertTrue(record.is_filled())
        self.assertEqual(record.label, Label.TRIANGLE)


class TestUnpossiblePolygons(unittest.TestCase):
    def setUp(self):
        self.re = RulesEngine()

    def test_same_length_sides_above_sides_number(self):
        record = Record(3, 0, 0, 4)
        self.re.fill(record)
        self.assertFalse(record.is_filled())

    def test_triangle_can_not_have_more_than_one_right_angle(self):
        record = Record(3, 2, 0, 0)
        self.re.fill(record)
        self.assertFalse(record.is_filled())

    def test_triangle_can_not_have_parallel_sides(self):
        record = Record(3, 0, 1, 0)
        self.re.fill(record)
        self.assertFalse(record.is_filled())


class TestPossiblePolygons(unittest.TestCase):
    def setUp(self):
        self.re = RulesEngine()

    def polygon_check(self, a, b, c, d, label):
        record = Record(a, b, c, d)
        self.re.fill(record)
        self.assertTrue(record.is_filled())
        self.assertEqual(record.label, label)

    def test_polygons(self):
        self.polygon_check(3, 0, 0, 0, Label.TRIANGLE)
        self.polygon_check(3, 1, 0, 0, Label.RIGHT_TRIANGLE)
        self.polygon_check(3, 0, 0, 3, Label.EQUILATERAL_TRIANGLE)
        self.polygon_check(3, 0, 0, 2, Label.ISOSCELES_TRIANGLE)
        self.polygon_check(3, 1, 0, 2, Label.RIGHT_ISOSCELES_TRIANGLE)
        self.polygon_check(4, 0, 0, 0, Label.TETRAGON)
        self.polygon_check(4, 4, 4, 4, Label.SQUARE)
        self.polygon_check(4, 4, 4, 2, Label.RECTANGLE)
        self.polygon_check(4, 0, 2, 0, Label.TRAPEZIUM)
        self.polygon_check(4, 0, 2, 2, Label.ISOSCELES_TRAPEZIUM)
        self.polygon_check(4, 0, 4, 2, Label.PARALLELOGRAM)
        self.polygon_check(4, 0, 4, 4, Label.RHOMBUS)
        self.polygon_check(5, 0, 0, 0, Label.PENTAGON)


if __name__ == '__main__':
    unittest.main()
