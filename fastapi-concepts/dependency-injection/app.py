from fastapi import FastAPI, Depends
from auth import authenticated_user
from database import get_db_session

app = FastAPI()

# Dependency for database session
def db_dependency():
    with get_db_session() as db:
        yield db

# Route with both dependencies: authentication and database
@app.get("/items/")
def read_items(
    user: dict = Depends(authenticated_user),  # Inject authenticated user
    db: dict = Depends(db_dependency)         # Inject database session
):
    return {
        "message": "Data fetched successfully",
        "user": user,
        "database_connection": db["connection"]
    }
