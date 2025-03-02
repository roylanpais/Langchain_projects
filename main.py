import streamlit as st
import langchain_helper as lch
import textwrap

st.title("Youtube assistant")
with st.sidebar:
    with st.form(key = "My form"):
        youtube_url = st.sidebar.text_area(label = "what is youtube url")
        query = st.sidebar.text_area(label = "Ask me the query")

        submit = st.form_submit_button(label = "Submit")

if query and youtube_url:
    db = lch.create_vectordb_youtube(youtube_url)
    response = lch.get_response_from_query(db, query)
    st.subheader("answer")
    st.text((response))
    st.text(textwrap.fill(response, width = 80))