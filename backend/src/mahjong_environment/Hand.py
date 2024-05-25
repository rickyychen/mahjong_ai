from utils.util import *
from Tile import *

class Hand:

    STATE_REP_LENGTH = read_from_config(CONFIG_FILE_PATH, "hand_state_rep_length")

    def __init__(self, tiles_indices=[]):
        self.close_tiles = [0] * Hand.STATE_REP_LENGTH 
        for tile_index in tiles_indices:
            self.close_tiles[tile_index] += 1
        self.open_tiles = [0] * Hand.STATE_REP_LENGTH

    def tiles(self):
        return [i + j for i, j in zip(self.close_tiles, self.open_tiles)]
    
    def addTile(self, tile_index):
        self.close_tiles[tile_index] += 1

    def discardTile(self, tile_index):
        assert self.close_tiles[tile_index] > 0
        self.close_tiles[tile_index] -= 1

    def can_chi_left(self, tile_index):
        #case of chi 1 when have tile 2 and tile 3
        assert tile_index < Tile.TILE_INDICES["W"]
        return (((tile_index + 2) % 9) > (tile_index % 9)) and (((tile_index + 1) % 9) > (tile_index % 9)) and self.close_tiles[tile_index + 2] and self.close_tiles[tile_index + 1]

    def can_chi_middle(self, tile_index):
        assert tile_index < Tile.TILE_INDICES["W"]
        return (((tile_index + 1) % 9) > (tile_index % 9)) and (((tile_index - 1) % 9)) < (tile_index % 9) and self.close_tiles[tile_index - 1] and self.close_tiles[tile_index + 1]

    def can_chi_right(self, tile_index):
        assert tile_index < Tile.TILE_INDICES["W"]
        return (((tile_index - 2) % 9) < (tile_index % 9)) and (((tile_index - 1) % 9) < (tile_index % 9)) and self.close_tiles[tile_index - 2] and self.close_tiles[tile_index - 1]

    def can_pong(self, tile_index):
        return self.close_tiles[tile_index] >= 2
    
    def pong(self, tile_index):
        self.close_tiles[tile_index] -= 2
        self.open_tiles[tile_index] += 3

    def can_gong(self, tile_index):
        return self.close_tiles[tile_index] >= 3 or self.open_tiles[tile_index] == 3 
    
    def gong(self, tile_index):
        if self.open_tiles[tile_index] == 3:
            self.open_tiles[tile_index] += 1
        else:
            self.close_tiles[tile_index] -= 3
            self.open_tiles[tile_index] += 4

    def is_win(self, tile_index):
        #should call this method before add tile to hand
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
        self.addTile(tile_index)
        result = backtracking(self.tiles(), False)
        self.discardTile(tile_index)
        return result
    
    def clear(self):
        self.close_tiles = [0] * Hand.STATE_REP_LENGTH 
        self.open_tiles = [0] * Hand.STATE_REP_LENGTH
    
    def __repr__(self):
        rep = "OPEN: "
        rep += print_tiles_from_list_form(self.open_tiles)
        rep += "\n"
        rep += "CLOSE: "
        rep += print_tiles_from_list_form(self.close_tiles)
        return rep
    
#https://stackoverflow.com/questions/4937771/mahjong-winning-hand-algorithm
#This is the algorithm to determine what tile is good and what tile is bad

def print_tiles_from_list_form(tiles_list_form):
    rep = ""
    for i in range(len(tiles_list_form)):
        for j in range(tiles_list_form[i]):
            tile_type, tile_value = get_tile_from_index(i)
            rep += tile_type + str(tile_value) + ", "
    return rep[:-2]