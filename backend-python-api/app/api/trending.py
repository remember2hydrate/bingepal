from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from datetime import datetime, timedelta

from app.db import get_db
from app.models import SearchLog

router = APIRouter()

@router.get("/trending")
async def get_trending(
    type: str = Query(..., description="Type of media (e.g., movie, series, anime)"),
    days: int = Query(7, description="Time range in days: 7 for week, 30 for month, 365 for year"),
    session: AsyncSession = Depends(get_db),
):
    since = datetime.utcnow() - timedelta(days=days)

    result = await session.execute(
        select(SearchLog.title, func.count().label("count"))
        .where(SearchLog.type == type)
        .where(SearchLog.timestamp >= since)
        .group_by(SearchLog.title)
        .order_by(func.count().desc())
        .limit(10)
    )

    trending = [{"title": row[0], "count": row[1]} for row in result.all()]
    return {"type": type, "days": days, "trending": trending}
