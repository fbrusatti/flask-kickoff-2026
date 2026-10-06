import functools
from flask import make_response

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.get('/login')
def login_get():
    username = request.cookies.get('username')
    print(f"USERNAME: %{username}")

    return render_template('login.html', username=username)

@bp.post('/login')
def login_post():
    error = None
    if valid_login(request.form['username'], request.form['password']):
        resp = make_response(log_the_user_in(request.form['username']))
        resp.set_cookie('username', request.form['username'])
        return resp
    else:
        error = 'Invalid username/password'
        return render_template('login.html', error=error)

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
   return render_template('dashboard.html', username=username)
