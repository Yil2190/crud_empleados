from sqlalchemy import Table, Column, Integer, String, Float
from database.database import engine, metadata
# from sqlmodel import SQLModel, Field

empleados = Table(
    "empleados",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("cargo", String(50), nullable=False),
    Column("salary", Float, nullable=False))

metadata.create_all(engine)
# Crea la tabla si no existe
