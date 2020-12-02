import unittest

from app.bad_cell_error import BadCellError
from app.player import Player


class TestBadCellError(unittest.TestCase):
    def test_init_exception_with_player_row_and_coll(self):
        player, row, col = Player('test'), 0, 1
        expect = "Cell at (0, 1) is already take by player test"
        bce = BadCellError(player, row, col)
        self.assertEqual(expect, str(bce))
