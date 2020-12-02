class AlreadyFilledCellException(Exception):
    def __init__(self, cell):
        self.message = "This cell is already filled by user {}".format(cell.player.name)
