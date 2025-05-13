from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

"""
# This module sets up the database connection and session management for the application.
https://medium.com/@caioeduardojm4/iniciando-com-fastapi-postgresql-e-docker-3b7b413dbb21
"""

DATABASE_URL = f"postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@localhost:5432/{os.getenv("POSTGRES_DB")}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
