#from langchain_openai import ChatOpenAI
#from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
#from langchai import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
#os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
#os.environ["ANTHROPIC_API_KEY"] = os.getenv("CLAUDE_API_KEY")
#Langsmith tracking
os.environ["LANGSMITH_TRACING"] = os.getenv("LANGSMITH_TRACING")
os.environ["LANGSMITH_ENDPOINT"] = os.getenv("LANGSMITH_ENDPOINT")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT")

#os.environ["LANGCHAIN_TRACING_V2"]= "true"

## Prompt Template

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
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
