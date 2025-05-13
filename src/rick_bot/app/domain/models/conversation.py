from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from config.db.session import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    session_id = Column(String, index=True)
    conversation = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", backref="conversations")
