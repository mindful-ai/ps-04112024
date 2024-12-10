import boto3
import json

# Initialize the boto3 client for Lambda
lambda_client = boto3.client('lambda')

def invoke_preprocess_data(features):
    # Prepare the input data
    payload = {
        'features': features
    }

    # Invoke the PreprocessData Lambda function
    response = lambda_client.invoke(
        FunctionName='PreprocessData',  # Name of the PreprocessData Lambda function
        InvocationType='RequestResponse',  # Synchronous invocation
        Payload=json.dumps(payload)  # Send input as JSON
    )
    
    # Read the response from the Lambda function
    response_payload = json.loads(response['Payload'].read())
    
    # Get the preprocessed data
    processed_data = response_payload['input_data']
    
    return processed_data


def invoke_load_model_and_predict(processed_data):
    # Prepare the input data for prediction
    payload = {
        'input_data': processed_data
    }

    # Invoke the LoadModelAndPredict Lambda function
    response = lambda_client.invoke(
        FunctionName='LoadModelAndPredict',  # Name of the LoadModelAndPredict Lambda function
        InvocationType='RequestResponse',  # Synchronous invocation
        Payload=json.dumps(payload)  # Send input as JSON
    )
    
    # Read the response from the Lambda function
    response_payload = json.loads(response['Payload'].read())
    
    # Get the prediction result
    prediction = response_payload['prediction']
    
    return prediction


def main():
    # Sample input features for heart disease prediction
    features = [63, 1, 3, 145, 233, 1, 2, 150, 0, 0, 1, 2, 3]  # Example heart disease features

    # Invoke the first Lambda (PreprocessData)
    processed_data = invoke_preprocess_data(features)
    print("Processed Data:", processed_data)

    # Invoke the second Lambda (LoadModelAndPredict) with the processed data
    prediction = invoke_load_model_and_predict(processed_data)
    print("Prediction:", prediction)

if __name__ == "__main__":
    main()
