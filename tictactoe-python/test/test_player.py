import unittest

from app.player import Player, PlayerX, PlayerO


class TestPlayer(unittest.TestCase):
    def test_init_one_named_player(self):
        p1 = Player('romain')
        self.assertIsNotNone(p1)

    def test_init_one_player_with_symbol(self):
        p1 = Player('romain', 'X')
        self.assertEqual('X', p1.symbol)

    def test_init_x_player(self):
        px = PlayerX('romain')
        self.assertEqual('X', px.symbol)

    def test_init_y_player(self):
        py = PlayerO('romain')
        self.assertEqual('O', py.symbol)
