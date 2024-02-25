from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import Html2TextTransformer
from langchain.document_loaders import SitemapLoader

import streamlit as st

st.set_page_config(
    page_title="SiteGPT",
    page_icon="🖥️",
)

st.markdown(
    """
    # SiteGPT
            
    Ask questions about the content of a website.
            
    Start by writing the URL of the website on the sidebar.
"""
)

with st.sidebar:
    url = st.text_input(
        "Write down a URL",
        placeholder="https://example.com",
    )

# # Using Chromium and Html2TextTransformer
# html2text_transformer = Html2TextTransformer()

# if url:
#     loader = AsyncChromiumLoader([url])
#     docs = loader.load()
#     transformed = html2text_transformer.transform_documents(docs)
#     st.write(docs)

@st.cache_data(show_spinner="Loading website...")
def load_website(url):
    loader = SitemapLoader(url)
    loader.requests_per_second = 5
    docs = loader.load()
    return docs

if url:
    if ".xml" not in url:
        with st.sidebar:
            st.error("Please write down a Sitemap URL.")
    else:
        docs = load_website(url)
        st.write(docs)