import pytest

def test_get_users_returns_empty_list(client):
    response = client.get("/users")

    assert response.status_code == 200
    assert response.get_json() == []


def test_create_user(client):
    response = client.post(
        "/users",
        json={
            "name": "Alice",
            "password": "secret",
        },
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["name"] == "Alice"
    assert "id" in data


def test_get_user(client):
    create_response = client.post(
        "/users",
        json={
            "name": "Alice",
            "password": "secret",
        },
    )

    user_id = create_response.get_json()["id"]

    response = client.get(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.get_json()["name"] == "Alice"


def test_update_user(client):
    create_response = client.post(
        "/users",
        json={
            "name": "Alice",
            "password": "secret",
        },
    )

    user_id = create_response.get_json()["id"]

    response = client.patch(
        f"/users/{user_id}",
        json={
            "name": "Alice Updated",
        },
    )

    assert response.status_code == 200
    assert response.get_json()["name"] == "Alice Updated"


def test_get_nonexistent_user_returns_404(client):
    response = client.get("/users/999")

    assert response.status_code == 404


