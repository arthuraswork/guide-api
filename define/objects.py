from pydantic import BaseModel, Field
from enum import Enum

class MealPlan(Enum):

    RO = "RO"  
    BB = "BB"  
    HB = "HB"  
    FB = "FB"  
    AI = "AI"  

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

class HotelModel(BaseModel):
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