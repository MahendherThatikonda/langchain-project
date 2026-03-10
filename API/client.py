import requests
import streamlit as st

def get_groq_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
                           json={"input":{'topic':input_text}}
                           )
    
    return response.json()['output']['content']

def get_ollama_response(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",
                           json={"input":{'poem':input_text}}
                           )
    
    return response.json()['output']['content']


st.title("LangChain Demo With LLama2 API")
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write an poem on")

if input_text:
    st.write(get_groq_response(input_text))


if input_text1:
    st.write(get_groq_response(input_text1))