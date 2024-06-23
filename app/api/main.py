from fastapi import APIRouter, Depends

from app.core.starlette.auth_key import validate_api_key
from app.api.routes import users, products, categories, supermarkets


api_router = APIRouter()

api_router.include_router(products.router, prefix="/api/product", tags=["products"], dependencies=[Depends(validate_api_key)])
api_router.include_router(supermarkets.router, prefix="/api/supermarket", tags=["supermarkets"], dependencies=[Depends(validate_api_key)])
api_router.include_router(categories.router, prefix="/api/category", tags=["categories"], dependencies=[Depends(validate_api_key)])
api_router.include_router(users.router, prefix="/api/user", tags=["users"], dependencies=[Depends(validate_api_key)])