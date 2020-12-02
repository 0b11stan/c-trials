from app.bad_cell_error import BadCellError
from app.grid import Grid


class Game:
    def __init__(self, player_x, player_o, players_interface):
        self.grid = Grid()
        self.player_x = player_x
        self.player_o = player_o
        self.pi = players_interface
        self.current_player = None
        self.current_player = player_x

    def get_switched_player(self):
        return self.player_o if self.current_player == self.player_x else self.player_x

    def play(self):
        (row, col) = self.pi.choose_cell(self.current_player, self.player_x, self.player_o, self.grid)
        if self.grid.is_empty(row, col):
            self.grid.fill(
                player=self.current_player,
                row=row,
                col=col
            )
        else: raise BadCellError(self.current_player, row, col)
        self.current_player = self.get_switched_player()

    def get_winner(self):
        return self.grid.get_winner()

    def is_won(self):
        return True if self.grid.get_winner() is not None else False
