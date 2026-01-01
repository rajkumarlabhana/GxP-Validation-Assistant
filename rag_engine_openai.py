"""
RAG Engine for query processing and response generation
"""
import logging
from typing import List, Dict
from openai import OpenAI
from config_openai import Config
from vector_store_openai import VectorStore

# Setup logging
Config.LOGS_DIR.mkdir(exist_ok=True)  # Create logs directory if it doesn't exist
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Config.LOGS_DIR / 'rag_engine_openai.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class RAGEngine:
    """Retrieval-Augmented Generation Engine"""
    
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        logger.info("RAG Engine (OpenAI) initialized successfully")
    
    def create_context(self, retrieved_docs: List[Dict]) -> str:
        """Create context from retrieved documents"""
        if not retrieved_docs:
            return "No relevant context found."
        
        context_parts = []
        for i, doc in enumerate(retrieved_docs, 1):
            source = doc['metadata'].get('source', 'Unknown')
            text = doc['text']
            context_parts.append(f"[Source {i}: {source}]\n{text}\n")
        
        return "\n".join(context_parts)
    
    def create_prompt(self, query: str, context: str) -> str:
        """Create a prompt for the generation model"""
        prompt = f"""You are a GxP Validation Assistant, an expert in pharmaceutical and medical device validation, compliance, and regulatory guidelines. Your role is to provide accurate, detailed, and actionable guidance based on the provided context from official GxP validation documents.

**Context from GxP Validation Guidelines:**
{context}

**User Question:**
{query}

**Instructions:**
1. Answer the question based ONLY on the provided context from the GxP validation guidelines.
2. If the context contains relevant information, provide a comprehensive and detailed answer.
3. Include specific references to the source documents when applicable (e.g., "According to GAMP 5..." or "As per FDA 21 CFR Part 11...").
4. If the context does not contain enough information to answer the question, clearly state this and explain what information is missing.
5. Use professional terminology appropriate for GxP validation professionals.
6. Structure your answer with clear sections if the response is lengthy.
7. If applicable, provide practical implementation guidance or best practices.

**Answer:**"""
        
        return prompt
    
    def generate_response(self, query: str, top_k: int = None) -> Dict:
        """Generate a response using RAG"""
        try:
            logger.info(f"Processing query: {query[:100]}...")
            
            # Retrieve relevant documents
            retrieved_docs = self.vector_store.search(query, top_k)
            
            if not retrieved_docs:
                return {
                    "answer": "I couldn't find relevant information in the GxP validation guidelines to answer your question. Please try rephrasing your question or ask about topics covered in GAMP 5, FDA Part 11, ISO 27001, or other GxP validation standards.",
                    "sources": [],
                    "context_used": False
                }
            
            # Create context and prompt
            context = self.create_context(retrieved_docs)
            prompt = self.create_prompt(query, context)
            
            # Generate response using OpenAI
            response = self.client.chat.completions.create(
                model=Config.GENERATION_MODEL,
                messages=[
                    {"role": "system", "content": "You are a GxP Validation Expert Assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=Config.TEMPERATURE,
                max_tokens=Config.MAX_TOKENS
            )
            
            answer = response.choices[0].message.content
            
            # Extract sources
            sources = []
            seen_sources = set()
            for doc in retrieved_docs:
                source = doc['metadata'].get('source', 'Unknown')
                if source not in seen_sources:
                    sources.append(source)
                    seen_sources.add(source)
            
            logger.info("Response generated successfully")
            
            return {
                "answer": answer,
                "sources": sources,
                "context_used": True,
                "num_chunks_retrieved": len(retrieved_docs)
            }
        
        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return {
                "answer": f"An error occurred while generating the response: {str(e)}",
                "sources": [],
                "context_used": False
            }
