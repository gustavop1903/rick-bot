from pydantic import BaseModel, EmailStr
from uuid import UUID
from .base import BaseSchema

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None

class UserOut(BaseSchema):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
