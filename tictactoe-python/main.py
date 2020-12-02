from app.bad_cell_error import BadCellError
from cli.cli import CLI
from app.game import Game


def main():
    player_interface = CLI()
    player_x, player_o = player_interface.init_players()
    game = Game(player_x, player_o, player_interface)
    while not game.is_won():
        try:
            game.play()
        except BadCellError as bce:
            player_interface.error(bce)
    player_interface.display_winner(game.get_winner(), player_x, player_o, game.grid)


if __name__ == '__main__':
    main()
