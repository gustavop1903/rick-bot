from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut, UserUpdate
from app.services.user_service import UserService
from ....config.security import get_db
from app.config.security import get_current_user

user = APIRouter(prefix="/users", tags=["Users"])

@user.post("/", response_model=UserOut, status_code=201)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    return UserService(db).create_user(data)

@user.get("/", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db)):
    return UserService(db).list_users()

@user.get("/me", response_model=UserOut)
def get_me(current_user: UserOut = Depends(get_current_user)):
    return current_user

@user.get("/{user_id}", response_model=UserOut)
def retrieve_user(user_id: str, db: Session = Depends(get_db)):
    user = UserService(db).get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

@user.put("/{user_id}", response_model=UserOut)
def update_user(user_id: str, data: UserUpdate, db: Session = Depends(get_db)):
    return UserService(db).update_user(user_id, data)

@user.delete("/{user_id}", status_code=204)
def delete_user(user_id: str, db: Session = Depends(get_db)):
    UserService(db).delete_user(user_id)
