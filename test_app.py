import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_addition(client):
    response = client.post("/", data={"num1": "10", "num2": "5", "operation": "add"})
    assert b"Result: 15.0" in response.data

def test_subtraction(client):
    response = client.post("/", data={"num1": "10", "num2": "5", "operation": "subtract"})
    assert b"Result: 5.0" in response.data
