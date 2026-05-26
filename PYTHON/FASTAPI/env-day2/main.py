from fastapi import FastAPI
from pydantic import BaseModel

class Profile(BaseModel):
    username: str
    email: str
    age: int
    price: int

class Product(BaseModel):
    name: str
    price: int
    discount: int = 0
    discounted_price: int = 0
    
    
class User(BaseModel):
    username: str
    email: str
    age: int
# Create a FastAPI instance
app = FastAPI()

# Define a route for the root URL --- decorator to specify the HTTP method and path
@app.get('/')
def read_root():
    return {"message": "Hello, there!"}  # Return a JSON response with a message

@app.get('/property/{id}')
def read_property(id: int):
    return {f"property": f"This is property {id}."}  # Return a JSON response with a property message

@app.get('/profile/{username}')
def read_profile(username: str):
    return {f"username": f"hii {username}"}  # Return a JSON response with the username

@app.get('/movies')
def read_movies():
    return {"movies": {"3", "Inception"}}  # Return a JSON response with a movies message

@app.get('/users/{username}/admin')
def read_admin(username: str):
    if username == "admin":
        return {"message": "Welcome Admin!"}  # Return a JSON response with a welcome message for admin
    else:
        return {"message": f"Welcome {username}!"}  # Return a JSON response with a welcome message for other users
    
@app.get('/users/{username}/profile')
def read_user(username: str, age: int = 0, price: int = 0):
    return {"username": f"Hello Welcome profile, {username}!", "age": age, "price": price}  # Return a JSON response with the username, age, and price


@app.post('/users')
def create_user(profile: Profile):
    return {'add user': profile}

@app.post('/addproducts/{product_id}')
def add_product(product_id:int,product: Product):
    product.discounted_price = product.price - (product.price * product.discount / 100)
    return {"product": product, "product_id": product_id}

@app.get('/products')
def read_products(product: Product):
    return {"products": [{"name": product.name, "price": product.price}]}

@app.post('/user/products')
def add_user_product(user: User, product: Product):
    return {"user": user, "product": product}