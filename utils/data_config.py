import json
from .config import DataConfig

PATH_TO_DATA_CONFIG = 'utils/data_config.json'

def read_config():
    with open(PATH_TO_DATA_CONFIG, 'r', encoding='utf-8') as f:
        configs = json.load(f)
        return configs
    
def create_actual_config():
    config  = read_config()
    obj = DataConfig(
        config['places']['count'],
        config['hotels']['count']
    )
    return obj