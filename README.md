# Multi-Document RAG System

A Retrieval-Augmented Generation (RAG) application that answers questions over PDF documents, running entirely locally using LangChain, ChromaDB, and Llama 3.1 via Ollama.

## Features

- Loads and chunks multiple PDFs
- Embeds and stores them in ChromaDB
- Retrieves relevant chunks per question
- Answers locally using Llama 3.1 (Ollama), with sources

## Technologies

| Technology | Purpose |
|---|---|
| [LangChain](https://www.langchain.com/) | RAG pipeline orchestration |
| [ChromaDB](https://www.trychroma.com/) | Vector database |
| Hugging Face Embeddings (`all-MiniLM-L6-v2`) | Text embeddings |
| [Ollama](https://ollama.com/) + Llama 3.1 | Local LLM inference |
| PyPDFLoader | PDF loading |

## Project Structure

```text
.
├── mainrag.py          # Main RAG application
├── requirements.txt     # Python dependencies
├── README.md
├── data/                 # Place your PDF documents here
└── chroma_db/            # Auto-generated vector database
```

## Installation

### 1. Clone the repository
```bash
git clone <repo-url>
cd <repo-folder>
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install langchain langchain-community langchain-text-splitters \
            langchain-huggingface langchain-chroma langchain-ollama \
            chromadb pypdf sentence-transformers
```

> Note: the `requirements.txt` in this project is a full dump of an Anaconda environment, so it's recommended to install the core packages above directly rather than using that file as-is.

### 4. Install Ollama and pull the model
After installing [Ollama](https://ollama.com/download), run:
```bash
ollama pull llama3.1
```

### 5. Add your PDF files
Place your PDF documents in the `data/` folder.

## Usage

```bash
python mainrag.py
```

When run, the script will:
1. Read and chunk all PDFs in the `data/` folder
2. Generate embeddings and store them in ChromaDB
3. Prompt you to enter a question in the terminal
4. Retrieve the 10 most relevant chunks and pass them to the LLM as context
5. Print the answer along with its sources (file name and page number)

### Example Run

```
Ask a question: What is the termination period of the contract?

Answer:

The contract may be terminated by either party with 30 days'
written notice.

Sources:

- contract.pdf, page 4
- contract.pdf, page 7
```

## Notes

- The `chroma_db/` folder is recreated on every run; if you want to keep an existing database, you'll need to modify the script.
- Answers are based solely on the provided PDF content; if the information isn't in the context, the model will say so explicitly.
- For better results, try tuning `chunk_size`, `chunk_overlap`, and `k` (the number of retrieved chunks).
