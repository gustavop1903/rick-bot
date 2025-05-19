


class AppIntegrationService:
    def __init__(self, db: Session):
        self.db = db

    def validate_integration(self, auth_header: str) -> AppIntegration:
        if not auth_header:
            raise HTTPException(status_code=401, detail="Authorization header missing")

        if auth_header.startswith("Api-Key "):
            api_key = auth_header.split(" ")[1]
            integration = self.db.query(AppIntegration).filter_by(api_key=api_key).first()
            if integration and integration.auth_mode == AuthModeEnum.API_KEY:
                return integration

        raise HTTPException(status_code=403, detail="Invalid integration credentials")
