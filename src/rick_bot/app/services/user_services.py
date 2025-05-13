
from sqlalchemy.orm import Session
from app.domain.schemas.user import UserCreateDTO, UserUpdateDTO
from app.domain.models.user import User
from passlib.context import CryptContext
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def get_all_users(self):
        return self.db.query(User).all()

    def create_user(self, payload: UserCreateDTO):
        hashed_password = pwd_context.hash(payload.password)
        user = User(username=payload.username, email=payload.email, hashed_password=hashed_password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user(self, user_id: int, payload: UserUpdateDTO):
        user = self.get_user_by_id(user_id)
        user.username = payload.username or user.username
        user.email = payload.email or user.email
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        self.db.delete(user)
        self.db.commit()
        return {"message": "User deleted successfully"}