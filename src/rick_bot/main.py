
from fastapi import FastAPI
from .routes.routes import router


app = FastAPI(title="Rick Bot  - IA Chatbot")

app.include_router(router)