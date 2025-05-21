# app/services/auth_service.py
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from ..domain.models import User
from ..repositories import UserRepository
from ....utils.utils import verify_password, create_tokens, verify_refresh_token

class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)

    def login(self, email: str, password: str):
        user = self.user_repo.get_by_email(email)
        if not user or not verify_password(password, user.password_hash):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas.")
        return create_tokens(user.id)

    def refresh(self, refresh_token: str):
        user_id = verify_refresh_token(refresh_token)
        return create_tokens(user_id)
