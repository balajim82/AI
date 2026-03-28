"""
This is file used for routers implementations
"""

from fastapi import APIRouter

user_router = APIRouter()


@user_router.get("/users/")
async def read_items():
    return {"message": "Read items from the items router"}


@user_router.get("/users/{users_id}")
async def read_item(users_id: int):
    return {"users_id": users_id}
