from flask import Flask, request
from markupsafe import escape
from flask import url_for
from flask import render_template


app = Flask(__name__)

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

"""
Variable routes...
"""
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

"""
Redirection
"""

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()

@app.route('/user/<username>')
def profile(username):
    return f'{escape(username)}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login_get'))
    print(url_for('login_get', next='/'))
    print(url_for('profile', username='John Doe'))

def do_the_login():
    username = request.form.get("username")
    password = request.form.get("password")

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
        <h1>Login</h1>
        <p>Username: {username}</p>
        <p>Password: {password}</p>
    </body>
    </html>
    """

def show_the_login_form():
    return """
        <h1>Login</h1>

        <form method="POST">
            <label>
                Username:
                <input type="text" name="username">
            </label>

            <br><br>

            <label>
                Password:
                <input type="password" name="password">
            </label>

            <br><br>

            <button type="submit">
                Login
            </button>
        </form>
    """

