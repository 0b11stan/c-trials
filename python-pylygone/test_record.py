import unittest
from record import *

class TestRecord(unittest.TestCase):
    def setUp(self):
        self.triangle = Record(3, 0, 0, 0)

    def test_label_can_be_set_to_fill_a_record(self):
        self.triangle.set_label(Label.TRIANGLE)
        self.assertTrue(self.triangle.is_filled())

    def test_export(self):
        trapezium = Record(4, 0, 2, 0)
        trapezium.set_label(Label.TRAPEZIUM)
        expect = {
            "sides": 4,
            "right_angles": 0,
            "parallel_sides": 2,
            "same_length_sides": 0,
            "label": "TRAPEZIUM"
        }
        self.assertEqual(expect, trapezium.export())

    def test_record_equality(self):
        filled_record = Record(4,4,4,4)
        filled_record.set_label(Label.SQUARE)
        unfilled_record = Record(4,4,4,4)
        self.assertEqual(filled_record, unfilled_record)

class TestLabel(unittest.TestCase):
    def test_existing_enums(self):
        self.assertTrue(
            Label.TRIANGLE                !=\
            Label.RIGHT_TRIANGLE          !=\
            Label.EQUILATERAL_TRIANGLE    !=\
            Label.ISOSCELES_TRIANGLE      !=\
            Label.RIGHT_ISOSCELES_TRIANGLE !=\
            Label.TETRAGON                !=\
            Label.SQUARE                  !=\
            Label.RECTANGLE               !=\
            Label.TRAPEZIUM               !=\
            Label.ISOSCELES_TRAPEZIUM     !=\
            Label.PARALLELOGRAM           !=\
            Label.RHOMBUS                 !=\
            Label.PENTAGON                !=\
            Label.EQUILATERAL_PENTAGON    !=\
            Label.HEXAGON                 !=\
            Label.REGULAR_HEXAGON         !=\
            Label.HEPTAGON                !=\
            Label.OCTAGON                 !=\
            Label.REGULAR_OCTAGON         !=\
            Label.NONAGON                 !=\
            Label.DECAGON                 !=\
            Label.REGULAR_DECAGON
        )
