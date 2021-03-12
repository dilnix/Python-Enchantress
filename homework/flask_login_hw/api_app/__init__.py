from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.cli import AppGroup

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
user_cli = AppGroup("user")


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'my_secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager = LoginManager()
    # login_manager.login_view = 'auth.login' # not needed more
    login_manager.init_app(app)

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    @app.cli.command('create-db')
    def create_db():
        db.create_all()

    app.cli.add_command(user_cli)

    return app
