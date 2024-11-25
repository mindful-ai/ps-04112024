import random
import time

def transaction_stream():
    """Generator function to simulate a streaming data source."""
    while True:
        yield {
            "amount": round(random.uniform(10, 5000), 2),          # Transaction amount
            "time_of_day": random.randint(0, 23),                  # Hour of transaction
            "transaction_type": random.choice([0, 1]),             # 0=debit, 1=credit
            "is_fraud": random.choice([0, 1])                     # 0=legit, 1=fraud
        }
        time.sleep(0.1)  # Simulate 10 transactions per second

if __name__ == "__main__":
    stream = transaction_stream()
    for transaction in stream:
        print(transaction)  # Print simulated data
