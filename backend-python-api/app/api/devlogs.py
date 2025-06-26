# app/api/devlogs.py
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import PlainTextResponse
from starlette.status import HTTP_401_UNAUTHORIZED
from hashlib import sha256
import os

from app.utils.logger import logger

router = APIRouter()

@router.get("/dev-logs", response_class=PlainTextResponse)
async def get_dev_logs(request: Request):
    token = request.headers.get("Authorization")
    token_hash = sha256(token.encode()).hexdigest()
    if token_hash != os.getenv("STORED_HASH"):
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    try:
        log_path = os.path.join(os.path.dirname(__file__), "..", "logs", "dev.log")
        with open(log_path, "r") as f:
            return f.read()
    except Exception as e:
        logger.error(f"Failed to read dev.log: {e}")
        raise HTTPException(status_code=500, detail="Could not read log file.")
