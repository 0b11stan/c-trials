import unittest

from utils import CellState


class TestAgent(unittest.TestCase):
    def test_cellstate_to_string(self):
        self.assertEqual("?", str(CellState.UNKNOWN))
        self.assertEqual("_", str(CellState.EMPTY))
        self.assertEqual("O", str(CellState.FULL))
        self.assertEqual("X", str(CellState.AGENT))

    def test_cellstate_from_string(self):
        self.assertEqual(CellState.UNKNOWN, CellState("?"))
        self.assertEqual(CellState.EMPTY, CellState("_"))
        self.assertEqual(CellState.FULL, CellState("O"))
        self.assertEqual(CellState.AGENT, CellState("X"))


if __name__ == '__main__':
    unittest.main()
