import boto3
import json
import numpy as np

# Define the endpoint name
endpoint_name = "california-housing-endpoint"  # Replace with your actual endpoint name

# Initialize SageMaker runtime client
runtime = boto3.client("sagemaker-runtime")

# Prepare a sample input (ensure it matches the training data format)
test_sample = [[8.3252, 41.0, 6.984127, 1.02381, 322.0, 2.555556, 37.88, -122.23]]   

# Invoke the endpoint
response = runtime.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType="application/json",
    Body=json.dumps(test_sample),
)

# Parse and print the response
prediction = json.loads(response["Body"].read().decode())
print(f"Prediction: {prediction}")
