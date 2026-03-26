from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db import SessionLocal, Base, engine
from .models import App
from .schemas import AppCreate, AppRead

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
    apps = db.query(App).all()
    return apps