from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle
from utils.consts import PATH_TO_EMBEDDINGS
from utils.data_config import create_actual_config

config = create_actual_config()

class SentenceModel():

    def __init__(self,
        model: SentenceTransformer,
        corpus: any,
        matrix: np.ndarray
        ):

        self.model = model
        self.corpus = corpus
        self.matrix = matrix

    def input(self, query: str, k: int):
        embedd = self.model.encode(query).reshape(1,-1)
        sims = cosine_similarity(self.matrix, embedd).flatten()
        sorted_vecs = np.argsort(sims)[-k:][::-1]
        return self.output(sorted_vecs)
    
    def output(self, vecs):
        return [self.corpus[i]['object'] for i in vecs]

class SentenceMiddleWare:
    def __init__(self, categories: list):
        self.common_model = SentenceTransformer('cointegrated/rubert-tiny2')
        self.models: dict[str, SentenceModel] = dict()
        
        for category in categories:
            path = PATH_TO_EMBEDDINGS.replace("{category}", category)
            with open(path, 'rb') as f:
                corpus = pickle.load(f)
            matrix = np.vstack([c['embedding'] for c in corpus])
            self.models[category] = SentenceModel(self.common_model, corpus, matrix)


            

search_by_sentence = SentenceMiddleWare(
    config.get_list()   
)

