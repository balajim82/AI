from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import List, Optional
from models.user_role import UserRole


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    role: Optional[UserRole] = None
