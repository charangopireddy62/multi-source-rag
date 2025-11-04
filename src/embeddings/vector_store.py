import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle, os

class VectorStore:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.vectors = None
        self.chunks = None

    def build(self, chunks):
        """Build FAISS index from text chunks."""
        self.chunks = chunks
        embeddings = self.model.encode(chunks)
        embeddings = np.array(embeddings).astype("float32")
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)
        self.vectors = embeddings

    def save(self, path="data/faiss_index"):
        os.makedirs(path, exist_ok=True)
        faiss.write_index(self.index, f"{path}/index.faiss")
        with open(f"{path}/chunks.pkl", "wb") as f:
            pickle.dump(self.chunks, f)

    def load(self, path="data/faiss_index"):
        self.index = faiss.read_index(f"{path}/index.faiss")
        with open(f"{path}/chunks.pkl", "rb") as f:
            self.chunks = pickle.load(f)

    def search(self, query, top_k=3):
        query_vec = self.model.encode([query])
        query_vec = np.array(query_vec).astype("float32")
        D, I = self.index.search(query_vec, top_k)
        results = [self.chunks[i] for i in I[0]]
        return results
