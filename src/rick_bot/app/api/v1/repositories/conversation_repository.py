
from .base_repository import BaseRepository
from ..domain.models import Conversation

class ConversationRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(Conversation, db)
