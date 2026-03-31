from fastapi import APIRouter
from src.dto.product_dto import ProductDetailsDTO
from src.services.product_service import ProductDetailsService

imcud_router = APIRouter()
productService = ProductDetailsService()


@imcud_router.post("/products/prodcreate")
async def create(p: ProductDetailsDTO):
    await productService.create_product(p)
    return {"msg": "Product Created Sucessfully"}


@imcud_router.put("/products/produpdate/{pid}")
async def update(pid: int, p: ProductDetailsDTO):
    await productService.update_product(pid, p)
    return {"msg": "Product Updated Sucessfully"}


@imcud_router.delete("/products/proddelete/{pid}")
async def delete(pid: int):
    await productService.delete_product(pid)
    return {"msg": "Product Deleted Sucessfully"}
