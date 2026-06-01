from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from routes.common import router
app = FastAPI(title='guide-api')

app.include_router(router)


@app.get('/')
async def api_map():
    return {
        "/": "map of API",
        ['hotels','places']:
            {
                "/list": "list of places ?limit: int",
                "/filter": "list of filter by ?param: str, ?op: str, ?value: any ",
                "/sentence": "list of N most similar objects by user query ?query str ?k: int)" 
            }
    }


@app.exception_handler(404)
async def redir_on_404(request: Request, exc):
    return RedirectResponse(url='/')