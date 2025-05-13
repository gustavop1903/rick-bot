
from fastapi import FastAPI
from sqlalchemy.orm import Session
from .routes.routes import router
from config.db.session import SessionLocal, engine
from app.domain.models import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Rick Bot  - IA Chatbot")

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

app.include_router(router, prefix="/api/v1")