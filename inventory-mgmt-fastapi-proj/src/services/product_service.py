from src.repositories.product_repository import ProductDetailsRepository
from src.repositories.inv_mgmt_opr_log_repository import InventoryMgmtOprLogRepository
from src.mappers.product_mapper import (
    dto_to_entity,
    entity_to_dto,
    entityimol_to_imoldto,
)
import os
import pandas as pd
from datetime import datetime
from config import EXPORT_PATH, IMPORT_PATH
from src.database.models import ProductDetails


class ProductDetailsService:

    def __init__(self):
        self.repo = ProductDetailsRepository()
        self.repolog = InventoryMgmtOprLogRepository()

    async def create_product(self, dto):
        try:
            if dto.prdprice <= 0:
                print("Invalid price")
                return
            productDetails = dto_to_entity(dto)
            self.repo.create(productDetails)
            self.repolog.log_action("Saved new Product into DB")
            print("Created Product Details sucessfully.")
        except Exception as e:
            print("In ProductDetailsService class - create_product Method failed:", e)

    async def update_product(self, prdid, dto):
        try:
            print("product DTO:", dto)
            # productDetails = self.repo.get_by_id(prdid)
            if not dto:
                print("Product Details Not Found with this product id ", prdid)
                return
            productDetails = dto_to_entity(dto)
            productDetails.PRD_ID = dto.prdid
            self.repo.update(productDetails)
            self.repolog.log_action("Updated Products into DB")
            print("Updated Product Details sucessfully.")
        except Exception as e:
            print("In ProductDetailsService class - update_product Method failed:", e)

    async def delete_product(self, prdId):
        try:
            productDetails = self.repo.get_by_id(prdId)
            if not productDetails:
                print("Product Details Not Found with this product id ", prdId)
                return
            self.repo.delete(productDetails)
            self.repolog.log_action("Deleted Products from DB")
            print("Deleted Product Details sucessfully.")
        except Exception as e:
            print("In ProductDetailsService class - delete_product Method failed:", e)

    async def get_all_products(self):
        try:
            product_dto_list = []
            productDetails = self.repo.get_all()
            product_dto_list = [entity_to_dto(p) for p in productDetails]
            # REMOVE None values
            product_dto_list = [p for p in product_dto_list if p is not None]
            print(product_dto_list)
            self.repolog.log_action("Feteched All products from DB")
            print("Loaded All Product Details sucessfully.")
            return product_dto_list
        except Exception as e:
            print("In ProductDetailsService class - get_all_products Method failed:", e)
            return []

    async def search_products(self, prdSearch):
        try:
            productDetails = self.repo.search(prdSearch)
            print(f"Product or Category - '{prdSearch}' feteched sucessfully.")
            product_dto_list = [entity_to_dto(p) for p in productDetails]
            # REMOVE None values
            product_dto_list = [p for p in product_dto_list if p is not None]
            print(product_dto_list)
            self.repolog.log_action("Feteched products by key Search from DB")
            return product_dto_list
        except Exception as e:
            print("In ProductDetailsService class - get_all_products Method failed:", e)
            return []

    async def get_by_prdid(self, prdid):
        try:
            productDetails = self.repo.get_by_id(prdid)
            print(f"Product or Category - '{prdid}' feteched sucessfully.")
            if not productDetails:
                return None
            self.repolog.log_action("Feteched Product id by key Search from DB")
            return entity_to_dto(productDetails)
        except Exception as e:
            print("In ProductDetailsService class - get_all_products Method failed:", e)
            return []

    async def stockMgmt(self):
        try:
            print("Below Stocks are going below Limit of 3 Qty")
            productDetails = self.repo.get_all()
            product_dto_list = [
                entity_to_dto(p)
                for p in productDetails
                if p is not None and p.PRD_QTY < 3
            ]
            print(product_dto_list)
            self.repolog.log_action("Load Stock Mangement from DB")
            return product_dto_list
        except Exception as e:
            print("In ProductDetailsService class - stockMgmt Method failed:", e)
            return []

    async def stockReports(self):
        try:
            productDetails = self.repo.get_all()
            product_summary = {}
            for p in productDetails:
                product_summary[p.PRD_NAME] = product_summary.get(p.PRD_NAME, 0) + (
                    p.PRD_PRICE * p.PRD_QTY
                )

            print("Total Inventory Value By Product :", product_summary)
            category_summary = {}
            for p in productDetails:
                category_summary[p.PRD_CATEGORY] = (
                    category_summary.get(p.PRD_CATEGORY, 0) + p.PRD_QTY
                )
            self.repolog.log_action("Load Reports from DB")
            print("Total Stock Qty by Category-wise ", category_summary)
            return {
                "product_summary": product_summary,
                "category_summary": category_summary,
            }
        except Exception as e:
            print("In ProductDetailsService class - stockReports Method failed:", e)
            return {"product_summary": {}, "category_summary": {}}

    async def productDetailsExport(self):
        try:
            productDetails = self.repo.get_all()
            df = pd.DataFrame(
                [
                    {
                        "product Id": p.PRD_ID,
                        "Product Name": p.PRD_NAME,
                        "Product Catgeory": p.PRD_CATEGORY,
                        "Product Quantity": p.PRD_QTY,
                        "Product Price": p.PRD_PRICE,
                        "Product Supplier": p.PRD_SUPPLIER,
                    }
                    for p in productDetails
                ]
            )
            # Ensure directory exists
            os.makedirs(EXPORT_PATH, exist_ok=True)

            # Timestamp format
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            # File path
            file_path = os.path.join(EXPORT_PATH, f"products_{timestamp}.csv")

            # Save file
            df.to_csv(file_path, index=False)
            self.repolog.log_action("ProductDetails Export from DB")
            print(f"Exported successfully to: {file_path}")
            return "Exported successfully to:" + file_path
        except Exception as e:
            print(
                "In ProductDetailsService class - productDetailsExport Method failed:",
                e,
            )
            return ""

    async def productDetailsImport(self):
        try:
            print("Started Reading Data from CSV file...")
            # Ensure folders exist
            os.makedirs(IMPORT_PATH, exist_ok=True)
            files = [f for f in os.listdir(IMPORT_PATH) if f.endswith(".csv")]
            if files:
                for file in files:
                    file_path = os.path.join(IMPORT_PATH, file)
                    try:
                        df = pd.read_csv(file_path)
                        for _, row in df.iterrows():
                            productDetails = ProductDetails(
                                PRD_NAME=row.get("Product Name"),
                                PRD_CATEGORY=row.get("Product Catgeory"),
                                PRD_QTY=int(row.get("Product Quantity", 0)),
                                PRD_PRICE=float(row.get("Product Price", 0)),
                                PRD_SUPPLIER=row.get("Product Supplier", "bulk"),
                                PRD_ROLE="admin",
                            )
                            self.repo.create(productDetails)
                            self.repolog.log_action("ProductDetails Import from DB")
                        print(f"Imported CSV File Sucessfully : {file}")
                    except Exception as e:
                        print(f"Error processing {file}: {e}")
            else:
                print("No CSV files found in import folder")
            return "Suceefully read files from :" + file_path
        except Exception as e:
            print(
                "In ProductDetailsService class - productDetailsImport Method failed:",
                e,
            )
        return ""

    async def productTransLog(self):
        try:
            print("Get all transaction log details")
            InvenotryMgmtOprLog = self.repolog.get_all_Log()
            invenotryMgmtOprLog_list = []
            invenotryMgmtOprLog_list = [
                entityimol_to_imoldto(p) for p in InvenotryMgmtOprLog
            ]
            return invenotryMgmtOprLog_list
        except Exception as e:
            print(
                "In ProductDetailsService class - productTransLog Method failed:",
                e,
            )
            return []
