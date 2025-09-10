from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData
# from sqlmodel import SQLModel, create_engine, Session


# ruta
DATABASE_URL = "sqlite:///./empleados.db"
# motor de conexion a bd
engine = create_engine(
    DATABASE_URL, echo=True
)

metadata = MetaData()
