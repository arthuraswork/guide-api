from fastapi import APIRouter, Query, HTTPException, Depends
from utils.consts import PATH_TO_DATA, Category, FilterParams, limit_args
from define.objects import LocalModel, models
from data.data_manager import get_lines
from sentence_compr import search_by_sentence

router = APIRouter()

@router.get('/{category}/list')
async def get_list(
    category: Category, 
    limit: int = Query(**limit_args)
    ) -> list : 
    result = []
    for line in get_lines(PATH_TO_DATA.replace('{category}', category)):
        result.append(line) 
        if limit == len(result):
            break          
    return result


@router.get('/{category}/filter')
async def get_filter(
    category: Category,
    params: FilterParams = Depends(),
    limit: int = Query(**limit_args) 
             ) -> list: 
    result = []
    for line in get_lines(PATH_TO_DATA.replace('{category}', category)):
        obj: LocalModel = models[category](**line)
        if obj.filter(params.param, params.op, params.val):
            result.append(obj)
        if len(result) == limit:
            return result
    return result


@router.get('/{category}/sentence')
def get_search_sentence(category: Category, query: str = Query(max_length=64), limit: int = Query(3)):
    return search_by_sentence.models[category].input(query, limit)


