# 🚀 OpenAI Version Setup Guide

This is the **OpenAI-powered version** of the GxP Validation Assistant - more reliable for production use!

## Why OpenAI Version?

✅ **Better Quota Limits** - More generous API limits  
✅ **More Reliable** - Proven embeddings and generation  
✅ **Production Ready** - Used by thousands of applications  
✅ **Better Quality** - GPT-3.5-turbo or GPT-4 for responses  

## Quick Setup (5 minutes)

### Step 1: Get OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key (starts with `sk-...`)

### Step 2: Install Dependencies

```bash
pip install -r requirements_openai.txt
```

### Step 3: Configure API Key

Edit your `.env` file and add:

```
OPENAI_API_KEY=sk-your_actual_openai_key_here
```

### Step 4: Initialize Database

```bash
python initialize_db_openai.py
```

This will:
- Process all 12 GxP validation PDFs
- Generate embeddings using OpenAI
- Store in ChromaDB (separate from Gemini version)
- Takes 5-10 minutes

### Step 5: Run the Application

```bash
streamlit run app_openai.py
```

The app will open at `http://localhost:8501` 🎉

## Features

- ✅ Full RAG system with document retrieval
- ✅ OpenAI GPT-3.5-turbo for responses (or upgrade to GPT-4)
- ✅ OpenAI text-embedding-ada-002 for embeddings
- ✅ Same beautiful UI as Gemini version
- ✅ Source citations for every answer
- ✅ Production-ready logging and error handling

## Cost Estimate

**OpenAI Pricing (as of 2026):**
- Embeddings: ~$0.0001 per 1K tokens
- GPT-3.5-turbo: ~$0.0015 per 1K tokens
- GPT-4: ~$0.03 per 1K tokens (optional upgrade)

**Typical Usage:**
- Database initialization: ~$0.50-1.00 (one-time)
- Per query: ~$0.002-0.005
- 100 queries/day: ~$15-30/month

**Free Tier:**
- New OpenAI accounts get $5 free credit
- Enough for testing and demo!

## Upgrading to GPT-4

For even better responses, edit `config_openai.py`:

```python
GENERATION_MODEL = "gpt-4"  # Instead of "gpt-3.5-turbo"
```

## Troubleshooting

### "OPENAI_API_KEY not found"
- Ensure `.env` file has `OPENAI_API_KEY=sk-...`
- Restart the application after editing `.env`

### "Insufficient quota"
- Add payment method to OpenAI account
- Or use free $5 credit for testing

### "Rate limit exceeded"
- Wait a few seconds and try again
- OpenAI has generous rate limits

## Comparison: OpenAI vs Gemini

| Feature | OpenAI | Gemini |
|---------|--------|--------|
| **Free Tier** | $5 credit | Limited quota |
| **Reliability** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Quality** | Excellent | Very Good |
| **Cost** | Moderate | Lower |
| **Rate Limits** | Generous | Restrictive |
| **Best For** | Production | Testing |

## For IIT Guwahati Submission

**Recommended:** Use the OpenAI version for your capstone demo and submission because:

1. ✅ More reliable during presentation
2. ✅ Better quota management
3. ✅ Professional-grade responses
4. ✅ Widely recognized technology
5. ✅ Easier to scale for future use

## Next Steps

1. Get your OpenAI API key
2. Run the setup steps above
3. Test with example questions
4. Prepare your demo for presentation!

---

**Questions?** Check the main [README.md](README.md) for more details.
