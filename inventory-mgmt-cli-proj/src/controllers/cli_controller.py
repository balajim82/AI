from src.services.product_service import ProductDetailsService
from src.dto.product_dto import ProductDetailsDTO


def launch_app():
    service = ProductDetailsService()

    role = input("Enter role (admin/reader): ").lower()

    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Modify Product")
        print("5. Delete Product")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            if role != "admin":
                print("Permission denied")
                continue

            dto = ProductDetailsDTO(
                prdName=input("Name: "),
                prdCategory=input("Category: "),
                prdQuantity=float(input("Quantity: ")),
                prdPrice=float(input("Price: ")),
                prdSupplier=input("Supplier: "),
                prdRole=role,
            )
            service.create_product(dto)

        elif choice == "2":
            service.get_all_products()

        elif choice == "3":
            prdSearch = input("Enter Product Name or Category: ")
            service.search_products(prdSearch)

        elif choice == "4":
            if role != "admin":
                print("Permission denied")
                continue
            service.update_product(role)

        elif choice == "5":
            if role != "admin":
                print("Permission denied")
                continue
            service.delete_product()

        elif choice == "6":
            break
