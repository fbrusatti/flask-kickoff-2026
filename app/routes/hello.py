from flask import Blueprint

bp = Blueprint('hello', __name__)

@bp.get('/hello')
def login_get():
    return f'Hola mundo'
