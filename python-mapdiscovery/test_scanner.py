import unittest
import os

from utils import CellState as C
from agent import Agent
from scanner import *


def build_scanner(matrix, px, py, ox, oy, agent=None):
    os.environ['MAP_FILE'] = 'test.map'
    with open(os.environ['MAP_FILE'], 'w') as f:
        f.write('\n')
    return {
        'field_matrix': matrix,
        'current_cell': (px, py),
        'orientation': (ox, oy),
        'agent': agent if agent else Agent()
    }


def remove_test_map_file():
    os.remove(os.environ['MAP_FILE'])


class TestScanner(unittest.TestCase):

    def _test_visited(self, function, result, test_matrix):
        for case in test_matrix:
            matrix, px, py, ox, oy = case
            self.assertEqual(result,
                function(
                    build_scanner(matrix, px, py, ox, oy)
                )
            )
        remove_test_map_file()

    def test_left_cell_visited(self):
        self._test_visited(left_cell_visited, True, (
            ([[1, 1]],   1, 0,  0,  1),
            ([[1], [1]], 0, 1,  1,  0),
            ([[1, 1]],   0, 0,  0, -1),
            ([[1], [1]], 0, 0, -1,  0)
        ))

    def test_left_cell_not_visited(self):
        self._test_visited(left_cell_visited, False, (
            ([[0, 1]],   1, 0,  0,  1),
            ([[0], [1]], 0, 1,  1,  0),
            ([[0, 1]],   1, 0,  0, -1),
            ([[1], [0]], 0, 0, -1,  0),
            ([[1]],      0, 0,  0,  1)
        ))

    def test_left_cell_not_visited_wall(self):
        self._test_visited(left_cell_visited, False, (
            ([[1]], 0, 0,  0,  1),
            ([[1]], 0, 0,  1,  0),
            ([[1]], 0, 0,  0, -1),
            ([[1]], 0, 0, -1,  0)
        ))

    def test_right_cell_visited(self):
        self._test_visited(right_cell_visited, True, (
            ([[C.EMPTY, C.EMPTY]],   0, 0,  0,  1),
            ([[C.EMPTY], [C.EMPTY]], 0, 0,  1,  0),
            ([[C.EMPTY, C.EMPTY]],   1, 0,  0, -1),
            ([[C.EMPTY], [C.EMPTY]], 0, 1, -1,  0)
        ))

    def test_right_cell_not_visited(self):
        self._test_visited(right_cell_visited, False, (
            ([[1, 0]],   0, 0,  0,  1),
            ([[1], [0]], 0, 0,  1,  0),
            ([[0, 1]],   1, 0,  0, -1),
            ([[0], [1]], 0, 1, -1,  0)
        ))

    def test_right_cell_not_visited_wall(self):
        self._test_visited(right_cell_visited, False, (
            ([[1]], 0, 0,  0,  1),
            ([[1]], 0, 0,  1,  0),
            ([[1]], 0, 0,  0, -1),
            ([[1]], 0, 0, -1,  0)
        ))

    def test_front_cell_visited(self):
        self._test_visited(front_cell_visited, True, (
            ([[1], [1]], 0, 1,  0,  1),
            ([[1, 1]],   0, 0,  1,  0),
            ([[1], [1]], 0, 0,  0, -1),
            ([[1, 1]], 1, 0, -1,  0)
        ))

    def test_front_cell_not_visited(self):
        self._test_visited(front_cell_visited, False, (
            ([[1, 1]],   0, 0,  0,  1),
            ([[1], [1]], 0, 0,  1,  0),
            ([[1, 1]],   1, 0,  0, -1),
            ([[1], [1]], 0, 1, -1,  0)
        ))

    def test_front_cell_not_visited_wall(self):
        self._test_visited(front_cell_visited, False, (
            ([[1]], 0, 0,  0,  1),
            ([[1]], 0, 0,  1,  0),
            ([[1]], 0, 0,  0, -1),
            ([[1]], 0, 0, -1,  0)
        ))


    def _test_mark_cell(self, marker, cell_init, cell_expect, success):
        scanner = build_scanner([[cell_init]], 0, 0, 0, 1)
        result = marker(scanner)
        self.assertEqual([[cell_expect]], scanner['field_matrix'])
        self.assertEqual(success, result)


    def test_fill_cell(self):
        self._test_mark_cell(mark_filled, 0, -1, True)
        self._test_mark_cell(mark_filled, 1, -1, True)
        self._test_mark_cell(mark_filled, -1, -1, False)


    def test_empty_cell(self):
        self._test_mark_cell(mark_empty, 0, 1, True)
        self._test_mark_cell(mark_empty, 1, 1, False)
        self._test_mark_cell(mark_empty, -1, 1, True)


    def test_orient_left_from_front(self):
        scanner = build_scanner([[-1]], 0, 0, 0, 1)
        orient_left(scanner)
        self.assertEqual((-1, 0), scanner['orientation'])


    def test_orient_right_from_front(self):
        scanner = build_scanner([[-1]], 0, 0, 0, 1)
        orient_right(scanner)
        self.assertEqual((1, 0), scanner['orientation'])


    def test_left_cell_empty_from_front(self):
        scanner = build_scanner([[1, -1]], 1, 0, 0, 1)
        self.assertEqual(True, left_cell_empty(scanner))


    def test_left_cell_not_empty_from_front(self):
        scanner = build_scanner([[0, -1]], 1, 0, 0, 1)
        self.assertEqual(False, left_cell_empty(scanner))


    def test_left_cell_not_empty_from_front_wall(self):
        scanner = build_scanner([[-1]], 0, 0, 0, 1)
        self.assertEqual(False, left_cell_empty(scanner))


    def test_create_scanner(self):
        expect = build_scanner([[C.AGENT]], 0, 0, 0, 1)
        self.assertEqual(expect, create_scanner(expect['agent']))
