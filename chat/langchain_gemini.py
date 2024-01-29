import pandas as pd
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
import time
from decouple import config
from .test import to_markdown


API_KEY = config("GOOGLE_API_KEY", default="AIzaSyCnMz4nOPyugJHhQu3qB8eydCzje8EDzzQ")

def geminiChat(problem, context):

    model = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=API_KEY,
                                temperature=0.4,convert_system_message_to_human=True)

    # pdf_loader = PyPDFLoader("C:/Users/leo-joseph/Desktop/new_project/cimplify/cimplify_ai/chat/Final Version.pdf")
    # pages = pdf_loader.load_and_split()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    # context = "\n\n".join(str(p.page_content) for p in pages)
    texts = text_splitter.split_text(context)
        
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=API_KEY)
        
    vector_index = Chroma.from_texts(texts, embeddings).as_retriever(search_kwargs={"k":5})   

    qa_chain = RetrievalQA.from_chain_type(
        model,
        retriever=vector_index,
        return_source_documents=True

    )


    template = """Use the following pieces of context gotten from a document to give a response to the question below. Also try to make up an answer if at and don't over generalize the answer you give and make it very detailed and simplified as possible like a teacher to a student. Always say "thanks for using Cimplify!" at the end of the answer.
    {context}
    Question: {question}
    Helpful Answer:"""
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)# Run chain
    qa_chain = RetrievalQA.from_chain_type(
        model,
        retriever=vector_index,
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )
    #question = "Describe Operating System in details?"
    result = qa_chain({"query": problem})
    print(result["result"])
    return to_markdown(result['result'])

     
