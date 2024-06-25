import os

from dotenv import load_dotenv
from fastapi import HTTPException, Header
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyHeader
from app.core.schemas import Response


async def validate_api_key(API_KEY: str = Header(alias="API_KEY")):
    load_dotenv()
    if API_KEY != os.getenv('API_KEY'):
        raise HTTPException(status_code = 400, detail = "API Key inválida")
