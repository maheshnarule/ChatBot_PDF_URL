
import streamlit as st
import tempfile

def upload_pdfs():
    with st.sidebar:
        st.header("📂 Upload PDFs")
        uploaded_files = st.file_uploader(
            "Choose PDF files",
            type="pdf",
            accept_multiple_files=True,
            help="You can upload multiple research papers, reports, etc."
        )
        submit = st.button("🚀 Submit ")
    return uploaded_files, submit   # ✅ Return both values

def save_uploaded_files(uploaded_files):
    file_paths = []
    for file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file.read())
            file_paths.append(tmp.name)
    return file_paths
