import pytest

from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    response = client.get("/")
    assert response.data == b"Hello, World!"
    assert response.status_code == 200


def test_get_visitors(client):
    response = client.get("/visitors")
    assert b"Total visitors:" in response.data
    assert response.status_code == 200


def test_visit(client):
    response = client.post("/visit", data={"username": "John"})
    assert b"Welcome, John!" in response.data
    assert response.status_code == 200

    response = client.post("/visit")
    assert b"No username provided!" in response.data
    assert response.status_code == 400
