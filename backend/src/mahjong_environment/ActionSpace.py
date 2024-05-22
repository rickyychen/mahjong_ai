class ActionSpace:
    """
    Action ID: action
    0 - 8: discard character 1 - 9
    9 - 17: discard ton 1 - 9
    18 - 26: discard stick 1 - 9
    27 - 30: discard east west south north
    31 - 33: discard middle, money, blank
    34: pong
    35: gong
    36: win
    37: gong
    """

    def __init__(self, open_tiles, close_tiles):
        self.open_tiles = open_tiles
        self.close_tiles = close_tiles
    
    def display_legal_action(self, tile):
