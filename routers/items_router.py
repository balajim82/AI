"""
This one more file to usage of Router implementations

"""

from fastapi import APIRouter

items_router = APIRouter()


@items_router.get("/items/")
async def read_items():
    return {"message": "Read items from the items router"}


@items_router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
