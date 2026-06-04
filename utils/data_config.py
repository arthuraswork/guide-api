import json
from .config import DataConfig, Category

PATH_TO_DATA_CONFIG = 'utils/data_config.json'

def read_config():
    with open(PATH_TO_DATA_CONFIG, 'r', encoding='utf-8') as f:
        configs = json.load(f)
        return configs
    
def create_actual_config():
    config = DataConfig(dict())
    config_json  = read_config()
    for c in config_json:
        cat = Category(c, config_json[c]['count'])
        config.category[c] = cat
    return config

def count_config_actualisation(params = ['places','hotels']):
    configs = read_config()
    for param in params:
        with open(f'data/{param}/{param}.jsonl', 'r') as f:
            count = sum([1 for _ in f])
        configs[param]['count'] = count
        with open('utils/data_config.json', 'w') as f:
            json.dump(configs, f, indent=4)