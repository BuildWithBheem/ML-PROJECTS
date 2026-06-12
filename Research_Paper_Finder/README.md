# 🔍 Research Paper Recommender System

> A lightweight ML-powered system to discover relevant academic papers using NLP — built as a learning experiment to explore information retrieval concepts hands-on.
> *Results are based on a limited dataset and simple similarity metrics; treat this as a sandbox, not a research tool.*

---

## 📌 Overview

The system uses **TF-IDF vectorization** and **Cosine Similarity** to match a user's search query against a database of research paper abstracts. Abstracts go through text cleaning, normalization, and stemming before being converted into numerical vectors. The query follows the same pipeline, and the closest matches are ranked and returned.

A simple **Streamlit** frontend lets you type a topic, browse results, and read abstracts — all in one place.

---

## ✨ Features

- 🔎 Natural language search over research paper abstracts
- 📊 TF-IDF based document representation
- 📐 Cosine similarity powered recommendation engine
- 🏆 Top-K relevant paper retrieval
- 🖥️ Interactive Streamlit frontend
- 📄 Inline abstract viewing from search results
- ⚡ Fast and lightweight — no heavy dependencies

---

## 🛠️ Tech Stack

| Tools |
|---|
| Python |
| Pandas, NumPy |
| Scikit-learn, NLTK |
| Streamlit |
| Joblib |

---

## ⚙️ Methodology

1. Research paper abstracts are collected and preprocessed
2. Text is cleaned, tokenized, and stemmed via NLTK
3. TF-IDF vectorization converts text into numerical vectors
4. User query is transformed using the same fitted vectorizer
5. Cosine similarity is computed between the query and all papers
6. Top-K most relevant papers are ranked and displayed

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/your-username/research-paper-recommender.git
cd research-paper-recommender

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 🔭 Future Improvements

- 🤖 AI-generated paper summaries
- 🌐 FastAPI backend integration
- 🧠 Local LLM support via Ollama
- 🔡 Semantic search using sentence embeddings
- 🗂️ FAISS-based vector retrieval
- 📚 Retrieval-Augmented Generation (RAG) pipeline
- 💬 Research paper chat assistant

---
