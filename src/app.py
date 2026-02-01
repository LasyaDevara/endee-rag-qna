
from ingest import ingest_documents
from query import query_documents

if __name__ == "__main__":
    documents = [
        "Endee is a high-performance vector database engine written in C++.",
        "Retrieval Augmented Generation combines vector search with text generation.",
        "Vector databases enable semantic and contextual search."
    ]

    store = ingest_documents(documents)

    question = input("Ask a question: ")
    context = query_documents(store, question)

    print("\nRetrieved Context:")
    print(context)
