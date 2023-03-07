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
from clases.itemMatriculaClass import getItemMatriculasByMatriculaId,addOneItemMatricula

itemMatricula_router = APIRouter()

async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn

#get all item matriculas : id_itemMatricula, matricula_itemMatricula, curso_itemMatricula
@itemMatricula_router.get("/getItemMatriculas")
async def getItemMatriculas():
    conn = await getConexion()
    try:
        itemMatriculas=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_itemMatricula,matricula_itemMatricula,curso_itemMatricula FROM ItemMatricula")
            resultado = await cur.fetchall()
            for result in resultado:
                itemMatricula = {'id_itemMatricula': result['id_itemMatricula'],'matricula_itemMatricula': result['matricula_itemMatricula'],'curso_itemMatricula': result['curso_itemMatricula']}
                itemMatriculas.append(itemMatricula)
        return {'data': itemMatriculas, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()

#post obtener itemMatriculas by matricula_itemMatricula
@itemMatricula_router.post("/getItemMatriculasByMatriculaId")
async def getItemMatriculasByMatriculaId(request: Request, itemMatricula: getItemMatriculasByMatriculaId = Body(...)):
    conn = await getConexion()
    try:
        itemMatriculas=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_itemMatricula,matricula_itemMatricula,curso_itemMatricula FROM ItemMatricula WHERE matricula_itemMatricula=%s", (itemMatricula.matricula_itemMatricula))
            resultado = await cur.fetchall()
            for result in resultado:
                itemMatricula = {'id_itemMatricula': result['id_itemMatricula'],'matricula_itemMatricula': result['matricula_itemMatricula'],'curso_itemMatricula': result['curso_itemMatricula']}
                itemMatriculas.append(itemMatricula)
        return {'data': itemMatriculas, 'accion': True}
    
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()


@itemMatricula_router.post("/addItemMatriculas")
async def addItemMatriculas(request: Request, itemMatricula: addOneItemMatricula = Body(...)):
    conn = await getConexion()
    try:
        #obtener username por medio del body del api
        matricula_itemMatricula = itemMatricula.matricula_itemMatricula
        curso_itemMatricula = itemMatricula.curso_itemMatricula
       
        global insertado
        insertado=False
        #insertar itemMatricula
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO ItemMatricula (matricula_itemMatricula, curso_itemMatricula)  VALUES ('{0}', '{1}');".format(matricula_itemMatricula,curso_itemMatricula))
            await conn.commit()
            #obtener true si se inserto correctamente
            if cur.rowcount > 0:
                insertado=True
        
        return {'data': {'insertado':insertado}, 'accion': True}
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()
