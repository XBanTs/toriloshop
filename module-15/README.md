# ToriloShop — Module 15: Deployment Preparation for Production

## Project Description

Module 15 focuses on transforming ToriloShop from a local development project into a production-ready Django application prepared for deployment on Render.

This module introduces real-world deployment practices including:

- Environment variable management
- PostgreSQL-ready database configuration
- Gunicorn production server setup
- WhiteNoise static file serving
- Production security practices
- `requirements.txt` management
- Render deployment preparation

The application is now fully configured for scalable cloud deployment.

---

# Features Implemented

## Environment Variables & Security

| Feature                 | Description                                       |
| ----------------------- | ------------------------------------------------- |
| `.env` File             | Sensitive values moved into environment variables |
| `python-decouple`       | Reads environment variables securely              |
| `SECRET_KEY` Protection | Removed from hardcoded settings                   |
| `DEBUG=False`           | Production debug disabled                         |
| `ALLOWED_HOSTS`         | Production hosts configured                       |
| `.gitignore` Protection | `.env` excluded from Git tracking                 |

---

## PostgreSQL Configuration

| Feature                | Description                              |
| ---------------------- | ---------------------------------------- |
| `dj-database-url`      | Parses database URLs automatically       |
| PostgreSQL Ready       | Production database support configured   |
| SQLite Fallback        | Local development still supported        |
| Persistent Connections | Database connection optimisation enabled |

---

## Gunicorn Production Server

| Feature                     | Description                        |
| --------------------------- | ---------------------------------- |
| Gunicorn Installed          | Production WSGI server configured  |
| Local Gunicorn Testing      | Verified locally before deployment |
| Concurrent Request Handling | Production-grade request handling  |
| Procfile Created            | Render startup command configured  |

---

## WhiteNoise Static Files

| Feature                 | Description                      |
| ----------------------- | -------------------------------- |
| WhiteNoise Installed    | Static file serving configured   |
| Middleware Added        | WhiteNoise middleware enabled    |
| STATIC_ROOT Configured  | Static files collected correctly |
| Compressed Static Files | Optimised production assets      |

---

## Production Deployment Features

| Feature             | Description                           |
| ------------------- | ------------------------------------- |
| `requirements.txt`  | Generated using `pip freeze`          |
| `collectstatic`     | Static files gathered successfully    |
| Render Preparation  | Project configured for deployment     |
| Production Settings | Deployment-ready Django configuration |

---

# Packages Installed

```bash
pip install python-decouple

pip install dj-database-url psycopg2-binary

pip install gunicorn

pip install whitenoise
```

---

# Environment Variables Example

## `.env`

```env
SECRET_KEY=your-secret-key

DEBUG=False

ALLOWED_HOSTS=localhost,127.0.0.1,yourapp.onrender.com

DATABASE_URL=postgres://user:password@host:5432/dbname
```

---

# Production Database Configuration

```python
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default='sqlite:///db.sqlite3'),
        conn_max_age=600,
    )
}
```

---

# Gunicorn Production Command

```bash
gunicorn toriloshop.wsgi:application
```

---

# Procfile

```bash
web: gunicorn toriloshop.wsgi --log-file -
```

---

# WhiteNoise Configuration

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
```

---

# Static Files Configuration

```python
STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

---

# requirements.txt Generation

```bash
pip freeze > requirements.txt
```

---

# collectstatic Command

```bash
python manage.py collectstatic --noinput
```

---

# Setup Instructions

```bash
git clone <your-repository-url>

cd module-15/toriloshop

python -m venv venv

venv\Scripts\activate
# source venv/bin/activate

pip install -r requirements.txt
```

---

# Local Environment Setup

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key

DEBUG=True

ALLOWED_HOSTS=127.0.0.1,localhost
```

---

# Run Development Server

```bash
python manage.py migrate

python manage.py runserver
```

---

# Run Production Server Locally

```bash
waitress-serve --host-0.0.0.0 --port=8000 toriloshop.wsgi:application
```

---

# Pre-Deployment Checklist

- `.env` created successfully
- `SECRET_KEY` removed from settings.py
- `.env` excluded from Git tracking
- PostgreSQL configuration completed
- Gunicorn installed successfully
- WhiteNoise configured correctly
- `collectstatic` executed successfully
- `requirements.txt` updated
- Procfile created successfully
- Project committed and pushed to GitHub

---

# Screenshots

## Waitress Running Successfully (In place of Gunicorn)

Waitress production server started successfully without errors.

![Gunicorn Running](screenshots/01_gunicorn_running.png)

---

## collectstatic Output

Static files successfully collected into the `staticfiles/` directory.

![Collectstatic](screenshots/02_collectstatic_output.png)

---

## requirements.txt Verification

Verified that all required deployment packages are listed.

![Requirements](screenshots/03_requirements_txt.png)

---

## .env Excluded from Git Tracking

Confirmed `.env` is excluded correctly using `.gitignore`.

![Gitignore](screenshots/04_gitignore_env_excluded.png)

---

# Repository Structure

```bash
module-15/
│
├── toriloshop/
│   ├── manage.py
│   ├── requirements.txt
│   ├── Procfile
│   ├── .gitignore
│   │
│   └── toriloshop/
│       └── settings.py
│
├── screenshots/
│   ├── 01_gunicorn_running.png
│   ├── 02_collectstatic_output.png
│   ├── 03_requirements_txt.png
│   └── 04_gitignore_env_excluded.png
│
└── README.md
```

---

# Key Concepts Learned

- Production vs development environments
- Environment variable security
- PostgreSQL deployment workflow
- Gunicorn production servers
- WhiteNoise static file handling
- Render deployment preparation
- Production-ready Django architecture
- Secure configuration management
- Cloud deployment best practices

---

# Final Result

ToriloShop is now fully prepared for cloud deployment with:

- Secure environment configuration
- Production-grade web server
- PostgreSQL-ready architecture
- Static file handling
- Deployment-ready project structure
- Production security practices
- Render-compatible deployment configuration