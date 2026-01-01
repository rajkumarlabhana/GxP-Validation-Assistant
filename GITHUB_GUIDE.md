# 📦 Push Your Code to GitHub - Complete Guide

## Step 1: Create GitHub Account

1. Go to [github.com](https://github.com)
2. Click "Sign up"
3. Enter email, password, username
4. Verify email
5. Done! ✅

---

## Step 2: Create New Repository

1. **Click "+" icon** (top right) → "New repository"
2. **Repository name:** `GxP-Validation-Assistant`
3. **Description:** "AI-powered chatbot for pharmaceutical validation guidance"
4. **Visibility:** 
   - ✅ **Public** (for Streamlit deployment)
   - Or **Private** (if you prefer)
5. **DO NOT** check "Add README" (we already have one)
6. Click **"Create repository"**

---

## Step 3: Install Git (If Not Installed)

### Check if Git is installed:
```bash
git --version
```

### If not installed:
1. Download from [git-scm.com](https://git-scm.com)
2. Install with default settings
3. Restart terminal

---

## Step 4: Configure Git (First Time Only)

```bash
git config --global user.name "Rajkumar Labhana"
git config --global user.email "your_email@example.com"
```

---

## Step 5: Push Your Code to GitHub

### Open PowerShell in your project folder:

```bash
cd C:\Users\Administrator\Desktop\GxP-Validation-Assistant
```

### Initialize Git repository:

```bash
git init
```

### Add all files:

```bash
git add .
```

### Commit your code:

```bash
git commit -m "Initial commit - GxP Validation Assistant"
```

### Add GitHub repository as remote:

```bash
git remote add origin https://github.com/YOUR_USERNAME/GxP-Validation-Assistant.git
```

**Replace `YOUR_USERNAME` with your actual GitHub username!**

### Push to GitHub:

```bash
git branch -M main
git push -u origin main
```

### Enter credentials when prompted:
- **Username:** Your GitHub username
- **Password:** Use **Personal Access Token** (not your password!)

---

## Step 6: Create Personal Access Token (For Password)

GitHub doesn't accept passwords anymore. You need a token:

1. Go to GitHub → Settings (your profile)
2. Scroll down → "Developer settings"
3. Click "Personal access tokens" → "Tokens (classic)"
4. Click "Generate new token (classic)"
5. **Name:** "GxP Project"
6. **Expiration:** 90 days (or custom)
7. **Select scopes:** Check "repo" (all repo permissions)
8. Click "Generate token"
9. **COPY THE TOKEN** (you won't see it again!)
10. Use this token as password when pushing

---

## 🎯 Complete Command Sequence:

```bash
# Navigate to project
cd C:\Users\Administrator\Desktop\GxP-Validation-Assistant

# Initialize Git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - GxP Validation Assistant"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/GxP-Validation-Assistant.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## ⚠️ IMPORTANT: Protect Your API Key!

### Your `.env` file is already in `.gitignore` ✅

This means your API key **won't be uploaded** to GitHub (safe!).

### Verify `.gitignore` contains:

```
.env
__pycache__/
*.pyc
logs/
vector_db_openai/
```

---

## 🔒 Security Checklist:

Before pushing:

- ✅ `.env` is in `.gitignore`
- ✅ No API keys in code
- ✅ `vector_db_openai/` excluded (large files)
- ✅ `logs/` excluded

---

## 📤 After Pushing to GitHub:

### Your repository will contain:

- ✅ All Python files
- ✅ Documentation (README, guides)
- ✅ Batch files
- ✅ Data folder (PDFs)
- ✅ requirements_openai.txt
- ❌ `.env` (excluded - safe!)
- ❌ `vector_db_openai/` (excluded - too large)

---

## 🚀 Next Step: Deploy to Streamlit Cloud

Once code is on GitHub:

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Choose `app_openai.py`
6. Add `OPENAI_API_KEY` in secrets
7. Deploy!

---

## 🆘 Troubleshooting:

### "Git not recognized"
- Install Git from [git-scm.com](https://git-scm.com)
- Restart terminal

### "Authentication failed"
- Use Personal Access Token (not password)
- Generate token in GitHub settings

### "Large files rejected"
- Make sure `vector_db_openai/` is in `.gitignore`
- Run: `git rm -r --cached vector_db_openai/`

### "Permission denied"
- Check your GitHub username
- Verify repository exists
- Use correct token

---

## 📝 Update Code Later:

When you make changes:

```bash
git add .
git commit -m "Updated design and features"
git push
```

---

## 🎓 Summary:

1. ✅ Create GitHub account
2. ✅ Create new repository
3. ✅ Install Git
4. ✅ Run commands to push code
5. ✅ Use Personal Access Token
6. ✅ Code is now on GitHub!

**Your code will be safely stored and ready to deploy!** 🎉
