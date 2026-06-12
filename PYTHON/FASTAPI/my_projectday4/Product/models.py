from sqlalchemy import Column, Integer, String
from .database import Base


class Product():
    __tablename__ = "products" #database model class 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    
    