from fastapi import FastAPI
from app.api.search import router as search_router
from app.api.detail import router as detail_router
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from fastapi import FastAPI, Request
from slowapi.errors import RateLimitExceeded
from fastapi.middleware.cors import CORSMiddleware
from app.models.db import Base, engine
from app.api.chapter import router as chapter_router

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="BingePal API",
    description="API for movies, anime, tv series, games and books",
    version="0.1.0"
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# https://www.youtube.com/watch?v=lFTNS_QStTs
app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later sth like allow_origins=["https://admin.bingepal.com", "https://app.bingepal.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(search_router, prefix="/api")
app.include_router(detail_router, prefix="/api")
app.include_router(chapter_router, prefix="/api")


#@app.get("/health")
#def health_check():
#    return {"status": "ok", "message": "BingePal API is alive"}