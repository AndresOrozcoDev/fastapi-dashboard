from app.core.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


class Supermarket(Base):
    __tablename__ = 'supermarket'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    product = relationship('Product', back_populates='supermarket')


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    product = relationship('Product', back_populates='category')


class Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    value = Column(Integer)
    unit = Column(String)
    created = Column(String)
    supermarket_id = Column(Integer, ForeignKey('supermarket.id', ondelete='CASCADE'))
    supermarket = relationship('Supermarket', back_populates='product')
    category_id = Column(Integer, ForeignKey('category.id', ondelete='CASCADE'))
    category = relationship('Category', back_populates='product')