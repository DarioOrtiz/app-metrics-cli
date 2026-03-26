import requests

BASE_URL = "http://127.0.0.1:8000"

def test_add_app():
    app_data = {
        "name": "TestApp",
        "version": "1.0",
        "status": "active"
    }
    resp = requests.post(f"{BASE_URL}/apps/", json=app_data)
    print("Agregar App:", resp.json())

def test_list_apps():
    resp = requests.get(f"{BASE_URL}/apps/")
    print("Listar Apps:", resp.json())

if __name__ == "__main__":
    test_add_app()
    test_list_apps()