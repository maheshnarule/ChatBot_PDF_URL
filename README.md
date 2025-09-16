<img width="1918" height="903" alt="image" src="https://github.com/user-attachments/assets/6dcefccb-06c8-47ed-9b74-f81e48ca8d7c" />
<img width="1918" height="910" alt="image" src="https://github.com/user-attachments/assets/8e9adb3a-a899-4784-a292-b5d095a36a70" />
put URL
<img width="1918" height="910" alt="image" src="https://github.com/user-attachments/assets/e7f06e9f-292d-42a5-989f-35d7ee69945a" />
Upload the PDF
<img width="1918" height="905" alt="image" src="https://github.com/user-attachments/assets/0934195f-84be-4282-976d-8b2b931e578d" />
Prompt the question and Result
<img width="1918" height="915" alt="image" src="https://github.com/user-attachments/assets/d681b7bd-5bc9-49b5-b3e2-771b1a4a3dd1" />


# 📚 RAGBot – PDF & URL Question Answering with Google Gemini + FAISS

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

git clone  https://github.com/maheshnarule/ChatBot_PDF_URL.git
cd ragbot
### 2. Create a virtual environment
python -m venv myenv
myenv\Scripts\activate      # Windows

### 3. Install dependencies
pip install -r requirement.txt

### 4. Setup API Keys

Create a .env file in the root directory:

GOOGLE_API_KEY="your-google-genai-key"


👉 Get your key here: Google AI Studio

### ▶️ Usage

Run the Streamlit app:

streamlit run app.py


### Steps:

Upload your PDF(s) from the sidebar
or 
Upload the url

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
