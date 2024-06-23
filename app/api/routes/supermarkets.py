from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Query, Depends, Body, Path

from app.core.db import Session
from app.core.schemas import Response
from app.api.services.supermarkets import SupermarketService


router = APIRouter()

@router.get('/all', response_model=Response)
async def get_supermarkets():
    db = Session()
    result = SupermarketService(db).get_supermarkets()
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Supermarkets list', 'data':jsonable_encoder(result)})


@router.get('/{id}', response_model=Response)
async def get_supermarket_by_id(id: int = Path()):
    db = Session()
    result = SupermarketService(db).get_supermarket_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'status_code': 404, 'message': 'Not found Supermarket', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Get Supermarket success', 'data':jsonable_encoder(result)})


@router.post('', response_model=Response)
async def create_supermarket(name: str = Body()):
    db = Session()
    SupermarketService(db).create_supermarket(name)
    return JSONResponse(status_code=201, content={'status_code': 201, 'message': 'Supermarket created', 'data': jsonable_encoder(name)})


@router.put('/{id}')
async def update_supermarket(id: int = Path(), name: str = Body()):
    db = Session()
    isUpdated, supermarket = SupermarketService(db).update_supermarket(id, name)
    if not supermarket:
        return JSONResponse(status_code=404, content={'status_code': 404, 'message': 'Not found supermarket', 'data': jsonable_encoder(supermarket)})
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Supermarked updated', 'data': jsonable_encoder(supermarket)})


@router.delete('/{id}')
async def delete_supermarket(id: int = Path()):
    db = Session()
    isDeleted, supermarket = SupermarketService(db).delete_supermarket(id)
    if not supermarket:
        return JSONResponse(status_code=404, content={'status_code': 404, 'message': 'Not found supermarket', 'data': jsonable_encoder(supermarket)})
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Supermarked deleted', 'data': jsonable_encoder(supermarket)})