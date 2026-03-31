from src.database.models import ProductDetails
from src.dto.product_dto import ProductDetailsDTO
from src.dto.invmgmt_opr_log_dto import InvenotryMgmtOprLogDTO


def dto_to_entity(productDetailsDTO):
    try:
        return ProductDetails(
            PRD_NAME=productDetailsDTO.prdname,
            PRD_CATEGORY=productDetailsDTO.prdcategory,
            PRD_QTY=productDetailsDTO.prdquantity,
            PRD_PRICE=productDetailsDTO.prdprice,
            PRD_SUPPLIER=productDetailsDTO.prdsupplier,
            PRD_ROLE=productDetailsDTO.prdrole,
        )
    except Exception as e:
        print("In product_mapper class - dto_to_entity Method failed:", e)


def entity_to_dto(productDetails):
    try:
        # print(productDetails.__dict__)
        productDetailsDTO = ProductDetailsDTO(
            prdid=productDetails.PRD_ID,
            prdname=productDetails.PRD_NAME,
            prdcategory=productDetails.PRD_CATEGORY,
            prdquantity=productDetails.PRD_QTY,
            prdprice=productDetails.PRD_PRICE,
            prdsupplier=productDetails.PRD_SUPPLIER,
            prdrole=productDetails.PRD_ROLE,
        )
        # print(productDetailsDTO.__dict__)
        return productDetailsDTO
    except Exception as e:
        print("In product_mapper class - entity_to_dto Method failed:", e)
        return None


def entityimol_to_imoldto(InvenotryMgmtOprLog):
    try:
        invenotryMgmtOprLogDTO = InvenotryMgmtOprLogDTO(
            imolid=InvenotryMgmtOprLog.IMOL_ID,
            imolaction=InvenotryMgmtOprLog.IMOL_ACTION,
            imoltimestamp=InvenotryMgmtOprLog.IMOL_TIMESTAMP,
        )
        return invenotryMgmtOprLogDTO
    except Exception as e:
        print("In product_mapper class - entity_to_dto Method failed:", e)
        return None
