from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from .base import BaseSchema

class AgentCreate(BaseModel):
    name: str
    prompt_context: str
    model_tuning: str | None = None

class AgentUpdate(BaseModel):
    id: UUID
    name: str | None = None
    prompt_context: str | None = None
    model_tuning: str | None = None

class AgentOut(BaseSchema):
    name: str
    prompt_context: str
    model_tuning: Optional[str]
    namespace: str
    creator_id: UUID

    class Config:
        orm_mode = True

class AgentAskResponse(BaseModel):
    agent_id: UUID
    answer: str
    class Config:
        orm_mode = True

class GenericAskRequest(BaseModel):
    question: str
    class Config:
        orm_mode = True
        
class DirectAskRequest(BaseModel):
    question: str
    agent_id: UUID
    class Config:
        orm_mode = True