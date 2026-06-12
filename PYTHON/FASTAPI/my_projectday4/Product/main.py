from fastapi import FastAPI
from .import schemas
from .import models
from .database import engine
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post('/product')
def add_product(request: schemas.Product):
    return {"product": request}