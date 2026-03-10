from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langserve import add_routes
from langchain_ollama import ChatOllama

import uvicorn 
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

app = FastAPI(
    title="Langchain Server",
    version="1.0",                    # ← fix: string not number
    description="A simple API Server"
)

# Groq model
model = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

# Ollama model
llm = ChatOllama(model="llama3.2")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} around 100 words?")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} around 100 words?")

add_routes(app, model, path="/Groq")
add_routes(app, prompt1 | model, path="/essay")
add_routes(app, prompt2 | llm, path="/poem")   # ← poem uses ollama

if __name__ == "__main__":             # ← fix: "__main__" not "main"
    uvicorn.run(app, host="localhost", port=8000)  # ← fix: "localhost" not "local"