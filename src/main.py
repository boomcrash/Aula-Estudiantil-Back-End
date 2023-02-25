#libreria para abrir server flask
from flask import Flask,jsonify,request
#cors para permitir peticiones desde cualquier origen
from flask_cors import CORS

#libreria para conectar flask con mysql
from flask_mysqldb import MySQL
#libreria que se importa de configuracion.py (contiene las configuraciones del server)
from configuracion import configuracion
#inicializar flask
app = Flask(__name__)
CORS(app)
#generar conexion entre flask y mysql (requiere parametros que estan en configuraciones.py)
conexion=MySQL(app)
#libreria para importar controladores

#importando usuarioController
from controladores.usuario.usuarioController import user
#instancia de usuarioController
user.conexion = conexion
app.register_blueprint(user,url_prefix='/usuario')


def errorCarga(error):
    return "<h1> ERROR AL CARGAR LA PAGINA -> RUTA (no existe)</h1>"

if __name__=="__main__":
    print("EJECUTANDO API")
    # agregar las configuraciones a flask ejemplo: (debug=True)
    app.config.from_object(configuracion['development'])
    # asignarle a flask que hacer en caso de error 404
    app.register_error_handler(404,errorCarga)
    app.run(host=configuracion['development'].HOST,port=configuracion['development'].PORT)
