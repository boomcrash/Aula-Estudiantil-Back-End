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
from clases.entregaClass import updateEntrega


entrega_router = APIRouter()

async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn

#post de updateEntrega con esta sentencia:
#UPDATE Entrega 
#SET fechaEnvio_entrega = '2022-10-04', fechaModificacion_entrega = '2022-10-04', archivo_entrega = 'https://bit.ly/3WsWcY9',
#    estado_entrega = 'Enviada'
#WHERE actividad_entrega = 1  AND estudiante_entrega = 1;

@entrega_router.post("/updateEntrega")
async def updateEntrega(request: Request, miEntrega: updateEntrega = Body(...)):
    conn = await getConexion()
    try:
        fechaEnvio_entrega = miEntrega.fechaEnvio_entrega
        fechaModificacion_entrega = miEntrega.fechaModificacion_entrega
        archivo_entrega = miEntrega.archivo_entrega
        estado_entrega = miEntrega.estado_entrega
        async with conn.cursor() as cur:
            await cur.execute("UPDATE Entrega SET fechaEnvio_entrega = '{0}', fechaModificacion_entrega = '{1}', archivo_entrega = '{2}', estado_entrega = '{3}' WHERE actividad_entrega = 1  AND estudiante_entrega = 1;".format(fechaEnvio_entrega, fechaModificacion_entrega, archivo_entrega, estado_entrega))
            resultado=await conn.commit()
            #validar que si se actualizo el registro
            if resultado == 1:
                return {'data': {'actualizado':True}, 'accion': True}
            else:
                return {'data': {'actualizado':False}, 'accion': True}
    except Exception as e:
         return {'data': '', 'accion': False}
    finally:
        conn.close()