from sqlalchemy.orm import Session

from ..repositories import AgentRepository
from ..domain.schemas import AgentCreate, AgentOut
from ..domain.models import Agent
from .base_service import BaseService
import uuid

class AgentService():
    def __init__(self,):
        self.repo = AgentRepository()

    def create_agent(self, data: AgentCreate, creator_id) -> AgentOut:
        namespace = f"agent_{data.name}"
        agent: Agent = self.repo.create({
            "name": data.name,
            "prompt_context": data.prompt_context,
            "model_tuning": data.model_tuning,
            "creator_id": creator_id,
            "namespace": namespace
        })

        return AgentOut.from_orm(agent)
