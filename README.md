# 📚 RAGBot – PDF Question Answering with Google Gemini + FAISS

RAGBot is a **Retrieval-Augmented Generation (RAG)** chatbot built with **Streamlit**, powered by **Google Gemini API** and **FAISS vector database**.  
You can upload your PDFs, and the bot will let you query their contents conversationally.  

---

## 🚀 Features
- 📂 **Upload multiple PDFs** from the sidebar  
- 🔎 **FAISS vector search** for fast and accurate document retrieval  
- 🤖 **Google Gemini LLM integration** (`gemini-2.5-flash` or `gemini-2.5-pro`)  
- 💬 **Chat UI with history** (powered by `st.chat_message`)  
- 💾 **Download chat history** as a `.txt` file  
- 🧪 **Inspector for stored document chunks**  

---

## 🛠️ Project Structure

---

## ⚡ Installation

### 1. Clone this repository

git clone https://github.com/your-username/ragbot.git
cd ragbot
### 2. Create a virtual environment
python -m venv myenv
source myenv/bin/activate   # Mac/Linux
myenv\Scripts\activate      # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Setup API Keys

Create a .env file in the root directory:

GOOGLE_API_KEY="your-google-genai-key"


👉 Get your key here: Google AI Studio

### ▶️ Usage

Run the Streamlit app:

streamlit run index.py


### Steps:

Upload your PDF(s) from the sidebar

Click "Submit to DB" to process and store embeddings

Start chatting with your documents 🎉

### 📦 Dependencies

Streamlit
 – UI framework

LangChain
 – RAG pipeline

FAISS
 – Vector similarity search

Google Generative AI
 – LLM backend

PyPDFLoader
 – PDF loader