class PlayersInterface:
    def init_players(self):
        # ASK the name of the two players
        # RETURN a tuple containing the x and o player
        # -> ( player_x : Player, player_y : Player )
        raise NotImplementedError("Player initialisation method should be implemented")

    def choose_cell(self, player, player_x, player_o, grid):
        # ASK the given player coordinates for the next play
        # RETURN a tuple containing the row and col of the nex cell to fill
        # -> ( row : int, col : int )
        raise NotImplementedError("Choosing cell method should be implemented")

    def display_winner(self, winner, player_x, player_o, grid):
        raise NotImplementedError("Display method should be implemented")
