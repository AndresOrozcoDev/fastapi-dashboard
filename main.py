from fastapi import FastAPI
from fastapi.routing import APIRoute

from app.api.main import api_router
from app.core.db import engine, Base

app = FastAPI()

origins = [
    "https://frontend-angular.azurewebsites.net",
    "http://localhost:4200",
    # Otros dominios permitidos pueden ir aquí
]

# app.add_middleware(
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(api_router)
Base.metadata.create_all(bind=engine)