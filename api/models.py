from sqlalchemy import Column, Integer, String
from .db import Base

class App(Base):
    __tablename__ = "apps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    version = Column(String, nullable=False)
    status = Column(String, nullable=False)