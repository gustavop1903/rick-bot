from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..repositories import AppIntegrationRepository
from ..domain.schemas import AppIntegrationOut
from ..domain.models import AppIntegration
from .base_service import BaseService

class AppIntegrationService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)
        self.repo = AppIntegrationRepository(db)
        self.db = db

    def validate_teams_request(self, request: dict) -> AppIntegrationOut:
        ...
        '''
        if not request:
            raise HTTPException(status_code=401, detail="Authorization header missing")

        if request.startswith("Api-Key"):
            api_key = request.get("from").aadObjectId
            integration = self.db.query(AppIntegration).filter_by(api_key=api_key).first()
            if integration and integration.auth_mode == AuthModeEnum.API_KEY:
                return AppIntegrationOut.from_orm(integration)

        raise HTTPException(status_code=403, detail="Invalid integration credentials")
    '''