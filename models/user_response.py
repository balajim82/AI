from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional
from models.user_role import UserRole
from datetime import datetime


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str]
    role: UserRole
    is_active: bool
    created_at: datetime
