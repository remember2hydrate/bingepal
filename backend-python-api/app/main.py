from fastapi import FastAPI

app = FastAPI(
    title="BingePal API",
    description="API for movies, anime, tv series, games and books",
    version="0.1.0"
)

app.include_router(search_router, prefix="/api")

    #@app.get("/health")
    #def health_check():
    #    return {"status": "ok", "message": "BingePal API is alive"}