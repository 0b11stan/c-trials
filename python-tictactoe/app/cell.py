from app.exceptions import AlreadyFilledCellException


class Cell:
    player = None

    def fill(self, player):
        if self.is_empty():
            self.player = player
        else:
            raise AlreadyFilledCellException(self)

    def is_empty(self):
        return True if self.player is None else False
