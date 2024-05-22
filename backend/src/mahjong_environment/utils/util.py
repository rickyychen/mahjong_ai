import json

CONFIG_FILE_PATH = 'backend/src/mahjong_environment/config/tile.json'


def read_from_config(relative_file_path, key):
    f = open(relative_file_path)

    data = json.load(f)

    f.close()

    return data[key]