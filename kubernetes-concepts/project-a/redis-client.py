import redis

def test_redis_connection():
    try:
        # Connect to Redis server
        client = redis.Redis(host='localhost', port=6379, decode_responses=True)

        # Set a key-value pair
        client.set('test_key', 'Hello, Kubernetes!')

        # Retrieve the value
        value = client.get('test_key')
        print(f"Value for 'test_key': {value}")

        if value == 'Hello, Kubernetes!':
            print("Redis server is working correctly!")
        else:
            print("Unexpected value received from Redis.")
    except Exception as e:
        print(f"Error connecting to Redis: {e}")

if __name__ == "__main__":
    test_redis_connection()
