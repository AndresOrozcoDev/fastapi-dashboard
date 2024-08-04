import uvicorn, multiprocessing

from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware

from app.api.main import api_router
from app.core.db import engine, Base
from app.rabbitmq.subscriber import consume_messages
from app.core.starlette.error_handle import ErrorHandler

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:4200"
    # Otros dominios permitidos pueden ir aquí
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello World from FastAPI"}

app.include_router(api_router)
app.add_middleware(ErrorHandler)
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    subscriber_process = multiprocessing.Process(target= consume_messages)
    try:
        subscriber_process.start()
        uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
    except KeyboardInterrupt:
        pass
    finally:
        subscriber_process.terminate()
        subscriber_process.join()
