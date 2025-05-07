# book handler

import httpx
from app.models import SearchResult
from app.utils.logger import logger

BASE_URL = "https://openlibrary.org/search.json"

async def search(query: str) -> list[SearchResult]:
    logger.info(f"[OpenLibrary] Searching '{query}'")

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(BASE_URL, params={"q": query})
            response.raise_for_status()
            data = response.json()
    except Exception as e:
        logger.error(f"[OpenLibrary] API error: {e}")
        return []

    results = []
    for item in data.get("docs", [])[:10]:
        results.append(SearchResult(
            id=item.get("key", "").replace("/works/", ""),
            title=item.get("title") or "Unknown Title",
            type="book",
            description=", ".join(item.get("author_name", [])[:3]) if item.get("author_name") else "No author listed.",
            poster_url=f"https://covers.openlibrary.org/b/olid/{item['cover_edition_key']}-L.jpg" if item.get("cover_edition_key") else None,
            year=item.get("first_publish_year"),
            source="openlibrary",
            genres=item.get("subject", [])[:5] if item.get("subject") else None,
            rating=None,
            rating_count=None,
            total_seasons=None,
            total_episodes=None,
            average_duration=None
        ))

    return results