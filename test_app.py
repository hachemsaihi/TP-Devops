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


def test_divide(client):
    response = client.get("/divide?numerator=10&denominator=2")
    assert response.json == {"result": 5.0}
    assert response.status_code == 200

    response = client.get("/divide?numerator=10&denominator=0")
    assert b"Cannot divide by zero!" in response.data
    assert response.status_code == 400

    response = client.get("/divide?numerator=10&denominator=abc")
    assert b"Invalid input!" in response.data
    assert response.status_code == 400


def test_create_user(client):
    response = client.post("/user", json={"name": "Alice"})
    assert response.json == {"user": {"name": "Alice"}}
    assert response.status_code == 201
