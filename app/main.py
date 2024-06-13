from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware

from app.api.main import api_router
from app.core.db import engine, Base
from app.core.starlette.error_handle import ErrorHandler

app = FastAPI()

origins = [
    "https://frontend-angular.azurewebsites.net",
    "http://localhost:4200",
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
    return {"Hello": "World"}

app.include_router(api_router)
app.add_middleware(ErrorHandler)
Base.metadata.create_all(bind=engine)