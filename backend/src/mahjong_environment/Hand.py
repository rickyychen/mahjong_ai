from Tile import Tile

class Hand:

    STATE_REP_LENGTH = 38

    def __init__(self, tiles):
        self.close_tiles = tiles
        self.open_tiles = []
    
    def list_form(self):
        hand = [0] * Hand.STATE_REP_LENGTH
        for tile in self.close_tiles:
            hand[tile.get_index()] += 1
        for tile in self.open_tiles:
            hand[tile.get_index()] += 1
        return hand
    
    def is_win(self):
        #reference to this code to determine winning algorithm
        #https://leetcode.com/discuss/interview-question/1921572/find-if-it-is-a-winning-hand-in-mahjong

        def backtracking(tiles, got_pair):
            if not any(tiles):
                return got_pair
            
            for i in range(len(tiles)):
                if tiles[i] == 4:
                    tiles[i] -= 4
                    if backtracking(tiles, got_pair):
                        return True
                    tiles[i] += 4

                if tiles[i] >= 3:
                    tiles[i] -= 3
                    if backtracking(tiles, got_pair):
                        return True
                    tiles[i] += 3

                if tiles[i] == 2 and (not got_pair):
                    tiles[i] -= 2
                    if backtracking(tiles, True):
                        return True
                    tiles[i] += 2

                if tiles[i] > 0:
                    if (((i + 2) % 9) > (i % 9)) and (((i + 1) % 9) > (i % 9)) and i < Tile.TILE_INDICES['W'] and tiles[i + 1] >= 1 and tiles[i + 2] >= 1:
                        tiles[i] -= 1
                        tiles[i + 1] -= 1
                        tiles[i + 2] -= 1
                        if backtracking(tiles, got_pair):
                            return True
                        tiles[i] += 1
                        tiles[i + 1] += 1
                        tiles[i + 2] += 1
            return False
        
        return backtracking(self.list_form(), False)
    
#https://stackoverflow.com/questions/4937771/mahjong-winning-hand-algorithm
#This is the algorithm to determine what tile is good and what tile is bad