from fastapi import FastAPI
from core.endpoints.endpoints import router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("INFO:     Uvicorn running on http://127.0.0.1:8000/api/data/ (Press CTRL+C to quit)")

app.include_router(router)
