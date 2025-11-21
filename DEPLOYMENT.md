# Deployment Guide for Django Blog Application

This guide will help you deploy your Django blog application to various cloud platforms.

## Table of Contents
1. [Pre-Deployment Checklist](#pre-deployment-checklist)
2. [Deploy to Render (Recommended - Free Tier Available)](#deploy-to-render)
3. [Deploy to Railway](#deploy-to-railway)
4. [Deploy to Heroku](#deploy-to-heroku)
5. [Deploy to PythonAnywhere](#deploy-to-pythonanywhere)
6. [Post-Deployment Steps](#post-deployment-steps)

---

## Pre-Deployment Checklist

Before deploying, make sure you have:

- [x] Updated `settings.py` with production settings (✅ Already done)
- [x] Added production dependencies to `requirements.txt` (✅ Already done)
- [ ] Generated a new `SECRET_KEY` for production
- [ ] Set up environment variables
- [ ] Committed all changes to Git
- [ ] Created a GitHub/GitLab repository

### Generate a New Secret Key

Run this command to generate a secure secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Save this key - you'll need it for environment variables.

---

## Deploy to Render

[Render](https://render.com) offers a free tier with PostgreSQL database included.

### Step 1: Prepare Your Repository

1. Push your code to GitHub/GitLab/Bitbucket
2. Make sure `render.yaml` is in your repository root

### Step 2: Create Render Account

1. Go to [render.com](https://render.com)
2. Sign up with GitHub/GitLab
3. Connect your repository

### Step 3: Deploy

**Option A: Using render.yaml (Automatic)**

1. In Render dashboard, click "New" → "Blueprint"
2. Connect your repository
3. Render will automatically detect `render.yaml`
4. Click "Apply" to deploy

**Option B: Manual Setup**

1. In Render dashboard, click "New" → "Web Service"
2. Connect your repository
3. Configure:
   - **Name**: blog-app (or your choice)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn blog_project.wsgi`
4. Add Environment Variables:
   ```
   SECRET_KEY=your-generated-secret-key
   DEBUG=False
   ALLOWED_HOSTS=your-app-name.onrender.com
   ```
5. Create PostgreSQL Database:
   - Click "New" → "PostgreSQL"
   - Name it "blog-db"
   - Copy the "Internal Database URL"
   - Add to environment variables as `DATABASE_URL`
6. Click "Create Web Service"

### Step 4: Run Migrations

After deployment, run migrations:

1. Go to your service → "Shell"
2. Run:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

### Step 5: Access Your App

Your app will be available at: `https://your-app-name.onrender.com`

---

## Deploy to Railway

[Railway](https://railway.app) offers a simple deployment process with a free tier.

### Step 1: Prepare Your Repository

1. Push your code to GitHub
2. Make sure `Procfile` is in your repository root

### Step 2: Create Railway Account

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"

### Step 3: Add PostgreSQL Database

1. In your project, click "New" → "Database" → "PostgreSQL"
2. Railway will automatically set `DATABASE_URL` environment variable

### Step 4: Configure Environment Variables

Go to "Variables" and add:

```
SECRET_KEY=your-generated-secret-key
DEBUG=False
ALLOWED_HOSTS=*.railway.app
```

### Step 5: Deploy

Railway will automatically:
- Detect Python
- Install dependencies from `requirements.txt`
- Run your app using `Procfile`

### Step 6: Run Migrations

1. Go to your service → "Deployments" → Click on the latest deployment
2. Open "Logs" tab
3. Click "Open Shell"
4. Run:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

---

## Deploy to Heroku

[Heroku](https://heroku.com) requires a credit card but offers a free tier for PostgreSQL.

### Step 1: Install Heroku CLI

Download from [devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)

### Step 2: Login to Heroku

```bash
heroku login
```

### Step 3: Create Heroku App

```bash
heroku create your-app-name
```

### Step 4: Add PostgreSQL

```bash
heroku addons:create heroku-postgresql:mini
```

### Step 5: Set Environment Variables

```bash
heroku config:set SECRET_KEY=your-generated-secret-key
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
```

### Step 6: Deploy

```bash
git push heroku main
```

### Step 7: Run Migrations

```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

---

## Deploy to PythonAnywhere

[PythonAnywhere](https://www.pythonanywhere.com) offers a free tier perfect for beginners.

### Step 1: Create Account

1. Go to [pythonanywhere.com](https://www.pythonanywhere.com)
2. Sign up for a free account

### Step 2: Upload Your Code

1. Go to "Files" tab
2. Upload your project or clone from Git:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   ```

### Step 3: Create Virtual Environment

1. Go to "Consoles" → "Bash"
2. Navigate to your project:
   ```bash
   cd ~/your-repo
   ```
3. Create virtual environment:
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### Step 4: Set Up Database

1. Go to "Databases" tab
2. Initialize MySQL database
3. Update `settings.py` to use MySQL (or use SQLite for free tier)

### Step 5: Configure Web App

1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration" → "Python 3.10"
4. Set:
   - **Source code**: `/home/yourusername/your-repo`
   - **Working directory**: `/home/yourusername/your-repo`
   - **WSGI configuration file**: Edit and point to `blog_project/wsgi.py`

### Step 6: Set Environment Variables

In WSGI configuration file, add:
```python
import os
os.environ['SECRET_KEY'] = 'your-secret-key'
os.environ['DEBUG'] = 'False'
os.environ['ALLOWED_HOSTS'] = 'yourusername.pythonanywhere.com'
```

### Step 7: Run Migrations

In "Consoles" → "Bash":
```bash
cd ~/your-repo
source venv/bin/activate
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

### Step 8: Reload Web App

Click "Reload" button in "Web" tab

---

## Post-Deployment Steps

### 1. Set Up Email (Optional but Recommended)

For password reset functionality, configure email:

**Using Gmail:**
1. Enable 2-Factor Authentication
2. Generate App Password: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Add to environment variables:
   ```
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   DEFAULT_FROM_EMAIL=your-email@gmail.com
   ```

**Using SendGrid (Recommended for Production):**
1. Sign up at [sendgrid.com](https://sendgrid.com)
2. Create API key
3. Use SendGrid SMTP settings

### 2. Set Up Media Files Storage (Important!)

For production, you should use cloud storage for media files:

**Option A: Cloudinary (Easiest)**
1. Sign up at [cloudinary.com](https://cloudinary.com)
2. Install: `pip install django-cloudinary-storage`
3. Update `settings.py`:
   ```python
   INSTALLED_APPS = [
       # ... other apps
       'cloudinary_storage',
       'django.contrib.staticfiles',
       'cloudinary',
   ]
   
   DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
   ```
4. Add to environment variables:
   ```
   CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name
   ```

**Option B: AWS S3**
- More complex but scalable
- See: [django-storages.readthedocs.io](https://django-storages.readthedocs.io)

### 3. Set Up Custom Domain (Optional)

1. Buy a domain from Namecheap, GoDaddy, etc.
2. Configure DNS:
   - Add CNAME record pointing to your app URL
3. Update `ALLOWED_HOSTS` environment variable
4. Configure SSL (usually automatic on most platforms)

### 4. Monitor Your Application

- Set up error tracking (Sentry, Rollbar)
- Monitor performance
- Set up backups for database

### 5. Security Checklist

- [x] `DEBUG = False` in production
- [x] Strong `SECRET_KEY`
- [x] `ALLOWED_HOSTS` configured
- [x] HTTPS enabled
- [x] Database credentials secure
- [ ] Regular security updates
- [ ] Backup strategy in place

---

## Troubleshooting

### Static Files Not Loading

1. Run `python manage.py collectstatic --noinput`
2. Check `STATIC_ROOT` in settings
3. Verify WhiteNoise is installed and configured

### Database Connection Issues

1. Check `DATABASE_URL` environment variable
2. Verify database is running
3. Check connection string format

### Media Files Not Uploading

1. For local storage, ensure directory permissions
2. For cloud storage, verify credentials
3. Check `MEDIA_ROOT` and `MEDIA_URL` settings

### 500 Internal Server Error

1. Check application logs
2. Verify all environment variables are set
3. Check `DEBUG = False` (errors won't show details)
4. Temporarily set `DEBUG = True` to see error details

---

## Need Help?

- Django Deployment Checklist: [docs.djangoproject.com/en/4.2/howto/deployment/checklist/](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)
- Platform-specific documentation
- Django Community Forums

---

**Good luck with your deployment! 🚀**

