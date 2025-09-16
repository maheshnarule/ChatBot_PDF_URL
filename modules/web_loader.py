import requests
from bs4 import BeautifulSoup
from langchain.docstore.document import Document

def load_webpage(url: str):
    """Fetch webpage content and return as LangChain Document list"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract text (remove scripts, styles, etc.)
        for script in soup(["script", "style"]):
            script.extract()

        text = soup.get_text(separator=" ", strip=True)

        # Wrap in LangChain Document
        return [Document(page_content=text, metadata={"source": url})]

    except Exception as e:
        print(f"Error loading {url}: {e}")
        return []
