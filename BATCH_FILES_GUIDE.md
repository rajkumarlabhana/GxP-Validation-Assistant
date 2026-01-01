# 🚀 Batch Files Guide

Easy-to-use batch files for running your GxP Validation Assistant on Windows.

## 📁 Available Batch Files

### 1. **START_HERE.bat** ⭐ (Main Menu)
**Double-click this to start!**

Interactive menu with all options:
- Run the full application
- Run demo version
- Setup dependencies
- Initialize database
- Test system

**Usage:** Just double-click `START_HERE.bat`

---

### 2. **run_app.bat** (Run Full Application)
Starts the production-ready OpenAI RAG application.

**Requirements:**
- Dependencies installed (`setup.bat`)
- Database initialized (`initialize_db.bat`)
- OPENAI_API_KEY in `.env` file

**Usage:** Double-click `run_app.bat`

**Opens:** http://localhost:8501 (or similar port)

---

### 3. **run_demo.bat** (Run Demo Version)
Starts the demo version without requiring database initialization.

**Requirements:**
- Dependencies installed
- GOOGLE_API_KEY in `.env` file

**Usage:** Double-click `run_demo.bat`

**Note:** Demo mode doesn't use RAG, just direct Gemini responses.

---

### 4. **setup.bat** (Install Dependencies)
Installs all required Python packages.

**What it does:**
- Runs `pip install -r requirements_openai.txt`
- Installs OpenAI, Streamlit, ChromaDB, etc.

**Usage:** Double-click `setup.bat`

**Run this:** Once before first use

---

### 5. **initialize_db.bat** (Initialize Database)
Processes all PDF documents and creates vector embeddings.

**What it does:**
- Processes 12 GxP validation PDFs
- Generates embeddings using OpenAI
- Stores in ChromaDB
- Takes 10-15 minutes

**Requirements:**
- Dependencies installed
- OPENAI_API_KEY in `.env` file

**Usage:** Double-click `initialize_db.bat`

**Run this:** Once before first use (or when adding new documents)

---

### 6. **test_system.bat** (Test System)
Runs system tests to verify everything is working.

**What it does:**
- Tests configuration
- Tests vector store
- Tests RAG engine
- Runs sample query

**Usage:** Double-click `test_system.bat`

---

## 🎯 Quick Start Guide

### First Time Setup:

1. **Double-click `START_HERE.bat`**
2. Choose option **3** (Setup)
3. Wait for dependencies to install
4. Edit `.env` file and add your `OPENAI_API_KEY`
5. Run `START_HERE.bat` again
6. Choose option **4** (Initialize Database)
7. Wait 10-15 minutes for completion
8. Run `START_HERE.bat` again
9. Choose option **1** (Run Application)
10. **Done!** 🎉

### Daily Use:

Just double-click `run_app.bat` to start the application!

---

## 🔧 Troubleshooting

### "Python is not recognized"
- Install Python 3.8+ from python.org
- Make sure Python is in your PATH

### "OPENAI_API_KEY not found"
- Edit `.env` file
- Add: `OPENAI_API_KEY=sk-your_key_here`

### "Vector database is empty"
- Run `initialize_db.bat`
- Wait for completion

### "Module not found"
- Run `setup.bat` to install dependencies

---

## 📝 File Locations

All batch files are in the project root:
```
GxP-Validation-Assistant/
├── START_HERE.bat          ⭐ Main menu
├── run_app.bat             Run full app
├── run_demo.bat            Run demo
├── setup.bat               Install deps
├── initialize_db.bat       Setup database
└── test_system.bat         Test system
```

---

## 💡 Tips

1. **Always use `START_HERE.bat`** - It's the easiest way!
2. **Run setup.bat first** - Before anything else
3. **Initialize database once** - Takes time but only needed once
4. **Keep .env secure** - Don't share your API keys
5. **Use run_app.bat daily** - Quick start for regular use

---

## 🎓 For IIT Guwahati Submission

**For demonstration:**
1. Double-click `run_app.bat`
2. Wait for browser to open
3. Try example questions
4. Show source citations
5. Explain RAG architecture

**For presentation:**
- Use `START_HERE.bat` to show the menu
- Demonstrate the full RAG system
- Show the professional UI
- Explain the technology stack

---

## 🆘 Need Help?

Check these files:
- `README.md` - Full documentation
- `QUICKSTART.md` - Quick setup guide
- `SETUP_OPENAI.md` - OpenAI version guide
- `PROJECT_DOCUMENTATION.md` - Academic documentation

---

**Created for IIT Guwahati Capstone Project 2026** 🎓
