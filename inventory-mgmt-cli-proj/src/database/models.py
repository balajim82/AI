from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ProductDetails(Base):
    __tablename__ = "PRODUCT_DETAILS"

    PRD_ID = Column(Integer, primary_key=True, index=True)
    PRD_NAME = Column(String(100))
    PRD_CATEGORY = Column(String(50))
    PRD_QTY = Column(Float)
    PRD_PRICE = Column(Float)
    PRD_SUPPLIER = Column(String(100))
    PRD_ROLE = Column(String(50))
