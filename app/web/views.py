from . import web

@web.route('/')
def index():
    return "Hello, world\n"