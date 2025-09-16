
# import warnings
# import logging
# import streamlit as st

# # Local modules
# from modules.chat import display_chat_history, handle_user_input, download_chat_history
# from modules.pdf_handler import upload_pdfs
# from modules.vectorstore import load_vectorstore
# from modules.llm import get_llm_chain
# from modules.chroma_inspector import inspect_faiss

# # Silence noisy logs
# warnings.filterwarnings("ignore")
# logging.getLogger("transformers").setLevel(logging.ERROR)

# st.set_page_config(
#     page_title="RagBot!",     
# )

# # CSS Styling for UI
# #CSS Styling for UI
# st.markdown(
#     """
#     <style>
#     /* App background */
#     .stApp {
#         background-color: #f8f9fa;
#         font-family: 'Segoe UI', sans-serif;
#     }

#     /* Sidebar green background + black border */
#     section[data-testid="stSidebar"] {
#     background-color: white;  /* ✅ Solid green */
#     border-right: 2px solid #000000;
# }


#     /* Fixed Title with background */
#     h1 {
#         color: #ffffff !important;  /* Pure white */
#         font-weight: bold !important;
#         text-align: center;
#         font-weight: 700;
#         margin-bottom: 1rem;
#         position: sticky;
#         top: 0;
#         background-color: #28a745;  /* soft green background */
#         z-index: 9999;
#         padding: 15px 0;
#         border-bottom: 2px solid #2c3e50;
#         box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
#     }
    

#     /* Chat bubbles */
#     .stChatMessage {
#         border-radius: 12px;
#         padding: 12px;
#         margin-bottom: 8px;
#     }
#     .stChatMessage[data-testid="stChatMessage-user"] {
#         background-color: #d1ecf1;
#         border: 1px solid #bee5eb;
#     }
#     .stChatMessage[data-testid="stChatMessage-assistant"] {
#         background-color: #e2e3e5;
#         border: 1px solid #d6d8db;
#     }

#     /* Buttons */
#     button {
#         border-radius: 8px !important;
#         font-weight: 600 !important;
#     }
#     /* Submit to DB button (dark gray style) */
#     section[data-testid="stSidebar"] div.stButton > button {
#         background-color: #218838 !important;
#         color: #ffffff !important;
#         border-radius: 8px !important;
#         font-weight: bold !important;
#         border: 2px solid #555555 !important;
#         transition: 0.3s;
#     }
#     section[data-testid="stSidebar"] div.stButton > button:hover {
#         background-color: #555555 !important;
#         color: #ffffff !important;
#     }
    
# /* 🔍 Sidebar FAISS Query Input */
# section[data-testid="stSidebar"] input[type="text"] {
#     border: 2px solid orange !important;
#     border-radius: 6px !important;
#     color: black !important;
# }


#     </style>
#     """,
#     unsafe_allow_html=True
# )



# # App title
# st.title("🤖 ChatBot – Ask Your PDFs")
# st.caption("Powered by Google Gemini + FAISS")

# # Step 1: Upload PDFs + wait for submit
# uploaded_files, submitted = upload_pdfs()

# # Step 2: If user clicks submit, update vectorstore
# if submitted:
#     if uploaded_files and len(uploaded_files) > 0:
#         with st.spinner("⚡ Updating vector database... Please wait."):
#             vectorstore = load_vectorstore(uploaded_files)
#             st.session_state.vectorstore = vectorstore
#         st.success("✅ Documents successfully processed!")
#     else:
#         st.warning("⚠️ Please upload at least one PDF before submitting.")

# # Step 3: Display vectorstore inspector (Sidebar)
# if "vectorstore" in st.session_state:
#     inspect_faiss(st.session_state.vectorstore)

# # Step 4: Display old chat messages
# display_chat_history()

# # Step 5: Handle new prompt input
# if "vectorstore" in st.session_state:
#     handle_user_input(get_llm_chain(st.session_state.vectorstore))

# # Step 6: Chat history export
# download_chat_history()



import warnings
import logging
import streamlit as st

# Local modules
from modules.chat import display_chat_history, handle_user_input, download_chat_history
from modules.pdf_handler import upload_pdfs
from modules.vectorstore import load_vectorstore
from modules.llm import get_llm_chain
from modules.chroma_inspector import inspect_faiss

# Silence noisy logs
warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.ERROR)

st.set_page_config(
    page_title="RagBot!",     
)

# CSS Styling for UI
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f8f9fa;
        font-family: 'Segoe UI', sans-serif;
    }
    section[data-testid="stSidebar"] {
        background-color: white;
        border-right: 2px solid #000000;
    }
    h1 {
        color: #ffffff !important;
        font-weight: bold !important;
        text-align: center;
        font-weight: 700;
        margin-bottom: 1rem;
        position: sticky;
        top: 0;
        background-color: #28a745;
        z-index: 9999;
        padding: 15px 0;
        border-bottom: 2px solid #2c3e50;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
    }
    .stChatMessage {
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 8px;
    }
    .stChatMessage[data-testid="stChatMessage-user"] {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
    }
    .stChatMessage[data-testid="stChatMessage-assistant"] {
        background-color: #e2e3e5;
        border: 1px solid #d6d8db;
    }
    button {
        border-radius: 8px !important;
        font-weight: 600 !important;
    }
    section[data-testid="stSidebar"] div.stButton > button {
        background-color: #218838 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        border: 2px solid #555555 !important;
        transition: 0.3s;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #555555 !important;
        color: #ffffff !important;
    }
    section[data-testid="stSidebar"] input[type="text"] {
        border: 2px solid orange !important;
        border-radius: 6px !important;
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("🤖 ChatBot – Ask Your PDFs or Websites")
st.caption("Powered by Google Gemini + FAISS")

# Step 1: Upload PDFs
uploaded_files, submitted = upload_pdfs()

# Step 2: Input Website URL (new feature 🚀)
url_input = st.sidebar.text_input("🌍 Enter Website URL (e.g. Wikipedia)")

if submitted or url_input:
    with st.spinner("⚡ Updating vector database... Please wait."):
        try:
            vectorstore = load_vectorstore(
                uploaded_files=uploaded_files if uploaded_files else None,
                url=url_input if url_input else None
            )
            st.session_state.vectorstore = vectorstore
            st.success("✅ Documents/Website successfully processed!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# Step 3: Display vectorstore inspector (Sidebar)
if "vectorstore" in st.session_state:
    inspect_faiss(st.session_state.vectorstore)

# Step 4: Display old chat messages
display_chat_history()

# Step 5: Handle new prompt input
if "vectorstore" in st.session_state:
    handle_user_input(get_llm_chain(st.session_state.vectorstore))

# Step 6: Chat history export
download_chat_history()
