from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, Body, Path

from app.core.db import Session
from app.core.schemas import Response, Product
from app.api.services.products import ProductService


router = APIRouter()

@router.get("/all", response_model=Response)
async def get_products():
    db = Session()
    result = ProductService(db).get_products()
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Products list', 'data':jsonable_encoder(result)})


@router.get("/{id}", response_model=Response)
async def get_product_by_id(id: int = Path()):
    db = Session()
    result = ProductService(db).get_product_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'status_code': 404, 'message': 'Product not found', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Get product success', 'data':jsonable_encoder(result)})


@router.post('/', response_model=Response)
async def create_product(product: Product = Body()):
    db = Session()
    message, isCreated = ProductService(db).create_product(product)
    if isCreated:
        return JSONResponse(status_code=201, content={'status_code': 201, 'message': message, 'data':jsonable_encoder(product)})
    return JSONResponse(status_code=404, content={'status_code': 404, 'message': message, 'data':jsonable_encoder(product)})


@router.put('/{id}')
async def update_product(id: int = Path(), product: Product = Body()):
    db = Session()
    result = ProductService(db).update_product(id, product)
    if not result:
        return JSONResponse(status_code=404, content={'status_code': 404, 'message': 'Not found product'})
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Product updated'})


@router.delete('/{id}')
async def delete_product(id: int = Path()):
    db = Session()
    isDeleted, product = ProductService(db).delete_product(id)
    if not product:
        return JSONResponse(status_code=404, content={'status_code': 404, 'message': 'Not found product', 'data':jsonable_encoder(product)})
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Product deleted', 'data':jsonable_encoder(product)})