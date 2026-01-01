"""
Vector store with ChromaDB and OpenAI
"""
import logging
import time
from typing import List, Dict
import chromadb
from chromadb.config import Settings
from openai import OpenAI
from config_openai import Config

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Config.LOGS_DIR / 'vector_store_openai.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class VectorStore:
    """Vector embeddings and similarity search"""
    
    def __init__(self):
        # Initialize OpenAI client
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        
        # Initialize ChromaDB
        self.chroma_client = chromadb.PersistentClient(
            path=str(Config.VECTOR_DB_DIR),
            settings=Settings(anonymized_telemetry=False)
        )
        
        # Get or create collection
        self.collection_name = "gxp_documents_openai"
        try:
            self.collection = self.chroma_client.get_collection(name=self.collection_name)
            logger.info(f"Loaded existing collection: {self.collection_name}")
        except:
            self.collection = self.chroma_client.create_collection(
                name=self.collection_name,
                metadata={"description": "GxP Validation Guidelines (OpenAI)"}
            )
            logger.info(f"Created new collection: {self.collection_name}")
    
    def generate_embedding(self, text: str) -> List[float]:
        """Generate embedding using OpenAI"""
        try:
            response = self.client.embeddings.create(
                model=Config.EMBEDDING_MODEL,
                input=text
            )
            return response.data[0].embedding
        except Exception as e:
            logger.error(f"Error generating embedding: {str(e)}")
            raise
    
    def add_documents(self, documents: List[Dict[str, str]]):
        """Add documents to the vector store"""
        if not documents:
            logger.warning("No documents to add")
            return
        
        logger.info(f"Adding {len(documents)} documents to vector store")
        
        # Prepare data for ChromaDB
        ids = []
        embeddings = []
        texts = []
        metadatas = []
        
        for i, doc in enumerate(documents):
            try:
                # Generate unique ID
                doc_id = f"{doc['metadata']['source']}_{doc['metadata']['chunk_id']}"
                ids.append(doc_id)
                
                # Generate embedding
                embedding = self.generate_embedding(doc['text'])
                embeddings.append(embedding)
                
                # Store text and metadata
                texts.append(doc['text'])
                metadatas.append(doc['metadata'])
                
                # Rate limiting: sleep to avoid rate limits
                if (i + 1) % 10 == 0:
                    logger.info(f"Processed {i + 1}/{len(documents)} documents")
                    time.sleep(0.5)  # Small delay to avoid rate limits
            
            except Exception as e:
                logger.error(f"Error processing document {i}: {str(e)}")
                continue
        
        # Add to collection
        if ids:
            self.collection.add(
                ids=ids,
                embeddings=embeddings,
                documents=texts,
                metadatas=metadatas
            )
            logger.info(f"Successfully added {len(ids)} documents to vector store")
    
    def search(self, query: str, top_k: int = None) -> List[Dict]:
        """Search for relevant documents"""
        if top_k is None:
            top_k = Config.TOP_K
        
        try:
            # Generate query embedding
            query_embedding = self.generate_embedding(query)
            
            # Search in ChromaDB
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k
            )
            
            # Format results
            formatted_results = []
            if results['documents'] and results['documents'][0]:
                for i in range(len(results['documents'][0])):
                    formatted_results.append({
                        'text': results['documents'][0][i],
                        'metadata': results['metadatas'][0][i],
                        'distance': results['distances'][0][i] if 'distances' in results else None
                    })
            
            logger.info(f"Found {len(formatted_results)} relevant documents for query")
            return formatted_results
        
        except Exception as e:
            logger.error(f"Error searching vector store: {str(e)}")
            return []
    
    def get_collection_count(self) -> int:
        """Get the number of documents in the collection"""
        try:
            return self.collection.count()
        except:
            return 0
    
    def clear_collection(self):
        """Clear all documents from the collection"""
        try:
            self.chroma_client.delete_collection(name=self.collection_name)
            self.collection = self.chroma_client.create_collection(
                name=self.collection_name,
                metadata={"description": "GxP Validation Guidelines (OpenAI)"}
            )
            logger.info("Collection cleared successfully")
        except Exception as e:
            logger.error(f"Error clearing collection: {str(e)}")
