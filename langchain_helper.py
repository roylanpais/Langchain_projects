from pathlib import Path
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS

dotenv_path = Path('D:\Coding\.env')
load_dotenv(dotenv_path=dotenv_path)