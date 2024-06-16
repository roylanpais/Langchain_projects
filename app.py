from langchain_groq import ChatGroq
from langchain.schema import BaseOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

from pathlib import Path
dotenv_path = Path('D:\Coding\.env')
load_dotenv(dotenv_path=dotenv_path)
import streamlit as st
GROQ_API_KEY = os.getenv('groq_api_key')

# Load LLM model and get response
def get_groq_model_response(question):
    llm = ChatGroq(model="llama3-70b-8192", temperature=0, )
    response = llm.invoke(question)
    return response


# Initialize streamlit app
st.set_page_config(page_title="Chat with groq")
st.header("Langchain application")

input = st.text_input("Input: ", key = "input")

submit = st.button("Please enter your question")
response = get_groq_model_response(input)
if submit: 
    st.header("The response is ")
    st.write(response)