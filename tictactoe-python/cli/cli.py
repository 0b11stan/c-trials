from os import system

from app.player import Player
from app.players_iface import PlayersInterface


class CLI(PlayersInterface):
    def init_players(self):
        name_px = input("Player X name: ")
        name_po = input("Player O name: ")
        return Player(name_px), Player(name_po)

    def choose_cell(self, player, player_x, player_o, grid):
        self.clear()
        self.display_player(player)
        self.display_grid(player_x, player_o, grid)
        row = input("ROW : ")
        col = input("COL : ")
        return int(row) - 1, int(col) - 1

    def display_winner(self, winner, player_x, player_o, grid):
        self.display_grid(player_x, player_o, grid)
        print("{} has won !".format(winner.name))

    @staticmethod
    def error(exception):
        print(str(exception))

    @staticmethod
    def display_player(player):
        print("Your turn {} !".format(player.name))

    @staticmethod
    def display_grid(player_x, player_o, grid):
        print(' 1 2 3')
        for n, row in enumerate(grid.cells):
            print(n + 1, end='')
            for index, cell in enumerate(row):
                if cell.player == player_x:
                    print('X', end='')
                elif cell.player == player_o:
                    print('O', end='')
                else:
                    print(' ', end='')
                if index < len(row) - 1: print('|', end='')
            print('')

    @staticmethod
    def clear():
        system('clear')
