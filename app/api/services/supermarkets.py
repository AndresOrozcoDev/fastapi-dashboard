from app.core.models import Supermarket as SupermarketModel


class SupermarketService():
    
    def __init__(self, db) -> None:
        self.db = db


    def get_supermarkets(self):
        result = self.db.query(SupermarketModel).all()
        return result
    

    def get_supermarket_by_id(self, id: int):
        result = self.db.query(SupermarketModel).filter(SupermarketModel.id == id).first()
        return result
    

    def get_supermarket_by_name(self, name: str):
        result = self.db.query(SupermarketModel).filter(SupermarketModel.name == name).first()
        return result
    

    def create_supermarket(self, name: str):
        new = SupermarketModel(**{"name": name})
        self.db.add(new)
        self.db.commit()
        return 
    

    def update_supermarket(self, id: int, name: str):
        supermarket = self.get_supermarket_by_id(id)
        if not supermarket:
            return False
        else:
            supermarket = self.db.query(SupermarketModel).filter(SupermarketModel.id == id).first()
            supermarket.name = name
            self.db.commit()
            return True, supermarket
    

    def delete_supermarket(self, id: int):
        supermarket = self.get_supermarket_by_id(id)
        if not supermarket:
            return False, supermarket
        else:
            self.db.query(SupermarketModel).filter(SupermarketModel.id == id).delete()
            self.db.commit()
            return True, supermarket