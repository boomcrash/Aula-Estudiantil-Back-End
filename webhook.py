from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    if request.method == 'POST':
        payload = request.json
        if payload['ref'] == 'refs/heads/main':
            subprocess.call(['git', 'pull'])
            subprocess.call(['pm2', 'restart', 'aula-backend'])
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)