module.exports = {
    apps: [{
      name: 'aula-backend',
      script: 'src/app.py',
      cwd: '/home/aula-backend',
      interpreter: 'python3',
      env: {
        NODE_ENV: 'production'
      },
      // Configuración de Git
      "post-deploy": "git pull origin main && pip install -r requirements.txt && pm2 reload ecosystem.config.js --env production"
    }]
  };