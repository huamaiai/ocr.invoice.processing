# backend/vector_search/embedder.py

from sentence_transformers import SentenceTransformer
from typing import List, Dict
import numpy as np

def get_embedder(model_name: str = "all-MiniLM-L6-v2") -> SentenceTransformer:
    """
    Load and return the SentenceTransformer model.
    """
    return SentenceTransformer(model_name)

def encode_catalog_descriptions(catalog: List[Dict], model: SentenceTransformer) -> np.ndarray:
    """
    Encode item descriptions in the catalog to vector embeddings.
    """
    descriptions = [entry["description"] for entry in catalog]
    return model.encode(descriptions)
