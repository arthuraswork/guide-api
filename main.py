from fastapi import FastAPI
from routes.places import places_router
app = FastAPI(title='coco-api')

app.include_router(places_router)

@app.get('/')
def api_map():
    return {
        "/": "map of API",
        "/help":"~in work~",
        "/places":
            {
                "/list": "list (count) of places, use ?count=(0 -gt int -le count(places))",
                "/filter": "list of filter by ?params and ?value: [title, type: str, rate: int] and ?count",
                "sentence": "~in work~"
            }
    }