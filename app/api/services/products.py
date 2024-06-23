from datetime import datetime
from app.core.models import Product as ProductModel
from app.core.schemas import Product as ProductInterface
from app.api.services.categories import CategoriesService
from app.api.services.supermarkets import SupermarketService


class ProductService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_products(self):
        result = self.db.query(ProductModel).all()
        return result


    def get_product_by_id(self, id: int):
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        return result


    def create_product(self, product: ProductInterface):
        existsSupermarket = SupermarketService(self.db).get_supermarket_by_id(product.supermarket_id)
        existsCategory = CategoriesService(self.db).get_category_by_id(product.category_id)

        if existsSupermarket is None:
            return 'Not found supermerkat', False
        elif existsCategory is None:
            return 'Not found category', False
        else:
            new = ProductModel(**{
                "name": product.name,
                "price": product.price,
                "value": product.value,
                "unit": product.unit,
                "created": datetime.now(),
                "supermarket_id": product.supermarket_id, 
                "category_id": product.category_id, 
            })
            self.db.add(new)
            self.db.commit()
            return 'Product created', True


    def update_product(self, id: int, product: ProductInterface):
        exists = self.get_product_by_id(id)
        if not exists:
            return False
        else:
            product = self.db.query(ProductModel).filter(ProductModel.id == id).first()
            product.name = product.name
            product.price = product.price
            product.value = product.value
            product.unit = product.unit
            product.created = product.created
            product.supermarket_id = product.supermarket_id
            product.category_id = product.category_id
            self.db.commit()
            return True, product
    

    def delete_product(self, id: int):
        product = self.get_product_by_id(id)
        if not product:
            return False, product
        else:
            self.db.query(ProductModel).filter(ProductModel.id == id).delete()
            self.db.commit()
            return True, product