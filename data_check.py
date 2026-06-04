from utils.data_config import PATH_TO_DATA_CONFIG
import json
import os
import sys

def check_data_files():
    with open(PATH_TO_DATA_CONFIG, 'r') as f:
        for dir in json.load(f):
            path = f'data/{dir}/{dir}.jsonl'
            if not os.path.exists(path):
                raise FileNotFoundError(
                    f'{path} not exists; fix config or add files'
                )


try:
    check_data_files()
except FileNotFoundError as e:
    print(e)
    sys.exit(1)    