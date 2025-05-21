from sqlalchemy import Column, Integer, String, Enum
from .base import Base
import enum

class AuthModeEnum(str, enum.Enum):
    NONE = "none"
    BEARER = "bearer"
    API_KEY = "api_key"
    OAUTH2 = "oauth2"

class AppIntegration(Base):
    __tablename__ = "app_integrations"

    name = Column(String(20), unique=True, nullable=False)
    auth_mode = Column(Enum(AuthModeEnum), default=AuthModeEnum.NONE)
    api_key = Column(String(255), nullable=True)
    bearer_token = Column(String(255), nullable=True)
    oauth2_client_id = Column(String(255), nullable=True)
    oauth2_client_secret = Column(String(255), nullable=True)
    oauth2_redirect_uri = Column(String(255), nullable=True)