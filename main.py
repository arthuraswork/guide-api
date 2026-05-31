from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from routes.common import router
app = FastAPI(title='guide-api')

app.include_router(router)


@app.get('/')
def api_map():
    return {
        "/": "map of API",
        "/help":"~in work~",
        "/places":
            {
                "/list": "list (count) of places, use ?count=(0 -gt int -le count(places))",
                "/filter": "list of filter by ?params and ?value: [title, type: str, rate: int] and ?count",
            },
        "/sentence":
        {
           "/places": "list of N most similar objects by user query ?query=(str))" 
        },
        "/hotels": {
            "/list": "list (count) of hotels, use ?count=(0 -gt int -le count(places))",
        }
    }


@app.exception_handler(404)
async def redir_on_404(request: Request, exc):
    return RedirectResponse(url='/')