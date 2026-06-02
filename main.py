from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from routes.common import router
from utils.data_config import count_config_actualisation
from utils.logger import info, warning


app = FastAPI(title='guide-api')

app.include_router(router)

count_config_actualisation()

@app.middleware('http')
async def request_logger(request: Request, call_next):
    try:
        response = await call_next(request)
        if response.status_code == 200:
            info(f"TO {request.url.path} FROM {request.client.host} AS {request.method} WITH {response.status_code}")
        else:
            warning(f"TO {request.url.path} FROM {request.client.host} AS {request.method} WITH {response.status_code}")
        return response
    except Exception as e:
        warning(f"TO {request.url.path} FROM {request.client.host} AS exception EXCEPTION {e}")
        raise

@app.get('/')
async def api_map():
    return {
        "/": "map of API",
        "hotels, places":
            {
                "/list": "list of places ?limit: int",
                "/filter": "list of filter by ?param: str, ?op: str, ?value: any ",
                "/sentence": "list of N most similar objects by user query ?query str ?k: int)" 
            }
    }

@app.exception_handler(404)
async def redir_on_404(request: Request, exc):
    return RedirectResponse(url='/')