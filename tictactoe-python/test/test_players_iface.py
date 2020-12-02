import unittest

from app.grid import Grid
from app.player import Player
from app.players_iface import PlayersInterface


class TestPlayerInterface(unittest.TestCase):
    # PlayerInterface is an abstract class
    # and all it's methods should raise a
    # "NotImplementedException"

    def test_init_players_interface(self):
        pi = PlayersInterface()
        self.assertIsNotNone(pi)

    def test_player_interface_can_ask_for_players_initiation(self):
        pi = PlayersInterface()
        with self.assertRaises(NotImplementedError):
            pi.init_players()

    def test_player_interface_can_ask_for_player_to_fill_a_cell(self):
        pi = PlayersInterface()
        x = Player('test')
        o = Player('test')
        g = Grid()
        with self.assertRaises(NotImplementedError):
            pi.choose_cell(x, x, o, g)

    def test_player_interface_can_display_winner(self):
        pi = PlayersInterface()
        x = Player('test')
        o = Player('test')
        g = Grid()
        with self.assertRaises(NotImplementedError):
            pi.display_winner(x, x, o, g)

