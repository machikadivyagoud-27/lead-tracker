from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# -----------------------
# Health Check
# -----------------------

def test_health():
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }


# -----------------------
# Create Lead
# -----------------------

def test_create_lead():

    response = client.post(
        "/api/v1/leads/",
        json={
            "name": "Moksha",
            "phone": "8889988005",
            "email": "moksha@gmail.com",
            "property_type": "apartment",
            "source": "website",
            "budget": 3000000
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Moksha"
    assert data["status"] == "new"


# -----------------------
# Get All Leads
# -----------------------

def test_get_all_leads():

    response = client.get("/api/v1/leads/")

    assert response.status_code == 200


# -----------------------
# Get Lead By ID
# -----------------------

def test_get_lead_by_id():

    response = client.get("/api/v1/leads/1")

    assert response.status_code == 200


# -----------------------
# Update Lead
# -----------------------

def test_update_lead():

    create_response = client.post(
        "/api/v1/leads/",
        json={
            "name": "Original Lead",
            "phone": "9999999999",
            "email": "original@gmail.com",
            "property_type": "apartment",
            "source": "website",
            "budget": 3000000
        }
    )

    assert create_response.status_code == 200

    lead_id = create_response.json()["id"]

    response = client.patch(
        f"/api/v1/leads/{lead_id}",
        json={
            "name": "Krishna"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Krishna"


# -----------------------
# Delete Lead
# -----------------------

def test_delete_lead():

    response = client.delete("/api/v1/leads/1")

    assert response.status_code in [200, 204]


# -----------------------
# Invalid Email
# -----------------------

def test_invalid_email():

    response = client.post(
        "/api/v1/leads/",
        json={
            "name": "Moksha",
            "phone": "8889988005",
            "email": "abc",
            "property_type": "apartment",
            "source": "website",
            "budget": 3000000
        }
    )

    assert response.status_code == 422


# -----------------------
# Search
# -----------------------

def test_search():

    response = client.get(
        "/api/v1/leads/?search=Moksha"
    )

    assert response.status_code == 200


# -----------------------
# Filter Status
# -----------------------

def test_filter_status():

    response = client.get(
        "/api/v1/leads/?status=new"
    )

    assert response.status_code == 200


# -----------------------
# Filter Property Type
# -----------------------

def test_filter_property():

    response = client.get(
        "/api/v1/leads/?property_type=apartment"
    )

    assert response.status_code == 200


# -----------------------
# Filter Source
# -----------------------

def test_filter_source():

    response = client.get(
        "/api/v1/leads/?source=website"
    )

    assert response.status_code == 200


# -----------------------
# Pagination
# -----------------------

def test_pagination():

    response = client.get(
        "/api/v1/leads/?page=1&page_size=2"
    )

    assert response.status_code == 200


# -----------------------
# Dashboard
# -----------------------

def test_dashboard():

    response = client.get(
        "/api/v1/dashboard/"
    )

    assert response.status_code == 200