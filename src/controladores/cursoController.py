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
from clases.cursoClass import cursoClass
from clases.cursoClass import getCursoDocente
from clases.cursoClass import getCursoEstudiante


course_router = APIRouter()

async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn

#get cursos
@course_router.get("/getCursos")
async def getCursos():
    conn = await getConexion()
    try:
        
        cursos=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM Curso")
            resultado = await cur.fetchall()
            for result in resultado:
                curso = {'id_curso': result['id_curso'],'paralelo_curso': result['paralelo_curso'],'materia_curso': result['materia_curso'],'docente_curso': result['docente_curso'],'estudiantes_curso': result['estudiantes_curso'],'ciclo_curso': result['ciclo_curso']}
                cursos.append(curso)
        return {'data': cursos, 'accion': True}
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()

#get cursosdocente
@course_router.post("/getCursosDocente")
async def getCursosDocente(request: Request, miCurso: getCursoDocente = Body(...)):
    conn = await getConexion()
    try:
        docente_curso = miCurso.docente_curso
        #id_paralelo = miCurso.id_paralelo
        #id_materia = miCurso.id_materia

        cursos=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_curso, nombre_materia, nombre_paralelo FROM Curso, Paralelo, Materia   WHERE docente_curso = '{0}' and id_paralelo = paralelo_curso  and id_materia = materia_curso;".format(docente_curso))
            resultado = await cur.fetchall()
            for result in resultado:
                curso = {'id_curso': result['id_curso'],'nombre_materia': result['nombre_materia'],'nombre_paralelo': result['nombre_paralelo']}
                cursos.append(curso)
        return {'data': cursos, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()

#get cursosestudiante con esta sentencia sql: SELECT  id_curso, nombre_materia, nombre_paralelo FROM curso, paralelo, materia, matricula, itemmatricula WHERE estudiante_matricula = 340 and id_paralelo = paralelo_curso  and id_materia = materia_curso and id_curso = curso_itemmatricula and id_matricula = matricula_itemmatricula;
@course_router.post("/getCursosEstudiante")
async def getCursosEstudiante(request: Request, miCurso: getCursoEstudiante = Body(...)):
    conn = await getConexion()
    try:
        estudiante_matricula = miCurso.estudiante_matricula
        #id_paralelo = miCurso.id_paralelo
        #id_materia = miCurso.id_materia

        cursos=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT  id_curso, nombre_materia, nombre_paralelo FROM Curso, Paralelo, Materia, Matricula, itemmatricula WHERE estudiante_matricula = '{0}' and id_paralelo = paralelo_curso  and id_materia = materia_curso and id_curso = curso_itemmatricula and id_matricula = matricula_itemmatricula;".format(estudiante_matricula))
            resultado = await cur.fetchall()
            for result in resultado:
                curso = {'id_curso': result['id_curso'],'nombre_materia': result['nombre_materia'],'nombre_paralelo': result['nombre_paralelo']}
                cursos.append(curso)
        return {'data': cursos, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()