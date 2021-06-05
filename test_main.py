import json
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

create_country_test_data = json.load(open("test_data/create_country.json"))
test_data = json.load(open("test_data/data.json"))
address_details = json.load(open("test_data/address_details.json"))

country_data = test_data["country"]
state_data = test_data["states"]
address_data = test_data["addresses"]


def test_create_country():
    response = client.post("/api/v1/countries/",
                           headers={"X-Token": "coneofsilence"},
                           json=create_country_test_data)
    assert response.status_code == 201
    assert response.json() == {"detail": "Country created successfully"}


def test_create_existing_country():
    response = client.post("/api/v1/countries/",
                           headers={"X-Token": "coneofsilence"},
                           json=create_country_test_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Country already exists"}


def test_get_all_countries():
    response = client.get("/api/v1/countries/",
                          headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert len(response.json()) == len(country_data)
    assert sorted(response.json()) == sorted(country_data)


def test_get_states_by_country():
    response = client.get("/api/v1/countries/1/states",
                          headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert len(response.json()) == len(state_data)
    assert sorted(response.json()) == sorted(state_data)


def test_get_addresses_by_state():
    response = client.get("/api/v1/countries/states/1/addresses",
                          headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert len(response.json()) == len(address_data)
    assert sorted(response.json()) == sorted(address_data)


def test_get_address_details():
    response = client.get("/api/v1/countries/states/address?address_name=Shantinagar",
                          headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == address_details


# try to get address details using address name as Bashundhora
def test_get_inxistent_address_details():
    response = client.get("/api/v1/countries/states/address?address_name=Bashundhora",
                          headers={"X-Token": "coneofsilence"})
    assert response.status_code == 404
    assert response.json() == {"detail": "No address found"}
