from fastapi import APIRouter
from typing import List
from src.dto.product_dto import ProductDetailsDTO
from src.services.product_service import ProductDetailsService
from src.dto.invmgmt_opr_log_dto import InvenotryMgmtOprLogDTO

imrr_router = APIRouter()
productService = ProductDetailsService()


@imrr_router.get("/products", response_model=List[ProductDetailsDTO])
async def get_all():
    return await productService.get_all_products()


@imrr_router.get(
    "/products/productNameorCat/{prdnameorcatergory}",
    response_model=list[ProductDetailsDTO],
)
async def get_productorcatergory(prdnameorcatergory: str):
    return await productService.search_products(prdnameorcatergory)


@imrr_router.get("/products/productid/{prdid}", response_model=ProductDetailsDTO)
async def get_by_prdid(prdid: int):
    return await productService.get_by_prdid(prdid)


@imrr_router.get("/products/stkmgmt", response_model=List[ProductDetailsDTO])
async def get_stkmgmt():
    return await productService.stockMgmt()


@imrr_router.get("/products/stkreports")
async def get_stkreports():
    return await productService.stockReports()


@imrr_router.get("/products/productexportcsv")
async def get_productexportcsv():
    return await productService.productDetailsExport()


@imrr_router.get("/products/productimportcsv")
async def get_productimportcsv():
    return await productService.productDetailsImport()


@imrr_router.get(
    "/products/producttransLog", response_model=List[InvenotryMgmtOprLogDTO]
)
async def get_producttransLog():
    return await productService.productTransLog()
