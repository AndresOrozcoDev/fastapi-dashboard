from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.core.db import Session
from app.api.services.products import ProductService

router = APIRouter()

@router.get("/")
def read_products():
    db = Session()
    result = ProductService(db).get_products()
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Products list', 'data':jsonable_encoder(result)})