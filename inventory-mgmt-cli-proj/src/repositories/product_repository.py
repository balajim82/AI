from src.database.db import SessionLocal
from src.database.models import ProductDetails


class ProductDetailsRepository:

    def create(self, productDetails):
        try:
            session = SessionLocal()
            session.add(productDetails)
            session.commit()
            session.close()
        except Exception as e:
            print("In ProductDetailsRepository class - create Method failed:", e)

    def get_all(self):
        try:
            session = SessionLocal()
            data = session.query(ProductDetails).all()
            session.close()
            return data
        except Exception as e:
            print("In ProductDetailsRepository class - get_all Method failed:", e)

    def search(self, prdSearch):
        try:
            session = SessionLocal()
            data = (
                session.query(ProductDetails)
                .filter(
                    (ProductDetails.PRD_NAME.like(f"%{prdSearch}%"))
                    | (ProductDetails.PRD_CATEGORY.like(f"%{prdSearch}%"))
                )
                .all()
            )
            session.close()
            return data
        except Exception as e:
            print("In ProductDetailsRepository class - search Method failed:", e)

    def get_by_id(self, prdId):
        try:
            session = SessionLocal()
            productDetails = session.get(ProductDetails, prdId)
            session.close()
            return productDetails
        except Exception as e:
            print("In ProductDetailsRepository class - get_by_id Method failed:", e)

    def update(self, productDetails):
        try:
            session = SessionLocal()
            session.merge(productDetails)
            session.commit()
            session.close()
        except Exception as e:
            print("In ProductDetailsRepository class - update Method failed:", e)

    def delete(self, productDetails):
        try:
            session = SessionLocal()
            session.delete(productDetails)
            session.commit()
            session.close()
        except Exception as e:
            print("In ProductDetailsRepository class - delete Method failed:", e)
