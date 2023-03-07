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
from clases.pagoDocenteClass import getPagoDocenteByDocenteId
pagoDocente_router = APIRouter()

async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn


#get de todos los pagoDocente: id_pagoDocente,docente_pagoDocente,fecha_pagoDocente,faltas_pagoDocente,descuento_pagoDocente,total_pagoDocente
@pagoDocente_router.get("/getPagoDocentes")
async def getPagoDocentes():
    conn = await getConexion()
    try:
        pagoDocentes=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_pagoDocente,docente_pagoDocente,fecha_pagoDocente,faltas_pagoDocente,descuento_pagoDocente,total_pagoDocente FROM PagoDocente")
            resultado = await cur.fetchall()
            for result in resultado:
                pagoDocente = {'id_pagoDocente': result['id_pagoDocente'],'docente_pagoDocente': result['docente_pagoDocente'],'fecha_pagoDocente': result['fecha_pagoDocente'],'faltas_pagoDocente': result['faltas_pagoDocente'],'descuento_pagoDocente': result['descuento_pagoDocente'],'total_pagoDocente': result['total_pagoDocente']}
                pagoDocentes.append(pagoDocente)
        return {'data': pagoDocentes, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()

#post de pago docente by docente_pagoDocente
@pagoDocente_router.post("/getPagoDocenteByDocenteId")
async def getPagoDocenteByDocenteId(request: Request, pagoDocente: getPagoDocenteByDocenteId):
    conn = await getConexion()
    try:
        pagoDocentes=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_pagoDocente,docente_pagoDocente,fecha_pagoDocente,faltas_pagoDocente,descuento_pagoDocente,total_pagoDocente FROM PagoDocente WHERE docente_pagoDocente=%s",(pagoDocente.docente_pagoDocente))
            resultado = await cur.fetchall()
            for result in resultado:
                pagoDocente = {'id_pagoDocente': result['id_pagoDocente'],'docente_pagoDocente': result['docente_pagoDocente'],'fecha_pagoDocente': result['fecha_pagoDocente'],'faltas_pagoDocente': result['faltas_pagoDocente'],'descuento_pagoDocente': result['descuento_pagoDocente'],'total_pagoDocente': result['total_pagoDocente']}
                pagoDocentes.append(pagoDocente)
        return {'data': pagoDocentes, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()


@pagoDocente_router.get("/getAdminPagoDocentes")
async def getAdminPagoDocentes():
    conn = await getConexion()
    try:
        pagoDocentes=[]
        async with conn.cursor() as cur:
            await cur.execute("""SELECT fecha_pagoDocente, sueldo_contrato, faltas_pagoDocente, 
                                descuento_pagoDocente, total_pagoDocente, cedula_docente, concat(nombres_docente, ' 
                                ', apellidos_docente) AS nombresCompletos_docente
                                FROM Docente, PagoDocente, Contrato
                                WHERE docente_pagoDocente = id_docente = docente_contrato;""")
            resultado = await cur.fetchall()
            for result in resultado:
                pagoDocente = {'fecha_pagoDocente': result['fecha_pagoDocente'],
                               'sueldo_contrato': result['sueldo_contrato'],
                               'faltas_pagoDocente': result['faltas_pagoDocente'],
                               'descuento_pagoDocente': result['descuento_pagoDocente'],
                               'total_pagoDocente': result['total_pagoDocente'],
                               'cedula_docente': result['cedula_docente'],
                               'nombresCompletos_docente': result['nombresCompletos_docente']}
                pagoDocentes.append(pagoDocente)
        return {'data': pagoDocentes, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()