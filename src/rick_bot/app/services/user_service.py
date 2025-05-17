from sqlalchemy.orm import Session
from app.domain.schemas import UserCreate, UserOut
from app.domain.models import User
from app.domain.repositories import UserRepository
from base_service import BaseService
from app.core.security import get_password_hash

class UserService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)
        self.repo = UserRepository(db)

    def create_user(self, data: UserCreate) -> UserOut:
        hashed_password = get_password_hash(data.password)
        user: User = self.repo.create({
            "username": data.username,
            "email": data.email,
            "password_hash": hashed_password,
        })

        return UserOut.from_orm(user)

    def get_by_email(self, email: str) -> User | None:
        return self.repo.get_by_email(email)
