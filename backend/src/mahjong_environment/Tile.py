from utils.util import *

class Tile:

    '''
    TILE is a dictionary of allowed pairs of tile_type and tile_value
    key: string where C is character, T is ton, S is stick, W is wind, B is bonus, F is flower 
    value: C, T, S is from 1 to 9; W is 1 to 4 for east, west, south, north; B is 1 to 3 for bonus tiles, F is from 1 to 4 for the 4 seasons
    
    TILE_INDICES indicates the index of tile in list form 
    '''

    TILE = read_from_config(CONFIG_FILE_PATH, "possible_values")
    TILE_INDICES = read_from_config(CONFIG_FILE_PATH, "indices")
    TILE_COUNT = read_from_config(CONFIG_FILE_PATH, "count")

    def __init__(self, tile_type, tile_value):
        assert tile_type in Tile.TILE.keys()
        assert tile_value in Tile.TILE[tile_type]
        self.tile_type = tile_type
        self.tile_value = tile_value

    def get_index(self):
        return Tile.TILE_INDICES[self.tile_type] + self.tile_value - 1 
    
    def __repr__(self):
        return self.tile_type + str(self.tile_value)
    
def get_tile_from_index(index):
    reverse_indices = {j: i for i, j in Tile.TILE_INDICES.items()}
    indices = sorted(list(Tile.TILE_INDICES.values()), reverse=True)
    for i in range(len(indices)):
        if index >= indices[i]:
            return reverse_indices[indices[i]], index - indices[i] + 1