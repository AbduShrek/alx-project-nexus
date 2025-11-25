# alx-project-nexus

## 🚀 Deployment (Fly.io)

* This project is deployed on Fly.io using Docker, Gunicorn, and a managed PostgreSQL database.
* Production Setup Includes
* Dockerized Django application (Dockerfile)
* Gunicorn as the production WSGI server
* Environment-based settings (SECRET_KEY, DEBUG, ALLOWED_HOSTS, DATABASE_URL)
* Fly.io PostgreSQL database attached to the app
* Automatic static files collection (collectstatic)