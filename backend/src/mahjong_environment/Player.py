class Player:
    def __init__(self, hand):
        self.hand = hand

    def can_win(self):
        return self.hand.is_win()
    
    def addTile(self, tile):
        self.hand.addTile(tile)

    def discardTile(self, tile):
        self.hand.discardTile(tile)
    
    def can_pong(self, tile):
        return self.hand.can_pong(tile)
    
    def pong(self, tile):
        self.hand.pong(tile)

    def can_gong(self, tile):
        return self.hand.can_gong(tile)
    
    def gong(self, tile):
        self.hand.gong(tile)