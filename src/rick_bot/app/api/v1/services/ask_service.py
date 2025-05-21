from .conversation_service import ConversationService
#from app.agents.agent_responder import AgentResponder
#from app.agents.orchestrator import Orchestrator
from ..domain.schemas import AgentAskResponse
from ..domain.models import User
import uuid
import json

class AskService:
    def __init__(self, db, redis):
        self.db = db
        self.redis = redis
        self.conversation_service = ConversationService(db=db, redis=redis)

    def handle(self, question: str, agent_id: str = None, session_id: str = None):
        session_id = session_id or str(uuid.uuid4())

        #if agent_id:
         #   responder = AgentResponder(db=self.db, agent_id=agent_id)
        #else:
        #    responder = Orchestrator(db=self.db)

        #answer = responder.answer(question)

        #elf.conversation_service.save(
        #    agent_id=responder.agent_id,
        #    question=question,
        #    answer=answer,
        #    session_id=session_id
       #)

        #return AgentAskResponse(agent_id=responder.agent_id, answer=answer)