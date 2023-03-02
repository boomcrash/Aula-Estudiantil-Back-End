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
from clases.evaluacionClass import getEvaluacionesCursoId

asistencia_router = APIRouter()

async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn


#metodo get obtener todas las evaluaciones
@asistencia_router.get("/getEvaluaciones")
async def getEvaluaciones():
    conn = await getConexion()
    try:
        evaluaciones=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_evaluacion,curso_evaluacion,cantidad_evaluacion,promedio_evaluacion FROM EvaluacionDocente")
            resultado = await cur.fetchall()
            for result in resultado:
                evaluacion = {'id_evaluacion': result['id_evaluacion'],'curso_evaluacion': result['curso_evaluacion'],'cantidad_evaluacion': result['cantidad_evaluacion'],'promedio_evaluacion': result['promedio_evaluacion']}
                evaluaciones.append(evaluacion)
        return {'data': evaluaciones, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()

#post obtener evaluaciones por curso_evaluacion
@asistencia_router.post("/getEvaluacionesByIdCurso")
async def getEvaluacionesByIdCurso(request: Request, evaluacion: getEvaluacionesCursoId = Body(...)):
    conn = await getConexion()
    try:
        evaluaciones=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_evaluacion,curso_evaluacion,cantidad_evaluacion,promedio_evaluacion FROM EvaluacionDocente WHERE curso_evaluacion=%s", (evaluacion.curso_evaluacion))
            resultado = await cur.fetchall()
            for result in resultado:
                evaluacion = {'id_evaluacion': result['id_evaluacion'],'curso_evaluacion': result['curso_evaluacion'],'cantidad_evaluacion': result['cantidad_evaluacion'],'promedio_evaluacion': result['promedio_evaluacion']}
                evaluaciones.append(evaluacion)
        return {'data': evaluaciones, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()