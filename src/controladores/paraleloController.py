from fastapi import  FastAPI,Request
from fastapi import APIRouter
#import database for mysql
import aiomysql
#libreria que se importa de configuracion.py (contiene las configuraciones del server)
from configuracion import configuracion
#pydantic para validar datos
from pydantic import BaseModel
# parametros de peticiones http en body
from fastapi.param_functions import Body
#importacion de clases de usuario
from clases.estudianteClass import estudianteClass

paralelo_router = APIRouter()

async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn


@paralelo_router.get("/getParalelos")
async def getParalelos():
    conn = await getConexion()
    try:
        
        usuarios=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM Paralelo")
            resultado = await cur.fetchall()
            for result in resultado:
                usuario = {'id_paralelo': result['id_paralelo'],'nombre_paralelo': result['nombre_paralelo']}
                usuarios.append(usuario)
        return {'data': usuarios, 'accion': "true"}
    except Exception as e:
        return {'data': '', 'accion': "false"}
    finally:
        conn.close()
