"""
GxP Validation Assistant
IIT Guwahati Capstone Project 2026
"""
import streamlit as st
import logging
from pathlib import Path
from datetime import datetime
from config_openai import Config
from vector_store_openai import VectorStore
from rag_engine_openai import RAGEngine

# Setup logging
Config.LOGS_DIR.mkdir(exist_ok=True)  # Create logs directory if it doesn't exist
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Config.LOGS_DIR / 'app_openai.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title=Config.APP_TITLE + " (OpenAI)",
    page_icon=Config.APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional UI with colors
st.markdown("""
<style>
    /* Main app background */
    .stApp {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0e7ff 100%);
    }
    
    /* Main content area */
    .main .block-container {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Fix text visibility in main area */
    .main .block-container * {
        color: #1f2937;
    }
    
    /* Chat input */
    .stChatInput {
        background-color: #ffffff !important;
    }
    
    /* Sidebar styling - Dedicated color */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e3a8a 0%, #1e40af 100%);
    }
    
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #ffffff !important;
    }
    
    /* Sidebar buttons */
    [data-testid="stSidebar"] button {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 5px !important;
    }
    
    [data-testid="stSidebar"] button:hover {
        background-color: rgba(255, 255, 255, 0.2) !important;
        border-color: rgba(255, 255, 255, 0.5) !important;
    }
    
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #64748B;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .user-message {
        background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
        border-left: 4px solid #3B82F6;
    }
    .assistant-message {
        background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%);
        border-left: 4px solid #10B981;
    }
    .source-box {
        background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%);
        padding: 1rem;
        border-radius: 0.5rem;
        margin-top: 1rem;
        border-left: 4px solid #F59E0B;
    }
    .stat-card {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid rgba(30, 58, 138, 0.2);
        color: #1f2937 !important;
    }
    
    .stat-card strong {
        color: #1e3a8a !important;
    }
    .footer {
        text-align: center;
        color: #64748B;
        margin-top: 3rem;
        padding: 1rem;
        border-top: 1px solid #E2E8F0;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def initialize_rag_system():
    """Initialize the RAG system (cached)"""
    try:
        Config.validate()
        vector_store = VectorStore()
        rag_engine = RAGEngine(vector_store)
        
        # Check if database is initialized
        doc_count = vector_store.get_collection_count()
        if doc_count == 0:
            st.error("⚠️ Vector database is empty! Please run `python initialize_db_openai.py` first.")
            return None, None, 0
        
        logger.info(f"RAG system initialized with {doc_count} documents")
        return vector_store, rag_engine, doc_count
    
    except ValueError as e:
        st.error(f"⚠️ Configuration Error: {str(e)}")
        st.info("Please create a `.env` file with your OPENAI_API_KEY")
        return None, None, 0
    except Exception as e:
        st.error(f"⚠️ Error initializing RAG system: {str(e)}")
        logger.error(f"Initialization error: {str(e)}")
        return None, None, 0


def display_chat_message(role: str, content: str, sources: list = None):
    """Display a chat message with styling"""
    if role == "user":
        st.markdown(f"""
        <div class="chat-message user-message">
            <strong>👨‍💻 You:</strong><br>
            {content}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message assistant-message">
            <strong>🤖 GxP Assistant:</strong><br>
            {content}
        </div>
        """, unsafe_allow_html=True)
        
        if sources:
            sources_text = "<br>".join([f"• {source}" for source in sources])
            st.markdown(f"""
            <div class="source-box">
                <strong>📚 Sources Referenced:</strong><br>
                {sources_text}
            </div>
            """, unsafe_allow_html=True)


def main():
    """Main application function"""
    
    # Header with Robot Chatbot Icon in Gradient Circle
    st.markdown('''
    <div style="text-align: center; padding: 1rem 0;">
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin: 0 auto 1rem auto;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 5rem;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        ">🤖</div>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown(f'''
    <div style="text-align: center; padding: 0.5rem 0 1rem 0;">
        <div class="main-header">{Config.APP_TITLE}</div>
        <div class="sub-header">
            AI-Powered Expert Guidance for Pharmaceutical & Medical Device Validation<br>
            <em style="color: #6366f1; font-weight: 600;">Powered by OpenAI GPT-3.5 + RAG Technology</em>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Initialize RAG system
    vector_store, rag_engine, doc_count = initialize_rag_system()
    
    if not rag_engine:
        st.stop()
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 📊 System Information")
        
        st.markdown(f"""
        <div class="stat-card">
            <strong>Documents Indexed:</strong> {doc_count}<br>
            <strong>Model:</strong> {Config.GENERATION_MODEL}<br>
            <strong>Embeddings:</strong> {Config.EMBEDDING_MODEL}<br>
            <strong>Retrieval:</strong> RAG with ChromaDB<br>
            <strong>Temperature:</strong> {Config.TEMPERATURE}
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 📖 Knowledge Base")
        st.markdown("""
        - GAMP 5 Guidelines
        - FDA 21 CFR Part 11
        - ISO/IEC 27001
        - FDA Software Validation
        - ICH Q9 Quality Risk Management
        - EU Annex 11
        - And more...
        """)
        
        st.markdown("---")
        st.markdown("### 💡 Example Questions")
        
        example_questions = [
            "What are the key requirements of GAMP 5?",
            "Explain FDA 21 CFR Part 11 compliance",
            "What is the difference between IQ, OQ, and PQ?",
            "How to validate a computerized system?",
            "What are the requirements for electronic signatures?"
        ]
        
        for question in example_questions:
            if st.button(question, key=question, use_container_width=True):
                st.session_state.example_question = question
        
        st.markdown("---")
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
        
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; padding: 1rem 0; font-size: 0.85rem;">
            <strong>Developed by</strong><br>
            <span style="font-size: 1rem; font-weight: 600;">Rajkumar Labhana</span>
        </div>
        """, unsafe_allow_html=True)

    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        display_chat_message(
            message["role"],
            message["content"],
            message.get("sources")
        )
    
    # Handle example question
    if "example_question" in st.session_state:
        user_input = st.session_state.example_question
        del st.session_state.example_question
    else:
        user_input = None
    
    # Chat input
    if prompt := st.chat_input("Ask me anything about GxP validation, compliance, or regulatory guidelines..."):
        user_input = prompt
    
    # Process user input
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })
        
        # Display user message
        display_chat_message("user", user_input)
        
        # Generate response
        with st.spinner("🔍 Searching knowledge base and generating response..."):
            try:
                response = rag_engine.generate_response(user_input)
                
                # Add assistant message to chat history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response["answer"],
                    "sources": response.get("sources", [])
                })
                
                # Display assistant message
                display_chat_message(
                    "assistant",
                    response["answer"],
                    response.get("sources")
                )
                
                logger.info(f"Query processed successfully: {user_input[:50]}...")
                
            except Exception as e:
                error_msg = f"An error occurred: {str(e)}"
                st.error(error_msg)
                logger.error(f"Error processing query: {str(e)}")
    
    # Footer
    st.markdown("""
    <div class="footer">
        <strong>Disclaimer:</strong> This assistant provides guidance based on GxP validation documents. 
        Always consult with qualified professionals and refer to official regulatory guidelines for compliance decisions.
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
