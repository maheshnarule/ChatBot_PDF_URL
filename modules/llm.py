import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

def get_llm_chain(vectorstore):
    llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.environ.get("GOOGLE_API_KEY")
)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
