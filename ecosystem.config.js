module.exports = {
    apps: [{
      name: 'aula-backend',
      script: 'src/app.py',
      cwd: '/home/aula-backend',
      interpreter: 'python3',
      env: {
        NODE_ENV: 'production'
      },
      
    }],
    deploy: {
      production: {
      user: 'root',
      host: '127.0.0.1',
      ref: 'origin/main',
      repo: 'https://github.com/boomcrash/Aula-Estudiantil-Back-End.git',
      path: '/home/aula-backend',
      // Configuración de Git
      "post-deploy": "git pull origin main && pip install -r requirements.txt && pm2 reload ecosystem.config.js --env production"
      }
    }
  };