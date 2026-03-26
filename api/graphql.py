import strawberry
from typing import List
from .models import App
from .db import SessionLocal

@strawberry.type
class AppType:
    id: int
    name: str
    version: str
    status: str

def get_apps() -> List[AppType]:
    db = SessionLocal()
    try:
        apps = db.query(App).all()
        return [AppType(id=a.id, name=a.name, version=a.version, status=a.status) for a in apps]
    finally:
        db.close()

@strawberry.type
class Query:
    apps: List[AppType] = strawberry.field(resolver=get_apps)

schema = strawberry.Schema(Query)