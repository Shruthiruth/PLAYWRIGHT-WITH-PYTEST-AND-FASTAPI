from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI() 


# Define a route for the root URL --- decorator to specify the HTTP method and path
@app.get('/')
def read_root():
    return {"message": "Hello, there!"}  # Return a JSON response with a message

#id is a path parameter that can be accessed in the functio
@app.get('/property/{id}')
def read_property(id: int):
    return {f"property": f"This is property {id}."}  # Return a JSON response with a property message

@app.get('/profile/{username}')
def read_profile(username: str):
    return {f"username": f"hii {username}"}  # Return a JSON response with the username

@app.get('/movies')
def read_movies():
    return {"movies": {"3", "Inception"}}  # Return a JSON response with a movies message

@app.get('/users/admin')
def read_admin():
    return {"message": "Welcome Admin!"}  # Return a JSON response with a welcome message for admin

@app.get('/users/{username}')
def read_user(username: str):
    return {"username": f"Hello Welcome profile, {username}!"}  # Return a JSON response with the username

@app.get('/products')
def read_products(id: int,price:int=0):
    return {f"products with ID {id}": f"Details for product price {price}"}  # Return a JSON response with a list of products

@app.get('/profile/{username}/details')
def read_profile_details(username: str, age: int = 0):
    return {f"profile details for {username}": f"Age: {age}"}  # Return a JSON response with profile details including age                  