from dataclasses import dataclass

@dataclass
class Category:
    title: str
    count: int

@dataclass
class DataConfig:
    category: dict

    def get_list(self):
        return list(self.category.keys())



