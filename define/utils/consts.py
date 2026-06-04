from enum import Enum
from pydantic import BaseModel
from typing import Literal
from define.utils.data_config import create_actual_config

config = create_actual_config()

PATH_TO_EMBEDDINGS = 'data/{category}/embeddings.pkl'

PATH_TO_DATA = 'data/{category}/{category}.jsonl'

class Category(str, Enum):
    hotels = 'hotels'
    places = 'places'

class FilterParams(BaseModel):
    param: str
    op: Literal['eq', 'neq', 'ge', 'le']
    val: int | float | bool

limit_args = dict(default=1, gt=0)