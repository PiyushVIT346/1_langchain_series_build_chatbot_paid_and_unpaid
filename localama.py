from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama

import streamlit as st 
import os
from dotenv import  load_dotenv


os.environ["LANGCHAIN_TRACING_V2"]='true'
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please rseponse to users query"),
        ("user","Question:{question}")
    ]
)

# ollama LLAma-2 llm
llm=ollama(model="llama2")
OutputParser=StrOutputParser()
chain=prompt|llm|OutputParser

#Streamlit framework
st.title("LAngchain Demo with OpenAI")
input_text=st.text_input("Search the topic u want")