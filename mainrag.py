import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

pdf_folder = "data"

all_docs = []

for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        file_path = os.path.join(pdf_folder, filename)

        loader = PyPDFLoader(file_path)
        docs = loader.load()

        for doc in docs:
            doc.metadata["source"] = filename

        all_docs.extend(docs)

print(f"Total PDF pages loaded: {len(all_docs)}")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(all_docs)

print(f"Total chunks created: {len(chunks)}")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 10}
)

prompt_template = PromptTemplate.from_template("""
You are a helpful assistant that answers questions using the provided technical documentation.

Use only the information provided in the context.

If the answer is not available in the context, say:
"I could not find this information in the provided documentation."

Context:
{context}

Question:
{question}

Answer:
""")

llm = ChatOllama(
    model="llama3.1",
    temperature=0
)

query = input("\nAsk a question: ")

results = retriever.invoke(query)

context = "\n\n".join(
    [doc.page_content for doc in results]
)

prompt = prompt_template.invoke({
    "context": context,
    "question": query
})

response = llm.invoke(prompt.to_string())

print("\nAnswer:\n")
print(response.content)

print("\nSources:\n")

seen_sources = set()

for doc in results:
    source = doc.metadata.get("source", "Unknown source")
    page = doc.metadata.get("page", "Unknown page")

    source_info = (source, page)

    if source_info not in seen_sources:
        seen_sources.add(source_info)
        print(f"- {source}, page {page + 1}")