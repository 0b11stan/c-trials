from utils import CellState
from agent import Agent

def step(scanner):
    if front_cell_visited(scanner):
        if left_cell_visited(scanner) and left_cell_empty(scanner):
            return False
        orient_left(scanner)
    else:
        if move(scanner):
            mark_empty(scanner)
        else:
            mark_filled(scanner)
        if not right_cell_visited:
            orient_right(scanner)
    return True


def create_scanner(agent):
    return {
        'field_matrix': [[CellState.AGENT]],
        'current_cell': (0, 0),
        'orientation': (0, 1),
        'agent': agent
    }


def x_border(scanner):
    return scanner['current_cell'][0] != len(scanner['field_matrix'][0]) - 1


def y_border(scanner):
    return scanner['current_cell'][1] != len(scanner['field_matrix']) - 1


def min_border(z):
    return z > 0


def cell_visited(scanner, limit, arg, fy, fx):
    px, py = scanner['current_cell']
    return limit(arg) and scanner['field_matrix'][py+fy][px+fx] != 0


def left_cell_visited(scanner):
    px, py = scanner['current_cell']
    ox, oy = scanner['orientation']
    if oy == 1:    return cell_visited(scanner, min_border, px, 0, -1)
    elif ox == 1:  return cell_visited(scanner, min_border, py, -1, 0)
    elif oy == -1: return cell_visited(scanner, x_border, scanner, 0, -1)
    elif ox == -1: return cell_visited(scanner, y_border, scanner, -1, 0)
    exit("Wrong Orientation")


def front_cell_visited(scanner):
    px, py = scanner['current_cell']
    ox, oy = scanner['orientation']
    if oy == 1:    return cell_visited(scanner, min_border, py, -1, 0)
    elif ox == 1:  return cell_visited(scanner, x_border, scanner, 0, 1)
    elif oy == -1: return cell_visited(scanner, y_border, scanner, 1, 0)
    elif ox == -1: return cell_visited(scanner, min_border, px, 0, -1)
    exit("Wrong Orientation")


def right_cell_visited(scanner):
    px, py = scanner['current_cell']
    ox, oy = scanner['orientation']
    if oy == 1:    return cell_visited(scanner, x_border, scanner, 0, 1)
    elif ox == 1:  return cell_visited(scanner, y_border, scanner, 1, 0)
    elif oy == -1: return cell_visited(scanner, min_border, px, 0, -1)
    elif ox == -1: return cell_visited(scanner, min_border, py, -1, 0)
    exit("Wrong Orientation")


def left_cell_empty(scanner):
    px, py = scanner['current_cell']
    ox, oy = scanner['orientation']
    if oy == 1:
        return scanner['field_matrix'][py][px-1] == 1
    exit("Wrong Orientation")


def mark_cell(scanner, data):
    px, py = scanner['current_cell']
    if scanner['field_matrix'][px][py] != data:
        scanner['field_matrix'][px][py] = data
        return True
    return False


def mark_filled(scanner):
    return mark_cell(scanner, -1)


def mark_empty(scanner):
    return mark_cell(scanner, 1)


def orient_left(scanner):
    scanner['agent'].rotate(-90)
    ox, oy = scanner['orientation']
    scanner['orientation'] = (-1, 0)


def orient_right(scanner):
    scanner['agent'].rotate(90)
    ox, oy = scanner['orientation']
    scanner['orientation'] = (1, 0)


def move(scanner):
    moved = scanner['agent'].move()
    if moved:
        ox, oy = scanner['orientation']
        px, py = scanner['current_cell']
        scanner['current_cell'] = (px + ox, py + oy)
        scanner['orientation'] = (0, 1)
