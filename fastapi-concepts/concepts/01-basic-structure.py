from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI app instance
app = FastAPI()

# Define a Pydantic model for POST request
class Item(BaseModel):
    name: str
    price: float
    description: str = None

# Define a GET route
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Define a POST route
@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price, "description": item.description}
