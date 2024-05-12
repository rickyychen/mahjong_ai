class Hand:

    STATE_REP_LENGTH = 33

    def __init__(self, tiles):
        self.tiles = tiles
    
    def list_form(self):
        hand = [0] * Hand.STATE_REP_LENGTH
        for tile in self.tiles:
            hand[tile.get_index()] += 1
        return hand