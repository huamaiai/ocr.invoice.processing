# backend/vector_search/index.py

import faiss
import numpy as np
import os

def build_faiss_index(embeddings: np.ndarray) -> faiss.IndexFlatL2:
    """
    Build a FAISS index from the given embeddings.
    """
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index

def save_index(index: faiss.IndexFlatL2, path: str = "data/faiss_index/catalog_index.faiss") -> None:
    """
    Save the FAISS index to the given file path.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    faiss.write_index(index, path)

def load_index(path: str = "data/faiss_index/catalog_index.faiss") -> faiss.IndexFlatL2:
    """
    Load the FAISS index from the given file path.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"FAISS index not found at {path}")
    return faiss.read_index(path)
