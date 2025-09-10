from typing import Optional

from pydantic import BaseModel


class EmpleadoSchema(BaseModel):
    id: Optional[int] = None
    name: str
    cargo: str
    salary: float


'''class EmpleadoCreate(BaseModel):
    name: str
    cargo: str
    salary: float'''
