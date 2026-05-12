from datetime import datetime
import uuid
from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: uuid
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)