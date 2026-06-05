from fastapi import FastAPI,Form,HTTPException
from pydantic import BaseModel,Field
from typing import List,Set
from pydantic import HttpUrl
from uuid import UUID
from datetime import datetime, date, time,timedelta


    

class Image(BaseModel):
    url: HttpUrl
    alt_text: str
    
class Product(BaseModel):
    name: str
    price: int = Field(title="Price of the product", gt=0 , description="Price of the product")  # Price must be a non-negative integer
    discount: int = Field(0, ge=0, le=100)  # Discount percentage between 0 and 100
    discounted_price: int = 0
    tags: Set[str] = []  # Set of tags for the product
    images: List[Image] = []  # List of images for the product
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Phone",
                "price": 100,
                "discount": 10,
                "discounted_price": 0,
                "tags": ["electronics", "sale"],
                "images": [
                    {"url": "http://example.com/image1.jpg", "alt_text": "Image 1"},
                    {"url": "http://example.com/image2.jpg", "alt_text": "Image 2"}
                ]
            }
        }
    
class Offer(BaseModel):
    name: str
    description: str
    price: float
    products: List[Product]
    
class Event(BaseModel):
    event_id: UUID
    start_date: date
    start_time: datetime
    end_time: datetime
    repeat_time: time
    execution_time: timedelta
    
# class Square(BaseModel):
#     value: float
    
#     @property
#     def area(self) -> float:
#         return self.value ** 2


class Product_item(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Price must be a positive number")
    
    
class Numbers(BaseModel):
    a: float

    b: float
    
    def sum(self) -> float:
        return self.a + self.b
    
    def subtract(self) -> float :
        return self.a - self.b
    
    def multiply(self) -> float:
        return self.a * self.b
    
    def divide(self) -> float:
        if self.b == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        return self.a / self.b
   
    
app = FastAPI()
    
@app.post('/addoffers')
def add_offers(offers: Offer):
    return {"offer": offers}


@app.post('/addevents')
def add_events(events: Event):
    return {"event": events}

@app.post('/login')
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}

@app.get('/square/{value}')
def square(value: float):
    return {"square": value ** 2}

@app.get('/add')
def add(a:int,b:int):
    return {"result": a + b}

@app.post('/addproductitem')
def add_product_item(product_item: Product_item):
    return {"product_item": product_item}

@app.post('/calculations')
def calculations(numbers: Numbers):
    return {
        "sum": numbers.sum(),
        "subtract": numbers.subtract(),
        "multiply": numbers.multiply(),
        "divide": numbers.divide()
    }
    
@app.get('/calculation')
def calculation(a: float, b: float):
    numbers = Numbers(a=a, b=b)
    return {
        "sum": numbers.sum(),
        "subtract": numbers.subtract(),
        "multiply": numbers.multiply(),
        "divide": numbers.divide()
    }