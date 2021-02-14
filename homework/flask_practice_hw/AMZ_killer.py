from flask import Flask, request, jsonify
from datetime import datetime

amz_killer = Flask(__name__)

USERS_DATABASE = {}
CARTS_DATABASE = {}
CART_DETAILS_DATABASE = {}
user_counter = 1
cart_counter = 1


class NoSuchUser(Exception):
    def __init__(self, user_id):
        self.user_id = user_id


@amz_killer.route('/users', methods=["POST"])
def create_user():
    global user_counter
    user = request.json
    user['user_id'] = user_counter
    response = {
        "registration_timestamp": datetime.now().isoformat(),
        "user_id": user_counter
    }
    user["registration_timestamp"] = response["registration_timestamp"]
    USERS_DATABASE[user_counter] = user

    user_counter += 1

    return response, 201


@amz_killer.errorhandler(NoSuchUser)
def no_such_user_handler(e):
    return {
        "error": f"no such user with id {e}"
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
    try:
        USERS_DATABASE.pop(user_id)
    except KeyError:
        raise NoSuchUser(user_id)
    else:
        return {"status": "success"}, 200


if __name__ == '__main__':
    amz_killer.run(debug=True)
