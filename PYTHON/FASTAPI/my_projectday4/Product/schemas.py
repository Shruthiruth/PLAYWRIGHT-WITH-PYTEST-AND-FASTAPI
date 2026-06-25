from typing import Optional

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
    
class Login(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username:Optional[str] = None
    