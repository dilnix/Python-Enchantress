from flask import Blueprint


hello = Blueprint('hello', __name__, url_prefix='/hello-bp')


@hello.route('/hi')
def hi():
    return 'hi from blueprint'


@hello.route('/aloha')
def aloha():
    return 'aloha from blueprint'
