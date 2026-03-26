import strawberry
from typing import List
from .db import conn


@strawberry.type
class AppType:
    id: int
    name: str
    version: str
    status: str

def get_apps() -> List[AppType]:
    cur = conn.cursor()
    cur.execute("SELECT id, name, version, status FROM apps")
    rows = cur.fetchall()
    cur.close()
    return [AppType(id=r[0], name=r[1], version=r[2], status=r[3]) for r in rows]

@strawberry.type
class Query:
    apps: List[AppType] = strawberry.field(resolver=get_apps)

schema = strawberry.Schema(Query)