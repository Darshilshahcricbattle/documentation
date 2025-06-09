import os
import hashlib
import json
from typing import List, Dict, Any
from pathlib import Path
import pandas as pd

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.schema import Document
from pinecone import Pinecone
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DocumentProcessor:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.pinecone_api_key = os.getenv("PINECONE_API_KEY")
        self.index_name = os.getenv("PINECONE_INDEX_NAME", "chatbot")
        self.region = os.getenv("REGION", "us-east-1")
        
        # Initialize Pinecone
        self.pc = Pinecone(api_key=self.pinecone_api_key)
        
        # Initialize embeddings
        self.embeddings = OpenAIEmbeddings(
            openai_api_key=self.openai_api_key,
            model="text-embedding-3-small"
        )
        
        # Initialize text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""]
        )
        
        # Create index if it doesn't exist
        self._ensure_index_exists()
        
        # Initialize vector store
        self.vector_store = PineconeVectorStore(
            index=self.pc.Index(self.index_name),
            embedding=self.embeddings
        )
        
        # File to track processed documents
        self.processed_files_path = "processed_files.json"
        self.processed_files = self._load_processed_files()
    
    def _ensure_index_exists(self):
        """Create Pinecone index if it doesn't exist"""
        try:
            existing_indexes = [index.name for index in self.pc.list_indexes()]
            if self.index_name not in existing_indexes:
                self.pc.create_index(
                    name=self.index_name,
                    dimension=1536,  # text-embedding-3-small dimension
                    metric='cosine',
                    spec={
                        'serverless': {
                            'cloud': 'aws',
                            'region': self.region
                        }
                    }
                )
        except Exception as e:
            print(f"Error creating index: {e}")
    
    def _load_processed_files(self) -> Dict[str, str]:
        """Load the record of processed files"""
        if os.path.exists(self.processed_files_path):
            with open(self.processed_files_path, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_processed_files(self):
        """Save the record of processed files"""
        with open(self.processed_files_path, 'w') as f:
            json.dump(self.processed_files, f, indent=2)
    
    def _get_file_hash(self, file_path: str) -> str:
        """Get MD5 hash of file content"""
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    
    def _has_file_changed(self, file_path: str) -> bool:
        """Check if file has changed since last processing"""
        current_hash = self._get_file_hash(file_path)
        stored_hash = self.processed_files.get(file_path)
        return current_hash != stored_hash
    
    def load_markdown_file(self, file_path: str) -> List[Document]:
        """Load and split a markdown file"""
        try:
            loader = UnstructuredMarkdownLoader(file_path)
            documents = loader.load()
            
            # Add metadata
            for doc in documents:
                doc.metadata.update({
                    'source': file_path,
                    'filename': os.path.basename(file_path),
                    'file_type': 'markdown'
                })
            
            # Split documents
            split_docs = self.text_splitter.split_documents(documents)
            return split_docs
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return []
    
    def process_single_file(self, file_path: str) -> bool:
        """Process a single markdown file"""
        try:
            print(f"Processing: {file_path}")
            
            # Load and split document
            documents = self.load_markdown_file(file_path)
            
            if not documents:
                return False
            
            # Add to vector store
            self.vector_store.add_documents(documents)
            
            # Update processed files record
            self.processed_files[file_path] = self._get_file_hash(file_path)
            self._save_processed_files()
            
            print(f"Successfully processed {file_path} - {len(documents)} chunks")
            return True
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return False
    
    def scan_and_process_new_documents(self, documentation_folder: str = "Documentation") -> Dict[str, Any]:
        """Scan documentation folder for new or changed files"""
        results = {
            'processed': [],
            'skipped': [],
            'errors': []
        }
        
        if not os.path.exists(documentation_folder):
            os.makedirs(documentation_folder)
            print(f"Created {documentation_folder} folder")
            return results
        
        # Get all markdown files
        md_files = list(Path(documentation_folder).glob("**/*.md"))
        
        for file_path in md_files:
            file_path_str = str(file_path)
            
            # Check if file needs processing
            if not self._has_file_changed(file_path_str):
                results['skipped'].append(file_path_str)
                continue
            
            # Process the file
            if self.process_single_file(file_path_str):
                results['processed'].append(file_path_str)
            else:
                results['errors'].append(file_path_str)
        
        return results
    
    def get_processed_files_info(self) -> pd.DataFrame:
        """Get information about processed files"""
        data = []
        for file_path, file_hash in self.processed_files.items():
            if os.path.exists(file_path):
                stat = os.stat(file_path)
                data.append({
                    'File': os.path.basename(file_path),
                    'Path': file_path,
                    'Size (KB)': round(stat.st_size / 1024, 2),
                    'Modified': pd.to_datetime(stat.st_mtime, unit='s').strftime('%Y-%m-%d %H:%M:%S'),
                    'Hash': file_hash[:8] + '...'
                })
        
        return pd.DataFrame(data)
    
    def remove_file_from_index(self, file_path: str):
        """Remove a file's documents from the vector store"""
        try:
            # This is a limitation - Pinecone doesn't easily support deletion by metadata
            # You would need to implement a more sophisticated tracking system
            print(f"Note: Direct file removal not implemented. Consider recreating index for {file_path}")
            
            # Remove from processed files
            if file_path in self.processed_files:
                del self.processed_files[file_path]
                self._save_processed_files()
                
        except Exception as e:
            print(f"Error removing file: {e}")
