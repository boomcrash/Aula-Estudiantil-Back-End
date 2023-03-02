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
from clases.ordenPagoMatriculaClass import getOrdenPagoMatriculaByIdPago
ordenPago_router = APIRouter()

async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn

#get obtener todas las ordenes de pago de matricula :id_itemMatricula,matricula_pagoMatricula,item_pagoMatricula,cantidad_pagoMatricula,subtotal_pagoMatricula,descuento_pagoMatricula,total_pagoMatricula
@ordenPago_router.get("/getItemOrdenPagoMatriculas")
async def getItemOrdenPagoMatriculas():
    conn = await getConexion()
    try:
        itemOrdenPagoMatriculas=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_itemMatricula,matricula_pagoMatricula,item_pagoMatricula,cantidad_pagoMatricula,subtotal_pagoMatricula,descuento_pagoMatricula,total_pagoMatricula FROM OrdenPagoMatricula")
            resultado = await cur.fetchall()
            for result in resultado:
                itemOrdenPagoMatricula = {'id_itemMatricula': result['id_itemMatricula'],'matricula_pagoMatricula': result['matricula_pagoMatricula'],'item_pagoMatricula': result['item_pagoMatricula'],'cantidad_pagoMatricula': result['cantidad_pagoMatricula'],'subtotal_pagoMatricula': result['subtotal_pagoMatricula'],'descuento_pagoMatricula': result['descuento_pagoMatricula'],'total_pagoMatricula': result['total_pagoMatricula']}
                itemOrdenPagoMatriculas.append(itemOrdenPagoMatricula)
        return {'data': itemOrdenPagoMatriculas, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()

#post  obtener orden de pago de matricula by matricula_pagoMatricula
@ordenPago_router.post("/getItemOrdenPagoMatriculasByMatriculaId")
async def getItemOrdenPagoMatriculasByMatriculaId(request: Request, itemOrdenPagoMatricula: getOrdenPagoMatriculaByIdPago = Body(...)):
    conn = await getConexion()
    try:
        itemOrdenPagoMatriculas=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_itemMatricula,matricula_pagoMatricula,item_pagoMatricula,cantidad_pagoMatricula,subtotal_pagoMatricula,descuento_pagoMatricula,total_pagoMatricula FROM OrdenPagoMatricula WHERE matricula_pagoMatricula = %s", (itemOrdenPagoMatricula.matricula_pagoMatricula))
            resultado = await cur.fetchall()
            for result in resultado:
                itemOrdenPagoMatricula = {'id_itemMatricula': result['id_itemMatricula'],'matricula_pagoMatricula': result['matricula_pagoMatricula'],'item_pagoMatricula': result['item_pagoMatricula'],'cantidad_pagoMatricula': result['cantidad_pagoMatricula'],'subtotal_pagoMatricula': result['subtotal_pagoMatricula'],'descuento_pagoMatricula': result['descuento_pagoMatricula'],'total_pagoMatricula': result['total_pagoMatricula']}
                itemOrdenPagoMatriculas.append(itemOrdenPagoMatricula)
        return {'data': itemOrdenPagoMatriculas, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()