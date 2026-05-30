from fastapi import APIRouter, Query
from sentence_compr import search_place


sentence_router = APIRouter()

@sentence_router.get('/sentence/places')
async def get_search_place(query: str = Query(), k: int = Query(3)):
    return search_place(query, k)