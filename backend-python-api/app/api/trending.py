@router.get("/trending")
async def get_trending(
    type: str = Query(...),
    limit: int = Query(10)
):
    query = """
        SELECT title, source_id, source, COUNT(*) as hits
        FROM search_logs
        WHERE type = $1
        GROUP BY title, source_id, source
        ORDER BY hits DESC
        LIMIT $2
    """
    rows = await database.fetch_all(query, (type, limit))
    return [dict(row) for row in rows]
