from app.AMZ_killer import Users, Carts, NoSuchUser, NoSuchCart
from flask import Flask
from flask_restful import Api

amz_killer = Flask(__name__)
api = Api(amz_killer)


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


api.add_resource(Users, '/users', '/users/<int:user_id>')
api.add_resource(Carts, '/carts', '/carts/<int:cart_id>')


if __name__ == '__main__':
    amz_killer.run(debug=True)
