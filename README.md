# Multi-Document RAG System

This project is a simple Retrieval-Augmented Generation (RAG) application built with LangChain.

The system loads PDF documents, converts them into vector embeddings, stores them in ChromaDB, retrieves the most relevant document chunks for a user query, and generates an answer using a local LLM running with Ollama.

## Technologies

* Python /  LangChain /  ChromaDB /  Hugging Face Embeddings / Ollama /  Llama 3.1

## How It Works

1. Load PDF documents
2. Split documents into chunks
3. Create embeddings
4. Store embeddings in ChromaDB
5. Retrieve relevant chunks based on a question
6. Send retrieved context to the LLM
7. Generate an answer



## Project Structure

```text
.
├── mainrag.py
├── requirements.txt
├── README.md
├── data/
└── chroma_db/
```

Elif Akar
