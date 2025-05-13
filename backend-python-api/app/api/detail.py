from fastapi import APIRouter, Query, HTTPException
from app.models import SearchResult
from app.services import tmdb, anilist, rawg, openlibrary, mangadex
from slowapi import Limiter
from slowapi.util import get_remote_address
from app.utils.limiter import limiter
from app.utils.request_log import log_request

router = APIRouter()

@router.get("/detail", response_model=SearchResult)
async def get_detail(id: str = Query(...), type: str = Query(...)):
    type = type.lower()
    await log_request(request)
    try:
        if type == "movie" or type == "series":
            return await tmdb.get_detail(id, type)
        elif type == "anime":
            return await anilist.get_detail(id)
        elif type == "game":
            return await rawg.get_detail(id)
        elif type == "book":
            return await openlibrary.get_detail(id)
        elif type == "manga":
            return await mangadex.get_detail(id)
        else:
            raise HTTPException(status_code=400, detail="Invalid media type")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch detail: {str(e)}")
