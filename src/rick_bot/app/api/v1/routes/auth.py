# app/controllers/auth_controller.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.domain.schemas.auth import LoginRequest, TokenResponse, RefreshTokenRequest
from app.services.auth_service import AuthService
from config.db.session import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenResponse, summary="Login do usuário")
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.login(payload.email, payload.password)

@router.post("/refresh", response_model=TokenResponse, summary="Renovar tokens")
def refresh_token(payload: RefreshTokenRequest, db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.refresh(payload.refresh_token)
