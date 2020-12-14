import unittest
from pathlib import Path
from record import *
from node import *
from factsengine import *
from rulesengine import *
from inferenceengine import *


class TestFactsEngine(unittest.TestCase):
    def setUp(self):
        self.fe = FactsEngine()

    def test_storing_in_empty_fact_database_create_a_root_node(self):
        record = Record(3, 0, 0, 0)
        record.set_label(Label.TRIANGLE)
        self.assertEqual(self.fe.root_node, None)
        self.fe.store(record)
        self.assertNotEqual(self.fe.root_node, None)

    def test_filling(self):
        filled_record = Record(4, 4, 4, 4)
        filled_record.set_label(Label.SQUARE)
        self.fe.store(filled_record)
        unfilled_record = Record(4, 4, 4, 4)
        self.fe.fill(unfilled_record)
        self.assertTrue(unfilled_record.is_filled())
        self.assertEqual(unfilled_record.label, Label.SQUARE)

    def test_save(self):
        square = Record(4, 4, 4, 4)
        square.set_label(Label.SQUARE)
        pentagon = Record(5, 0, 0, 0)
        pentagon.set_label(Label.PENTAGON)
        self.fe.store(square)
        self.fe.store(pentagon)
        path = Path("/tmp/polytest")
        if path.exists():
            path.unlink()
        path.touch()
        self.fe.save("/tmp/polytest")
        with open(path) as f:
            self.assertEqual(json.dumps(self.fe.export()), f.read())
        path.unlink()

    def test_load(self):
        path = Path("/tmp/polytest")
        if path.exists():
            path.unlink()
        path.touch()
        content = '{"records": [{"sides": 4, "right_angles": 4, "parallel_sides": 4, "same_length_sides": 4, "label": "SQUARE"}], "L": null, "R": {"records": [{"sides": 5, "right_angles": 0, "parallel_sides": 0, "same_length_sides": 0, "label": "PENTAGON"}], "L": null, "R": null}}'
        with open(path, 'w') as f:
            f.write(content)
        self.fe.load("/tmp/polytest")
        self.assertEqual(content, json.dumps(self.fe.export()))
        path.unlink()


class TestInferenceEngine(unittest.TestCase):
    def setUp(self):
        fe = FactsEngine()
        re = RulesEngine()
        self.ie = InferenceEngine(fe, re)

    def test_process(self):
        record = Record(4, 4, 4, 4)
        self.assertFalse(record.is_filled())
        self.ie.process(record)
        self.assertTrue(record.is_filled())
        self.assertEqual(record.label, Label.SQUARE)

    def test_storing(self):
        record = Record(4, 4, 4, 4)
        result = self.ie.process(record)
        self.assertFalse(result)
        result = self.ie.process(record)
        self.assertTrue(result)
        self.assertTrue(record.is_filled())
        self.assertEqual(record.label, Label.SQUARE)


if __name__ == '__main__':
    unittest.main()
