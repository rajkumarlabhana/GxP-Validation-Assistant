"""
Initialize vector database with GxP documents
"""
import logging
from pathlib import Path
from config_openai import Config
from document_processor import DocumentProcessor
from vector_store_openai import VectorStore

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def initialize_database():
    """Initialize the vector database with documents"""
    try:
        # Validate configuration
        logger.info("Validating configuration...")
        Config.validate()
        
        # Initialize components
        logger.info("Initializing document processor...")
        doc_processor = DocumentProcessor()
        
        logger.info("Initializing vector store (OpenAI)...")
        vector_store = VectorStore()
        
        # Check if database already has documents
        existing_count = vector_store.get_collection_count()
        if existing_count > 0:
            logger.info(f"Vector store already contains {existing_count} documents")
            response = input("Do you want to clear and reinitialize? (yes/no): ")
            if response.lower() == 'yes':
                logger.info("Clearing existing collection...")
                vector_store.clear_collection()
            else:
                logger.info("Keeping existing documents")
                return
        
        # Process documents
        logger.info(f"Processing documents from {Config.DATA_DIR}...")
        documents = doc_processor.process_all_documents(Config.DATA_DIR)
        
        if not documents:
            logger.error("No documents were processed!")
            return
        
        # Add to vector store
        logger.info("Adding documents to vector store (this will take several minutes)...")
        logger.info("Using OpenAI embeddings - this is more reliable than Gemini free tier")
        vector_store.add_documents(documents)
        
        # Verify
        final_count = vector_store.get_collection_count()
        logger.info(f"✓ Database initialized successfully with {final_count} document chunks")
        logger.info("You can now run: streamlit run app_openai.py")
        
    except Exception as e:
        logger.error(f"Error initializing database: {str(e)}")
        raise


if __name__ == "__main__":
    initialize_database()
