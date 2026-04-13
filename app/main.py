from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Multi-Agent Data Analyst")

app.include_router(router)