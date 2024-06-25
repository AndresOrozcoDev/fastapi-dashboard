from app.core.models import Category as CategoryModel


class CategoriesService():
    
    def __init__(self, db) -> None:
        self.db = db


    def get_categories(self):
        result = self.db.query(CategoryModel).all()
        return result
    

    def get_category_by_id(self, id: int):
        result = self.db.query(CategoryModel).filter(CategoryModel.id == id).first()
        return result
    

    def get_category_by_name(self, name: str):
        result = self.db.query(CategoryModel).filter(CategoryModel.name == name).first()
        return result
    

    def create_category(self, name: str):
        new = CategoryModel(**{"name": name})
        self.db.add(new)
        self.db.commit()
        return 
    

    def update_category(self, id: int, name: str):
        exists = self.get_category_by_id(id)
        if not exists:
            return False, exists
        else:
            category = self.db.query(CategoryModel).filter(CategoryModel.id == id).first()
            category.name = name
            self.db.commit()
            return True, category
    

    def delete_category(self, id: int):
        exists = self.get_category_by_id(id)
        if not exists:
            return False, exists
        else:
            self.db.query(CategoryModel).filter(CategoryModel.id == id).delete()
            self.db.commit()
            return True, exists