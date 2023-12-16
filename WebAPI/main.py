from fastapi import FastAPI
from core.endpoints.endpoints import router

app = FastAPI()

app.include_router(router)
