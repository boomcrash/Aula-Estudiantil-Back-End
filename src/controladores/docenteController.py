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
from clases.docenteClass import addUserAndDocente
from clases.docenteClass import addDocenteByUserId


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
            resultado = await cur.fetchall()
            for result in resultado:
                usuario = {'usuario_docente': result['usuario_docente'],'nombres_docente': result['nombres_docente'],'apellidos_docente': result['apellidos_docente'],'cedula_docente': result['cedula_docente'],'fechaNacimiento_docente': result['fechaNacimiento_docente'],'edad_docente': result['edad_docente'],'direccion_docente': result['direccion_docente'],'telefono_docente': result['telefono_docente'],'email_docente': result['email_docente'],'titulo_docente': result['titulo_docente'],'nivelEducacion_docente': result['nivelEducacion_docente'],'estado_docente': result['estado_docente']}
                usuarios.append(usuario)
        return {'data': usuarios, 'accion': "true"}
    except Exception as e:
        return {'data': '', 'accion': "false"}
    finally:
        conn.close()



@teacher_router.post("/addUserAndTeachers")
async def addUserAndTeachers(request: Request, docente: addUserAndDocente = Body(...)):
    conn = await getConexion()
    try:
        #obtener username por medio del body del api
        username = docente.nombre_usuario
        password = docente.contrasena_usuario
        rol = docente.rol_usuario
        nombres = docente.nombres_docente
        apellidos = docente.apellidos_docente
        cedula = docente.cedula_docente
        fechaNacimiento = docente.fechaNacimiento_docente
        edad = docente.edad_docente
        direccion = docente.direccion_docente
        telefono = docente.telefono_docente
        email = docente.email_docente
        titulo = docente.titulo_docente
        nivelEducacion = docente.nivelEducacion_docente
        promedio = docente.promedio_docente

        #variable para saber si se inserto el usuario
        global usuarioInsertado
        usuarioInsertado=False
        #insertar el usuario
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO Usuario(nombre_usuario, contrasena_usuario, rol_usuario) VALUES ('{0}','{1}','{2}')".format(username,password,rol))
            await conn.commit()
            #obtener true si se inserto correctamente
            if cur.rowcount > 0:
                usuarioInsertado=True
            else :
                usuarioInsertado=False
        
        global id_usuario
        if usuarioInsertado:
            id_usuario=0
            #obtener el id del usuario insertado
            async with conn.cursor() as cur:
                await cur.execute("Select id_usuario from Usuario where nombre_usuario='{0}' and contrasena_usuario='{1}'".format(username,password))
                result = await cur.fetchone()
                id_usuario=result['id_usuario']   

        #insertar el docente
        global docenteInsertado
        if usuarioInsertado ==True and id_usuario > 0:
            docenteInsertado=False
            async with conn.cursor() as cur:
                await cur.execute("INSERT INTO Docente(usuario_docente, nombres_docente, apellidos_docente, cedula_docente, fechaNacimiento_docente, edad_docente, direccion_docente, telefono_docente, email_docente, titulo_docente, nivelEducacion_docente,promedio_docente) VALUES ({0},'{1}','{2}','{3}','{4}',{5},'{6}','{7}','{8}','{9}','{10}','{11}')".format(id_usuario,nombres,apellidos,cedula,fechaNacimiento,edad,direccion,telefono,email,titulo,nivelEducacion,promedio))
                await conn.commit()
                #obtener true si se inserto correctamente
                if cur.rowcount > 0:
                    docenteInsertado=True
                else:
                    docenteInsertado=False
        if usuarioInsertado and docenteInsertado:
            return {'data': [{'usuario':usuarioInsertado,'docente':docenteInsertado}], 'accion': "true"}
        else:
            return {'data': [{'usuario':usuarioInsertado,'docente':docenteInsertado}], 'accion': "false"}
    except Exception as e:
        return {'data': '', 'accion': "false"}
    finally:
        conn.close()



@teacher_router.post("/addTeachersByUserId")
async def addTeachersByUserId(request: Request, docente: addDocenteByUserId = Body(...)):
    conn = await getConexion()
    try:
        #obtener username por medio del body del api
        id_usuario = docente.usuario_docente
        nombres = docente.nombres_docente
        apellidos = docente.apellidos_docente
        cedula = docente.cedula_docente
        fechaNacimiento = docente.fechaNacimiento_docente
        edad = docente.edad_docente
        direccion = docente.direccion_docente
        telefono = docente.telefono_docente
        email = docente.email_docente
        titulo = docente.titulo_docente
        nivelEducacion = docente.nivelEducacion_docente
        promedio = docente.promedio_docente
        
        #insertar el docente
        global docenteInsertado
        docenteInsertado=False
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO Docente(usuario_docente, nombres_docente, apellidos_docente, cedula_docente, fechaNacimiento_docente, edad_docente, direccion_docente, telefono_docente, email_docente, titulo_docente, nivelEducacion_docente,promedio_docente) VALUES ({0},'{1}','{2}','{3}','{4}',{5},'{6}','{7}','{8}','{9}','{10}','{11}')".format(id_usuario,nombres,apellidos,cedula,fechaNacimiento,edad,direccion,telefono,email,titulo,nivelEducacion,promedio))
            await conn.commit()
            #obtener true si se inserto correctamente
            if cur.rowcount > 0:
                docenteInsertado=True
            else:
                docenteInsertado=False
        if docenteInsertado:
            return {'data': [{'docente':docenteInsertado}], 'accion': "true"}
        else:
            return {'data': [{'docente':docenteInsertado}], 'accion': "false"}
    except:
        pass
    finally:
        conn.close()
