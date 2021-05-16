import json

OUTPUT_FOLDER = 'dist/'
info = None
posts = None

with open('info.json') as f:
    info = json.load(f)

with open('posts.json') as f:
    posts = json.load(f)
