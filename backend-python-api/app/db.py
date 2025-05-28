from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgresql://postgresql_bingepal_db_user:2WYQGIX7VEfka46ETQujHDuZtEVzSWJd@dpg-d0do94juibrs73d0e9m0-a.oregon-postgres.render.com/postgresql_bingepal_db"

engine = create_async_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
