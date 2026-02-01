
from sentence_transformers import SentenceTransformer

def query_documents(store, question, top_k=3):
    """
    Retrieves relevant document chunks using Endee-backed
    vector similarity search.
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = model.encode(question)

    results = store.search(query_embedding, top_k=top_k)
    context = " ".join([r[1]["text"] for r in results])
    return context
