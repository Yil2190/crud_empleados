from fastapi import FastAPI

from controllers.empleado_controller import router as empleado_router

app = FastAPI(
    title="Sistema de Gestion de Empleados",
    description="CRUD",
    version="1.0.0"

)
# creo las tablas de bd
# SQLModel.metadata.create_all(engine)


@app.get('/')
def root():
    return {'message': 'Bienvenido'}

# revisa si existe la tabla en la bd


app.include_router(empleado_router)

'''@app.on_event('startup')
def on_startup():
    create_db_and_tables()'''
