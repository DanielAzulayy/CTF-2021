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
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    #AutoIndex(app, browse_root='flask_internals/static/assets/css')
    
    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes
        #from .assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        #app.register_blueprint(auth.auth_bp)

        # Create Database Models
        # db.create_all()
        return app
