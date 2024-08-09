# app/__init__.py
from flask import Flask
from app.routes import api_blueprint
from app.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(api_blueprint)

    return app
