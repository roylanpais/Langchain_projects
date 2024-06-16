from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["GOOGLE_API_KEY"] = os.getenv("gemini_api_key")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("langchain_tracing")


##Prompt template
promt = ChatPromptTemplate.from_messages([
    ("system", "You are a assistant.Please respond"),
    ("user", "Question:{question}")
])

##streamlit frameword
st.title(mode)