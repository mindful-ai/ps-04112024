import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# Initialize S3 client
s3_client = boto3.client('s3')

def create_s3_bucket(bucket_name):
    """
    Create an S3 bucket in a specific region.
    
    :param bucket_name: The name of the S3 bucket to be created.
    """
    try:
        s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}  # Change region if necessary
        )
        print(f"Bucket '{bucket_name}' created successfully.")
    except ClientError as e:
        print(f"Error creating bucket: {e}")

def upload_to_s3(bucket_name, file_path, object_name=None):
    """
    Upload a file to an S3 bucket.
    
    :param bucket_name: The name of the S3 bucket.
    :param file_path: The path to the file on your local system.
    :param object_name: The name of the object in the S3 bucket (optional).
    """
    if object_name is None:
        object_name = file_path.split("/")[-1]  # If no object name is given, use the file name

    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File '{file_path}' uploaded successfully to {bucket_name}/{object_name}")
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except NoCredentialsError:
        print("Credentials not available.")
    except ClientError as e:
        print(f"Error uploading file: {e}")

def delete_file_from_s3(bucket_name, object_name):
    """
    Delete a file from an S3 bucket.
    
    :param bucket_name: The name of the S3 bucket.
    :param object_name: The name of the object to delete in the S3 bucket.
    """
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=object_name)
        print(f"File '{object_name}' deleted successfully from {bucket_name}.")
    except ClientError as e:
        print(f"Error deleting file: {e}")

def delete_s3_bucket(bucket_name):
    """
    Delete an S3 bucket.
    
    :param bucket_name: The name of the S3 bucket to delete.
    """
    try:
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully.")
    except ClientError as e:
        print(f"Error deleting bucket: {e}")

if __name__ == "__main__":
    # Replace these with your actual values
    bucket_name = 'purush-aws-s3-test-22081982'  # Must be globally unique
    file_path = 'manual.txt'  # Local file path to upload
    object_name = 'boto3-s3-test.txt'  # Object name in the bucket

    # Create an S3 bucket
    #create_s3_bucket(bucket_name)

    # Upload a file to the S3 bucket
    #upload_to_s3(bucket_name, file_path, object_name)

    # Delete the file from the S3 bucket
    delete_file_from_s3(bucket_name, object_name)

    # Delete the S3 bucket
    delete_s3_bucket(bucket_name)
