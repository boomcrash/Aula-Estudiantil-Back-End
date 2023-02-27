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
from clases.docenteClass import docenteClass

teacher_router = APIRouter()

async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn


@teacher_router.get("/getTeachers")
async def getTeachers():
    conn = await getConexion()
    try:
        
        usuarios=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM Docente")
            result = await cur.fetchall()
            for data in result:
                usuario = {'usuario_docente': result['usuario_docente'],'nombres_docente': result['nombres_docente'],'apellidos_docente': result['apellidos_docente'],'cedula_docente': result['cedula_docente'],'fechaNacimiento_docente': result['fechaNacimiento_docente'],'edad_docente': result['edad_docente'],'direccion_docente': result['direccion_docente'],'telefono_docente': result['telefono_docente'],'email_docente': result['email_docente'],'titulo_docente': result['titulo_docente'],'nivelEducacion_docente': result['nivelEducacion_docente'],'estado_docente': result['estado_docente']}
                usuarios.append(usuario)
        return {'data': usuarios, 'accion': "true"}
    except Exception as e:
        return {'data': '', 'accion': "false"}
    finally:
        conn.close()