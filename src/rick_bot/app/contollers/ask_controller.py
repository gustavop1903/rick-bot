from fastapi import APIRouter, Depends
from src.rick_bot.domain.schemas.request import QuestionRequest
from src.rick_bot.app.services.question_answering import StaticAnsweringService
from app.services.ask_service import AskService
from app.auth.security.get_current_user import get_current_user


router = APIRouter()
service = AskService()

def ask_question(payload: QuestionRequest, user: str = Depends(get_current_user)):
    return service.answer(payload, user)
