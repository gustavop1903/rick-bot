from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreateDTO(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserUpdateDTO(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]

class UserResponseDTO(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
