from Tile import Tile
from Hand import Hand
from random import shuffle, randint

class Game:

    def __init__(self, players, num_dices):
        self.deck = None
        self.players = players
        self.num_dices = num_dices

    def start(self):
        self.deck = [Tile(i, j) for i in Tile.TILE.keys() for j in Tile.TILE[i] for k in range(Tile.TILE_COUNT[i])]
        shuffle(self.deck)
