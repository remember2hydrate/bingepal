# games handler

from app.utils.logger import logger
import os
import httpx
from dotenv import load_dotenv
from app.models import SearchResult
from app.utils.logger import logger

load_dotenv()

API_KEY = os.getenv("RAWG_API_KEY")
BASE_URL = "https://api.rawg.io/api/games"

async def search(query: str) -> list[SearchResult]:
    logger.info(f"[RAWG] Searching '{query}'")

    params = {
        "key": API_KEY,
        "search": query,
        "page_size": 10
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
    except Exception as e:
        logger.error(f"[RAWG] API error: {e}")
        return []

    results = []
    for item in data.get("results", []):
        results.append(SearchResult(
            id=str(item["id"]),
            title=item.get("name"),
            type="game",
            description=None,  # RAWG doesn't return full desc in search
            poster_url=item["background_image"] if item.get("background_image") else None,
            year=(item.get("released") or "")[:4],
            source="rawg",
            total_seasons=None,
            total_episodes=None,
            average_duration=None
        ))

    return results