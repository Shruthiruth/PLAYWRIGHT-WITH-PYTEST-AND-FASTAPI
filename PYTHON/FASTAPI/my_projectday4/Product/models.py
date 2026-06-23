from sqlalchemy import Column, Integer, String , ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "products" #database model class 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    seller_id = Column(Integer, ForeignKey("sellers.id")) #foreign key to link product to seller
    seller = relationship("Seller", back_populates="products") #relationship to access seller information from product
    
class Seller(Base):
    __tablename__= "sellers"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    products = relationship("Product", back_populates="seller") #relationship to access products from seller