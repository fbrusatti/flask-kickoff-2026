from app import create_app

def test_config():
    assert not create_app().testing
    assert create_app('testing').testing

def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hola mundo'

def test_landing_page(client):
    response = client.get('/')
    assert response.status_code == 200

