from src.repositories.product_repository import ProductDetailsRepository
from src.repositories.inv_mgmt_opr_log_repository import InventoryMgmtOprLogRepository
from src.mappers.product_mapper import dto_to_entity
import os
import pandas as pd
from datetime import datetime
from config import EXPORT_PATH, IMPORT_PATH
from src.database.models import ProductDetails


class ProductDetailsService:

    def __init__(self):
        self.repo = ProductDetailsRepository()
        self.repolog = InventoryMgmtOprLogRepository()

    def create_product(self, dto):
        if dto.prdPrice <= 0:
            print("Invalid price")
            return

        productDetails = dto_to_entity(dto)
        self.repo.create(productDetails)
        self.repolog.log_action("Saved new Product into DB")
        print("Created Product Details sucessfully.")

    def get_all_products(self):
        productDetails = self.repo.get_all()
        for p in productDetails:
            print(
                p.PRD_ID,
                p.PRD_NAME,
                p.PRD_CATEGORY,
                p.PRD_QTY,
                p.PRD_PRICE,
                p.PRD_SUPPLIER,
                p.PRD_ROLE,
            )
        self.repolog.log_action("Feteched All products from DB")
        print("Loaded All Product Details sucessfully.")

    def search_products(self, prdSearch):
        results = self.repo.search(prdSearch)
        print(f"Product or Category - '{prdSearch}' feteched sucessfully.")
        self.repolog.log_action("Feteched products by key Search from DB")
        for p in results:
            print(
                p.PRD_ID,
                p.PRD_NAME,
                p.PRD_CATEGORY,
                p.PRD_QTY,
                p.PRD_PRICE,
                p.PRD_SUPPLIER,
                p.PRD_ROLE,
            )

    def update_product(self, prdRole):
        prdId = int(input("Enter ID: "))
        productDetails = self.repo.get_by_id(prdId)

        if not productDetails:
            print("Not found")
            return
        productDetails.PRD_QTY = int(input("New quantity: "))
        productDetails.PRD_PRICE = float(input("New price: "))
        productDetails.PRD_ROLE = prdRole
        self.repo.update(productDetails)
        self.repolog.log_action("Updated Products into DB")
        print("Updated Product Details sucessfully.")

    def delete_product(self):
        prdId = int(input("Enter ID: "))
        productDetails = self.repo.get_by_id(prdId)

        if not productDetails:
            print("Product Not found", prdId)
            return

        confirm = input("Confirm delete (y/n): ")
        if confirm.lower() == "y":
            self.repo.delete(productDetails)
            self.repolog.log_action("Deleted Products from DB")
        print("Deleted Product Details sucessfully.")

    def stockMgmt(self):
        print("Below Stocks are going below Limit of 3 Qty")
        productDetails = self.repo.get_all()
        self.repolog.log_action("Load Stock Mangement from DB")
        for p in productDetails:
            if p.PRD_QTY < 3:
                print(f"LOW STOCK Qty: {p.PRD_NAME} | Qty: {p.PRD_QTY}")

    def stockReports(self):
        productDetails = self.repo.get_all()
        product_summary = {}
        for p in productDetails:
            product_summary[p.PRD_NAME] = product_summary.get(p.PRD_NAME, 0) + (
                p.PRD_PRICE * p.PRD_QTY
            )
        self.repolog.log_action("Load Reports from DB")
        print("Total Inventory Value By Product :", product_summary)

        category_summary = {}
        for p in productDetails:
            category_summary[p.PRD_CATEGORY] = (
                category_summary.get(p.PRD_CATEGORY, 0) + p.PRD_QTY
            )

        print("Total Stock Qty by Category-wise ", category_summary)

    def productDetailsExport(self):
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

    def productDetailsImport(self, role):
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
                            PRD_ROLE=role,
                        )
                        self.repo.create(productDetails)
                        self.repolog.log_action("ProductDetails Import from DB")
                    print(f"Imported CSV File Sucessfully : {file}")
                except Exception as e:
                    print(f"Error processing {file}: {e}")
        else:
            print("No CSV files found in import folder")

    def productTransLog(self):
        print("Get all transaction log details")
        InvenotryMgmtOprLog = self.repolog.get_all_Log()
        for p in InvenotryMgmtOprLog:
            print(
                p.IMOL_ID,
                p.IMOL_ACTION,
                p.IMOL_TIMESTAMP,
            )
