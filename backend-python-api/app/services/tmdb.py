# movie + series handler

import os
import httpx
from dotenv import load_dotenv
from app.models import SearchResult

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3/search"

async def search(query: str, type: str) -> list[SearchResult]:
    endpoint = "movie" if type == "movie" else "tv"
    url = f"{BASE_URL}/{endpoint}"
    params = {"api_key": API_KEY, "query": query}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        data = response.json()

    results = []
    for item in data.get("results", [])[:10]:
        results.append(SearchResult(
            id=str(item["id"]),
            title=item.get("title") or item.get("name"),
            type=type,
            description=item.get("overview"),
            poster_url=f"https://image.tmdb.org/t/p/w500{item.get('poster_path')}" if item.get("poster_path") else None,
            year=(item.get("release_date") or item.get("first_air_date") or "")[:4],
            source="tmdb",
            total_seasons=item.get("number_of_seasons"),  # May not exist in search results
            total_episodes=None,  # Fill via `/episodes` endpoint
            average_duration=None  # Not available in TMDb search response
        ))

    return results