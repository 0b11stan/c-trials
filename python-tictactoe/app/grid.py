from app.cell import Cell


class Grid:
    def __init__(self):
        self.cells = [
            [Cell(), Cell(), Cell()],
            [Cell(), Cell(), Cell()],
            [Cell(), Cell(), Cell()]
        ]

    def is_empty(self, row=None, col=None):
        if row is not None and col is not None:
            return self.cells[row][col].is_empty()
        else:
            for row in self.cells:
                for cell in row:
                    if not cell.is_empty():
                        return False
            return True

    def fill(self, player, row, col):
        self.cells[row][col].fill(player)

    def _get_horizontal_winner(self):
        for row in self.cells:
            row_win = row[0].player == row[1].player and row[1].player == row[2].player
            if row_win:
                return row[0].player

    def _get_vertical_winner(self):
        for col in range(0, len(self.cells[0])):
            col_win = self.cells[0][col].player == self.cells[1][col].player and \
                      self.cells[1][col].player == self.cells[2][col].player and \
                      self.cells[0][col].player is not None
            if col_win:
                return self.cells[0][col].player

    def _get_left_right_diagonal_winner(self):
        win = self.cells[0][0].player == self.cells[1][1].player and \
              self.cells[1][1].player == self.cells[2][2].player and \
              self.cells[0][0].player is not None
        if win:
            return self.cells[0][0].player

    def _get_right_left_diagonal_winner(self):
        win = self.cells[2][0].player == self.cells[1][1].player and \
              self.cells[1][1].player == self.cells[0][2].player and \
              self.cells[2][0].player is not None
        if win:
            return self.cells[2][0].player

    def get_winner(self):
        return self._get_horizontal_winner() or \
               self._get_vertical_winner() or \
               self._get_left_right_diagonal_winner() or \
               self._get_right_left_diagonal_winner()
