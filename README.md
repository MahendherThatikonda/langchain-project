# LangChain Project

A hands-on exploration of the LangChain ecosystem, covering RAG pipelines, 
AI agents, API integrations, and multiple LLM/vector store combinations.

## Overview

This repo documents my learning journey with LangChain — each folder is a 
self-contained module exploring a different capability, from basic API calls 
to agentic workflows and document Q&A systems.

## Modules

| Folder | What it covers |
|---|---|
| `RAG/` | Retrieval-Augmented Generation pipelines with Chroma vector store |
| `Agents/` | LangChain agents with tool use and ReAct reasoning |
| `groq/` | Fast inference using Groq-hosted LLMs |
| `huggingface/` | Open-source models via HuggingFace |
| `objectbox/` | Document Q&A using ObjectBox as the vector database |
| `API/` | Working with LangChain's core API abstractions |

## Tech Stack

| Component | Technology |
|---|---|
| Framework | LangChain |
| LLMs | OpenAI GPT, Groq (Llama3), HuggingFace, Ollama |
| Vector Stores | Chroma, ObjectBox |
| Embeddings | OpenAI Embeddings |
| Interface | Jupyter Notebooks, Streamlit |
| Language | Python |

## Key Concepts Covered

- RAG pipeline design (chunking, embedding, retrieval, generation)
- Agentic workflows with dynamic tool selection
- Switching between local and cloud-hosted LLMs
- Document Q&A with multiple vector database backends
- Prompt engineering and chain composition
