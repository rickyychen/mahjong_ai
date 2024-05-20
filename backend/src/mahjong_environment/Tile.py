import json


def read_from_config(relative_file_path, key):
    f = open(relative_file_path)

    data = json.load(f)

    f.close()

    return data[key]
class Tile:

    '''
    TILE is a dictionary of allowed pairs of tile_type and tile_value
    key: string where C is character, T is ton, S is stick, W is wind, B is bonus, F is flower 
    value: C, T, S is from 1 to 9; W is 1 to 4 for east, west, south, north; B is 1 to 3 for bonus tiles, F is from 1 to 4 for the 4 seasons
    
    TILE_INDICES indicates the index of tile in list form 
    '''

    # TILE = {'C': {i for i in range(1, 10)}, 'T': {i for i in range(1, 10)}, 'S': {i for i in range(1, 10)}, 'W': {i for i in range(1, 5)}, 'B': {i for i in range(1, 4)}, 'F': {i for i in range(1, 5)}}
    # TILE_INDICES = {'C': 0, 'T': 9, 'S': 18, 'W': 27, 'B': 31, 'F': 34}
    # TILE_COUNT = {'C': 4, 'T': 4, 'S': 4, 'W': 4, 'B': 4, 'F': 2}

    CONFIG_FILE_PATH = 'backend/src/mahjong_environment/config/tile.json'
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