from fastapi import FastAPI
from .schemas import App
from .db import conn
from .graphql import schema
from strawberry.fastapi import GraphQLRouter

app = FastAPI()

@app.post("/apps/")
def add_app(app: App):
    cur = conn.cursor()
    cur.execute("INSERT INTO apps (name, version, status) VALUES (?, ?, ?)",
                (app.name, app.version, app.status))
    conn.commit()
    return {"message": "App added"}

@app.get("/apps/")
def list_apps():
    cur = conn.cursor()
    cur.execute("SELECT id, name, version, status FROM apps")
    apps = cur.fetchall()
    return [{"id": a[0], "name": a[1], "version": a[2], "status": a[3]} for a in apps]

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")