from utils.util import *

class ActionSpace:
    """
    Action ID: action
    0 - 8: discard character 1 - 9
    9 - 17: discard ton 1 - 9
    18 - 26: discard stick 1 - 9
    27 - 30: discard east west south north
    31 - 33: discard middle, money, blank
    34: chi_left
    35: chi_middle
    36: chi_right
    37: pong
    38: gong
    39: win
    40: pass
    """

    STATE_REP_LENGTH = read_from_config(CONFIG_FILE_PATH, "action_state_rep_length")
    ACTIONS = read_from_config(CONFIG_FILE_PATH, "actions")

    def __init__(self, player):
        self.player = player

    def display_legal_actions(self, tile):
        #display legal actions when last player played a tile
        legal_actions = set()
        legal_actions.add(ActionSpace.ACTIONS["pass"])

    def display_legal_actions(self):
        #display legal actions when self draw a tile
        legal_actions = set()
        if self.player.can_win():
            return {ActionSpace.ACTIONS["win"]}
        for tile in self.player.close_tiles():
            legal_actions.add(tile.get_index())