from sqlalchemy import Column, Integer, EmailType, String
from sqlalchemy.dialects.postgresql import UUID
from config.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(EmailType, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
