class ProductDetailsDTO:
    def __init__(
        self, prdName, prdCategory, prdQuantity, prdPrice, prdSupplier, prdRole
    ):
        self.prdName = prdName
        self.prdCategory = prdCategory
        self.prdQuantity = prdQuantity
        self.prdPrice = prdPrice
        self.prdSupplier = prdSupplier
        self.prdRole = prdRole
