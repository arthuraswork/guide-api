from pydantic import BaseModel, Field

class PlaceModel(BaseModel):
    title: str = Field(min_length= 1, max_length= 31)
    description: str = Field(min_length= 8, max_length= 255)
    type: str

    rate: int = Field(ge=0, le=5)
    price: int = Field(ge=0)

    lat: float = Field(ge=-90, le=90)
    lon: float = Field(ge=-180, le=180)

    def __ge__(self, value):
        if self.price >= value:
            return True
        return False

    def __le__(self, value):
        return self.price <= value

    def as_html(self):
        return f"""
<h1>{self.title}</h1>
<p> {self.description}</p>
"""