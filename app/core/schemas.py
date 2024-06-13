from pydantic import BaseModel
from datetime import datetime


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
    value: int | None
    unit: str | None
    created: datetime | None
    supermarket_id: int
    category_id: int