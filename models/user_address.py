from pydantic import BaseModel, Field


# Body validation with nested models
class UserAddress(BaseModel):
    street: str
    city: str
    country: str
    postal_code: str = Field(..., pattern=r"^\d{5,6}$")  # Changed regex to pattern
