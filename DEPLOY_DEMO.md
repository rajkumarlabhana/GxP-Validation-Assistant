# 🚀 Deploy for Demo - Quick Guide

## Option 1: Streamlit Cloud (Recommended) ⭐

### Step 1: Prepare Your Code

1. **Create GitHub account** (if you don't have one)
2. **Create new repository** on GitHub
3. **Upload your project** (exclude `.env` file!)

### Step 2: Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Choose `app_openai.py` as main file
6. Click "Deploy"

### Step 3: Add API Key

1. Click "Advanced settings"
2. Add to "Secrets":
```toml
OPENAI_API_KEY = "your_api_key_here"
```
3. Save and deploy

### Step 4: Share!

You'll get a URL like: `https://gxp-validation-assistant.streamlit.app`

**Share this URL with anyone for demo!**

---

## Option 2: Quick Local Network Demo

### For Same WiFi Network:

1. **Find your IP address:**
   ```bash
   ipconfig
   ```
   Look for IPv4 (e.g., 192.168.1.100)

2. **Run with network access:**
   ```bash
   streamlit run app_openai.py --server.address 0.0.0.0
   ```

3. **Share URL:**
   ```
   http://YOUR_IP:8505
   ```

**Example:** `http://192.168.1.100:8505`

---

## Option 3: ngrok (Temporary Public URL)

### Quick Public Access:

1. **Download ngrok:**
   - Visit [ngrok.com](https://ngrok.com)
   - Download and extract

2. **Run your app:**
   ```bash
   streamlit run app_openai.py
   ```

3. **In new terminal, run ngrok:**
   ```bash
   ngrok http 8505
   ```

4. **Copy the public URL:**
   ```
   https://abc123.ngrok.io
   ```

5. **Share this URL!**

**Note:** URL changes each time (free tier)

---

## Option 4: Hugging Face Spaces

### Deploy to Hugging Face:

1. **Create account:** [huggingface.co](https://huggingface.co)
2. **Create new Space:**
   - Choose "Streamlit" SDK
   - Name it (e.g., "gxp-validation-assistant")
3. **Upload files:**
   - All Python files
   - requirements_openai.txt
   - Data folder
4. **Add secrets:**
   - Settings → Repository secrets
   - Add `OPENAI_API_KEY`
5. **Deploy!**

**URL:** `https://huggingface.co/spaces/YOUR_USERNAME/gxp-validation-assistant`

---

## 📊 Comparison

| Option | Cost | Setup Time | Best For |
|--------|------|------------|----------|
| **Streamlit Cloud** | FREE | 5 min | Public demos |
| **Local Network** | FREE | 1 min | Same WiFi |
| **ngrok** | FREE | 2 min | Quick share |
| **Hugging Face** | FREE | 10 min | ML community |

---

## 🎯 For IIT Guwahati Presentation:

### **Recommended Approach:**

1. **For live demo:** Use **Local Network** (instant, no setup)
2. **For sharing with professors:** Use **Streamlit Cloud** (professional URL)
3. **For quick test:** Use **ngrok** (instant public access)

---

## ⚠️ Important Notes:

### Before Deploying:

1. **Never upload `.env` file** to GitHub!
2. **Use secrets management** for API keys
3. **Test locally first**
4. **Check API quota limits**

### Cost Considerations:

- **Streamlit Cloud:** FREE (with limits)
- **OpenAI API:** Pay per use (~$0.002 per query)
- **Hugging Face:** FREE
- **ngrok:** FREE (with limitations)

---

## 🆘 Troubleshooting:

### "Module not found"
- Make sure `requirements_openai.txt` is uploaded
- Check all dependencies are listed

### "API Key not found"
- Add `OPENAI_API_KEY` to secrets/environment variables
- Don't hardcode in code!

### "Database not initialized"
- Upload `vector_db_openai` folder
- Or reinitialize on server

---

## 📞 Quick Demo Setup (5 minutes):

**Fastest way for demo:**

1. Run: `streamlit run app_openai.py --server.address 0.0.0.0`
2. Find your IP: `ipconfig`
3. Share: `http://YOUR_IP:8505`
4. Done! ✅

**Anyone on same WiFi can access!**

---

**Need help?** Check [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.
