from sentence_transformers import SentenceTransformer
import json 
import pickle
from utils.consts import PATH_TO_DATA, PATH_TO_EMBEDDINGS
from utils.data_config import PATH_TO_DATA_CONFIG

model = SentenceTransformer('cointegrated/rubert-tiny2')

def embedding_calc(category: str):
    objects = []
    with open(PATH_TO_DATA.replace('{category}', category), 'r', encoding='utf-8') as f:
        for o in f:
             objects.append(json.loads(o))

    embedds = []
    for obj in objects:
        text = obj['description']
        embedd = model.encode(text, normalize_embeddings=True)
        embedds.append({'title': obj['title'], 'object': obj,'embedding':embedd})

    with open(PATH_TO_EMBEDDINGS.replace('{category}',category), 'wb') as f:
        pickle.dump(embedds, f)


