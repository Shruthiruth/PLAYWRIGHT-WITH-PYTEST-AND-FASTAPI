from typing import List

from fastapi import FastAPI , status , Response , HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from .import schemas
from .import models
from .database import engine, SessionLocal
app = FastAPI()

models.Base.metadata.create_all(bind=engine) #create the database tables based on the models defined in models.py


def get_db(): #get session for database --- get access to database
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.delete('/product/{id}')
def delete_product(id:int, db : Session = Depends(get_db)):
    db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    db.commit()
    return {"product": f"Product with id {id} has been deleted successfully."}

@app.get('/products', response_model=List[schemas.ProductResponse])
def get_products(db : Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@app.get('/product/{id}', response_model=schemas.ProductResponse)
def get_productby_id(id:int, db : Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} does not exist.")  
    return product

@app.post('/product',status_code=status.HTTP_201_CREATED)
def add_product(request: schemas.Product, db : Session = Depends(get_db)):
    new_product = models.Product(name=request.name, price=request.price, description=request.description)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"product": new_product}

@app.put('/product/{id}')
def update_product(id:int, request: schemas.Product, db : Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        return {"product": f"Product with id {id} does not exist."}
    product.update(request.dict())
    db.commit()
    return {"product": f"Product with id {id} has been updated successfully."}