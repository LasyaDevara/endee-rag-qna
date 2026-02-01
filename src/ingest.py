
from sentence_transformers import SentenceTransformer
from vector_store import EndeeVectorStore

def ingest_documents(texts):
    """
    Converts documents into embeddings and stores them
    in the Endee vector database abstraction.
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")
    store = EndeeVectorStore()

    embeddings = model.encode(texts)
    metadata = [{"text": t} for t in texts]

    store.add_vectors(embeddings, metadata)
    return store
