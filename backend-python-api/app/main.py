from fastapi import FastAPI
from app.api.search import router as search_router
from app.api.detail import router as detail_router

app = FastAPI(
    title="BingePal API",
    description="API for movies, anime, tv series, games and books",
    version="0.1.0"
)

app.include_router(search_router, prefix="/api")
app.include_router(detail_router, prefix="/api")

#@app.get("/health")
#def health_check():
#    return {"status": "ok", "message": "BingePal API is alive"}