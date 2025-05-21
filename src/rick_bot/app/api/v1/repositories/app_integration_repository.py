
from .base_repository import BaseRepository
from ..domain.models import Conversation

class AppIntegrationRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(Conversation, db)
