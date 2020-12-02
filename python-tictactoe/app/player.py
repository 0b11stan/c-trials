class Player:
    def __init__(self, name, symbol=None):
        self.name = name
        self.symbol = symbol


class PlayerX(Player):
    def __init__(self, name):
        super().__init__(name, 'X')


class PlayerO(Player):
    def __init__(self, name):
        super().__init__(name, 'O')
