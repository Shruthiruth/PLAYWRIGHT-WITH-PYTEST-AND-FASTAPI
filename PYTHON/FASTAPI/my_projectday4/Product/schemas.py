from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: int
    description: str = None
    
    
class ProductResponse(BaseModel):
    name: str
    description: str
    

    class Config:
        orm_mode = True