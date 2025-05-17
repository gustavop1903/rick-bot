from uuid import UUID
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from .base import Base

class Agent(Base):
    __tablename__ = "agents"

    name = Column(String(20), nullable=False)
    prompt_context = Column(Text, nullable=False)
    model_tuning = Column(String, nullable=True)
    namespace = Column(String, nullable=False, unique=True)
    
    creator_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    creator = relationship("User", back_populates="agents")
    
    conversations = relationship("Conversation", back_populates="agent")
