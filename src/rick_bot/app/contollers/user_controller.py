from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.services.user_service import UserService
from app.domain.schemas.user import UserCreateDTO, UserUpdateDTO, UserResponseDTO
from app.db.session import get_db
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponseDTO, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreateDTO, db: Session = Depends(get_db)):
    return UserService(db).create_user(payload)


@router.get("/{user_id}", response_model=UserResponseDTO)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserService(db).get_user_by_id(user_id)


@router.get("/", response_model=List[UserResponseDTO])
def list_users(db: Session = Depends(get_db)):
    return UserService(db).get_all_users()


@router.put("/{user_id}", response_model=UserResponseDTO)
def update_user(user_id: int, payload: UserUpdateDTO, db: Session = Depends(get_db)):
    return UserService(db).update_user(user_id, payload)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return UserService(db).delete_user(user_id)
