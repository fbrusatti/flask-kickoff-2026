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
    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', person=name)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    @app.route('/')
    def index():
        return 'index'

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        # show the post with the given id, the id is an integer
        return f'Post {post_id}'

    @app.route('/path/<path:subpath>')
    def show_subpath(subpath):
        # show the subpath after /path/
        return f'Subpath {escape(subpath)}'

    @app.route('/projects/')
    def projects():
        return 'The project page'

    @app.route('/about')
    def about():
        return 'The about page'

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        error = None
        if request.method == 'POST':
            if valid_login(request.form['username'],
                        request.form['password']):
                return log_the_user_in(request.form['username'])
            else:
                error = 'Invalid username/password'

        # the code below is executed if the request method
        # was GET or the credentials were invalid
        return render_template('login.html', error=error)

    @app.route('/user/<username>')
    def profile(username):
        return f'{escape(username)}\'s profile'

    return app



def valid_login(username, password):
    # A simple dictionary acting as our temporary "database"
    USER_DATABASE = {
        "admin": "secret123",
        "user1": "password125"
    }

    # 1. Check if the username exists in our records
    if username in USER_DATABASE:
        # 2. Check if the password matches exactly
        return USER_DATABASE[username] == password

    return False

def log_the_user_in(username):
    css_url = url_for('static', filename='style.css')

    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Fondo Multicolor</title>
        <link rel="stylesheet" href="{css_url}">
    </head>
    <body>
        <h1>Hola</h1> {username}
    </body>
    </html>
    """
