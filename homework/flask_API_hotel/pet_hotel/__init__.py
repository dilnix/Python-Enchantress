from flask import Flask
from pet_hotel.routes import check_in_bp
from pet_hotel.models import db
from pet_hotel.config import Config
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(check_in_bp)
    return app
