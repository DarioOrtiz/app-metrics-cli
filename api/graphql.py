import strawberry
from typing import List
from sqlalchemy.orm import Session
from .db import SessionLocal
from .models import App


@strawberry.type
class AppType:
    id: int
    name: str
    version: str
    status: str

# Resolver de consultas
def get_apps_resolver() -> List[AppType]:
    with SessionLocal() as db:
        apps = db.query(App).all()
        return [AppType(id=a.id, name=a.name, version=a.version, status=a.status) for a in apps]


@strawberry.type
class Query:
    apps: List[AppType] = strawberry.field(resolver=get_apps_resolver)


schema = strawberry.Schema(query=Query)