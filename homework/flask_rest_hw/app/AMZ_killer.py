from flask import Flask, request, jsonify
from datetime import datetime

amz_killer = Flask(__name__)

USERS_DATABASE = {}
CARTS_DATABASE = {}
user_counter = 1
cart_counter = 1


class NoSuchUser(Exception):
    def __init__(self, user_id):
        self.user_id = user_id


class NoSuchCart(Exception):
    def __init__(self, cart_id):
        self.cart_id = cart_id


@amz_killer.route('/users', methods=["POST"])
def create_user():
    global user_counter
    user = request.json
    user['user_id'] = user_counter
    response = {
        "user_id": user_counter,
        "registration_timestamp": datetime.now().isoformat()
    }
    user['registration_timestamp'] = response['registration_timestamp']
    USERS_DATABASE[user_counter] = user

    user_counter += 1

    return response, 201


@amz_killer.errorhandler(NoSuchUser)
def no_such_user_handler(e):
    return {
        "error": f"no such user with id {e}"
    }, 404


@amz_killer.errorhandler(NoSuchCart)
def no_such_cart_handler(e):
    return {
        "error": f"no such cart with id {e}"
    }, 404


@amz_killer.route('/users/<int:user_id>')
def get_user(user_id):
    try:
        user = USERS_DATABASE[user_id]
    except KeyError:
        raise NoSuchUser(user_id)
    else:
        return user


@amz_killer.route('/users/<int:user_id>', methods=['PUT'])
def set_user(user_id):
    data = request.json
    try:
        user = USERS_DATABASE[user_id]
        user['name'] = data['name']
        user['email'] = data['email']
    except KeyError:
        raise NoSuchUser(user_id)
    else:
        return {"status": "success"}, 200


@amz_killer.route('/users/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    global user_counter
    try:
        USERS_DATABASE.pop(user_id)
    except KeyError:
        raise NoSuchUser(user_id)
    else:
        user_counter -= 1
        return {"status": "success"}, 200


@amz_killer.route('/carts', methods=['POST'])
def create_cart():
    global cart_counter
    cart = request.json
    try:
        cart['cart_id'] = cart_counter
        response = {
            "cart_id": cart_counter,
            "creation_time": datetime.now().isoformat()
        }
        cart['creation_time'] = response['creation_time']
        CARTS_DATABASE[cart_counter] = cart
    except KeyError:
        raise NoSuchUser(cart['user_id'])
    else:
        cart_counter += 1
        return response, 201


@amz_killer.route('/carts/<int:cart_id>')
def get_cart(cart_id):
    try:
        cart = CARTS_DATABASE[cart_id]
    except KeyError:
        raise NoSuchCart(cart_id)
    else:
        return cart


@amz_killer.route('/carts/<int:cart_id>', methods=['PUT'])
def set_cart(cart_id):
    data = request.json
    try:
        cart = CARTS_DATABASE[cart_id]
        if cart['user_id'] == data['user_id']:
            cart['products'] = data['products']
        else:
            raise NoSuchUser(data['user_id'])
    except KeyError:
        raise NoSuchCart(cart_id)
    else:
        return {'status': 'success'}, 200


@amz_killer.route('/carts/<int:cart_id>', methods=['DELETE'])
def remove_cart(cart_id):
    global cart_counter
    try:
        CARTS_DATABASE.pop(cart_id)
    except KeyError:
        raise NoSuchCart(cart_id)
    else:
        cart_counter -= 1
        return {'status': 'success'}, 200


if __name__ == '__main__':
    amz_killer.run(debug=True)
