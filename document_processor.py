"""
Document processing for PDF extraction and chunking
"""
import logging
from pathlib import Path
from typing import List, Dict
import PyPDF2
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config_openai import Config

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Config.LOGS_DIR / 'document_processor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class DocumentProcessor:
    """Process and chunk documents for RAG"""
    
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP,
            length_function=len,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
    
    def extract_text_from_pdf(self, pdf_path: Path) -> str:
        """Extract text from a PDF file"""
        try:
            text = ""
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                num_pages = len(pdf_reader.pages)
                
                logger.info(f"Processing {pdf_path.name} ({num_pages} pages)")
                
                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text() + "\n"
            
            return text
        except Exception as e:
            logger.error(f"Error extracting text from {pdf_path}: {str(e)}")
            return ""
    
    def process_document(self, pdf_path: Path) -> List[Dict[str, str]]:
        """Process a single document and return chunks with metadata"""
        text = self.extract_text_from_pdf(pdf_path)
        
        if not text:
            return []
        
        # Split text into chunks
        chunks = self.text_splitter.split_text(text)
        
        # Create documents with metadata
        documents = []
        for i, chunk in enumerate(chunks):
            documents.append({
                "text": chunk,
                "metadata": {
                    "source": pdf_path.name,
                    "chunk_id": i,
                    "total_chunks": len(chunks)
                }
            })
        
        logger.info(f"Created {len(documents)} chunks from {pdf_path.name}")
        return documents
    
    def process_all_documents(self, data_dir: Path) -> List[Dict[str, str]]:
        """Process all PDF documents in the data directory"""
        all_documents = []
        
        pdf_files = list(data_dir.glob("*.pdf"))
        logger.info(f"Found {len(pdf_files)} PDF files to process")
        
        for pdf_file in pdf_files:
            documents = self.process_document(pdf_file)
            all_documents.extend(documents)
        
        logger.info(f"Total chunks created: {len(all_documents)}")
        return all_documents
