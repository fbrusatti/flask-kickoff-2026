from flask import Blueprint, render_template

bp = Blueprint('hello', __name__)

@bp.get('/hello')
def login_get():
    return f'Hola mundo'

@bp.get('/')
def landing():
    return render_template('landing.html')

