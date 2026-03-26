# api/init_db.py
from .db import Base, engine
from .models import App

Base.metadata.create_all(bind=engine)
print("Tablas creadas correctamente")