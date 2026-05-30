from fastapi import APIRouter, Query
from utils.consts import PATH_TO_HOTELS_DATA, PATH_TO_HOTELS_EMBEDDINGS
from utils.data_config import create_actual_config
from data.database import get_lines
from typing import Literal

config = create_actual_config()

hotels_router = APIRouter()

@hotels_router.get('/hotels/list')
async def get_list(count: int = Query(1, gt=0, le=config.count_of_hotels)):
    lines = get_lines(PATH_TO_HOTELS_DATA) 
    result = []
    for line in lines:
        result.append(line) 
        if count == len(result):
            break          
    return result

@hotels_router.get('/hotels/filter')
async def get_filter(param: Literal['title','type','rate'] = Query("rate"), value: int | str = Query(5), count: int = Query(1, gt=0, le=config.count_of_places)):
    result = []
    for line in get_lines(PATH_TO_PLACES_DATA):
        if line.get(param) == value:
            result.append(line)
        if count == len(result):
            break
    return result
