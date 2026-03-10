from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv  import load_dotenv


load_dotenv 

os.environ["LANGSMITH_TRACING"] = os.getenv("LANGSMITH_TRACING")
os.environ["LANGSMITH_ENDPOINT"] = os.getenv("LANGSMITH_ENDPOINT")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
#os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT")


prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You're are a helpful assistant.Please response to the user queries."),
        ("user","Question:{question}")
    ]
)

# Streamlit framework

st.title("Langchain Demo with OpenAPI")
input_text = st.text_input("Search the topic you want")

#Anthropic LLM

#llm = ChatAnthropic(model="claude-3-5-haiku-20241022")
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
