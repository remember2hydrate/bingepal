from fastapi import APIRouter, Depends, Header, HTTPException
from typing import Optional
from app.core.config import settings
import os

router = APIRouter()

@router.get("/admin-logs")
async def get_logs(authorization: Optional[str] = Header(None)):
    if authorization != f"Bearer {settings.ADMIN_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    log_path = "app.log"
    if not os.path.exists(log_path):
        return {"logs": "No logs found."}

    with open(log_path, "r") as f:
        return {"logs": f.read()}
