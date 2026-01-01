"""
Configuration for GxP Validation Assistant
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Application configuration"""
    
    # Base paths
    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR / "Data"
    VECTOR_DB_DIR = BASE_DIR / "vector_db_openai"
    LOGS_DIR = BASE_DIR / "logs"
    
    # API Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    
    # Model Configuration
    EMBEDDING_MODEL = "text-embedding-ada-002"
    GENERATION_MODEL = "gpt-3.5-turbo"  # or "gpt-4" for better quality
    
    # RAG Configuration
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    TOP_K = int(os.getenv("TOP_K", 5))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", 2048))
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.3))
    
    # Application Settings
    APP_TITLE = os.getenv("APP_TITLE", "GxP Validation Assistant")
    APP_ICON = os.getenv("APP_ICON", "🏥")
    
    # Supported file types
    SUPPORTED_EXTENSIONS = [".pdf"]
    
    @classmethod
    def validate(cls):
        """Validate configuration"""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        # Create necessary directories
        cls.VECTOR_DB_DIR.mkdir(exist_ok=True)
        cls.LOGS_DIR.mkdir(exist_ok=True)
        
        return True
