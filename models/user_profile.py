from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from models.user_address import UserAddress


class UserProfile(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: str
    age: int = Field(..., ge=18, le=120)
    addresses: List[UserAddress] = []

    @field_validator("email")
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email")
        return v.lower()
