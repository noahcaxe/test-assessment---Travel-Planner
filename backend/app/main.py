from fastapi import FastAPI
from app.core.middleware.error_handler import error_handler
from app.api.test import router as test_router

app = FastAPI() #lifespan=lifespan



@app.middleware("http")
async def global_error_middleware(request, call_next):
    return await error_handler(request, call_next)
