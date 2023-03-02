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
from clases.matriculaClass import getItemMatriculaByEstudianteId

matricula_router = APIRouter()

async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn

#get de todos las matriculas : id_matricula, estudiante_matricula, fecha_matricula, ciclo_matricula
@matricula_router.get("/getItemMatriculas")
async def getItemMatriculas():
    conn = await getConexion()
    try:
        itemMatriculas=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_matricula,estudiante_matricula,fecha_matricula,ciclo_matricula FROM Matricula")
            resultado = await cur.fetchall()
            for result in resultado:
                itemMatricula = {'id_matricula': result['id_matricula'],'estudiante_matricula': result['estudiante_matricula'],'fecha_matricula': result['fecha_matricula'],'ciclo_matricula': result['ciclo_matricula']}
                itemMatriculas.append(itemMatricula)
        return {'data': itemMatriculas, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()

#post obtener matriculas by estudiante_matricula
@matricula_router.post("/getItemMatriculasByEstudianteId")
async def getItemMatriculasByEstudianteId(request: Request, itemMatricula: getItemMatriculaByEstudianteId = Body(...)):
    conn = await getConexion()
    try:
        itemMatriculas=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_matricula,estudiante_matricula,fecha_matricula,ciclo_matricula FROM Matricula WHERE estudiante_matricula=%s", (itemMatricula.estudiante_matricula))
            resultado = await cur.fetchall()
            for result in resultado:
                itemMatricula = {'id_matricula': result['id_matricula'],'estudiante_matricula': result['estudiante_matricula'],'fecha_matricula': result['fecha_matricula'],'ciclo_matricula': result['ciclo_matricula']}
                itemMatriculas.append(itemMatricula)
        return {'data': itemMatriculas, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()

