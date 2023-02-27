
#importando controladores
from controladores.usuario.usuarioController import user_router
from controladores.home.homeController import home_router
from controladores.docenteController import teacher_router
from controladores.estudianteController import student_router

#libreria que se importa de configuracion.py (contiene las configuraciones del server)
from configuracion import configuracion
#inicializar flask con fastApi
from fastapi import  FastAPI,Request
#router
from fastapi import APIRouter
#uvicorn execute fastApi
import uvicorn
#pydantic para validar datos
from pydantic import BaseModel
# parametros de peticiones http en body
from fastapi.param_functions import Body
# evitar cors
from fastapi.middleware.cors import CORSMiddleware

#inicializar fastApi
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    student_router,
    prefix='/api/v1/estudiantes',
    tags=['Estudiantes'],
    responses={404: {'description': 'Not found'}}
)

app.include_router(
    teacher_router,
    prefix='/api/v1/docentes',
    tags=['Docentes'],
    responses={404: {'description': 'Not found'}}
)

app.include_router(
    user_router,
    prefix='/api/v1/usuarios',
    tags=['Usuarios'],
    responses={404: {'description': 'Not found'}}
)

app.include_router(
    home_router,
    prefix='/home',
    tags=['Inicio'],
    responses={404: {'description': 'Not found'}}
)

#app.include_router(user_router, prefix="/api/v1")

if __name__=="__main__":
    uvicorn.run(app,host=configuracion['development'].HOST,port=configuracion['development'].PORT)