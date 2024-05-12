from Tile import Tile
from Hand import Hand
from random import shuffle

class Game:

    def __init__(self):
        self.tiles = [Tile(i, j) for i in Tile.TILE.keys() for j in Tile.TILE[i]]
        shuffle(self.tiles)
        self.deck = Hand(self.tiles)