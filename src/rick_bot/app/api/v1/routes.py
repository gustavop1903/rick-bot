from fastapi import APIRouter
from src.rick_bot.domain.schemas.request import QuestionRequest
from src.rick_bot.app.controllers.ask_controller import ask_question

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Rick Bot está rodando 🧠"}

@router.post("/ask")
def ask_question(payload: QuestionRequest):
    answer = ask_question(payload)
    return {"answer": answer}
