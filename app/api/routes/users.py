from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, Body

from app.core.db import Session
from app.core.schemas import Response
from app.api.services.users import UserService


router = APIRouter()

@router.post("/", response_model=Response)
def send_email(email: str = Body()):
    isSend, message = UserService().send_email(email)
    if isSend:
        return JSONResponse(status_code=200, content={'status_code': 200, 'message': message, 'data':email})
    return JSONResponse(status_code=500, content={'status_code': 500, 'message': message, 'data':email})