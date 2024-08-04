from fastapi import APIRouter, HTTPException
from app.rabbitmq.publisher import publish_message


router = APIRouter()

@router.post("/send-message/")
async def send_message(message: str):
    try:
        publish_message(message)
        return {"status": "Message sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

