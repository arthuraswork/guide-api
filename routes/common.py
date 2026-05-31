from fastapi import APIRouter, Query, HTTPException, Depends
from pydantic import BaseModel
from enum import Enum
from utils.consts import PATH_TO_DATA
from define.objects import LocalModel, models
from data.database import get_lines
from typing import Literal


router = APIRouter()

class Category(str, Enum):
    hotels = 'hotels'
    places = 'places'

@router.get('/common/{category}/list')
def get_list(category: Category, limit: int = Query(1)): 
    result = []
    for line in get_lines(PATH_TO_DATA.replace('{category}', category)):
        result.append(line) 
        if limit == len(result):
            break          
    return result

class FilterParams(BaseModel):
    param: str
    op: Literal['eq', 'neq', 'ge', 'le']
    val: int | float | bool

@router.get('/common/{category}/filter')
def get_list(
    category: Category,
    params: FilterParams = Depends(),
    limit: int = Query(1)
             ): 
    result = []
    for line in get_lines(PATH_TO_DATA.replace('{category}', category)):
        obj: LocalModel = models[category](**line)
        if obj.filter(params.param, params.op, params.val):
            result.append(obj)
        if len(result) == limit:
            return result
    return result
