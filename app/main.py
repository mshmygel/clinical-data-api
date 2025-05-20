from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Clinical Data API")

app.include_router(router)

