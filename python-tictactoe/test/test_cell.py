import unittest

from app.cell import Cell
from app.exceptions import AlreadyFilledCellException
from app.player import PlayerX


class TestCell(unittest.TestCase):
    def test_init_cell(self):
        cell = Cell()
        self.assertIsNotNone(cell)

    def test_empty_cell_have_no_user(self):
        cell = Cell()
        self.assertIsNotNone(cell)
        self.assertIsNone(cell.player)

    def test_empty_cell_can_be_filled_by_a_user(self):
        cell = Cell()
        player = PlayerX('romain')
        cell.fill(player)
        self.assertEqual(player, cell.player)

    def test_filled_cell_can_not_be_overriden(self):
        cell = Cell()
        px = PlayerX('romain')
        cell.fill(px)
        with self.assertRaises(AlreadyFilledCellException):
            cell.fill(px)

    def test_that_an_empty_cell_know_its_emptiness(self):
        cell = Cell()
        self.assertTrue(cell.is_empty())

    def test_that_an_filled_cell_know_its_fullness(self):
        player = PlayerX('test')
        cell = Cell()
        cell.fill(player)
        self.assertFalse(cell.is_empty())
