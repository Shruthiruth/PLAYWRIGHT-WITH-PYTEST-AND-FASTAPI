from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI() 


# Define a route for the root URL --- decorator to specify the HTTP method and path
@app.get('/')
def read_root():
    return {"message": "Hello, there!"}  # Return a JSON response with a message


@app.get('/property')
def read_property():
    return {"property": "This is a property endpoint."}  # Return a JSON response with a property message

@app.get('/movies')
def read_movies():
    return {"movies": {"3", "Inception"}}  # Return a JSON response with a movies message