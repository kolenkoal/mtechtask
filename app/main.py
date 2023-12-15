from fastapi import FastAPI

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

# Подключение к базе данных
POSTGRESQL_DATABASE = "postgresql://user:password@db:5432/mvideotest"
engine = create_engine(POSTGRESQL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()