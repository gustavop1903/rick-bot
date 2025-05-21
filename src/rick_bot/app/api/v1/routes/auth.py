# app/controllers/auth_controller.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..domain.schemas import LoginRequest, TokenResponse, RefreshTokenRequest
from ..services import AuthService
from ....config.security import get_db
from app.config.security import get_current_user

auth = APIRouter(prefix="/auth", tags=["Auth"])

@auth.post("/login", response_model=TokenResponse, summary="Login do usuário")
def login(payload: LoginRequest, db: Session = Depends(get_db)) -> TokenResponse:
    service = AuthService(db)
    return service.login(payload.email, payload.password)

@auth.post("/refresh", response_model=TokenResponse, summary="Renovar tokens")
def refresh_token(payload: RefreshTokenRequest, db: Session = Depends(get_db)) -> TokenResponse:
    service = AuthService(db)
    return service.refresh(payload.refresh_token)
