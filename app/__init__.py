import os
from flask import Flask
from config import config
from .extensions import db, migrate


def create_app(environment="development"):
    app = Flask(__name__, instance_relative_config=True)

    os.makedirs(app.instance_path, exist_ok=True)

    # cofigure this app within the environment
    app.config.from_object(config[environment])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)


    # ROUTES
    from .routes.auth import bp as auth_bp
    from .routes.hello import bp as hello_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(hello_bp)

    return app
