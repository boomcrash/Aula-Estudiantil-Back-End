class DevelopmentConfig():
    DEBUG=True
    #puerto de conexion
    PORT=3000
    #host de conexion
    HOST="0.0.0.0"
    MYSQL_HOST="localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "centroartesanal"

configuracion={
    'development':DevelopmentConfig
}