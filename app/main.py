from fastapi import FastAPI
from app.api.routes import router
from app.core.database import init_db

init_db()

app = FastAPI(title="AI Multi-Agent Data Analyst")

app.include_router(router)