class ConversationCacheService:
    def __init__(self, redis_client):
        self.redis = redis_client

    def _session_key(self, session_id, agent_id: str) -> str:
        return f"chat:{session_id}:{agent_id}"

    def save_message(self, session_id, agent_id: str, message: str):
        key = self._session_key(session_id, agent_id)
        self.redis.rpush(key, message)
        self.redis.expire(key, 21600) 
        
    def get_history(self, session_id, agent_id: str) -> list:
        key = self._session_key(session_id, agent_id)
        return self.redis.lrange(key, 0, -1)

    def clear_history(self, session_id, agent_id: str):
        key = self._session_key(session_id, agent_id)
        self.redis.delete(key)
