from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from .schemas import App
from .db import conn  # psycopg2 connection
from .graphql import schema

app = FastAPI(title="App Metrics CLI API")


@app.post("/apps/")
def add_app(app: App):
    try:
        cur = conn.cursor()
        # ⚠️ Cambiado ? por %s
        cur.execute(
            "INSERT INTO apps (name, version, status) VALUES (%s, %s, %s)",
            (app.name, app.version, app.status)
        )
        conn.commit()
        cur.close()
        return {"message": f"App '{app.name}' agregada exitosamente"}
    except Exception as e:
        return {"error": str(e)}


@app.get("/apps/")
def list_apps():
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, name, version, status FROM apps")
        rows = cur.fetchall()
        cur.close()
        apps = [
            {"id": r[0], "name": r[1], "version": r[2], "status": r[3]}
            for r in rows
        ]
        return apps
    except Exception as e:
        return {"error": str(e)}


graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")