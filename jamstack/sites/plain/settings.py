import json

OUTPUT_FOLDER = 'dist/'
info = None

with open('info.json') as f:
    info = json.load(f)
