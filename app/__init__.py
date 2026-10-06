import os
from flask import Flask

from flask import Flask, request
from markupsafe import escape
from flask import url_for
from flask import render_template


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    os.makedirs(app.instance_path, exist_ok=True)

    # ROUTES
    from .routes.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app
