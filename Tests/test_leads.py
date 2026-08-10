from fastapi.testclient import TestClient


def test_create_lead(client: TestClient):
    response = client.post(
        "/api/v1/leads/",
        json={
            "name": "Test Lead",
            "phone": "9876543210",
            "email": "test@gmail.com",
            "property_type": "apartment",
            "source": "website",
            "budget": 3000000
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Test Lead"
    assert data["phone"] == "9876543210"
    assert data["email"] == "test@gmail.com"
    assert data["property_type"] == "apartment"
    assert data["source"] == "website"
    assert data["budget"] == 3000000
    assert data["status"] == "new"


def test_get_leads(client: TestClient):
    response = client.get("/api/v1/leads/")

    assert response.status_code == 200

    data = response.json()

    assert "total" in data
    assert "items" in data


def test_get_lead_by_id(client: TestClient):
    create_response = client.post(
        "/api/v1/leads/",
        json={
            "name": "John",
            "phone": "9999999999",
            "email": "john@gmail.com",
            "property_type": "villa",
            "source": "website",
            "budget": 5000000
        }
    )

    lead_id = create_response.json()["id"]

    response = client.get(
        f"/api/v1/leads/{lead_id}"
    )

    assert response.status_code == 200
    assert response.json()["id"] == lead_id