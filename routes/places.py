from fastapi import APIRouter, Query
from define.objects import PlaceModel
from utils.data_config import create_actual_config
from data.database import get_lines
from utils.consts import PATH_TO_PLACES_DATA
from typing import Literal

config = create_actual_config()
places_router = APIRouter()

@places_router.get('/places/list')
async def get_list(count: int = Query(1, gt=0, le=config.count_of_places)):
    lines = get_lines(PATH_TO_PLACES_DATA) 
    result = []
    for i, line in enumerate(lines):
        result.append(line) 
        if count <= i:
            break
    return result

@places_router.get('/places/filter')
async def get_filter(param: Literal['title','type','rate'] = Query("rate"), value: int | str = Query(5), count: int = Query(1, gt=0, le=config.count_of_places)):
    result = []
    for line in get_lines(PATH_TO_PLACES_DATA):
        if line.get(param) == value:
            result.append(line)
        if count == len(result):
            break
    return result

@places_router.get('/places/filter-price')
async def get_filter_price(op: Literal['ge', 'le'] = Query('le'), value: int | float = Query(0), count: int = Query(1, gt=0, le=config.count_of_places)):
    ops = {'ge':lambda x, y: x >= y, 'le':lambda x, y: x <= y}
    result = []
    for line in get_lines(PATH_TO_PLACES_DATA):
        place = PlaceModel(**line)
        if ops[op](place, value):
            result.append(place.__dict__)
            if len(result) == count:
                break
    return result