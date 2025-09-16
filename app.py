
# import streamlit as st

# st.set_page_config(page_title="Welcome to PDF Reader Bot", page_icon="🤖", layout="centered")

# # CSS Styling
# st.markdown("""
#     <style>
#     .main {
#         text-align: center;
#         padding-top: 100px;
#     }
#     .title {
#         font-size: 36px;
#         font-weight: bold;
#         color: #2c3e50;
#     }
#     .subtitle {
#         font-size: 18px;
#         color: #555;
#         margin-bottom: 30px;
#     }

#     /* ✅ Green Get Started Button */
#     div.stButton > button {
#         font-size: 20px !important;
#         font-weight: bold !important;
#         background-color: #28a745 !important;  /* Green */
#         color: white !important;
#         border-radius: 10px !important;
#         padding: 10px 24px !important;
#         border: none !important;
#         transition: 0.3s;
#     }
#     div.stButton > button:hover {
#         background-color: #218838 !important;  /* Darker green on hover */
#         color: white !important;
#     }
#     section[data-testid="stSidebar"] {
#     background-color: white;  /* ✅ Solid green */
#     border-right: 2px solid #000000;
# }
#     </style>
# """, unsafe_allow_html=True)

# # Landing Content
# st.markdown("<div class='main'>", unsafe_allow_html=True)

# st.image("logo.png", width=200)  
# st.markdown("<div class='title'>Welcome to 🤖 RAGBot</div>", unsafe_allow_html=True)
# st.markdown("<div class='subtitle'>Ask questions directly from your PDFs</div>", unsafe_allow_html=True)

# # Get Started button
# if st.button("🚀 Get Started", key="start", use_container_width=True):
#     st.switch_page("pages/index.py")

# st.markdown("</div>", unsafe_allow_html=True)



# import streamlit as st

# st.set_page_config(page_title="Welcome to PDF Reader Bot", page_icon="🤖", layout="centered")

# # CSS Styling
# st.markdown("""
#     <style>
#     /* Flex container for horizontal alignment */
#     .hero {
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         gap: 30px;  /* Space between elements */
#         margin-top: 80px;
#     }

#     /* Logo styling */
#     .hero img {
#         width: 120px;  /* Adjust size */
#         height: auto;
#     }

#     /* Text container */
#     .hero-text {
#         display: flex;
#         flex-direction: column;
#         align-items: flex-start; /* Align title/subtitle left */
#     }

#     .title {
#         font-size: 36px;
#         font-weight: bold;
#         color: #2c3e50;
#         margin: 0;
#     }

#     .subtitle {
#         font-size: 18px;
#         color: #555;
#         margin: 5px 0 0 0;
#     }

#     /* Green Get Started Button */
#     div.stButton > button {
#         font-size: 20px !important;
#         font-weight: bold !important;
#         background-color: #28a745 !important;
#         color: white !important;
#         border-radius: 10px !important;
#         padding: 10px 24px !important;
#         border: none !important;
#         transition: 0.3s;
#     }
#     div.stButton > button:hover {
#         background-color: #218838 !important;
#     }

#     section[data-testid="stSidebar"] {
#         background-color: white;
#         border-right: 2px solid #000000;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Hero Section
# st.markdown("""
# <div class="hero">
#     <img src="logo.png" alt="Logo">
#     <div class="hero-text">
#         <div class="title">Welcome to 🤖 RAGBot</div>
#         <div class="subtitle">Ask questions directly from your PDFs</div>
#     </div>
#     <div>
#         <!-- Streamlit button will appear here -->
#     </div>
# </div>
# """, unsafe_allow_html=True)

# # # Landing Content
# # st.markdown("<div class='main'>", unsafe_allow_html=True)

# # st.image("logo.png", width=200)  
# # st.markdown("<div class='title'>Welcome to 🤖 RAGBot</div>", unsafe_allow_html=True)
# # st.markdown("<div class='subtitle'>Ask questions directly from your PDFs</div>", unsafe_allow_html=True)

# # Get Started button
# if st.button("🚀 Get Started", key="start", use_container_width=True):
#     st.switch_page("pages/index.py")

# st.markdown("</div>", unsafe_allow_html=True)


import streamlit as st

st.set_page_config(page_title="Welcome to PDF Reader Bot", page_icon="🤖", layout="centered")

# CSS Styling
st.markdown("""
    <style>
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #2c3e50;
        margin: 0;
    }
    .subtitle {
        font-size: 18px;
        color: #555;
        margin: 5px 0 0 0;
    }
    div.stButton > button {
        font-size: 20px !important;
        font-weight: bold !important;
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 10px 24px !important;
        border: none !important;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #218838 !important;
    }
    .hero {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        margin-top: 80px;
        flex-wrap: wrap;
    }
    .text-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

# Hero section with logo and title/subtitle
st.markdown("<div class='hero'>", unsafe_allow_html=True)

# Logo
st.image("logo.png", width=120, use_container_width=False)  # Updated parameter

# Title & Subtitle
st.markdown("""
<div class='text-container'>
    <div class='title'>Welcome to 🤖 ChatBot</div>
    <div class='subtitle'>Ask questions directly from your PDFs</div>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Get Started Button centered
st.markdown("<div style='text-align:center; margin-top:30px;'>", unsafe_allow_html=True)
if st.button("🚀 Get Started", key="start"):
    st.switch_page("pages/index.py")
st.markdown("</div>", unsafe_allow_html=True)
