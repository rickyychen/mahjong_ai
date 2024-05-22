from Tile import Tile
from Hand import Hand
from random import shuffle, randint

class Game:

    def __init__(self, players):
        self.deck = None
        self.players = players
        self.player_discard_tiles = dict()

    def start(self):
        self.deck = [Tile(i, j) for i in Tile.TILE.keys() for j in Tile.TILE[i] for k in range(Tile.TILE_COUNT[i])]
        shuffle(self.deck)
        for i in range(4):
            for player in self.players:
                for j in range(4):
                    player.addTile(self.deck.pop())

    def play(self):
        