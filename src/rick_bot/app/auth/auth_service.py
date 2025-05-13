from http.client import HTTPException
from sqlalchemy.orm import Session
from jose import JWTError
from app.auth.security.password_handler import verify_password
from app.auth.security.jwt_handler import create_access_token, create_refresh_token, decode_token
from app.auth.toke_response import TokenResponse
from app.domain.models.user import User

class AuthService:

  def authenticate_user(self, username: str, password: str, db: Session) -> TokenResponse | None:
    user = db.query(User).filter(User.username == username).first()

    if not user or not verify_password(password, user.hashed_password):
      return None

    return TokenResponse(
      access_token=create_access_token(user_id=str(user.id)),
      refresh_token=create_refresh_token(user_id=str(user.id)),
      token_type="bearer"
    )
  
  def refresh_access_token(self, refresh_token: str, db: Session) -> TokenResponse:
        try:
            payload = decode_token(refresh_token)
            user_id = payload.get("sub")
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid refresh token")

        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return TokenResponse(
            access_token=create_access_token(user_id=str(user.id)),
            refresh_token=refresh_token,
        )
