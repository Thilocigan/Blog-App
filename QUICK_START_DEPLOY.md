# Quick Start: Deploy Your Django Blog App

## 🚀 Fastest Way: Deploy to Render (Free)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit - ready for deployment"
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```

### Step 2: Deploy on Render
1. Go to [render.com](https://render.com) and sign up
2. Click "New" → "Blueprint"
3. Connect your GitHub repository
4. Render will auto-detect `render.yaml` and deploy!

### Step 3: Generate Secret Key
Run this locally:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Then add it to Render's Environment Variables:
- Go to your service → "Environment"
- Add: `SECRET_KEY` = (paste your generated key)

### Step 4: Run Migrations
1. Go to your service → "Shell"
2. Run:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

### Step 5: Access Your App!
Your app is live at: `https://your-app-name.onrender.com`

---

## 📝 Environment Variables to Set

In your hosting platform, add these:

```
SECRET_KEY=your-generated-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
```

**Note:** `DATABASE_URL` is usually auto-provided by the platform.

---

## ✅ What's Already Configured

- ✅ Production-ready settings
- ✅ WhiteNoise for static files
- ✅ PostgreSQL database support
- ✅ Security headers
- ✅ Environment variable support
- ✅ Deployment configs (render.yaml, Procfile)

---

## 📚 Full Guide

See `DEPLOYMENT.md` for detailed instructions for:
- Render
- Railway
- Heroku
- PythonAnywhere
- Post-deployment setup
- Troubleshooting

---

## 🆘 Common Issues

**Static files not loading?**
- Make sure `collectstatic` runs during build
- Check WhiteNoise is in middleware

**Database errors?**
- Verify `DATABASE_URL` is set
- Run migrations: `python manage.py migrate`

**500 errors?**
- Check all environment variables are set
- Temporarily set `DEBUG=True` to see error details

---

**Need help? Check `DEPLOYMENT.md` for detailed instructions!**

