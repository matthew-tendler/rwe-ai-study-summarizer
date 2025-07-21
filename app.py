import streamlit as st
import pandas as pd
from summarization_chain import fetch_abstracts_from_europepmc, summarize_abstract, get_tech_stack

st.set_page_config(page_title="AI Study Summarizer", layout="centered")

st.title("🔬 AI Study Summarizer")

query = st.text_input("Enter your medical search topic", "type 1 diabetes")

if st.button("Search and Summarize"):
    with st.spinner("Fetching studies and generating summary..."):
        abstracts = fetch_abstracts_from_europepmc(query)
        summary = summarize_abstract(abstracts)

        st.subheader("📌 AI Summary")
        st.markdown(summary)

        if abstracts:
            st.subheader("📋 Source Studies")
            df = pd.DataFrame(abstracts)
            st.dataframe(df[["title", "journal", "pmid", "doi"]])

st.caption(get_tech_stack())
