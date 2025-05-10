from src.rick_bot.domain.schemas.request import QuestionRequest
from src.rick_bot.app.services.question_answering import StaticAnsweringService
from src.rick_bot.domain.models.question import Question


def handle_ask(payload: QuestionRequest):
    question = Question(payload.question)
    service = StaticAnsweringService()
    return service.answer(question)
