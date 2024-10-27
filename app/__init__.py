from flask import Flask
from flask_restx import Api
from flask_security import SQLAlchemyUserDatastore

from .admin import setup_admin
from .config import config
from .extensions import db, ma, migrate, security
from .resources import register_resources


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Setup Flask-Security
    from .models import Role, User

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    # Setup Flask-Admin
    setup_admin(app)

    # Register API resources
    api = Api(app)
    register_resources(api)

    return app
