# manga handler

import httpx
from app.models import SearchResult
from app.utils.logger import logger

BASE_URL = "https://api.mangadex.org"

async def search(query: str) -> list[SearchResult]:
    logger.info(f"[MangaDex] Searching '{query}'")

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/manga", params={
                "title": query,
                "limit": 10,
                "includes[]": "cover_art"
            })
            response.raise_for_status()
            data = response.json()
    except Exception as e:
        logger.error(f"[MangaDex] API error: {e}")
        return []

    results = []
    for item in data.get("data", []):
        attr = item["attributes"]
        title = attr["title"].get("en") or list(attr["title"].values())[0]
        description = attr.get("description", {}).get("en") or "No description."
        genres = [t["attributes"]["name"].get("en") for t in attr.get("tags", []) if "attributes" in t]

        # Find cover filename
        cover = None
        for rel in item["relationships"]:
            if rel["type"] == "cover_art":
                cover = rel["attributes"].get("fileName")

        poster_url = f"https://uploads.mangadex.org/covers/{item['id']}/{cover}" if cover else None

        results.append(SearchResult(
            id=item["id"],
            title=title,
            type="manga",
            description=description,
            poster_url=poster_url,
            year=None,  # MangaDex does not give publish year in search
            source="mangadex",
            genres=genres or None,
            rating=None,
            rating_count=None,
            total_seasons=None,
            total_episodes=None,
            average_duration=None
        ))

    return results