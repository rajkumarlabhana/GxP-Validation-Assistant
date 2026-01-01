# 🚀 Deploy to Streamlit Cloud - Step by Step Guide

## Step 1: Go to Streamlit Cloud

1. Open browser and go to: **https://share.streamlit.io**
2. Click **"Sign in"** button (top right)
3. Choose **"Continue with GitHub"**
4. Authorize Streamlit to access your GitHub account
5. You'll be redirected to Streamlit dashboard

---

## Step 2: Create New App

1. Click the **"New app"** button (big button on the page)
   - OR click **"Create app"** if you see that instead

2. You'll see a form with three dropdown menus:

---

## Step 3: Fill in the Deployment Form

### **Repository** (First Dropdown)
- Click the dropdown
- You'll see a list of your GitHub repositories
- Select: **`rajkumarlabhana/GxP-Validation-Assistant`**
- (It should show your username/repository-name)

### **Branch** (Second Dropdown)
- Click the dropdown
- Select: **`main`**
- (This is your main branch)

### **Main file path** (Third Dropdown or Text Field)
- Click the dropdown or text field
- Type or select: **`app_openai.py`**
- Make sure it's exactly: `app_openai.py` (not app.py)

### **App URL** (Optional)
- You can customize the URL
- Default will be something like: `gxp-validation-assistant.streamlit.app`
- Or leave it as auto-generated

---

## Step 4: Advanced Settings (IMPORTANT!)

1. Click **"Advanced settings"** (below the form)

2. You'll see a **"Secrets"** section

3. In the secrets text box, add:
```toml
OPENAI_API_KEY = "sk-proj-your-actual-api-key-here"
```

**Replace with your actual OpenAI API key from `.env` file!**

4. Other settings (optional):
   - **Python version:** 3.9 or 3.10 (default is fine)
   - **Requirements file:** `requirements_openai.txt` (auto-detected)

---

## Step 5: Deploy!

1. Click the **"Deploy!"** button (bottom of form)

2. Wait for deployment (takes 2-5 minutes)

3. You'll see a progress screen showing:
   - Installing dependencies
   - Building app
   - Starting app

4. Once done, your app will open automatically! 🎉

---

## 📝 Your Deployment Settings Summary:

```
Repository: rajkumarlabhana/GxP-Validation-Assistant
Branch: main
Main file: app_openai.py
Secrets: OPENAI_API_KEY = "your-key"
```

---

## ⚠️ Common Issues & Solutions:

### Issue 1: "Repository not found"
**Solution:**
- Make sure you authorized Streamlit to access your GitHub
- Refresh the page
- Check repository is public (not private)

### Issue 2: "Module not found" error
**Solution:**
- Make sure `requirements_openai.txt` is in your repository
- Check all dependencies are listed
- Streamlit auto-detects this file

### Issue 3: "OPENAI_API_KEY not found"
**Solution:**
- Go to app settings (three dots menu)
- Click "Settings" → "Secrets"
- Add your API key in TOML format:
```toml
OPENAI_API_KEY = "your-key-here"
```

### Issue 4: "Database not initialized"
**Solution:**
- The `vector_db_openai` folder is NOT uploaded (too large)
- You need to initialize database on first run
- OR remove database dependency for demo

**Quick Fix:** Create a version without database requirement:
- Use direct OpenAI calls without RAG
- Or initialize database on Streamlit Cloud (takes time)

### Issue 5: Large files error
**Solution:**
- GitHub has 100 MB file limit
- Streamlit has storage limits
- Consider removing large PDFs or using external storage

---

## 🔄 Update Your App Later:

When you make changes to your code:

1. Push changes to GitHub:
```bash
git add .
git commit -m "Updated features"
git push
```

2. Streamlit Cloud will **auto-deploy** the changes!
   - No need to redeploy manually
   - Takes 1-2 minutes to update

---

## 🎯 After Successful Deployment:

### Your app will be live at:
```
https://gxp-validation-assistant.streamlit.app
```
(or your custom URL)

### Share this URL with:
- ✅ Professors
- ✅ Classmates
- ✅ Anyone for demo!

### Manage Your App:
- Go to: https://share.streamlit.io/
- Click on your app
- You can:
  - View logs
  - Restart app
  - Update settings
  - Delete app

---

## 💡 Pro Tips:

1. **Test locally first** before deploying
2. **Keep API key secret** - never commit to GitHub
3. **Monitor usage** - OpenAI charges per API call
4. **Check logs** if something breaks
5. **Free tier limits:**
   - 1 GB storage
   - 1 GB RAM
   - May sleep after inactivity

---

## 📊 Streamlit Cloud Free Tier:

✅ **Included:**
- Unlimited public apps
- Auto-deployment from GitHub
- HTTPS by default
- Community support

⚠️ **Limitations:**
- Apps may sleep after inactivity
- Limited resources (1 GB RAM)
- No custom domain (free tier)

---

## 🆘 Need Help?

### Streamlit Documentation:
- https://docs.streamlit.io/streamlit-community-cloud

### Streamlit Community:
- https://discuss.streamlit.io/

### Common Error Solutions:
- Check logs in Streamlit dashboard
- Verify all files are in GitHub
- Ensure secrets are properly set

---

## ✅ Deployment Checklist:

Before deploying, make sure:

- [ ] Code is pushed to GitHub
- [ ] Repository is public (or Streamlit has access)
- [ ] `requirements_openai.txt` is in repository
- [ ] `app_openai.py` exists and works locally
- [ ] `.env` is NOT in repository (in .gitignore)
- [ ] You have your OpenAI API key ready
- [ ] You've tested the app locally

---

## 🎉 Success!

Once deployed, your GxP Validation Assistant will be:
- ✅ Live on the internet
- ✅ Accessible from anywhere
- ✅ Professional URL to share
- ✅ Ready for IIT Guwahati presentation!

**Your chatbot is now live for the world to see!** 🌍🤖

---

## 📸 Visual Guide:

### What You'll See:

**Step 1:** Streamlit Cloud homepage
- Big "New app" button in center

**Step 2:** Deployment form
- Three dropdowns (Repository, Branch, File)
- Advanced settings link below

**Step 3:** Secrets section (in Advanced settings)
- Text area to paste your API key in TOML format

**Step 4:** Deploy button
- Big blue "Deploy!" button at bottom

**Step 5:** Building screen
- Progress bars showing installation
- Logs scrolling

**Step 6:** Your live app!
- Opens automatically when ready
- Public URL at top

---

Good luck with your deployment! 🚀
