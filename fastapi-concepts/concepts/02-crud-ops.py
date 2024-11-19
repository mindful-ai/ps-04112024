from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, validator
from enum import Enum
from typing import List, Optional
from datetime import datetime

# Initialize FastAPI app
app = FastAPI()

# In-memory user store (simulating a database)
users_db = {}

# Enum for user role
class UserRole(str, Enum):
    admin = "admin"
    user = "user"
    moderator = "moderator"

# Pydantic model for address
class Address(BaseModel):
    street: str
    city: str
    country: str

    @validator('street')
    def validate_street(cls, v):
        if len(v) < 5:
            raise ValueError('Street name must be at least 5 characters long.')
        return v

# Pydantic model for preferences
class Preferences(BaseModel):
    newsletter: bool
    notifications: bool

# Pydantic model for User
class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    role: UserRole
    signup_date: datetime
    address: Address
    preferences: Preferences
    is_active: bool
    friends: Optional[List[str]] = []

    @validator('age')
    def validate_age(cls, v):
        if v < 18:
            raise ValueError('Age must be at least 18.')
        return v

# Create a new user (POST request)
@app.post("/users/", response_model=User)
def create_user(user: User):
    user_id = len(users_db) + 1  # Simple ID generator
    users_db[user_id] = user
    return user

# Get a user by ID (GET request)
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    if user_id in users_db:
        return users_db[user_id]
    raise HTTPException(status_code=404, detail="User not found")

# Get a list of all users (GET request)
@app.get("/users/", response_model=List[User])
def get_users():
    return list(users_db.values())

# Update a user's information (PUT request)
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    if user_id in users_db:
        users_db[user_id] = user
        return user
    raise HTTPException(status_code=404, detail="User not found")

# Delete a user by ID (DELETE request)
@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int):
    if user_id in users_db:
        deleted_user = users_db.pop(user_id)
        return deleted_user
    raise HTTPException(status_code=404, detail="User not found")

# Route to retrieve a greeting message (just to check the app is working)
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with CRUD operations!"}
