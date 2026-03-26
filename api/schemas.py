from pydantic import BaseModel

class App(BaseModel):
    name: str
    version: str
    status: str