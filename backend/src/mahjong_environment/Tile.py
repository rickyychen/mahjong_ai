class Tile:

    '''
    TILE is a dictionary of allowed pairs of tile_type and tile_value
    key: string where C is character, T is ton, S is stick, W is wind, B is bonus, F is flower 
    value: C, T, S is from 1 to 9; W is 1 to 4 for east, west, south, north; B is 1 to 3 for 中發白, F is from 1 to 4 for the 4 seasons
    
    TILE_INDICES indicates the index of tile in list form 
    '''

    TILE = {'C': {i for i in range(1, 10)}, 'T': {i for i in range(1, 10)}, 'S': {i for i in range(1, 10)}, 'W': {i for i in range(1, 5)}, 'B': {i for i in range(1, 4)}, 'F': {i for i in range(1, 5)}}
    TILE_INDICES = {'C': 0, 'T': 9, 'S': 18, 'W': 22, 'B': 25, 'F': 29}

    def __init__(self, tile_type, tile_value):
        assert tile_type in Tile.TILE.keys()
        assert tile_value in Tile.TILE[tile_type]
        self.tile_type = tile_type
        self.tile_value = tile_value

    def get_index(self):
        return Tile.TILE_INDICES[self.tile_type] + self.tile_value - 1 