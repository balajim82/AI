from pydantic import BaseModel
from typing import Optional


class ProductDetailsDTO(BaseModel):
    prdid: Optional[int]
    prdname: str
    prdcategory: str
    prdquantity: float
    prdprice: float
    prdsupplier: str
    prdrole: Optional[str]
