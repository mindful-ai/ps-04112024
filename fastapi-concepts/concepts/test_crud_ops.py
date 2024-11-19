import requests
import json

BASE_URL = "http://127.0.0.1:8000"  # URL for the FastAPI app

# Sample user data
user_data = {
    "name": "John Doe",
    "age": 25,
    "email": "johndoe@example.com",
    "role": "user",
    "signup_date": "2024-11-18T14:00:00",
    "address": {
        "street": "456 Elm St",
        "city": "Chicago",
        "country": "USA"
    },
    "preferences": {
        "newsletter": True,
        "notifications": True
    },
    "is_active": True,
    "friends": ["Alice", "Bob"]
}

# 1. Test POST request - Create a user
def test_create_user():
    response = requests.post(f"{BASE_URL}/users/", json=user_data)
    assert response.status_code == 200, f"Error: {response.status_code}"
    created_user = response.json()
    assert created_user["name"] == user_data["name"], "Name mismatch"
    assert created_user["email"] == user_data["email"], "Email mismatch"
    print("Create User Test Passed")

# 2. Test GET request - Get a user by ID
def test_get_user():
    # First, create a user to fetch
    response = requests.post(f"{BASE_URL}/users/", json=user_data)
    user_id = response.json()["id"]
    
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200, f"Error: {response.status_code}"
    user = response.json()
    assert user["name"] == user_data["name"], "Name mismatch"
    print("Get User Test Passed")

# 3. Test GET request - List all users
def test_list_users():
    response = requests.get(f"{BASE_URL}/users/")
    assert response.status_code == 200, f"Error: {response.status_code}"
    users = response.json()
    assert len(users) > 0, "No users found"
    print("List Users Test Passed")

# 4. Test PUT request - Update a user
def test_update_user():
    # First, create a user
    response = requests.post(f"{BASE_URL}/users/", json=user_data)
    user_id = response.json()["id"]
    
    updated_user_data = user_data.copy()
    updated_user_data["name"] = "John Updated"
    
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=updated_user_data)
    assert response.status_code == 200, f"Error: {response.status_code}"
    updated_user = response.json()
    assert updated_user["name"] == "John Updated", "Name did not update"
    print("Update User Test Passed")

# 5. Test DELETE request - Delete a user
def test_delete_user():
    # First, create a user to delete
    response = requests.post(f"{BASE_URL}/users/", json=user_data)
    user_id = response.json()["id"]
    
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200, f"Error: {response.status_code}"
    deleted_user = response.json()
    assert deleted_user["id"] == user_id, "Deleted user ID mismatch"
    
    # Try fetching the deleted user to ensure they are removed
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 404, "User still exists after deletion"
    print("Delete User Test Passed")

# Run all tests
def run_tests():
    test_create_user()
    test_get_user()
    test_list_users()
    test_update_user()
    test_delete_user()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
