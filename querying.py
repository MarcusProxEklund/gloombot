from chromadb import PersistentClient
from chromadb.config import Settings
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()
chroma_client = PersistentClient(
    # Persistent storage path
    settings=Settings(anonymized_telemetry=False),
)

def data_querying(input_text: str):
    """Embeds the input text, queries the ChromaDB collection, \n
    and returns a response from OpenAI's API based on the context retrieved.

    Args:
        input_text (str): Query text to be processed.

    Returns:
        str: Response from OpenAI's API based on the context retrieved from ChromaDB.
    """
    # Load collcetion
    collection = chroma_client.get_collection("pdf_knowledge_base")
    
    results = collection.query(
        query_texts=[input_text],
        n_results=4,  # Number of results to retrieve
    )
    # Flatten the list of lists into a single list
    flat_results = [doc for sublist in results["documents"] for doc in sublist]

    prompt = f"User query: {input_text}\n\nContext:\n{flat_results}\n\nPlease provide a concise and relevant answer based on this information."
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Use "gpt-4" if available
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that provides concise answers related to the game Gloomhaven based on provided context.",
                },
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return "I have no answer for this. Please ask something related to Gloomhaven."
    