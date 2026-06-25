from fastapi import FastAPI
from .import models
from .database import engine
from .routers import product , seller , login

app = FastAPI(
    
    title="Product API",
    description="This is a Product API built with FastAPI and SQLAlchemy.",
    terms_of_service="https://shruthi-portfolio-two.vercel.app/",
    contact={
        "Developer Name": "Shruthi",
        "url": "https://shruthi-portfolio-two.vercel.app/",
        "email": "shruthiruth21@gmail.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/license/mit/"
    },
    docs_url="/docs",
    
)
app.include_router(product.router) #include the product router to the main app
app.include_router(seller.router) #include the seller router to the main app
app.include_router(login.router) #include the login router to the main app
models.Base.metadata.create_all(bind=engine) #create the database tables based on the models defined in models.py








