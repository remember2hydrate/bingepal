import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "BingePal API"
    TMDB_API_KEY: str = os.getenv("TMDB_API_KEY", "")
    ADMIN_TOKEN: str = os.getenv("ADMIN_TOKEN", "my_secret_token")

settings = Settings()
