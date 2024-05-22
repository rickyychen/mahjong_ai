from Tile import Tile
from utils.util import *

class Hand:

    STATE_REP_LENGTH = read_from_config(CONFIG_FILE_PATH, "hand_state_rep_length")

    def __init__(self, tiles):
        self.close_tiles = tiles
        self.open_tiles = []
    
    def list_form(self):
        hand = [0] * Hand.STATE_REP_LENGTH
        for i in range(Hand.STATE_REP_LENGTH):
            hand[i] += self.open_tiles_list_form()[i] + self.close_tiles_list_form()[i]
        return hand
    
    def close_tiles_list_form(self):
        hand = [0] * Hand.STATE_REP_LENGTH
        for tile in self.close_tiles:
            hand[tile.get_index()] += 1
        return hand
    
    def open_tiles_list_form(self):
        hand = [0] * Hand.STATE_REP_LENGTH
        for tile in self.open_tiles:
            hand[tile.get_index()] += 1
        return hand
    
    def addTile(self, tile):
        self.close_tiles.append(tile)

    def discardTile(self, tile):
        assert self.close_tiles.contains(tile)
        self.close_tiles.remove(tile)

    def can_pong(self, tile):
        return self.close_tiles.count(tile) >= 2
    
    def pong(self, tile):
        for i in range(2):
            self.close_tiles.remove(tile)
            self.open_tiles.append(tile)
        self.open_tiles.append(tile)

    def can_gong(self, tile):
        return self.close_tiles.count(tile) >= 3 or self.open_tiles.count(tile) == 3 
    
    def gong(self, tile):
        if self.open_tiles.count(tile) == 3:
            self.open_tiles.append(tile)
        else:
            for i in range(3):
                self.close_tiles.remove(tile)
                self.open_tiles.append(tile)
            self.open_tiles.append(tile)

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