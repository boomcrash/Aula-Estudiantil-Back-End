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
from clases.actaClass import getActaCurso,getActaEstudiante,addActaCurso

acta_router = APIRouter()

async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn


#post acta de SELECT nombre_materia, nombre_paralelo, modulo_materia, promedioCalificaciones_itemActa, promedioAsistencias_itemActa, estado_itemActa 
#FROM ItemActa, Materia, Paralelo, Acta, Curso
#WHERE estudiante_itemActa = 601 
#	and id_acta = acta_itemActa 
#	and curso_Acta = id_curso 
#	and materia_curso = id_materia 
#	and paralelo_curso = id_paralelo;
@acta_router.post("/getActaEstudiante")
async def getActaEstudiante(request: Request, miActa: getActaEstudiante = Body(...)):
    conn = await getConexion()
    try:
        estudiante_itemacta = miActa.estudiante_itemacta

        actas=[]
        async with conn.cursor() as cur:
            await cur.execute("""SELECT nombre_materia, nombre_paralelo, modulo_materia, 
                            promedioCalificaciones_itemActa, promedioAsistencias_itemActa, estado_itemActa 
                            FROM ItemActa, Materia, Paralelo, Acta, Curso
                            WHERE estudiante_itemacta = '{0}' 
                            and id_acta = acta_itemActa 
                            and curso_Acta = id_curso 
                            and materia_curso = id_materia 
                            and paralelo_curso = id_paralelo
                            AND estado_acta = 'Activo';""".format(estudiante_itemacta))
            resultado = await cur.fetchall()
            for result in resultado:
                acta = {'nombre_materia': result['nombre_materia'],'nombre_paralelo': result['nombre_paralelo'],'modulo_materia': result['modulo_materia'],'promedioCalificaciones_itemActa': result['promedioCalificaciones_itemActa'],'promedioAsistencias_itemActa': result['promedioAsistencias_itemActa'],'estado_itemActa': result['estado_itemActa']}
                actas.append(acta)
        return {'data': actas, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()

# post acta de SELECT CONCAT(nombreS_ESTUDIANTE, " ", APELLIDOS_ESTUDIANTE) AS NOMBRESCOMPLETOS_ESTUDIANTE, 
#		promedioCalificaciones_itemActa, 
#		promedioAsistencias_itemActa, 
#		estado_itemacta 
#FROM ItemActa, Acta, Estudiante
#WHERE   id_acta = acta_itemActa 
#	and curso_acta = 188
 #   and id_estudiante = estudiante_itemActa;
@acta_router.post("/getActaCurso")
async def getActaCurso(request: Request, miActa: getActaCurso = Body(...)):
    # usando la sentencia sql de arriba
    conn = await getConexion()
    try:
        curso_acta = miActa.curso_acta

        actas=[]
        async with conn.cursor() as cur:
            await cur.execute("""SELECT CONCAT(nombres_estudiante, " ", apellidos_estudiante) AS nombresCompletos_estudiante, 
                            promedioCalificaciones_itemActa, 
                            promedioAsistencias_itemActa, 
                            estado_itemActa 
                            FROM ItemActa, Acta, Estudiante
                            WHERE   id_acta = acta_itemActa 
                            and curso_acta = '{0}'
                            and id_estudiante = estudiante_itemActa
                            AND estado_acta = 'Activo';""".format(curso_acta))
            resultado = await cur.fetchall()
            for result in resultado:
                acta = {'nombresCompletos_estudiante': result['nombresCompletos_estudiante'],'promedioCalificaciones_itemActa': result['promedioCalificaciones_itemActa'],'promedioAsistencias_itemActa': result['promedioAsistencias_itemActa'],'estado_itemActa': result['estado_itemActa']}
                actas.append(acta)
        return {'data': actas, 'accion': True}

    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()


@acta_router.put("/addActa")
async def addActa(request: Request, miActa: addActaCurso = Body(...)):
    conn = await getConexion()
    try:
        curso_acta = miActa.curso_acta
        async with conn.cursor() as cur:
            await cur.execute("UPDATE Acta SET estado_acta = 'Activo' WHERE curso_acta = '{0}';".format(curso_acta))
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