from pydantic import BaseModel
from .base import BaseSchema
from .app_integration import AuthModeEnum

class AppIntegrationCreate(BaseModel):
    name: str
    auth_mode: AuthModeEnum
    api_key: str | None = None
    bearer_token: str | None = None
    oauth2_client_id: str | None = None
    oauth2_client_secret: str | None = None
    oauth2_redirect_uri: str | None = None

class AppIntegrationOut(BaseSchema):
    name: str
    auth_mode: AuthModeEnum
