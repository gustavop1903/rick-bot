from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from .base import BaseSchema

class ConversationCreate(BaseModel):
    session_id: str
    content: str
    agent_id: UUID
    app_integration_id: UUID | None = None

class ConversationOut(BaseSchema):
    session_id: str
    content: str
    agent_id: UUID
    app_integration_id: UUID | None
    namespace: str

    class Config:
        orm_mode = True
