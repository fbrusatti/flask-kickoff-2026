import pytest

from app import create_app
from app.extensions import db

@pytest.fixture(scope="session")
def client():
    app = create_app("testing")

    with app.app_context():
        db.create_all()

    client = app.test_client()

    ctx = app.test_request_context()
    ctx.push()

    yield client

    ctx.pop()
    with app.app_context():
        db.session.remove()
        db.drop_all()
