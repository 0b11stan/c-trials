import unittest

from app.grid import Grid
from app.player import Player


class TestGrid(unittest.TestCase):

    @staticmethod
    def draw_winning_pattern(player, grid, row, col, vertical, horizontal):
        if vertical and horizontal and col == 0:
            grid.fill(player, row, col)
            grid.fill(player, row + 1, col + 1)
            grid.fill(player, row + 2, col + 2)
        elif vertical and horizontal and col == 2:
            grid.fill(player, row, col)
            grid.fill(player, row + 1, col - 1)
            grid.fill(player, row + 2, col - 2)
        elif vertical:
            grid.fill(player, row, col)
            grid.fill(player, row + 1, col)
            grid.fill(player, row + 2, col)
        else:
            grid.fill(player, row, col)
            grid.fill(player, row, col + 1)
            grid.fill(player, row, col + 2)

    def test_grid_can_exist(self):
        grid = Grid()
        self.assertIsNotNone(grid)

    def test_that_a_grid_contain_the_right_cell_matrix(self):
        grid = Grid()
        self.assertEqual(3, len(grid.cells))
        self.assertEqual(3, len(grid.cells[0]))
        self.assertEqual(3, len(grid.cells[1]))
        self.assertEqual(3, len(grid.cells[2]))
        self.assertTrue(grid.cells[0][0].is_empty())
        self.assertTrue(grid.cells[2][2].is_empty())

    def test_is_empty_return_grids_emptiness(self):
        grid = Grid()
        self.assertTrue(grid.is_empty())

    def test_cells_can_be_filled(self):
        grid = Grid()
        player = Player('test')
        grid.fill(player, 1, 1)
        self.assertFalse(grid.is_empty())
        self.assertEqual(player, grid.cells[1][1].player)

    def test_3_horizontal_fill_is_a_winning_pattern(self):
        player = Player('test')
        grid = Grid()
        self.assertIsNone(grid.get_winner())
        self.draw_winning_pattern(player, grid, row=0, col=0,
                                  vertical=False, horizontal=True)
        self.assertEqual(player, grid.get_winner())

    def test_3_vertical_fill_on_first_col_is_a_winning_pattern(self):
        player = Player('test')
        grid = Grid()
        self.assertIsNone(grid.get_winner())
        self.draw_winning_pattern(player, grid, row=0, col=0,
                                  vertical=True, horizontal=False)
        self.assertEqual(player, grid.get_winner())

    def test_3_vertical_fill_on_last_col_is_a_winning_pattern(self):
        player = Player('test')
        grid = Grid()
        self.assertIsNone(grid.get_winner())
        self.draw_winning_pattern(player, grid, row=0, col=1,
                                  vertical=True, horizontal=False)
        self.assertEqual(player, grid.get_winner())

    def test_left_right_diagonal_is_a_winning_pattern(self):
        player = Player('test')
        grid = Grid()
        self.assertIsNone(grid.get_winner())
        self.draw_winning_pattern(player, grid, row=0, col=0,
                                  vertical=True, horizontal=True)
        self.assertEqual(player, grid.get_winner())

    def test_right_left_diagonal_is_a_winning_pattern(self):
        player = Player('test')
        grid = Grid()
        self.assertIsNone(grid.get_winner())
        self.draw_winning_pattern(player, grid, row=0, col=2,
                                  vertical=True, horizontal=True)
        self.assertEqual(player, grid.get_winner())

    def test_is_empty_can_take_args_for_cell_emptiness(self):
        player = Player('test')
        grid = Grid()
        grid.fill(player, 0, 2)
        self.assertTrue(grid.is_empty(0, 1))
        self.assertFalse(grid.is_empty(0, 2))
