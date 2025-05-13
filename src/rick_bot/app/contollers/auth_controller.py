from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Header
from sqlalchemy.orm import Session

from app.auth.auth_service import AuthService
from config.db.session import get_db
from app.domain.schemas.auth import TokenResponse

from app.domain.models.user import User


router = APIRouter()
auth = AuthService()

@router.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm, db: Session = Depends(get_db)):
  tokens = auth.authenticate_user(form_data.username, form_data.password, db)
  if not tokens:
      raise HTTPException(status_code=401, detail="Invalid credentials")
  return tokens

@router.post("/auth/refresh", response_model=TokenResponse)
def refresh_token(refresh_token: str = Header(...), db: Session = Depends(get_db)):
    return auth.refresh_access_token(refresh_token, db)