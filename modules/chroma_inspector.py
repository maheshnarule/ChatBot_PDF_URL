import streamlit as st

def inspect_faiss(vectorstore):
    st.sidebar.markdown("🧪 **FAISS Inspector**")

    query = st.sidebar.text_input("🔍 Test a query against FAISS")
    if query:
        try:
            results = vectorstore.similarity_search(query, k=3)
            st.sidebar.markdown("### Top Matching Chunks:")
            for i, doc in enumerate(results):
                st.sidebar.markdown(f"**Result {i+1}:**")
                st.sidebar.markdown(doc.page_content[:300] + "...")
                st.sidebar.markdown("---")
        except Exception as e:
            st.sidebar.error("Error querying FAISS")
            st.sidebar.code(str(e))
