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
from clases.evaluacionClass import getEvaluacionesCursoId,updateOneEvaluacion,getEvaluacionesDocenteId

evaluacion_router = APIRouter()

async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn


#metodo get obtener todas las evaluaciones
@evaluacion_router.get("/getEvaluaciones")
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
@evaluacion_router.post("/getEvaluacionesByIdCurso")
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



@evaluacion_router.put("/updateEvaluacion")
async def updateEvaluacion(request: Request, evaluacion: updateOneEvaluacion = Body(...)):
    conn = await getConexion()
    try:
        cantidad_evaluacion = evaluacion.cantidad_evaluacion
        curso_evaluacion= evaluacion.curso_evaluacion
        promedio_evaluacion=evaluacion.promedio_evaluacion
        async with conn.cursor() as cur:
            await cur.execute("UPDATE EvaluacionDocente  SET cantidad_evaluacion = '{0}',  promedio_evaluacion = '{2}' WHERE curso_evaluacion = '{1}'; ".format(cantidad_evaluacion,curso_evaluacion,promedio_evaluacion))
            result= await conn.commit()
            print(result)
            #validando que se inserto un registro
            if cur.rowcount>0:
                return {'data': {'actualizado':True}, 'accion': True}
            else:
                return {'data': {'actualizado':False}, 'accion': True}
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()



#post obtener itemActas por estudiante_itemActa
@evaluacion_router.post("/getEvaluacionesByDocente")
async def getEvaluacionesByDocente(request: Request, evaluacion: getEvaluacionesDocenteId = Body(...)):
    conn = await getConexion()
    try:
        docente_curso=evaluacion.docente_curso
        Evaluaciones=[]
        async with conn.cursor() as cur:
            await cur.execute("""SELECT nombre_materia, nombre_paralelo, modulo_materia, 
                concat(cantidad_evaluacion,'/','40') AS evaluo, promedio_evaluacion
                FROM EvaluacionDocente, Materia, Paralelo, Curso
                WHERE curso_evaluacion = id_curso
                AND materia_curso = id_materia
                AND paralelo_curso = id_paralelo
                AND docente_curso = '{0}';""".format(docente_curso))
            resultado = await cur.fetchall()
            for result in resultado:
                evaluacion = {'id_itemActa': result['id_itemActa'],'acta_itemActa': result['acta_itemActa'],'estudiante_itemActa': result['estudiante_itemActa'],'promedioCalificaciones_itemActa': result['promedioCalificaciones_itemActa'],'promedioAsistencias_itemActa': result['promedioAsistencias_itemActa'],'estado_itemActa': result['estado_itemActa']}
                Evaluaciones.append(evaluacion)
        return {'data': Evaluaciones, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()