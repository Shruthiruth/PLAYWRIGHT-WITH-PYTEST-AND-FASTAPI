from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: int
    description: str = None
    
class SellerResponse(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True
        
class ProductResponse(BaseModel):
    name: str
    description: str
    seller: SellerResponse

    class Config:
        from_attributes = True
        
class Seller(BaseModel):
    username: str
    email: str
    password: str
    
