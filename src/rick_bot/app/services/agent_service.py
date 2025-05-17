from sqlalchemy.orm import Session
from app.domain.repositories import AgentRepository
from app.domain.schemas import AgentCreate, AgentOut
from app.domain.models import Agent
from app.domain.services import BaseService
import uuid

class AgentService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)
        self.repo = AgentRepository(db)

    def create_agent(self, data: AgentCreate, creator_id) -> AgentOut:
        namespace = f"agent_{uuid.uuid4().hex[:8]}"
        agent: Agent = self.repo.create({
            "name": data.name,
            "prompt_context": data.prompt_context,
            "model_tuning": data.model_tuning,
            "creator_id": creator_id,
            "namespace": namespace
        })

        return AgentOut.from_orm(agent)
