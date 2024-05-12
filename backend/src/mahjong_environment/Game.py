from random import shuffle
from . import Tile

class Game:

    def __init__(self):
        self.tiles = [Tile(i, j) for i in Tile.TILE.keys() for j in Tile.TILE[i]]
        shuffle(self.tiles)