from fastapi import HTTPException, Depends

# Simulated authentication dependency
def get_current_user(token: str):
    # Simulate token validation
    if token == "valid-token":
        return {"username": "rakesh", "role": "user"}
    else:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

# Dependency to inject
def authenticated_user(token: str = "valid-token"):  # Default token for simplicity
    return get_current_user(token)
