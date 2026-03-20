from src.database.models import ProductDetails


def dto_to_entity(productDetailsDTO):
    return ProductDetails(
        PRD_NAME=productDetailsDTO.prdName,
        PRD_CATEGORY=productDetailsDTO.prdCategory,
        PRD_QTY=productDetailsDTO.prdQuantity,
        PRD_PRICE=productDetailsDTO.prdPrice,
        PRD_SUPPLIER=productDetailsDTO.prdSupplier,
        PRD_ROLE=productDetailsDTO.prdRole,
    )
