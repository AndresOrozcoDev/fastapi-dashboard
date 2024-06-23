from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Query, Depends, Body, Path

from app.core.db import Session
from app.core.schemas import Response
from app.api.services.categories import CategoriesService


router = APIRouter()

@router.get('/all', response_model=Response)
async def get_categories():
    db = Session()
    result = CategoriesService(db).get_categories()
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Categories list', 'data':jsonable_encoder(result)})


@router.get('/{id}', response_model=Response)
async def get_category_by_id(id: int = Path()):
    db = Session()
    result = CategoriesService(db).get_category_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'status_code': 404, 'message': 'Not found category', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Get category success', 'data':jsonable_encoder(result)})


@router.post('', response_model=Response)
async def create_category(name: str = Body()):
    db = Session()
    CategoriesService(db).create_category(name)
    return JSONResponse(status_code=201, content={'status_code': 201, 'message': 'Category created', 'data': jsonable_encoder(name)})


@router.put('/{id}')
async def update_category(id: int = Path(), name: str = Body()):
    db = Session()
    isUpdated, category = CategoriesService(db).update_category(id, name)
    if not category:
        return JSONResponse(status_code=404, content={'status_code': 404, 'message': 'Not found category', 'data': jsonable_encoder(category)})
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Supermarked updated', 'data': jsonable_encoder(category)})


@router.delete('/{id}')
async def delete_category(id: int = Path()):
    db = Session()
    isDeleted, category = CategoriesService(db).delete_category(id)
    if not category:
        return JSONResponse(status_code=404, content={'status_code': 404, 'message': 'Not found category', 'data': jsonable_encoder(category)})
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Supermarked deleted', 'data': jsonable_encoder(category)})