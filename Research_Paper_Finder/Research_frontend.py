
import streamlit as st
import pandas as pd
import joblib as jb
import time
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Research Paper Assistant", layout="wide")

@st.cache_resource
def load_models():
    tfidf = jb.load("TF-IDF Vectorizer")
    x = jb.load("Abstracts.pkl")
    papers = jb.load("papers.pkl")
    return tfidf, x, papers
if "selected_summary" not in st.session_state:
    st.session_state.selected_summary = ""

tfidf, x, papers = load_models()

st.title("Research Paper Assistant")

query = st.text_input(
    "Search Research Papers",
    placeholder="e.g. Depth Estimation"
)

if query:

    query_vector = tfidf.transform([query])

    scores = cosine_similarity(query_vector, x).flatten()

    top = scores.argsort()[::-1][:10]

    st.subheader("Search Results")

    for rank, idx in enumerate(top, start=1):

        title = papers.iloc[idx]["titles"]
        abstract = papers.iloc[idx]["summaries"]

        col1, col2 = st.columns([8, 2])

        with col1:
            st.markdown(f"### {rank}. {title}")

        with col2:
            if st.button(
                "Generate Abstract",
                key=f"summary_{idx}"
            ):
                with st.spinner("Generating Abtract..."):
                    time.sleep(0.05)
                st.session_state.selected_summary = abstract
st.markdown("---")

st.subheader("Generated Abstract")

if st.session_state.selected_summary:

    st.info(st.session_state.selected_summary)

