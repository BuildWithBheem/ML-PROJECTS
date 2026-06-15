# 🔍 Academic Research Search & AI Assistant

A Retrieval-Augmented Generation (RAG) application that enables semantic search across research papers and provides AI-generated answers based on the most relevant documents.

## Features

* Semantic search using FAISS and Sentence Transformers
* Retrieval of the most relevant research papers from a vector database
* Context-aware AI responses powered by a local LLM
* FastAPI backend for search and inference APIs
* Streamlit-based interactive web interface
* Fully local deployment with Ollama

## Tech Stack

### Backend

* Python
* FastAPI
* Pydantic

### Search & Retrieval

* FAISS
* Sentence Transformers (`all-MiniLM-L6-v2`)
* Pandas
* Joblib

### AI Model

* Ollama
* Qwen3:4B

### Frontend

* Streamlit
* Custom HTML/CSS

> Note: Parts of the frontend layout and styling were developed with AI-assisted code generation and later customized for project requirements.

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### Install Dependencies

```bash
pip install fastapi uvicorn pydantic sentence-transformers faiss-cpu joblib streamlit requests pandas
```

### Install and Start Ollama

Pull the required model:

```bash
ollama pull qwen3:4b
```

## Running the Application

### Start the Backend

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://localhost:8000
```

### Start the Frontend

```bash
streamlit run app.py
```

Frontend URL:

```text
http://localhost:8501
```

## API Endpoints

### Search Papers

**POST** `/Search`

Request:

```json
{
  "Query": "machine learning for healthcare"
}
```

Returns the most relevant research papers based on semantic similarity.

---

### Research Paper Assistant

**POST** `/research-paper-assistant`

Request:

```json
{
  "Query": "Summarize recent approaches for monocular depth estimation"
}
```

Returns an AI-generated response grounded in the retrieved research papers.

## Future Improvements

* Research paper recommendations
* PDF upload and indexing
* Citation generation
* Multi-turn conversation memory
* Advanced filtering and sorting

## Author

Bhimaraju Sai Koundinya, KIIT CSE(AI/ML)

Built as a practical implementation of Retrieval-Augmented Generation (RAG), semantic search, vector databases, and local LLM deployment.