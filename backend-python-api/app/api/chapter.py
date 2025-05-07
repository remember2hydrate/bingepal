from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from app.services import tmdb, anilist, mangadex

router = APIRouter()


class ChapterOut(BaseModel):
    season: Optional[int] = None  # only for series/anime
    number: int
    title: str
    air_date: Optional[str] = None


@router.get("/chapter", response_model=List[ChapterOut])
async def get_chapters(type: str = Query(...), id: str = Query(...)):
    type = type.lower()

    try:
        if type == "series":
            return await tmdb.get_episodes(id)
        elif type == "anime":
            return await anilist.get_episodes(id)
        elif type == "manga":
            return await mangadex.get_chapters(id)
        else:
            raise HTTPException(status_code=400, detail="Invalid media type")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch chapters: {str(e)}")
