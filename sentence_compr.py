from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 
import pickle
from utils.consts import PATH_TO_PLACES_EMBEDDINGS

def sentence_vars():
    """
    load corpus and module 
    """
    model = SentenceTransformer('cointegrated/rubert-tiny2')
    with open(PATH_TO_PLACES_EMBEDDINGS, 'rb') as f:
        corpus = pickle.load(f)
    matrix = np.vstack([i['embedding'] for i in corpus])
    return model, corpus, matrix

def search_place(query: str, k: int) -> list[dict]:
    """
    search by user query
    """
    embedd = model.encode(query).reshape(1,-1)
    sims = cosine_similarity(matrix, embedd).flatten()
    sorted_vecs = np.argsort(sims)[-k:][::-1]
    return [corpus[i]['object'] for i in sorted_vecs]

model, corpus, matrix = sentence_vars()


