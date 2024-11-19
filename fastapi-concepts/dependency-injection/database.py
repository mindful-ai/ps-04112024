from contextlib import contextmanager

# Simulated database session
@contextmanager
def get_db_session():
    db = {"connection": "active"}  # Simulated DB connection
    try:
        print("Opening database session...")
        yield db
    finally:
        print("Closing database session...")
        db["connection"] = "closed"
