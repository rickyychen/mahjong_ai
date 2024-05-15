import unittest, sys

sys.path.insert(0, './backend/src/mahjong_environment')

from Tile import Tile
from Hand import Hand

class TestHand(unittest.TestCase):
    
    def setUp(self):
        self.tile_c1 = Tile('C', 1)
        self.tile_c2 = Tile('C', 2)
        self.tile_c3 = Tile('C', 3)
        self.tile_c4 = Tile('C', 4)
    
    def testIsWinPairNonFlush(self):
        hand = Hand([self.tile_c1, self.tile_c1])
        self.assertTrue(hand.is_win())

    def testIsWinNonPairFlush(self):
        hand = Hand([self.tile_c1, self.tile_c2, self.tile_c3])
        self.assertFalse(hand.is_win())

    def testIsWinPairFlush(self):
        hand = Hand([self.tile_c1, self.tile_c1, self.tile_c2, self.tile_c3, self.tile_c4])
        self.assertTrue(hand.is_win())
        hand = Hand([self.tile_c1, self.tile_c1, self.tile_c1, self.tile_c2, self.tile_c3])
        self.assertTrue(hand.is_win())
    
    def testIsWinTwoPairs(self):
        hand = Hand([self.tile_c1, self.tile_c1, self.tile_c2, self.tile_c2])
        self.assertFalse(hand.is_win())

if __name__ == "__main__":
    unittest.main()