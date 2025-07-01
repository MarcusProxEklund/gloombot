from chromadb import PersistentClient
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import pdfplumber
import os


load_dotenv()

# Initialize PersistentClient and load the collection
client = PersistentClient(
    # Persistent storage path
    settings=Settings(anonymized_telemetry=False),
)


def create_collection(directory_path : str = r'data', collection_name: str = "pdf_knowledge_base"):
    """Goes through the pdf file in the directory_path, \n 
    extracts text from each page, \n 
    splits it into chunks, and adds it to a ChromaDB collection.

    Args:
        directory_path (str, optional): Path to pdf that will be extracted. Defaults to r'data'.
        collection_name (str, optional): Name of the collection for easy reference. Defaults to "pdf_knowledge_base".

    Returns:
        ChromaDBCollection: Returns the collection created in chromaDB with the text extracted from the pdf.
    """
    
    data = []
    with pdfplumber.open(directory_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                chunks = text.split('\n\n')  # Split by double newlines
                for chunk_num, chunk in enumerate(chunks):
                    data.append(
                        {
                            "id": f"{os.path.basename(directory_path)}_page{page_num}_chunk{chunk_num}",
                            "text": chunk.strip(),
                            "source": directory_path,
                            "page": page_num
                        }
                    )
    print(f"loaded documents with {len(data)} pages")

    collection = client.get_or_create_collection(collection_name)        
    # Load the SentenceTransformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    #Extract and add embeddings to the collection
    for item in data:
        embedding = model.encode(item["text"]).tolist()
        collection.upsert(
            ids=[item["id"]],
            documents=[item["text"]],
            embeddings=[embedding],
            metadatas=[
                {
                    "source": item["source"], 
                    "page": item["page"]
                }
            ]
        )
    print("Documents added to the collection.")

    return collection