from fastapi.testclient import TestClient
from api.main import app  # <-- cambiar 'main' por 'api.main'

client = TestClient(app)

def test_add_app():
    response = client.post("/apps/", json={"name":"TestApp","version":"1.0","status":"active"})
    assert response.status_code == 200
    assert response.json()["name"] == "TestApp"

def test_list_apps():
    response = client.get("/apps/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)