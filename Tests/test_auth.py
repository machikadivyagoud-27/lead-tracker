import pytest
from fastapi.testclient import TestClient


def test_register_user_success(client: TestClient):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "strongpassword123"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "testuser@example.com"
    assert data["role"] == "user"
    assert data["is_active"] is True
    assert "id" in data


def test_register_duplicate_user(client: TestClient):
    # First registration
    client.post(
        "/api/v1/auth/register",
        json={
            "username": "duplicateuser",
            "email": "duplicate@example.com",
            "password": "password"
        }
    )

    # Second registration with same username
    response = client.post(
        "/api/v1/auth/register",
        json={
            "username": "duplicateuser",
            "email": "another@example.com",
            "password": "password"
        }
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Username or email already exists"
