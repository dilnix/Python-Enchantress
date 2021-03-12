from flask_login import login_user, logout_user, login_required, current_user
from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User

from . import db


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return {'login': 'success'}, 200


@auth.route('/signup')
def signup():
    return {'signup': 'success'}, 200


@auth.route('/logout')
@login_required
def logout():
    email = current_user.email
    logout_user()
    return {f'logout for {email}': 'success'}, 200


@auth.route('/signup', methods=['POST'])
def signup_post():
    values = request.get_json()
    email = values['email']
    name = values['name']
    password = values['password']

    # if this returns a user, then the email already exists in database
    user = User.query.filter_by(email=email).first()

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        return {f'signup for user {user.email}': 'failed, user already exists'}, 400

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name,
                    password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return {f'signup for user {new_user.email}': 'success'}, 200


@auth.route('/login', methods=['POST'])
def login_post():
    while not current_user.is_authenticated():
        values = request.get_json()
        email = values['email']
        password = values['password']
        remember = True if values['remember'] else False

        user = User.query.filter_by(email=email).first()

        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        # if the user doesn't exist or password is wrong, reload the page
        if not user or not check_password_hash(user.password, password):
            return {f'login for user {email}': 'failed, check your details'}, 401

        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        return {f'login for user {user.email}': 'success', 'your user_id': user.id}, 200
    else:
        return {f'login for user {current_user.email}': 'sorry, you already logged in'}, 202
