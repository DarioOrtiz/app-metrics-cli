from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .db import SessionLocal, Base, engine
from .models import App
from .schemas import AppCreate, AppRead
from strawberry.fastapi import GraphQLRouter
from .graphql import schema
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(title="App Metrics CLI API")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/apps/", response_model=AppRead)
def add_app(app: AppCreate, db: Session = Depends(get_db)):
    db_app = App(name=app.name, version=app.version, status=app.status)
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app


@app.get("/apps/", response_model=list[AppRead])
def list_apps(db: Session = Depends(get_db)):
    return db.query(App).all()


@app.put("/apps/{app_id}", response_model=AppRead)
def update_app(app_id: int, app: AppCreate, db: Session = Depends(get_db)):
    db_app = db.query(App).filter(App.id == app_id).first()
    if not db_app:
        raise HTTPException(status_code=404, detail="App no encontrada")

    db_app.name = app.name
    db_app.version = app.version
    db_app.status = app.status
    db.commit()
    db.refresh(db_app)
    return db_app


@app.delete("/apps/{app_id}")
def delete_app(app_id: int, db: Session = Depends(get_db)):
    db_app = db.query(App).filter(App.id == app_id).first()

    if not db_app:
        raise HTTPException(status_code=404, detail="App no encontrada")

    db.delete(db_app)
    db.commit()

    return {"message": f"App con id {app_id} eliminada"}


@app.get("/apps/stats")
def apps_stats(db: Session = Depends(get_db)):
    total = db.query(App).count()
    active = db.query(App).filter(App.status == "active").count()
    inactive = total - active

    return {
        "total": total,
        "active": active,
        "inactive": inactive
    }


graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")