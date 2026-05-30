from fastapi import APIRouter, Query
from utils.consts import PATH_TO_HOTELS_DATA, PATH_TO_HOTELS_EMBEDDINGS
from utils.data_config import create_actual_config
from data.database import get_lines

config = create_actual_config()

hotels_router = APIRouter()

@hotels_router.get('/hotels/list')
async def get_list(count: int = Query(1, gt=0, le=config.count_of_hotels)):
    lines = get_lines(PATH_TO_HOTELS_DATA) 
    result = []
    for i, line in enumerate(lines):
        result.append(line) 
        if count <= i:
            break
    return result
