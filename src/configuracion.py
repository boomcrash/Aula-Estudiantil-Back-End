import os

class DevelopmentConfig():
    DEBUG=True
    #puerto de conexion
    PORT=3000
    #host de conexion
    HOST="0.0.0.0"
    MYSQL_HOST="167.71.26.121"
    MYSQL_USER = "root"
    MYSQL_PASSWORD =os.environ['MYSQL_ROOT_PASSWORD']
    MYSQL_DB = "CENTROARTESANAL"

configuracion={
    'development':DevelopmentConfig
}