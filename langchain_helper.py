from pathlib import Path
from dotenv import load_dotenv
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS

dotenv_path = Path('D:\Coding\.env')
load_dotenv(dotenv_path=dotenv_path)


embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vector = embeddings.embed_query("hello, world!")

def create_vectordb_youtube(video_url: str) -> FAISS:
    """
    load transcipt and save to FAISS
    input:
        video url
    """
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100 )
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)

    return db

video_url = "https://youtu.be/ZprzYoTK-UM?si=t8t498IhKS5_0m7t"

print(create_vectordb_youtube(video_url))