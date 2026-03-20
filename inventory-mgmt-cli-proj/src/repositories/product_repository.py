from src.database.db import SessionLocal
from src.database.models import ProductDetails


class ProductDetailsRepository:

    def create(self, productDetails):
        session = SessionLocal()
        session.add(productDetails)
        session.commit()
        session.close()

    def get_all(self):
        session = SessionLocal()
        data = session.query(ProductDetails).all()
        session.close()
        return data

    def search(self, prdSearch):
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

    def get_by_id(self, prdId):
        session = SessionLocal()
        productDetails = session.get(ProductDetails, prdId)
        session.close()
        return productDetails

    def update(self, productDetails):
        session = SessionLocal()
        session.merge(productDetails)
        session.commit()
        session.close()

    def delete(self, productDetails):
        session = SessionLocal()
        session.delete(productDetails)
        session.commit()
        session.close()
