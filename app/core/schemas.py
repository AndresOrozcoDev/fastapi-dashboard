from pydantic import BaseModel


class Response(BaseModel):
    status_code: int
    message: str
    data: list

class Supermarket(BaseModel):
    name: str

class Category(BaseModel):
    name: str

class Product(BaseModel):
    name: str
    price: int
    value: int
    unit: str
    supermarket_id: int
    category_id: int