from main import app
import os
import sys
from fastapi.testclient import TestClient

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

client = TestClient(app)


def test_empleado_payload():
    empleado = {
        "name": "Juan Perez",
        "cargo": "Administrativo",
        "salary": 2500000
    }
    assert isinstance(empleado["name"], str)
    assert isinstance(empleado["cargo"], str)
    assert isinstance(empleado["salary"], (int, float))


def test_salary_positive():
    empleado = {"salary": 2500000}
    assert empleado["salary"] > 0


def test_create_empleado():
    payload = {
        "name": "Juan Test",
        "cargo": "Developer",
        "salary": 3000000
    }

    response = client.post("/api/empleado", json=payload)
    assert response.status_code == 201
