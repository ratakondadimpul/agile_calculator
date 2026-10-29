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

def test_multiplication(client):
    response = client.post("/", data={"num1": "10", "num2": "5", "operation": "multiply"})
    assert b"Result: 50.0" in response.data

def test_division(client):
    response = client.post("/", data={"num1": "10", "num2": "5", "operation": "divide"})
    assert b"Result: 2.0" in response.data

def test_division_by_zero(client):
    response = client.post("/", data={"num1": "10", "num2": "0", "operation": "divide"})
    assert b"Result: Error: Division by Zero" in response.data
