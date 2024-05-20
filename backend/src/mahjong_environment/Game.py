from Tile import Tile
from Hand import Hand
from random import shuffle

class Game:

    def __init__(self, players):
        self.deck = None
        self.players = players

    def start(self):
        self.deck = [Tile(i, j) for i in Tile.TILE.keys() for j in Tile.TILE[i] for k in range(Tile.TILE_COUNT[i])]
        shuffle(self.deck)
