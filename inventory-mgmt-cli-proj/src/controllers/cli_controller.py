from src.services.product_service import ProductDetailsService
from src.dto.product_dto import ProductDetailsDTO


def launch_app():
    service = ProductDetailsService()

    role = input("Enter role (admin/reader): ").lower()
    if role in ("admin", "reader"):
        while True:
            print("\n--- Inventory Management System ---")
            print("1. Add Product")
            print("2. View Products")
            print("3. Search Product")
            print("4. Modify Product")
            print("5. Delete Product")
            print("6. Stock Management")
            print("7. Reports")
            print("8. Data Export(CSV)")
            print("9. Data Import(CSV)")
            print("10.Search Transactiion Log By Date time")
            print("11. Exit")

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
                service.stockMgmt()

            elif choice == "7":
                if role != "admin":
                    print("Permission denied")
                    continue
                service.stockReports()

            elif choice == "8":
                if role != "admin":
                    print("Permission denied")
                    continue
                service.productDetailsExport()

            elif choice == "9":
                if role != "admin":
                    print("Permission denied")
                    continue
                service.productDetailsImport(role)

            elif choice == "10":
                if role != "admin":
                    print("Permission denied")
                    continue
                service.productTransLog()

            elif choice == "11":
                break
    else:
        print("you have entered role Wrong name")
