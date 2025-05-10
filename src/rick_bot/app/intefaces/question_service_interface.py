from abc import ABC, abstractmethod
from src.rick_bot.domain.models.question import Question

class QuestionServiceInterface(ABC):
    @abstractmethod
    def answer(self, question: Question) -> str:
        pass
