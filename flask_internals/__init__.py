"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_autoindex import AutoIndex
import os

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    """Construct the core app object."""
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from flask_internals import routes
        from flask_internals.auth import auth_bp
        # Register Blueprints - auth & main.
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth_bp)

        # Create Database Models
        db.create_all()
        return app
