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
from clases.horarioClass import horarioClass,getHorarioPersonalizado,getHorarioDocente

horario_router = APIRouter()

#clase para validar conexion
async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn

#post getHorarioDocente de este sql: Select id_curso, nombre_materia, modulo_materia, nombre_paralelo, 
#		dia_horario, 
#        concat(horaInicio_horario, ' - ',horaFin_horario) as hora_horario
#from Horario, Curso, Materia, Paralelo
#where   docente_curso = 9
#    and curso_horario = id_curso 
#	and materia_curso = id_materia 
#	and paralelo_curso = id_paralelo;

@horario_router.post("/getHorarioDocente")
async def getHorarioDocente(request: Request, miHorario: getHorarioDocente = Body(...)):
    conn = await getConexion()
    try:
        docente_curso = miHorario.docente_curso

        horarios=[]
        async with conn.cursor() as cur:
            await cur.execute("Select id_curso, nombre_materia, modulo_materia, nombre_paralelo, dia_horario, concat(horaInicio_horario, ' - ',horaFin_horario) as hora_horario from Horario, Curso, Materia, Paralelo where docente_curso = '{0}' and curso_horario = id_curso and materia_curso = id_materia and paralelo_curso = id_paralelo;".format(docente_curso))
            resultado = await cur.fetchall()
            for result in resultado:
                horario = {'id_curso': result['id_curso'],'nombre_materia': result['nombre_materia'],'modulo_materia': result['modulo_materia'],'nombre_paralelo': result['nombre_paralelo'],'dia_horario': result['dia_horario'],'hora_horario': result['hora_horario']}
                horarios.append(horario)
        return {'data': horarios, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()