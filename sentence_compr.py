from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 
import pickle
from utils.consts import PATH_TO_PLACES_EMBEDDINGS

model = SentenceTransformer('cointegrated/rubert-tiny2')

with open(PATH_TO_PLACES_EMBEDDINGS, 'rb') as f:
    corpus = pickle.load(f)

matrix = np.vstack([i['embedding'] for i in corpus])

def search(query, k=3):
    embedd = model.encode(query)
    sims = []
    for i, m in enumerate(matrix):
        sims.append((corpus[i]['title'], cosine_similarity([m], [embedd])))
    sorted_m = sorted(sims, reverse=True, key=lambda x: x[1])[:k]
    return [n[0] for n in sorted_m]

