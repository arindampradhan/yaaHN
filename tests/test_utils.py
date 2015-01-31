from os import path

PRESET_DIR = path.join(path.dirname(__file__), 'presets')


def get_content(file):
    with open(path.join(PRESET_DIR, file)) as f:
        return f.read()
