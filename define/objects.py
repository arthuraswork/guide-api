from pydantic import BaseModel, Field
from enum import Enum



class LocalModel:
    ...

    def filter(self, param: str, op: str, val: any): 
        if param in self.__dict__:
            return ops[op](getattr(self, param), val)
        raise KeyError()


class MealPlan(Enum):

    RO = "RO"  
    BB = "BB"  
    HB = "HB"  
    FB = "FB"  
    AI = "AI"  

class PlaceModel(BaseModel, LocalModel):
    title: str = Field(min_length= 1, max_length= 31)
    description: str = Field(min_length= 8, max_length= 255)
    type: str

    rate: int = Field(ge=0, le=5)
    price: int = Field(ge=0)

    lat: float = Field(ge=-90, le=90)
    lon: float = Field(ge=-180, le=180)



class HotelModel(BaseModel, LocalModel):
    title: str = Field(min_length=1, max_length=31)
    description: str = Field(min_length=8, max_length=255)
    type: str

    rate: int = Field(ge=0, le=5)
    price: int = Field(ge=0)

    meal_plan: MealPlan = Field(MealPlan.RO)
    beach_access: bool = Field(False)
    pool: bool = Field(False)
    spa: bool = Field(False)

    lat: float = Field(ge=-90, le=90)
    lon: float = Field(ge=-180, le=180)

    

models = {
    'places': PlaceModel,
    'hotels': HotelModel
} 



ops = {
    'eq': lambda x, y: x == y,
    'neq': lambda x, y: x != y,
    'ge': lambda x, y: x >= y,
    'le': lambda x, y: x <= y,
}