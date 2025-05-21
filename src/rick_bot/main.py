
from fastapi import FastAPI
from sqlalchemy.orm import Session

from rick_bot.app.api.v1.routes import agent, auth, ask, user
from rick_bot.app.config.db import SessionLocal, engine
from rick_bot.app.api.v1.domain.models import models



models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Rick Bot  - IA Chatbot")

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

app.include_router(agent_router, prefix="/api/v1")