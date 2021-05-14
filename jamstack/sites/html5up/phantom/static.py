# https://github.com/pymug/website-AV19-AV20

import sys
from os.path import join

import settings
from flask import Flask
from jamstack.api.template import base_context, generate
from livereload import Server

context = base_context()
context.update({
    "info": settings.info,
    "posts": settings.posts
})


def main(args):
    def gen():
        generate('index.html', join(
            settings.OUTPUT_FOLDER, 'index.html'), **context)

        # Generate pages based in sidebar items
        sidebar = settings.info['sidebar']
        for item in sidebar:
            page = sidebar[item]['page']
            generate(page, join(settings.OUTPUT_FOLDER, page), **context)

        # Generate posts pages
        posts = settings.posts['posts']
        for post in posts:
            page = posts[post]['page']
            generate(page, join(
                settings.OUTPUT_FOLDER, page), **context)

    if len(args) > 1 and args[1] == '--server':
        app = Flask(__name__)

        # remember to use DEBUG mode for templates auto reload
        # https://github.com/lepture/python-livereload/issues/144
        app.debug = True
        server = Server(app.wsgi_app)

        # run a shell command
        # server.watch('.', 'make static')

        # run a function

        server.watch('.', gen, delay=5)
        server.watch('*.py')

        # output stdout into a file
        # server.watch('style.less', shell('lessc style.less', output='style.css'))

        server.serve()
    else:
        gen()


if __name__ == '__main__':
    main(sys.argv)
