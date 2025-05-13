
from src.rick_bot.domain.models.question import Question
from src.rick_bot.app.interfaces.question_service_interface import QuestionServiceInterface


class StaticAnsweringService(QuestionServiceInterface):
    def answer(self, question: Question) -> str:
      

      return "Ainda estou aprendendo, mas em breve vou te ajudar com isso!"
