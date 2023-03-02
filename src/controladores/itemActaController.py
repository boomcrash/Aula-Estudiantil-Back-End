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
from clases.itemActaClass import getItemActaByEstudianteId

itemActa_router = APIRouter()

async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn

#metodo get obtener todas las itemActas
@itemActa_router.get("/getItemActas")
async def getItemActas():
    conn = await getConexion()
    try:
        itemActas=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_itemActa,acta_itemActa,estudiante_itemActa,promedioCalificaciones_itemActa,promedioAsistencias_itemActa,estado_itemActa FROM ItemActa")
            resultado = await cur.fetchall()
            for result in resultado:
                itemActa = {'id_itemActa': result['id_itemActa'],'acta_itemActa': result['acta_itemActa'],'estudiante_itemActa': result['estudiante_itemActa'],'promedioCalificaciones_itemActa': result['promedioCalificaciones_itemActa'],'promedioAsistencias_itemActa': result['promedioAsistencias_itemActa'],'estado_itemActa': result['estado_itemActa']}
                itemActas.append(itemActa)
        return {'data': itemActas, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()


#post obtener itemActas por estudiante_itemActa
@itemActa_router.post("/getItemActasByIdEstudiante")
async def getItemActasByIdEstudiante(request: Request, itemActa: getItemActaByEstudianteId = Body(...)):
    conn = await getConexion()
    try:
        itemActas=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_itemActa,acta_itemActa,estudiante_itemActa,promedioCalificaciones_itemActa,promedioAsistencias_itemActa,estado_itemActa FROM ItemActa WHERE estudiante_itemActa=%s", (itemActa.estudiante_itemActa))
            resultado = await cur.fetchall()
            for result in resultado:
                itemActa = {'id_itemActa': result['id_itemActa'],'acta_itemActa': result['acta_itemActa'],'estudiante_itemActa': result['estudiante_itemActa'],'promedioCalificaciones_itemActa': result['promedioCalificaciones_itemActa'],'promedioAsistencias_itemActa': result['promedioAsistencias_itemActa'],'estado_itemActa': result['estado_itemActa']}
                itemActas.append(itemActa)
        return {'data': itemActas, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()