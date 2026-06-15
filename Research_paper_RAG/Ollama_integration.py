import ollama
from sentence_transformers import SentenceTransformer
import joblib as jb
import faiss

df = jb.load("Papers")
faiss_indexes = faiss.read_index("Faiss_indexes")
embed = SentenceTransformer('all-MiniLM-L6-v2')
query = "Explain What is Depth Estimation "

query_emb = embed.encode([query])
query_emb = query_emb.astype('float32')

Distances, faiss_index = faiss_indexes.search(query_emb,3)
paper1 = df.iloc[faiss_index[0,0]]
paper2 = df.iloc[faiss_index[0,1]]
paper3 = df.iloc[faiss_index[0,2]]

prompt = f"answer the user {query} concisely, with the context of {paper1},{paper2},{paper3}"
ai_summary = ollama.chat(
    model = 'qwen3:4b',
    messages= [
        {"role":"system", "content":"You are a research paper assistant Do not reveal reasoning.Do not explain your thought process.Return only the final answer. Maximum 150 words."},
        {"role":"user","content":prompt}
    ]
)

result = ai_summary["message"]["content"]

print(result)