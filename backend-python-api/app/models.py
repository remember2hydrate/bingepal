# schemas

from pydantic import BaseModel
from typing import Optional, List

class SearchResult(BaseModel):
    id: str
    title: str
    type: str  # movie, series, anime, game, book, manga
    description: Optional[str]
    poster_url: Optional[str]
    year: Optional[int]
    source: str

    # Optional enhancements
    genres: Optional[List[str]] = None
    rating: Optional[float] = None
    rating_count: Optional[int] = None
    total_seasons: Optional[int] = None
    total_episodes: Optional[int] = None
    average_duration: Optional[int] = None