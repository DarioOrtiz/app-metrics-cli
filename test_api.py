# test_api.py
import requests
import json

REST_URL = "http://127.0.0.1:8000/apps/"
GRAPHQL_URL = "http://127.0.0.1:8000/graphql"


def agregar_app(nombre, version, status):
    payload = {"name": nombre, "version": version, "status": status}
    r = requests.post(REST_URL, json=payload)
    if r.status_code == 200:
        print(f" App agregada: {nombre}")
    else:
        print(f" Error agregando app: {r.text}")

def listar_apps_rest():
    r = requests.get(REST_URL)
    if r.status_code == 200:
        apps = r.json()
        print("\n Listado de apps REST:")
        for a in apps:
            print(f"- {a['id']}: {a['name']} ({a['version']}) - {a['status']}")
    else:
        print(f" Error al listar apps: {r.text}")


def listar_apps_graphql():
    query = """
    query {
        apps {
            id
            name
            version
            status
        }
    }
    """
    r = requests.post(GRAPHQL_URL, json={"query": query})
    if r.status_code == 200:
        result = r.json()
        apps = result.get("data", {}).get("apps", [])
        print("\n Listado de apps GraphQL:")
        for a in apps:
            print(f"- {a['id']}: {a['name']} ({a['version']}) - {a['status']}")
    else:
        print(f"❌ Error fetching apps: {r.text}")


if __name__ == "__main__":

    agregar_app("MiApp", "1.0", "active")
    agregar_app("TestApp", "2.3", "inactive")
    agregar_app("DemoApp", "0.9", "active")


    listar_apps_rest()

    listar_apps_graphql()