import os
import unittest

from utils import CellState as C
from agent import Agent, Orientation


def create_test_map_file(map_array):
    os.environ['MAP_FILE'] = 'test.map'
    with open(os.environ['MAP_FILE'], 'w') as f:
        for line in map_array:
            strline = [str(char) for char in line]
            f.write('{}\n'.format(''.join(strline)))


def remove_test_map_file():
    os.remove(os.environ['MAP_FILE'])


class TestAgent(unittest.TestCase):
    map_array = [[C.EMPTY, C.FULL, C.EMPTY], [C.EMPTY, C.EMPTY, C.EMPTY], [C.EMPTY, C.EMPTY, C.EMPTY]]

    def setUp(self):
        create_test_map_file(self.map_array)
        self.agent = Agent()

    def tearDown(self):
        remove_test_map_file()

    def test_init(self):
        self.assertEqual(self.map_array, self.agent.environment)
        self.assertEqual({'x': 0, 'y': 0}, self.agent.position)
        self.assertEqual(Orientation.TOP, self.agent.orientation)

    def test_move_up(self):
        self.agent.position = {'x': 0, 'y': 1}
        self.agent.orientation = Orientation.TOP
        self.assertEqual(True, self.agent.move())
        self.assertEqual({'x': 0, 'y': 0}, self.agent.position)

    def test_move_down(self):
        self.agent.orientation = Orientation.DOWN
        self.assertEqual(True, self.agent.move())
        self.assertEqual({'x': 0, 'y': 1}, self.agent.position)

    def test_move_left(self):
        self.agent.position = {'x': 1, 'y': 1}
        self.agent.orientation = Orientation.LEFT
        self.assertEqual(True, self.agent.move())
        self.assertEqual({'x': 0, 'y': 1}, self.agent.position)

    def test_move_right(self):
        self.agent.position = {'x': 0, 'y': 1}
        self.agent.orientation = Orientation.RIGHT
        self.assertEqual(True, self.agent.move())
        self.assertEqual({'x': 1, 'y': 1}, self.agent.position)

    def test_move_against_top_wall(self):
        expect = self.agent.position
        self.assertEqual(False, self.agent.move())
        self.assertEqual(expect, self.agent.position)

    def test_move_against_bottom_wall(self):
        expect = {'x': 0, 'y': len(self.map_array) - 1}
        self.agent.position = expect
        self.agent.orientation = Orientation.DOWN
        self.assertEqual(False, self.agent.move())
        self.assertEqual(expect, self.agent.position)

    def test_move_against_left_wall(self):
        expect = self.agent.position
        self.agent.orientation = Orientation.LEFT
        self.assertEqual(False, self.agent.move())
        self.assertEqual(expect, self.agent.position)

    def test_move_against_right_wall(self):
        expect = {'x': len(self.map_array[0]) - 1, 'y': 0}
        self.agent.position = expect
        self.agent.orientation = Orientation.RIGHT
        self.assertEqual(False, self.agent.move())
        self.assertEqual(expect, self.agent.position)

    def test_move_against_left_obstacle(self):
        expect = {'x': len(self.map_array[0]) - 1, 'y': 0}
        self.agent.position = expect
        self.agent.orientation = Orientation.LEFT
        self.assertEqual(False, self.agent.move())
        self.assertEqual(expect, self.agent.position)

    def _assert_rotates(self, rotation, expects):
        inits = [
            Orientation.TOP, Orientation.RIGHT,
            Orientation.DOWN, Orientation.LEFT
        ]
        for x in range(len(inits)):
            self.agent.orientation = inits[x]
            self.agent.rotate(rotation)
            self.assertEqual(expects[x], self.agent.orientation)
            self.agent.rotate(-rotation)
            self.assertEqual(inits[x], self.agent.orientation)

    def test_rotate_90(self):
        self._assert_rotates(90, [
            Orientation.RIGHT, Orientation.DOWN,
            Orientation.LEFT, Orientation.TOP
        ])

    def test_rotate_180(self):
        self._assert_rotates(180, [
            Orientation.DOWN, Orientation.LEFT,
            Orientation.TOP, Orientation.RIGHT
        ])

    def test_rotate_270(self):
        self._assert_rotates(270, [
            Orientation.LEFT, Orientation.TOP,
            Orientation.RIGHT, Orientation.DOWN
        ])

    def test_rotate_360(self):
        self._assert_rotates(360, [
            Orientation.TOP, Orientation.RIGHT,
            Orientation.DOWN, Orientation.LEFT
        ])


if __name__ == '__main__':
    unittest.main()
