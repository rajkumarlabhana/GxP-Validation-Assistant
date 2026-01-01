# 🏥 GxP Validation Assistant

AI-powered chatbot for pharmaceutical and medical device validation guidance.

**IIT Guwahati Capstone Project - 2026**

## 🎯 Overview

The GxP Validation Assistant uses **OpenAI GPT-3.5-turbo** with **Retrieval-Augmented Generation (RAG)** to provide expert guidance on GxP validation, compliance, and regulatory guidelines.

## ✨ Features

- **🤖 AI-Powered Responses**: Uses OpenAI GPT-3.5-turbo for intelligent responses
- **📚 RAG Architecture**: Retrieves relevant information from official GxP documents before generating responses
- **🔍 Vector Search**: ChromaDB-powered semantic search for accurate document retrieval
- **💬 Interactive Chat Interface**: Modern, user-friendly Streamlit web application
- **📊 Source Attribution**: Cites specific documents used to generate each response
- **🔒 Production-Ready**: Includes logging, error handling, and configuration management

## 📖 Knowledge Base

The assistant is trained on comprehensive GxP validation guidelines including:

- **GAMP 5** - Good Automated Manufacturing Practice
- **FDA 21 CFR Part 11** - Electronic Records and Signatures
- **ISO/IEC 27001** - Information Security Management
- **FDA Software Validation Guidelines**
- **ICH Q9** - Quality Risk Management
- **EU Annex 11** - Computerized Systems
- And more regulatory documents

## 🏗️ Architecture

```
User Query → OpenAI Embeddings → ChromaDB Search → 
Retrieve Documents → Build Context → OpenAI GPT-3.5 → Response
```

## 🚀 Installation

### Prerequisites

- Python 3.8+
- OpenAI API Key

### Setup Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd c:\Users\Administrator\Desktop\GxP-Validation-Assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API key**
   
   Edit `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. **Initialize the database**
   ```bash
   python initialize_db_openai.py
   ```
   
   This processes all PDFs and creates embeddings (takes 10-15 minutes).

5. **Run the application**
   ```bash
   streamlit run app_openai.py
   ```
   
   Or simply double-click `run_app.bat`

## 📁 Project Structure

```
GxP-Validation-Assistant/
├── Data/                          # GxP validation PDFs
├── vector_db_openai/              # ChromaDB storage
├── logs/                          # Application logs
├── app_openai.py                  # Main application
├── config_openai.py               # Configuration
├── document_processor.py          # PDF processing
├── vector_store_openai.py         # Vector database
├── rag_engine_openai.py           # RAG engine
├── initialize_db_openai.py        # Database setup
├── requirements_openai.txt        # Dependencies
├── run_app.bat                    # Quick launcher
└── README.md                      # Documentation
```

## 🎮 Usage

### Starting the Application

```bash
streamlit run app.py
```

### Example Questions

- "What are the key requirements of GAMP 5?"
- "Explain FDA 21 CFR Part 11 compliance for electronic signatures"
- "What is the difference between IQ, OQ, and PQ in validation?"
- "How do I validate a computerized system according to GAMP 5?"
- "What are the requirements for audit trails in GxP systems?"

### Advanced Configuration

Edit `config.py` or `.env` to customize:

- **CHUNK_SIZE**: Size of document chunks (default: 1000)
- **CHUNK_OVERLAP**: Overlap between chunks (default: 200)
- **TOP_K**: Number of documents to retrieve (default: 5)
- **TEMPERATURE**: Model creativity (default: 0.3)
- **MAX_TOKENS**: Maximum response length (default: 2048)

## 🔧 Technical Details

### Document Processing

- **PDF Extraction**: PyPDF2 for text extraction
- **Text Chunking**: RecursiveCharacterTextSplitter with smart splitting
- **Chunk Size**: 1000 characters with 200 character overlap
- **Metadata**: Source document and chunk information preserved

### Vector Store

- **Database**: ChromaDB
- **Embeddings**: OpenAI text-embedding-ada-002
- **Similarity**: Cosine similarity

### RAG Pipeline

1. Query → Embedding
2. Semantic search in ChromaDB
3. Retrieve top-K documents
4. Build context with retrieved chunks
5. Generate response with OpenAI GPT-3.5
6. Display answer with source citations

## 📊 Performance

- **Initialization Time**: 5-10 minutes (one-time)
- **Query Response Time**: 2-5 seconds
- **Accuracy**: High relevance due to domain-specific knowledge base
- **Scalability**: Handles 1000+ document chunks efficiently

## 🔒 Security & Compliance

- **API Key Management**: Environment variables (never hardcoded)
- **Logging**: Comprehensive logging for audit trails
- **Error Handling**: Graceful error handling and user feedback
- **Data Privacy**: Local vector storage, no data sent except to Gemini API

## 🐛 Troubleshooting

### "Vector database is empty" Error
```bash
python initialize_db.py
```

### "OPENAI_API_KEY not found"
- Add API key to `.env` file
- Restart the application

### Import Errors
```bash
pip install -r requirements.txt --upgrade
```

### ChromaDB Issues
- Delete `vector_db` folder and reinitialize
- Ensure write permissions in project directory

## 📝 Adding Documents

1. Add PDF files to `Data` folder
2. Run `python initialize_db_openai.py`
3. Restart application

## 🎓 Academic Context

**Institution**: IIT Guwahati  
**Project**: Capstone 2026  
**Domain**: Pharmaceutical Validation  
**Tech Stack**: Python, OpenAI GPT-3.5, RAG, ChromaDB, Streamlit

## 📄 License

This project is developed for academic purposes as part of IIT Guwahati capstone requirements.



---

**Disclaimer**: This assistant provides guidance based on GxP validation documents. Always consult qualified professionals for compliance decisions.
