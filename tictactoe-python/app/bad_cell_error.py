class BadCellError(Exception):
    def __init__(self, player, row, col):
        message = "Cell at ({}, {}) is already take by player {}".format(row, col, player.name)
        super().__init__(message)
