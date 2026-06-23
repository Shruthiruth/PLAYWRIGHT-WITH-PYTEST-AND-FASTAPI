from fastapi import APIRouter , status , Response , HTTPException
from typing import List
from sqlalchemy.orm import Session
from fastapi.params import Depends
from ..database import get_db
from .. import models, schemas


router = APIRouter(
    tags=["Products"],
    prefix="/product"
)

@router.delete('/{id}')
def delete_product(id:int, db : Session = Depends(get_db)):
    db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    db.commit()
    return {"product": f"Product with id {id} has been deleted successfully."}

@router.get('/', response_model=List[schemas.ProductResponse])
def get_products(db : Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@router.get('/{id}', response_model=schemas.ProductResponse)
def get_productby_id(id:int, db : Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} does not exist.")  
    return product

@router.post('/',status_code=status.HTTP_201_CREATED)
def add_product(request: schemas.Product, db : Session = Depends(get_db)):
    new_product = models.Product(name=request.name, price=request.price, description=request.description , seller_id=1) #seller_id is hardcoded for now, you can modify it to accept seller_id from the request if needed
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"product": new_product}

@router.put('/{id}')
def update_product(id:int, request: schemas.Product, db : Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        return {"product": f"Product with id {id} does not exist."}
    product.update(request.dict())
    db.commit()
    return {"product": f"Product with id {id} has been updated successfully."}