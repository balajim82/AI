from src.repositories.product_repository import ProductDetailsRepository
from src.mappers.product_mapper import dto_to_entity


class ProductDetailsService:

    def __init__(self):
        self.repo = ProductDetailsRepository()

    def create_product(self, dto):
        if dto.prdPrice <= 0:
            print("Invalid price")
            return

        productDetails = dto_to_entity(dto)
        self.repo.create(productDetails)
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

    print("Loaded All Product Details sucessfully.")

    def search_products(self, prdSearch):
        results = self.repo.search(prdSearch)
        print(f"Product or Category - '{prdSearch}' feteched sucessfully.")
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
        print("Deleted Product Details sucessfully.")
