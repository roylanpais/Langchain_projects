from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate


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
    print(video_url)
    loader = YoutubeLoader.from_youtube_url(
    video_url, add_video_info=False)
    transcript = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100 )
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)

    return db

video_url = "https://youtu.be/ZprzYoTK-UM?si=t8t498IhKS5_0m7t"

def get_response_from_query(db, query, k = 4):
    docs= db.similarity_search(query, k = k)
    docs_page_content = " ".join([d.page_content for d in docs])

    print(docs_page_content)
    llm = GoogleGenerativeAI(model="gemini-pro")
    prompt = PromptTemplate(
        input_variables = ["question", "docs"], 
        template = "help me answer the question {question} based on the following youtube transcript {docs}"
    )
    input_data = {
        'question': query,
        'docs': docs_page_content,
    
    }

    chain = prompt | llm
    response = chain.invoke(input = input_data)
    response = response.replace("\n", " ")
    return response
