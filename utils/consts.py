from enum import Enum
from pydantic import BaseModel
from typing import Literal
from utils.data_config import create_actual_config

config = create_actual_config()

PATH_TO_PLACES_DATA = 'data/places/places.jsonl'
PATH_TO_PLACES_EMBEDDINGS = 'data/places/embeddings.pkl'
PATH_TO_EMBEDDINGS = 'data/{category}/embeddings.pkl'

PATH_TO_HOTELS_DATA = 'data/hotels/hotels.jsonl'
PATH_TO_HOTELS_EMBEDDINGS = 'data/hotels/embeddings.pkl'

PATH_TO_DATA = 'data/{category}/{category}.jsonl'

class Category(str, Enum):
    hotels = 'hotels'
    places = 'places'

class FilterParams(BaseModel):
    param: str
    op: Literal['eq', 'neq', 'ge', 'le']
    val: int | float | bool

limit_args = dict(default=1, gt=0, le=config.count_of_places)