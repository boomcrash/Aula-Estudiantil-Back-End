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
from clases.materiaClass import getItemMateriaByName    

materia_router = APIRouter()

async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn


#get todas las materias : id_materia, nombre_materia, precio_materia, modulo_materia
@materia_router.get("/getItemMaterias")
async def getItemMaterias():
    conn = await getConexion()
    try:
        itemMaterias=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_materia,nombre_materia,precio_materia,modulo_materia FROM Materia")
            resultado = await cur.fetchall()
            for result in resultado:
                itemMateria = {'id_materia': result['id_materia'],'nombre_materia': result['nombre_materia'],'precio_materia': result['precio_materia'],'modulo_materia': result['modulo_materia']}
                itemMaterias.append(itemMateria)
        return {'data': itemMaterias, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()

#post obtener itemMaterias by nombre_materia
@materia_router.post("/getItemMateriasByName")
async def getItemMateriasByName(request: Request, itemMateria: getItemMateriaByName = Body(...)):
    conn = await getConexion()
    try:
        itemMaterias=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_materia,nombre_materia,precio_materia,modulo_materia FROM Materia WHERE nombre_materia=%s", (itemMateria.nombre_materia))
            resultado = await cur.fetchall()
            for result in resultado:
                itemMateria = {'id_materia': result['id_materia'],'nombre_materia': result['nombre_materia'],'precio_materia': result['precio_materia'],'modulo_materia': result['modulo_materia']}
                itemMaterias.append(itemMateria)
        return {'data': itemMaterias, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()