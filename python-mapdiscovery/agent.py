import os

from utils import Orientation, CellState


class Agent:
    def __init__(self, map_file=None):
        map_file = map_file if map_file else os.environ['MAP_FILE']
        self.position = {'x': 0, 'y': 0}
        self.environment = []
        self._read_map(map_file)
        self.orientation = Orientation.TOP

    def _read_map(self, filename):
        with open(filename, 'r') as file:
            line_index = -1
            char_index = -1
            for line in file:
                line_index += 1
                self.environment.append([])
                for char in line:
                    if char != '\n':
                        char_index += 1
                        cell = CellState(char)
                        self.environment[line_index].append(cell)
                        if cell == CellState.AGENT:
                            self.position = {'x': char_index, 'y': line_index}

    def _hit_border(self):
        o = self.orientation
        if o == Orientation.TOP:
            return self.position['y'] == 0
        elif o == Orientation.DOWN:
            return self.position['y'] == len(self.environment) - 1
        elif o == Orientation.LEFT:
            return self.position['x'] == 0
        elif o == Orientation.RIGHT:
            return self.position['x'] == len(self.environment[0]) - 1
        else:
            exit("Wrong Enum")

    def move(self):
        p = self.position.copy()

        if self._hit_border():
            return False

        if self.orientation == Orientation.TOP:
            p['y'] -= 1
        elif self.orientation == Orientation.DOWN:
            p['y'] += 1
        elif self.orientation == Orientation.LEFT:
            p['x'] -= 1
        elif self.orientation == Orientation.RIGHT:
            p['x'] += 1
        else:
            exit("Wrong Enum")

        if (self.environment[p['y']][p['x']] == CellState.FULL):
            return False

        self.position = p
        return True

    def rotate(self, angle):
        orientations = list(Orientation)
        self.orientation = orientations[
            (self.orientation.value + int(angle / 90) - 1) % 4
        ]
