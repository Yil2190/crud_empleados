from typing import List

from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from database.database import engine
from models.empleado import empleados
from schemas.empleado_schema import EmpleadoSchema

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Bienvenidos"}


@router.get("/api/empleado", response_model=List[EmpleadoSchema])
def get_empleados():
    with engine.connect() as conn:
        # llamado a todos los usuarios
        result = conn.execute(empleados.select()).fetchall()

        return result

# solicitud de un solo usuario por id


@router.get("/api/empleado/{empleado_id}", response_model=EmpleadoSchema)
def get_empleado(empleado_id):
    with engine.connect() as conn:
        result = conn.execute(empleados.select().where(
            empleados.c.id == empleado_id)).first()
        # obtener los nombres de las columnas
        Columns = empleados.Column.keys()
        # see convierte el resultado a una lista
        empleados_list = [dict(zip(Columns, row))for row in result]
        return empleados_list


@router.post("/api/empleado", status_code=HTTP_201_CREATED)
def create_empleado(data_empleado: EmpleadoSchema):
    new_empleado = data_empleado.dict()
    with engine.begin() as conn:  # cuando ya no se usa se cierra la conexion

        conn.execute(empleados.insert().values(new_empleado))

    # conn.commit()
    return Response(status_code=HTTP_201_CREATED)


@router.put("/api/empleado/{empleado_id}", response_model=EmpleadoSchema)
def update_empleado(data_update: EmpleadoSchema, empleado_id):
    with engine.connect() as conn:
        conn.execute(empleados.update().values(name=data_update.name,
                     cargo=data_update.cargo, salary=data_update.salary))
        result = conn.execute(empleados.select().where(
            empleados.c.id == empleado_id))
        return result


@router.delete("/api/empleado/{empleado_id}", status_code=HTTP_204_NO_CONTENT)
def delete_empleado(empleado_id):
    with engine.connect() as conn:
        conn.execute(empleados.delete().where(empleados.c.id == empleado_id))

        return Response(stats_code=HTTP_204_NO_CONTENT)
