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
from clases.contratoClass import getContratosDocenteId

asistencia_router = APIRouter()

async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn


#metodo get para obtener todos los contratos
@asistencia_router.get("/getContratos")
async def getContratos():
    conn = await getConexion()
    try:
        contratos=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_contrato,docente_contrato,fecha_contrato,ciclo_contrato,nombramiento_contrato,especialidad_contrato,tipo_contrato,jornada_contrato,sueldo_contrato FROM Contrato")
            resultado = await cur.fetchall()
            for result in resultado:
                contrato = {'id_contrato': result['id_contrato'],'docente_contrato': result['docente_contrato'],'fecha_contrato': result['fecha_contrato'],'ciclo_contrato': result['ciclo_contrato'],'nombramiento_contrato': result['nombramiento_contrato'],'especialidad_contrato': result['especialidad_contrato'],'tipo_contrato': result['tipo_contrato'],'jornada_contrato': result['jornada_contrato'],'sueldo_contrato': result['sueldo_contrato']}
                contratos.append(contrato)
        return {'data': contratos, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()

#metodo post para obtener contratos mediante docente_contrato
@asistencia_router.post("/getContratosByIdDocente")
async def getContratosByIdDocente(request: Request, contrato: getContratosDocenteId = Body(...)):
    conn = await getConexion()
    try:
        contratos=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_contrato,docente_contrato,fecha_contrato,ciclo_contrato,nombramiento_contrato,especialidad_contrato,tipo_contrato,jornada_contrato,sueldo_contrato FROM Contrato WHERE docente_contrato=%s", (contrato.docente_contrato))
            resultado = await cur.fetchall()
            for result in resultado:
                contrato = {'id_contrato': result['id_contrato'],'docente_contrato': result['docente_contrato'],'fecha_contrato': result['fecha_contrato'],'ciclo_contrato': result['ciclo_contrato'],'nombramiento_contrato': result['nombramiento_contrato'],'especialidad_contrato': result['especialidad_contrato'],'tipo_contrato': result['tipo_contrato'],'jornada_contrato': result['jornada_contrato'],'sueldo_contrato': result['sueldo_contrato']}
                contratos.append(contrato)
        return {'data': contratos, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()
