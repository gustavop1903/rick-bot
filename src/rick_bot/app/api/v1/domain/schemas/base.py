from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

class BaseSchema(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Config:
        orm_mode = True
