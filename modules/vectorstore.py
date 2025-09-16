

from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader, WebBaseLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from modules.pdf_handler import save_uploaded_files

def load_vectorstore(uploaded_files=None, url=None):
    docs = []

    # Handle PDF files
    if uploaded_files:
        paths = save_uploaded_files(uploaded_files)
        for path in paths:
            loader = PyPDFLoader(path)
            docs.extend(loader.load())

    # Handle Website URL
    if url:
        loader = WebBaseLoader(url)
        docs.extend(loader.load())

    if not docs:
        raise ValueError("No documents found. Please upload a PDF or provide a valid URL.")

    # Split text
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = splitter.split_documents(docs)

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2")

    # FAISS (in-memory)
    vectorstore = FAISS.from_documents(texts, embeddings)
    return vectorstore
