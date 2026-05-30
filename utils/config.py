from dataclasses import dataclass

@dataclass
class DataConfig:
    __count_of_places: int
    __count_of_hotels: int

    @property
    def count_of_places(self) -> str:
        return self.__count_of_places
    
    @count_of_places.setter
    def set_count_of_places(self, new_count: int):
        self.__count_of_places = new_count

    @property
    def count_of_hotels(self) -> str:
        return self.__count_of_hotels
    
    @count_of_hotels.setter
    def count_of_hotels(self, new_count: int):
        self.__count_of_hotels = new_count




