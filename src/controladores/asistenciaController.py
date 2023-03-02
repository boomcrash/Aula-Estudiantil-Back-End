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
from clases.asistenciaClass import getAsistenciaEstudiante

asistencia_router = APIRouter()

async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn

#metodo get para obtener:id_asistencia,curso_asistencia,estudiante_asistencia,fecha_asistencia,estado_asistencia
@asistencia_router.get("/getAsistenciasEstudiante")
async def getAsistenciasEstudiante():
    conn = await getConexion()
    try:
        asistencias=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_asistencia,curso_asistencia,estudiante_asistencia,fecha_asistencia,estado_asistencia FROM Asistencia")
            resultado = await cur.fetchall()
            for result in resultado:
                asistencia = {'id_asistencia': result['id_asistencia'],'curso_asistencia': result['curso_asistencia'],'estudiante_asistencia': result['estudiante_asistencia'],'fecha_asistencia': result['fecha_asistencia'],'estado_asistencia': result['estado_asistencia']}
                asistencias.append(asistencia)
        return {'data': asistencias, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()

#metodo get para obtener:id_asistencia,curso_asistencia,estudiante_asistencia,fecha_asistencia,estado_asistencia por estudiante_asistencia
@asistencia_router.post("/getAsistenciasByIdEstudiante")
async def getAsistenciasByIdEstudiante(request: Request, asistencia: getAsistenciaEstudiante = Body(...)):
    conn = await getConexion()
    try:
        asistencias=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_asistencia,curso_asistencia,estudiante_asistencia,fecha_asistencia,estado_asistencia FROM Asistencia WHERE estudiante_asistencia=%s", (asistencia.estudiante_asistencia))
            resultado = await cur.fetchall()
            for result in resultado:
                asistencia = {'id_asistencia': result['id_asistencia'],'curso_asistencia': result['curso_asistencia'],'estudiante_asistencia': result['estudiante_asistencia'],'fecha_asistencia': result['fecha_asistencia'],'estado_asistencia': result['estado_asistencia']}
                asistencias.append(asistencia)
        return {'data': asistencias, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()



