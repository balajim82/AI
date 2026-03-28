"""
This program, We are going discuss
 1. Request Types and validation using pydantic
 2. Response Handling and status code.
 3.
"""

# Basic Sample Program
from fastapi import FastAPI, Path, Query, Body, HTTPException, status
from typing import Optional, List
import uvicorn
from pydantic import BaseModel, Field, field_validator
from models.user_profile import UserProfile
from models.user_create import UserCreate
from fastapi.responses import (
    JSONResponse,
    HTMLResponse,
    FileResponse,
    StreamingResponse,
)

app = FastAPI(
    title="My API", description="API for production services", version="1.0.0"
)

# Request Validation


# Query parameter validation
@app.get("/items/")
async def list_items(
    q: Optional[str] = Query(
        None,
        min_length=3,
        max_length=50,
        pattern="^[a-zA-Z0-9_-]+$",  # Changed regex to pattern
        description="Search query",
    ),
    page: int = Query(1, ge=1, le=1000),
    page_size: int = Query(10, ge=1, le=100),
    tags: List[str] = Query([], max_items=10),
):
    return {"q": q, "page": page, "page_size": page_size, "tags": tags}


# Path parameter validation
@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(..., gt=0, le=1000000, description="User ID")):
    return {"user_id": user_id}


@app.post("/profiles/")
async def create_profile(profile: UserProfile):
    return profile


# Response Models and Status Codes


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = ""  # hypothetical

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    return user


@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    existing_user = ""  # check_user_exists(user.username)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Username already exists"
        )

    return {"id": 1, "username": user.username}


@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    deleted = ""  # delete_user_from_db(user_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return None


# To start server you use uvicorn.run method
# Here important "reload=True" is that, Now if we running server but if you change logic of the file,
# then without stop server you can see latest changes.

if __name__ == "__main__":
    uvicorn.run("03_py_fasapi_request:app", host="0.0.0.0", port=8000, reload=True)
