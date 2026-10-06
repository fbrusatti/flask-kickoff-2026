import pytest

from app import create_app


@pytest.fixture(scope="session")
def client():
    app = create_app("testing")

    client = app.test_client()

    ctx = app.test_request_context()
    ctx.push()

    yield client

    ctx.pop()
