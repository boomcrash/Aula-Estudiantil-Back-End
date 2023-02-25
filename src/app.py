
#importando controladores
from controladores.usuario.usuarioController import user_router
from controladores.home.homeController import home_router

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



#inicializar fastApi
app=FastAPI()


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