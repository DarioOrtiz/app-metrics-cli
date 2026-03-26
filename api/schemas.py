from pydantic import BaseModel
from pydantic.types import StringConstraints
from typing import Annotated
from enum import Enum

class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"


NameType = Annotated[str, StringConstraints(min_length=1)]
VersionType = Annotated[str, StringConstraints(pattern=r"^\d+\.\d+(\.\d+)?$")]

class AppBase(BaseModel):
    name: NameType
    version: VersionType
    status: StatusEnum

class AppCreate(AppBase):
    pass

class AppRead(AppBase):
    id: int

    class Config:
        orm_mode = True