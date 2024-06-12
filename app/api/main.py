from fastapi import APIRouter

from app.api.routes import products

api_router = APIRouter()
api_router.include_router(products.router, prefix="/api/products", tags=["Products"])