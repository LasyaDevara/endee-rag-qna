# Document Question Answering using RAG with Endee

## Project Overview
This project implements a Retrieval Augmented Generation (RAG) based document question answering system using Endee as the vector database. The system allows users to ask natural language questions over a set of documents and retrieves semantically relevant context using vector similarity search.

The focus of this project is to demonstrate how a vector database can be integrated into an AI/ML pipeline for semantic search and retrieval-based applications.

---

## Problem Statement
Traditional keyword-based search techniques often fail to capture the semantic meaning of text, especially when users ask natural language questions. This leads to poor retrieval results when working with large or unstructured document collections.

---

## Solution Approach
The solution converts documents into dense vector embeddings that capture semantic meaning. User queries are also embedded into vectors. Similarity search is then performed to retrieve the most relevant document chunks.

This retrieved context is used as part of a Retrieval Augmented Generation (RAG) workflow, enabling more accurate and context-aware responses.

---

## Use of Endee
Endee is a high-performance vector database engine written in C++ that supports efficient vector storage and similarity search using HNSW-based indexing.

In this project:
- Python is used for embedding generation and RAG orchestration
- Endee serves as the vector database layer responsible for storing and retrieving embeddings
- An abstraction layer (`EndeeVectorStore`) represents Endee’s role in the system architecture

Endee is included as an external dependency under the `third_party` directory.

---

## System Architecture
Documents are converted into embeddings and stored in the Endee vector database.  
User queries are embedded and matched against stored vectors using similarity search.  
The most relevant document chunks are retrieved and returned as contextual output.

Architecture flow:  
Documents → Embeddings → Endee Vector Database → Top-K Retrieval → Context Output

---

## Project Structure
src/
app.py
ingest.py
query.py
vector_store.py
third_party/
endee/
requirements.txt
README.md


---

## Setup Instructions

### Install Dependencies
```bash
pip install -r requirements.txt

Run the Application
python src/app.py

Example Usage

Question: What is Endee?

Retrieved Context:
Endee is a high-performance vector database engine written in C++. Vector databases enable semantic and contextual search. Retrieval Augmented Generation combines vector search with text generation.

Conclusion

This project demonstrates how vector databases such as Endee can be used as a core component in modern AI applications. By combining semantic embeddings with efficient vector search, the system enables accurate and meaningful information retrieval for natural language queries.


---

## ✅ Verify it was created

Run:
```python
!ls
