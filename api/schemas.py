from pydantic import BaseModel

class AppBase(BaseModel):
    name: str
    version: str
    status: str

class AppCreate(AppBase):
    pass

class AppRead(AppBase):
    id: int  

    class Config:
        orm_mode = True  