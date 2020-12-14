import unittest
from record import *
from node import *


class TestNode(unittest.TestCase):
    def test_initialization(self):
        record = Record(4, 0, 0, 0)
        node = Node(record)
        self.assertFalse(node.has_left())
        self.assertFalse(node.has_right())

    def test_ordering_a_lesser_record_create_a_new_left_child(self):
        first_record = Record(4, 0, 0, 0)
        second_record = Record(3, 0, 0, 0)
        node = Node(first_record)
        node.order(second_record)
        self.assertTrue(node.has_left())
        self.assertFalse(node.has_right())

    def test_filling(self):
        filled_record = Record(3, 0, 0, 0)
        filled_record.set_label(Label.TRIANGLE)
        node = Node(filled_record)
        test_record = Record(3, 0, 0, 0)
        node.fill(test_record)
        self.assertTrue(test_record.is_filled())
        self.assertEqual(test_record.label, Label.TRIANGLE)

    def test_walking(self):
        triangle = Record(3, 0, 0, 0)
        triangle.set_label(Label.TRIANGLE)
        square = Record(4, 4, 4, 4)
        square.set_label(Label.SQUARE)
        parent = Node(triangle)
        parent.order(square)

        class TreeWalker:
            all_records = []

            def process(self, depth, node):
                if node is not None:
                    for record in node.records:
                        self.all_records.append(record.label)
        walker = TreeWalker()
        Node.walk(parent, walker)
        self.assertEqual([triangle.label, square.label], walker.all_records)

    def test_to_json(self):
        square = Record(4, 4, 4, 4)
        square.set_label(Label.SQUARE)
        rectangle = Record(4, 4, 4, 2)
        rectangle.set_label(Label.RECTANGLE)
        triangle = Record(3, 0, 0, 0)
        triangle.set_label(Label.TRIANGLE)
        pentagon = Record(5, 0, 0, 0)
        pentagon.set_label(Label.PENTAGON)
        parent = Node(square)
        parent.order(rectangle)
        parent.order(triangle)
        parent.order(pentagon)
        export = parent.export()
        expect = {
            "records": [
                square.__dict__,
                rectangle.__dict__
            ],
            "L": {
                "records": [
                    triangle.__dict__
                ],
                "R": None,
                "L": None
            },
            "R": {
                "records": [
                    pentagon.__dict__
                ],
                "R": None,
                "L": None
            }
        }
        self.assertEqual(expect, export)


if __name__ == '__main__':
    unittest.main()
