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
from clases.actividadClass import getActividadesByCurso


actividad_router = APIRouter()

async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn

#post de getActividadesByCurso con esta sentencia:
#SELECT id_actividad, fechaPublicacion_actividad, 
#		fechaVencimiento_actividad, nombre_actividad, 
#		descripcion_actividad, archivosPermitidos_actividad, 
#        tipo_actividad, count(archivo_entrega) AS envios
#from Actividad, Entrega
#where  curso_actividad = 1
#		AND actividad_entrega = id_actividad
#		AND archivo_entrega IS NOT NULL
#GROUP BY id_actividad;

@actividad_router.post("/getActividadesByCurso")
async def getActividadesByCurso(request: Request, miCurso: getActividadesByCurso = Body(...), response_model=None):
    conn = await getConexion()
    try:
        curso_actividad = miCurso.curso_actividad
        actividades=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT id_actividad, fechaPublicacion_actividad, fechaVencimiento_actividad, nombre_actividad, descripcion_actividad, archivosPermitidos_actividad, tipo_actividad, count(archivo_entrega) AS envios from Actividad, Entrega where  curso_actividad = '{0}' AND actividad_entrega = id_actividad AND archivo_entrega IS NOT NULL GROUP BY id_actividad;".format(curso_actividad))
            resultado = await cur.fetchall()
            for result in resultado:
                actividad = {'id_actividad': result['id_actividad'],'fechaPublicacion_actividad': result['fechaPublicacion_actividad'],'fechaVencimiento_actividad': result['fechaVencimiento_actividad'],'nombre_actividad': result['nombre_actividad'],'descripcion_actividad': result['descripcion_actividad'],'archivosPermitidos_actividad': result['archivosPermitidos_actividad'],'tipo_actividad': result['tipo_actividad'],'envios': result['envios']}
                actividades.append(actividad)
        return {'data': actividades, 'accion': True}
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()

#post de entrgaActividad con esta sentencia:
#SELECT actividad_entrega, estudiante_entrega, fechaEnvio_entrega, fechaModificacion_entrega, archivo_entrega, calificacion_entrega, estado_entrega
#from Actividad, Entrega
#where  curso_actividad = 1
#		AND actividad_entrega = id_actividad;

@actividad_router.post("/entregaActividad")
async def entregaActividad(request: Request, miCurso: getActividadesByCurso = Body(...), response_model=None):
    conn = await getConexion()
    try:
        curso_actividad = miCurso.curso_actividad
        entregas=[]
        async with conn.cursor() as cur:
            await cur.execute("SELECT actividad_entrega, estudiante_entrega, fechaEnvio_entrega, fechaModificacion_entrega, archivo_entrega, calificacion_entrega, estado_entrega from Actividad, Entrega where  curso_actividad = '{0}' AND actividad_entrega = id_actividad;".format(curso_actividad))
            resultado = await cur.fetchall()
            for result in resultado:
                entrega = {'actividad_entrega': result['actividad_entrega'],'estudiante_entrega': result['estudiante_entrega'],'fechaEnvio_entrega': result['fechaEnvio_entrega'],'fechaModificacion_entrega': result['fechaModificacion_entrega'],'archivo_entrega': result['archivo_entrega'],'calificacion_entrega': result['calificacion_entrega'],'estado_entrega': result['estado_entrega']}
                entregas.append(entrega)
        return {'data': entregas, 'accion': True}
    except Exception as e:
        return {'data': '', 'accion': False}
    finally:
        conn.close()


