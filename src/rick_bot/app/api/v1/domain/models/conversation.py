from sqlalchemy.dialects.postgresql import UUID 
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Text, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .base import Base

class Conversation(Base):
    __tablename__ = "conversations"

    session_id = Column(String(255), nullable=False) 
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    agent_id = Column(UUID(as_uuid=True), ForeignKey("agents.id"), nullable=False)
    agent = relationship("Agent", back_populates="conversations")