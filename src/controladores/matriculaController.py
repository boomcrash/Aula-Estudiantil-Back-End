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
from clases.materiaClass import addOneMatricula

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


#addMatricula post addMatricula
@matricula_router.post("/addMatricula")
async def addMatricula(request: Request, matricula: addOneMatricula = Body(...)):
    conn = await getConexion()
    try:
        #obtener username por medio del body del api
        estudiante_matricula = matricula.estudiante_matricula
        fecha_matricula = matricula.fecha_matricula
       
        global insertado
        insertado=False
        #insertar matricula
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO Matricula (estudiante_matricula, fecha_matricula) VALUES ('{0}', '{1}');".format(estudiante_matricula,fecha_matricula))
            await conn.commit()
            #obtener true si se inserto correctamente
            if cur.rowcount > 0:
                insertado=True
        
        return {'data': {'insertado':insertado}, 'accion': True}
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()
