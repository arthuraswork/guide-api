from sentence_transformers import SentenceTransformer
#from sklearn.metrics.pairwise import cosine_similarity
import json 
import pickle
from utils.consts import PATH_TO_PLACES_DATA, PATH_TO_PLACES_EMBEDDINGS

model = SentenceTransformer('cointegrated/rubert-tiny2')
objects = []
with open(PATH_TO_PLACES_DATA, 'r', encoding='utf-8') as f:
    for o in f:
         objects.append(json.loads(o))

embedds = []

for obj in objects:
    text = f"{obj['title']} {obj['type']}: {obj['description']}"
    embedd = model.encode(text, normalize_embeddings=True)
    embedds.append({'title': obj['title'], 'embedding':embedd})

with open(PATH_TO_PLACES_EMBEDDINGS, 'wb') as f:
    pickle.dump(embedds, f)