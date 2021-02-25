from flask import request
from flask_restful import Resource
from datetime import datetime

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


class Users(Resource):
    def post(self):
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

    def get(self, user_id):
        try:
            user = USERS_DATABASE[user_id]
        except KeyError:
            raise NoSuchUser(user_id)
        else:
            return user

    def put(self, user_id):
        data = request.json
        try:
            user = USERS_DATABASE[user_id]
            user['name'] = data['name']
            user['email'] = data['email']
        except KeyError:
            raise NoSuchUser(user_id)
        else:
            return {"status": "success"}, 200

    def delete(self, user_id):
        global user_counter
        try:
            USERS_DATABASE.pop(user_id)
        except KeyError:
            raise NoSuchUser(user_id)
        else:
            user_counter -= 1
            return {"status": "success"}, 200


class Carts(Resource):
    def post(self):
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

    def get(self, cart_id):
        try:
            cart = CARTS_DATABASE[cart_id]
        except KeyError:
            raise NoSuchCart(cart_id)
        else:
            return cart

    def put(self, cart_id):
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

    def delete(self, cart_id):
        global cart_counter
        try:
            CARTS_DATABASE.pop(cart_id)
        except KeyError:
            raise NoSuchCart(cart_id)
        else:
            cart_counter -= 1
            return {'status': 'success'}, 200
