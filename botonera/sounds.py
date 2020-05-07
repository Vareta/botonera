import json

LIBRARY_PATH = './botonera/sounds.json'

library = {}
with open(LIBRARY_PATH, 'r') as f:
    library = json.load(f)['sounds']