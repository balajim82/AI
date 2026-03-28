"""
Pydantic is a data validation library that uses Python type hints to validate data at runtime. Unlike traditional validation libraries, Pydantic:

Leverages type hints: Uses Python's native type system (PEP 484)

Fast: Written in Rust (v2), significantly faster than pure Python validators

IDE-friendly: Excellent autocomplete and type checking support

JSON Schema: Auto-generates JSON schemas for your models

Parsing: Converts input data to the correct types automatically

If you're using Pydantic v2 (released 2023), be aware of significant changes:

Complete rewrite in Rust for performance

New validation core

Breaking API changes from v1

pydantic.v1 compatibility layer available

This tutorial focuses on Pydantic v2.

The below Imp topics discussed.
==========================
1. Pydantic Models
2. Pydantic Field and Field Validators
3. Pydantic CustomField Validator
4. Pydantic Model Validator (Event Based meaning, After fields execution.)
5. Pydantic Deserialization (Json to Pydantic Object : json -> pydantic (Also called Deserialization))
6. Pydantic Serialization ((Pydantic to Json : pydantic -> json (Also called Serialization)))
"""


# Normal class has no strict validation
# Below Program username provided as int still considered without checking type.
class User:
    def __init__(self, id: int, username: str, email: str):
        self.id = id
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"


user = User(19, 890, "abc@gmail.com")
print(user)

# pydantic does data validation and data conversion
# No, you don't need to create init with Pydantic's BaseModel.
# It's automatically generated for you, just like @dataclass.
# Adavantages using pydantic
# ✅ __init__ - Constructor
# ✅ __repr__ - String representation
# ✅ __str__ - String conversion
# ✅ __eq__ - Equality comparison
# ✅ Data validation (this is the key difference from @dataclass!)
# ✅ JSON serialization
# ✅ Schema generation

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str


# user = User(id=1, username=890, email="raaj@example.com")
user = User(id=1, username="raaj", email="raaj@example.com")
print(user)  # It will throw error. Strictly checking data type. (ex: username)


# Creating Your First Model
# Adavantage : Automatic Type Conversion
# (Username : str but your passing "123" it converts auto data type int)

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    is_active: bool = True  # Default value
    metadata: Optional[dict] = None


user = User(
    id=1,
    username="123",
    email="raaj@example.com",
    created_at="2024-01-01T10:00:00",  # Automatic parsing
)

print(user.id)  # 1
print(user.created_at)  # datetime object
print(user.model_dump())  # Convert to dict
x = int(user.username)
print(x, type(x))

# How to deal with Validation errors.
# user id  passing as string and exptecs integer. then should throw error.

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    username: str
    age: int


try:
    user = User(id="not_a_number", username="john", age=-5)
except ValidationError as e:
    print(e.json(indent=2))

# How to validate Each and every field.
# Field Types & Constraints {#field-types}
# Field Validators and Constraints
# Custom Field Types

from pydantic import BaseModel, Field, EmailStr, HttpUrl, field_validator
from typing import List, Annotated
from datetime import datetime
from decimal import Decimal  # Import Decimal

# Create a custom type with validation
PhoneNumber = Annotated[str, Field(pattern=r"^\+?1?\d{9,15}$")]


class UserProfile(BaseModel):
    # String constraints
    username: str = Field(
        min_length=3,
        max_length=50,
        pattern=r"^[a-zA-Z0-9_]+$",
        description="Alphanumeric username with underscores",
    )

    # Email validation (requires pydantic[email])
    email: EmailStr

    # URL validation
    website: HttpUrl | None = None

    # Numeric constraints
    age: int = Field(ge=18, le=40, description="Age must be between 18 and 120")

    # Using conint (constrained int) - alternative syntax
    followers: int = Field(0, ge=0)

    # List with constraints
    tags: List[str] = Field(max_length=10, default_factory=list)

    # Decimal precision
    balance: Decimal = Field(ge=0.0, decimal_places=2)  # Changed type to Decimal

    # Create a custom type with validation
    phone: PhoneNumber

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str) -> str:
        # Additional custom validation
        if not v.startswith("+"):
            raise ValueError("Phone must start with + and country code")
        return v


# Usage
profile = UserProfile(
    username="raaj_kumar",
    email="raaj@example.com",
    website="https://genelite@co.in",
    age=20,
    followers=2,
    tags=["bac"],
    balance=Decimal("1234.56"),  # Provided as a Decimal object,
    phone="+919916030247",
)
print(profile)

# Complex Types and One class use by Other Class.

from pydantic import BaseModel
from typing import Dict, List, Union, Literal, Tuple
from datetime import datetime
from enum import Enum


class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


class Address(BaseModel):
    street: str
    city: str
    country: str
    postal_code: str


class Company(BaseModel):
    name: str
    employees: int


class User(BaseModel):
    id: int
    role: UserRole  # Enum validation

    # Nested models
    address: Address

    # Union types
    employer: Union[Company, str]  # Either a Company object or string

    # Literal types (only specific values allowed)
    account_type: Literal["free", "premium", "enterprise"]

    # Dict with type constraints
    metadata: Dict[str, Union[str, int, float]]

    # Tuple with fixed length
    coordinates: Tuple[float, float]  # (lat, lon)

    # List of nested models
    friends: List["User"] = []  # Self-referential model


user = User(
    id=1,
    role="admin",  # Automatically converted to UserRole.ADMIN
    address={
        "street": "123 Main St",
        "city": "Bangalore",
        "country": "India",
        "postal_code": "560001",
    },
    employer={"name": "Genai Elite", "employees": 50000},
    account_type="premium",
    metadata={"last_login": "2024-01-01", "login_count": 42},
    coordinates=(12.9716, 77.5946),
)

print(user.role.value)  # "admin"
print(user.address.city)  # "Bangalore"

# Custom Validators - field_validator

from pydantic import BaseModel, field_validator, ValidationError
from typing import List
import re


class Article(BaseModel):
    title: str
    content: str
    tags: List[str]
    slug: str = ""

    @field_validator("title")
    @classmethod
    def title_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Title cannot be empty")
        if len(v) > 200:
            raise ValueError("Title too long")
        return v.strip()

    @field_validator("tags")
    @classmethod
    def validate_tags(cls, v: List[str]) -> List[str]:
        if len(v) > 10:
            raise ValueError("Maximum 10 tags allowed")
        # Normalize tags
        return [tag.lower().strip() for tag in v]

    @field_validator("slug", mode="before")
    @classmethod
    def generate_slug(cls, v: str, info) -> str:
        # Auto-generate slug from title if not provided
        if not v and "title" in info.data:
            title = info.data["title"]
            slug = re.sub(r"[^\w\s-]", "", title.lower())
            slug = re.sub(r"[-\s]+", "-", slug)
            return slug
        return v


# Usage
article = Article(
    title="  Pydantic Tutorial  ",
    content="Content here...",
    tags=["Python", "PYDANTIC", "validation"],
)

print(article.title)  # "Pydantic Tutorial" (stripped)
print(article.tags)  # ["python", "pydantic", "validation"] (normalized)
print(article.slug)  # "pydantic-tutorial" (auto-generated)

# Model Validators
from pydantic import BaseModel, model_validator
from typing import Optional
from datetime import datetime, timedelta


class Event(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime
    duration_minutes: Optional[int] = None

    @model_validator(mode="after")
    def validate_dates_and_duration(self) -> "Event":
        # Validate that end_date is after start_date
        if self.end_date <= self.start_date:
            raise ValueError("end_date must be after start_date")

        # Calculate duration if not provided
        if self.duration_minutes is None:
            delta = self.end_date - self.start_date
            self.duration_minutes = int(delta.total_seconds() / 60)

        # Validate provided duration matches dates
        expected_duration = int((self.end_date - self.start_date).total_seconds() / 60)
        if abs(self.duration_minutes - expected_duration) > 1:
            raise ValueError("Duration does not match date range")

        return self


# Usage
event = Event(
    name="Workshop", start_date="2024-01-01T10:00:00", end_date="2024-01-01T12:00:00"
)
print(event.duration_minutes)  # 120 (auto-calculated)

# Deserialization
# Json to Pydantic Object : json -> pydantic (Also called Deserialization)
# To convert JSON data into a Pydantic model, you need to first define the Pydantic model with the expected structure and data types, and then use a built-in method like model_validate_json() or model_validate() to parse the JSON.

from pydantic import BaseModel


class Name(BaseModel):
    first: str | None
    last: str | None


class Customer(BaseModel):
    id: int
    name: Name
    notes: str


# Suppose The below Json String coming through FastAPI then if
# want to convert into Pydantic model.
json_string = """
{
    "id": "123",
    "name": {
        "first": "santosh",
        "last": "kumar"
    },
    "notes": "Some notes about Santosh"
}
"""
customer_model = Customer.model_validate_json(json_string)

print(customer_model)
print(f"Customer name: {customer_model.name.first}")


# Serialization
# Pydantic to Json : pydantic -> json (Also called Serialization)
# To convert a Pydantic object to a JSON string, you use the .model_dump_json() method on the model instance. If you need a standard Python dictionary containing only JSON-compatible types, use .model_dump(mode='json').

from pydantic import BaseModel
from datetime import datetime
import uuid


class User(BaseModel):
    id: uuid.UUID
    name: str
    signup_time: datetime


# Create a Pydantic model instance
user = User(id=uuid.uuid4(), name="Jane Doe", signup_time=datetime.utcnow())

# Convert the instance to a JSON string
json_string = user.model_dump_json(indent=2)
print("--- JSON String ---")
print(json_string)

# Convert the instance to a JSON-compatible Python dictionary
jsonable_dict = user.model_dump(mode="json")
print("\n--- JSON-compatible Dict ---")
print(jsonable_dict)


# Below example for both serialization and De-serialization

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import json


class Author(BaseModel):
    name: str
    email: str


class BlogPost(BaseModel):
    title: str
    content: str
    author: Author
    tags: List[str]
    published_at: datetime
    views: int = 0
    metadata: dict = Field(default_factory=dict)


post = BlogPost(
    title="Pydantic Guide",
    content="Content here...",
    author={"name": "Raaj", "email": "raaj@example.com"},
    tags=["python", "pydantic"],
    published_at=datetime.now(),
)

# 1. model_dump() - Python dict
print(post.model_dump())

# 2. model_dump_json() - JSON string
json_str = post.model_dump_json(indent=2)
print(json_str)

# 3. Exclude fields
print(post.model_dump(exclude={"metadata", "views"}))

# 4. Include specific fields
print(post.model_dump(include={"title", "author"}))

# 5. Exclude unset fields (fields with default values that weren't explicitly set)
print(post.model_dump(exclude_unset=True))

# 6. Nested exclusion
print(post.model_dump(exclude={"author": {"email"}}))
# Excludes author.email only

# 7. mode='json' for JSON-serializable dict
print(post.model_dump(mode="json"))
# Converts datetime to string, etc.

# Custom Serializer.
# When ever converting json to Model, Some fields want to with own custom logic then use like below code.
from pydantic import BaseModel, field_serializer, model_serializer
from typing import List
from datetime import datetime


class User(BaseModel):
    username: str
    email: str
    created_at: datetime
    roles: List[str]

    @field_serializer("email")
    def serialize_email(self, email: str):
        # Mask email for privacy
        parts = email.split("@")
        if len(parts) == 2:
            masked = parts[0][:2] + "***@" + parts[1]
            return masked
        return email

    @field_serializer("created_at")
    def serialize_datetime(
        self,
        dt: datetime,
    ):
        # Custom datetime format
        return dt.strftime("%Y-%m-%d %H:%M:%S UTC")

    @field_serializer("roles")
    def serialize_roles(self, roles: List[str]):
        # Join roles as comma-separated string
        return ",".join(roles)


user = User(
    username="raaj",
    email="raaj@example.com",
    created_at=datetime.now(),
    roles=["admin", "user"],
)

print(user.model_dump())


# Model Serializer

from pydantic import BaseModel, model_serializer


class APIResponse(BaseModel):
    success: bool
    data: dict
    error: str | None = None

    @model_serializer
    def serialize_model(self) -> dict:
        # Custom serialization logic for entire model
        result = {
            "status": "success" if self.success else "error",
            "payload": self.data,
        }
        if self.error:
            result["error_message"] = self.error
        return result


response = APIResponse(success=True, data={"user_id": 123})
print(response.model_dump())
# {'status': 'success', 'payload': {'user_id': 123}}

# Settings Management
# Pydantic Settings Management uses pydantic-settings (install with pip install pydantic-settings) to create type-hinted configuration classes inheriting from BaseSettings, automatically loading settings from environment variables, .env files, or secrets files, and validating them. You define fields with types, and Pydantic handles the loading and validation, supporting nested models, secrets management (like SecretStr), and precedence rules for different sources, making configuration robust and declarative.


from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class AppSettings(BaseSettings):
    # Environment variables are automatically loaded
    app_name: str = "MyApp"
    debug: bool = False
    database_url: str = "sqlite:///test.db"
    redis_host: str = "localhost"
    redis_port: int = 6379
    api_key: str = "dummy_key"
    max_connections: int = 100

    # Nested config
    model_config = SettingsConfigDict(
        env_file=".venv",
        env_file_encoding="utf-8",
        case_sensitive=False,
        # You can use prefixes for namespacing
        # env_prefix='APP_'
    )


# Load settings from environment variables or .env file
# Environment variables like APP_DATABASE_URL, APP_API_KEY will be loaded
settings = AppSettings()

print(settings.database_url)
print(settings.api_key)

# You can also override with explicit values
"""settings = AppSettings(
    database_url="postgresql://localhost/mydb",
    api_key="secret-key-123"
)"""
