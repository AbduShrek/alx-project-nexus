# ALX Project Nexus

My Backend Learning Notes & Journey

This repo is my small “knowledge place” for everything I learned in the ALX Backend Engineering program.
I made it to help myself remember things later, and maybe help someone else, too.
---

## 🛠️ My Chosen Project
### **E-Commerce Backend**
A small backend that supports:

- Products + Categories CRUD
- JWT authentication
- Filtering, sorting, and pagination
- PostgreSQL with indexing

Simple, but real.
---

## 🚀 Deployment (Fly.io)

This project is deployed on **Fly.io** using Docker, Gunicorn, and a managed PostgreSQL database.

You can access the fly.io deployed project here https://alx-project-nexus-hilya.fly.dev/api/docs/

### **Production Setup Includes**
- Dockerized Django application (`Dockerfile`)
- Gunicorn as the production WSGI server
- Environment-based settings:
  - `SECRET_KEY`
  - `DEBUG`
  - `ALLOWED_HOSTS`
  - `DATABASE_URL`
- Fly.io PostgreSQL database attached to the app  
- Automatic static files collection (`collectstatic`)

This was my first real deployment experience, and it taught me something that had always been missing from all my older projects.
---

## 🔧 Things I Can Do Now
- Build APIs with Django
- Make clean database tables
- Add filters, search, and ordering
- Create user login/signup with tokens
- Test APIs using Postman
- Run apps with Docker
- Deploy apps online
- Push code properly with Git/GitHub

Deployment especially removed a big fear for me.  
I still have a lot to learn, but I’m much better than when I started.
---

## 😅 Challenges I Faced
- Serializers are confusing at first
- JWT errors
- Docker “works on my machine” lies
- Deployment mistakes
- Tiny errors that break everything 😅

But after breaking things many times, everything started to click.
---

## 🏃‍♂️ How to Run This Project Locally (Tested on Win 11 only)

If you want to run the backend on your computer after cloning the repo, here are the simple steps:

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/AbduShrek/alx-project-nexus.git
cd alx-project-nexus
```
### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```
### 3️⃣ Activate the Virtual Environment
```bash
venv\Scripts\activate
```
### 4️⃣ Install Requirements
```bash
pip install -r requirements.txt
```
### 5️⃣ Create a .env File
```ini
SECRET_KEY="Generate a random String very long, very complicated"
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```
  (You can use SQLite locally. No need for PostgreSQL.)
### 6️⃣ Run Migrations
```bash
python manage.py migrate
```
### 7️⃣ Create a Superuser (optional)
```bash
python manage.py createsuperuser
```
  Then follow the instructions, and you will be able to sign in as an admin
### 8️⃣ Start the Server
```bash
python manage.py runserver
```
### 🎉 Done!
  Open the project in your browser:

  http://127.0.0.1:8000/api/

  APIs will be available under /api/.
