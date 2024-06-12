from app.core.models import Product as ProductModel


class ProductService():
    
    def __init__(self, db) -> None:
        self.db = db


    def get_products(self):
        result = self.db.query(ProductModel).all()
        return result