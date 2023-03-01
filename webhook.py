from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    if request.method == 'POST':
        payload = request.json
        if payload['ref'] == 'refs/heads/main':
            os.chdir('/home/aula-backend')
            result = subprocess.run(['git', 'pull', 'aula', 'main'], capture_output=True)
            if result.returncode != 0:
                # Ocurrió un error al hacer git pull
                return 'Error al hacer git pull', 500
            # Ejecutar el comando pm2 restart
            subprocess.run(['pm2', 'restart', 'aula-backend'])
    return 'OK'

#rertornar hola
@app.route('/hola', methods=['GET'])
def hola():
    return 'Hola Como estas'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)