import unittest
from unittest.mock import MagicMock

from app.bad_cell_error import BadCellError
from app.game import Game
from app.player import Player
from app.players_iface import PlayersInterface


class TestGame(unittest.TestCase):

    class MockPlayerInterface(PlayersInterface):
        def init_players(self):
            pass

        def choose_cell(self, player, player_x, player_y, grid):
            pass

        def display_grid(self, player_x, player_o, grid):
            pass

        def display_player(self, player):
            pass

        def display_winner(self, winner, player_x, player_y, grid):
            pass

        def clear(self):
            pass

    pi = MockPlayerInterface()
    player1 = Player('romain')
    player2 = Player('tristan')

    def test_game_init_an_empty_grid(self):
        game = Game(self.player1, self.player2, self.pi)

        self.assertIsNotNone(game.grid)
        self.assertTrue(game.grid.is_empty())

    def test_playing_may_fill_an_empty_cell_with_first_player_on_first_play(self):
        self.pi.choose_cell = MagicMock(return_value=(0, 1))
        game = Game(self.player1, self.player2, self.pi)

        game.play()

        self.assertFalse(game.grid.is_empty())
        self.assertEqual('romain', game.grid.cells[0][1].player.name)

    def test_playing_change_the_current_user(self):
        game = Game(self.player1, self.player2, self.pi)

        self.pi.choose_cell = MagicMock(return_value=(0, 1))
        game.play()
        self.pi.choose_cell = MagicMock(return_value=(0, 2))
        game.play()

        self.assertFalse(game.grid.is_empty())
        self.assertEqual('romain', game.grid.cells[0][1].player.name)
        self.assertEqual('tristan', game.grid.cells[0][2].player.name)

    def test_playing_a_filled_cell_raise_a_bad_cell_error(self):
        game = Game(self.player1, self.player2, self.pi)
        self.pi.choose_cell = MagicMock(return_value=(0, 1))

        game.play()

        with self.assertRaises(BadCellError):
            game.play()

    def test_is_won_return_the_winning_state(self):
        game = Game(self.player1, self.player2, self.pi)
        game.grid.fill(self.player1, 0, 0)
        game.grid.fill(self.player1, 0, 1)
        game.grid.fill(self.player1, 0, 2)

        self.assertTrue(game.is_won())

    def test_get_winner_return_the_winner(self):
        game = Game(self.player1, self.player2, self.pi)
        game.grid.fill(self.player2, 0, 1)
        game.grid.fill(self.player2, 1, 1)
        game.grid.fill(self.player2, 2, 1)

        self.assertEqual(self.player2, game.get_winner())
