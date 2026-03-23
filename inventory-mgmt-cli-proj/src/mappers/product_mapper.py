from src.database.models import ProductDetails


def dto_to_entity(productDetailsDTO):
    try:
        return ProductDetails(
            PRD_NAME=productDetailsDTO.prdName,
            PRD_CATEGORY=productDetailsDTO.prdCategory,
            PRD_QTY=productDetailsDTO.prdQuantity,
            PRD_PRICE=productDetailsDTO.prdPrice,
            PRD_SUPPLIER=productDetailsDTO.prdSupplier,
            PRD_ROLE=productDetailsDTO.prdRole,
        )
    except Exception as e:
        print("In product_mapper class - dto_to_entity Method failed:", e)
