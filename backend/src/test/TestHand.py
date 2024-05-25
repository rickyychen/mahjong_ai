import unittest, sys

sys.path.insert(0, './backend/src/mahjong_environment')

from Tile import Tile
from Hand import Hand

class TestHand(unittest.TestCase):
    
    def setUp(self):
        self.tile_c1 = Tile('C', 1).get_index()
        self.tile_c2 = Tile('C', 2).get_index()
        self.tile_c3 = Tile('C', 3).get_index()
        self.tile_c4 = Tile('C', 4).get_index()
        self.hand = Hand()
    
    def testIsWinPairNonFlush(self):
        self.hand.addTile(self.tile_c1)
        self.assertTrue(self.hand.is_win(self.tile_c1))

    def testIsWinNonPairFlush(self):
        self.hand.addTile(self.tile_c1)
        self.hand.addTile(self.tile_c2)
        self.assertFalse(self.hand.is_win(self.tile_c3))

    def testIsWinPairFlush(self):
        hand = Hand([self.tile_c1, self.tile_c1, self.tile_c2, self.tile_c3])
        self.assertTrue(hand.is_win(self.tile_c4))
        hand = Hand([self.tile_c1, self.tile_c1, self.tile_c1, self.tile_c2])
        self.assertTrue(hand.is_win(self.tile_c3))
    
    def testIsWinTwoPairs(self):
        hand = Hand([self.tile_c1, self.tile_c1, self.tile_c2])
        self.assertFalse(hand.is_win(self.tile_c2))