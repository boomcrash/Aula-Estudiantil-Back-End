from flask import Blueprint, jsonify,request

user = Blueprint('user',__name__)

@user.route('/getUsers',methods=['GET'])
def getUsuarios():
    conexion = user.conexion 
    cursor = conexion.connection.cursor()
    try:
        
        sql = "Select * from usuario"
        cursor.execute(sql)
        datos = cursor.fetchall()
        usuarios=[]
        for data in datos:
            usuario = {'id_usuario': data[0], 'nombre_usuario': data[1], 'contrasena_usuario': data[2], 'rol_usuario': data[3]}
            usuarios.append(usuario)
        return jsonify({'data': usuarios, 'accion': "true"})
    except:
        return jsonify({'data': '','accion': "false"})
    finally:
        cursor.close()
    
@user.route('/getUsersByUserName/<string:username>',methods=['GET'])
def getUsersByUserName(username):
    conexion = user.conexion 
    cursor = conexion.connection.cursor()    
    try:

        sql = "Select * from usuario where nombre_usuario='{0}'".format(username)
        cursor.execute(sql)
        datos = cursor.fetchall()
        usuarios=[]
        for data in datos:
            usuario = {'id_usuario': data[0], 'nombre_usuario': data[1], 'contrasena_usuario': data[2], 'rol_usuario': data[3]}
            usuarios.append(usuario)
        return jsonify({'data': usuarios, 'accion': "true"})
    except:
        return jsonify({'data': '','accion': "false"})
    finally:
        cursor.close()
   

@user.route('/getUsersWithRol',methods=['GET'])
def getUsuariosWithRol():

    conexion = user.conexion 
    cursor = conexion.connection.cursor()
    try:
        sql = "Select * from usuario INNER JOIN rol ON usuario.rol_usuario = rol.id_rol"
        cursor.execute(sql)
        datos = cursor.fetchall()
        usuarios=[]
        for data in datos:
            usuario = {'id_usuario': data[0], 'nombre_usuario': data[1], 'contrasena_usuario': data[2], 'rol_usuario': data[3],'nombre_rol': data[5]}
            usuarios.append(usuario)
        return jsonify({'data': usuarios, 'accion': "true"})
        
    except:
        return jsonify({'data': '','accion': "false"})
    finally:
        cursor.close()
    
@user.route('/getUsersById/<int:id>',methods=['GET'])
def getUsuariosById(id):

    conexion = user.conexion 
    cursor = conexion.connection.cursor()
    try:
        sql = "Select * from usuario INNER JOIN rol ON usuario.rol_usuario = rol.id_rol where id_usuario={0}".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            usuario = {'id_usuario': datos[0], 'nombre_usuario': datos[1], 'contrasena_usuario': datos[2], 'rol_usuario': datos[3],'nombre_rol': datos[5]}
            return jsonify({'data': usuario, 'accion': "true"})
        else:    
            return jsonify({'data': '','accion': "false"})
    except:
        return jsonify({'data': '','accion': "false"})
    finally:
        cursor.close()
    
#getUsuarios con datos dependiendo si el rol_usuario  es docente o estudiante
@user.route('/getUsersCompleteData/<int:id>',methods=['GET'])
def getUsuariosWithRolById(id):
    conexion = user.conexion 
    cursor = conexion.connection.cursor()
    try:
        sql = "Select * from usuario INNER JOIN rol ON usuario.rol_usuario = rol.id_rol where id_usuario={0}".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            usuario = {'nombre_rol': datos[5]}
            if datos[5] == "Docente":
                sql = "Select * from usuario INNER JOIN docente ON usuario.id_usuario = docente.usuario_docente where usuario.id_usuario={0}".format(id)
                cursor.execute(sql)
                datos = cursor.fetchone()
                usuario = {'id_usuario': datos[0], 'nombre_usuario': datos[1], 'contrasena_usuario': datos[2], 'rol_usuario': datos[3],'usuario_docente': datos[4],'nombres_docente': datos[5],'apellidos_docente': datos[6],'cedula_docente': datos[7],'fechaNacimiento_docente': datos[8],'edad_docente': datos[9],'direccion_docente': datos[10],'telefono_docente': datos[11],'email_docente': datos[12],'titulo_docente': datos[13],'nivelEducacion_docente': datos[14],'estado_docente': datos[15]}
            elif datos[5] == "Estudiante":
                sql = "Select * from usuario INNER JOIN estudiante ON usuario.id_usuario = estudiante.usuario_estudiante where usuario.id_usuario={0}".format(id)
                cursor.execute(sql)
                datos = cursor.fetchone()
                usuario = {'id_usuario': datos[0], 'nombre_usuario': datos[1], 'contrasena_usuario': datos[2], 'rol_usuario': datos[3],'usuario_estudiante': datos[4],'nombres_estudiante': datos[5],'apellidos_estudiante': datos[6],'cedula_estudiante': datos[7],'fechaNacimiento_estudiante': datos[8],'edad_estudiante': datos[9],'direccion_estudiante': datos[10],'telefono_estudiante': datos[11],'email_estudiante': datos[12],'nivelEducacion_estudiante': datos[13],'promedioAnterior_estudiante': datos[14],'medio_estudiante': datos[15],'estado_estudiante': datos[16]}

            return jsonify({'data': usuario, 'accion': "true"})
        else:
            return jsonify({'data': '','accion': "false"})
    except:
        return jsonify({'data': '','accion': "false"})
    finally:
        cursor.close()
    



@user.route('/verifyUserByUser',methods=['POST'])
def verifyUserByUser():
    
    conexion = user.conexion 
    cursor = conexion.connection.cursor()
    try:
        username = request.json['username']
        sql = "Select * from usuario where nombre_usuario='{0}' ".format(username)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            result={'existe':True}
            return jsonify({'data': result, 'accion': "true"})
        else:
            result={'existe':False}
            return jsonify({'data': result, 'accion': "false"})
    except:
        return jsonify({'data': '','accion': "false"})
    finally:
        cursor.close()


@user.route('/verifyUserByUserAndPassword',methods=['POST'])
def verifyUserByUserAndPassword():
    
    conexion = user.conexion 
    cursor = conexion.connection.cursor()
    try:
        username = request.json['username']
        password = request.json['password']
        sql = "Select * from usuario where nombre_usuario='{0}' and contrasena_usuario='{1}'".format(username,password)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            result={'existe':True}
            return jsonify({'data': result, 'accion': "true"})
        else:
            result={'existe':False}
            return jsonify({'data': result, 'accion': "false"})
    except:
        return jsonify({'data': '','accion': "false"})
    finally:
        cursor.close()
    