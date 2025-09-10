from pydantic import BaseModel
from typing import Optional


class EmpleadoSchema(BaseModel):
    id: Optional[int] = None
    name: str
    cargo: str
    salary: float


class EmpleadoCreate(BaseModel):
    name: str
    cargo: str
    salary: float
