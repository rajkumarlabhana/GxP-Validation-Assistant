# 🚀 Quick Start Guide

Get your GxP Validation Assistant up and running in 5 minutes!

## Prerequisites

- Python 3.8+ installed
- Google API Key ([Get one here](https://makersuite.google.com/app/apikey))
- Internet connection

## Step-by-Step Setup

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Configure API Key

Create a `.env` file in the project root:

```bash
copy .env.example .env
```

Edit `.env` and add your Google API key:

```
GOOGLE_API_KEY=your_actual_api_key_here
```

### 3️⃣ Run Setup

```bash
python setup.py
```

This will create necessary directories and verify your setup.

### 4️⃣ Initialize Database

```bash
python initialize_db.py
```

This will:
- Process all PDF documents in the `Data` folder
- Generate embeddings
- Store them in the vector database
- **Takes 5-10 minutes** ⏱️

### 5️⃣ Test the System (Optional)

```bash
python test_system.py
```

Verify everything is working correctly.

### 6️⃣ Launch the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501` 🎉

## First Query

Try asking:
- "What are the key requirements of GAMP 5?"
- "Explain FDA 21 CFR Part 11 compliance"
- "What is the difference between IQ, OQ, and PQ?"

## Troubleshooting

### "GOOGLE_API_KEY not found"
- Make sure `.env` file exists in the project root
- Check that the API key is correctly set

### "Vector database is empty"
- Run `python initialize_db.py`
- Wait for it to complete (5-10 minutes)

### Import errors
```bash
pip install -r requirements.txt --upgrade
```

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Customize settings in `config.py`
- Add more documents to the `Data` folder and reinitialize

---

**Need Help?** Check the logs in the `logs` folder for detailed error messages.
