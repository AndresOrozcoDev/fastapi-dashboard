from pydantic import BaseModel
from typing import Optional
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
    value: Optional[int]
    unit: Optional[str]
    created: Optional[str]
    supermarket_id: int
    category_id: int