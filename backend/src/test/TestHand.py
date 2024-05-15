import unittest, sys

sys.path.insert(0, './backend/src/mahjong_environment')

from Tile import Tile
from Hand import Hand

class TestHand(unittest.TestCase):
    
    def setUp(self):
        tile1_0 = Tile('C', 1)
        tile1_1 = Tile('C', 1)
        self.hand = Hand([tile1_0, tile1_1])
    
    def testIsWin(self):
        self.assertTrue(self.hand.is_win())

if __name__ == "__main__":
    unittest.main()