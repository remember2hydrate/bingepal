# schemas

from pydantic import BaseModel
from typing import Optional

class SearchResult(BaseModel):
    id: str
    title: str
    type: str                    # movie, series, anime, etc.
    description: Optional[str]
    poster_url: Optional[str]
    year: Optional[int]
    source: str                  # e.g., "tmdb", "anilist"
    total_episodes: Optional[int] = None
    total_seasons: Optional[int] = None
    average_duration: Optional[int] = None  # in minutes