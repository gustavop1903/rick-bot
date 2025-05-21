# conversation_service.py
import uuid
import json
from .cache.conversation_cache_service import ConversationCacheService
from ..repositories.conversation_repository import ConversationRepository

class ConversationService:
    def __init__(self, db, redis):
        self.db = db
        self.redis = redis
        self.cache = ConversationCacheService(redis)
        self.repo = ConversationRepository(db)

    def save(self, agent_id: str, question: str, answer: str, session_id: str):
        self.cache.save_message(agent_id, json.dumps({
            "question": question,
            "answer": answer
        }))

        self.repo.create({
            "id": str(uuid.uuid4()),
            "session_id": session_id,
            "content": json.dumps({"question": question, "answer": answer}),
            "agent_id": agent_id
        })
