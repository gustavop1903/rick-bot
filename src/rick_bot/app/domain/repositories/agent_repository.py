from sqlalchemy.orm import Session
from app.domain.models.agent import Agent
from .base_repository import BaseRepository

class AgentRepository(BaseRepository[Agent]):
    def __init__(self, db: Session):
        super().__init__(Agent, db)

    def get_by_namespace(self, namespace: str) -> Agent | None:
        return self.db.query(Agent).filter(Agent.namespace == namespace).first()
