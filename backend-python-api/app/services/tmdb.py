# movie + series handler

import os
import httpx
from app.utils.logger import logger
from dotenv import load_dotenv
from app.models import SearchResult

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3/search"

async def search(query: str, type: str) -> list[SearchResult]:
    endpoint = "movie" if type == "movie" else "tv"
    url = f"{BASE_URL}/{endpoint}"
    params = {"api_key": API_KEY, "query": query}
    
    logger.info(f"[TMDb] Searching '{query}' as type '{type}'")

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
    except Exception as e:
        logger.error(f"[TMDb] API error: {e}")
        return []

    results = []
    for item in data.get("results", [])[:10]:
        year_raw = item.get("release_date") or item.get("first_air_date")
        year = int(year_raw[:4]) if year_raw else None
        genres = [str(g) for g in item.get("genre_ids", [])]  # not names in search
        results.append(SearchResult(
            id=str(item["id"]),
            title=item.get("title") or item.get("name") or "Unknown Title",
            type=type,
            description=item.get("overview") or "No description available.",
            poster_url=f"https://image.tmdb.org/t/p/w500{item['poster_path']}" if item.get("poster_path") else None,
            year=(item.get("release_date") or item.get("first_air_date") or "")[:4],
            source="tmdb",
            genres=genres,
            rating=item.get("vote_average"),
            rating_count=item.get("vote_count"),
            total_seasons=None,
            total_episodes=None,
            average_duration=None
        ))
    return results