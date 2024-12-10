import boto3
import subprocess
import time

# AWS region
region = 'us-east-1'

# Initialize Boto3 ECS and ECR clients
ecr_client = boto3.client('ecr', region_name=region)
ecs_client = boto3.client('ecs', region_name=region)

# Variables for ECS and ECR
repository_name = 'my-repository'
image_name = 'my-docker-image'
ecs_cluster_name = 'my-ecs-cluster'
task_definition_name = 'my-task-definition'
service_name = 'my-service'
container_name = 'my-container'
image_tag = 'latest'

# Step 1: Create ECR Repository
def create_ecr_repository():
    try:
        response = ecr_client.create_repository(repositoryName=repository_name)
        print(f"Created repository: {response['repository']['repositoryUri']}")
    except ecr_client.exceptions.RepositoryAlreadyExistsException:
        print(f"Repository {repository_name} already exists.")

# Step 2: Build and Push Docker Image to ECR
def build_and_push_docker_image():
    # Step 2a: Get ECR login command
    login_command = subprocess.check_output(
        ['aws', 'ecr', 'get-login-password', '--region', region],
        universal_newlines=True
    )
    
    # Step 2b: Log in to ECR
    subprocess.run(['docker', 'login', '--username', 'AWS', '--password-stdin', f'{ecr_client.meta.endpoint_url}'], input=login_command.strip(), text=True)

    # Step 2c: Build the Docker image
    subprocess.run(['docker', 'build', '-t', image_name, '.'])

    # Step 2d: Tag the Docker image
    docker_image_uri = f'{ecr_client.meta.endpoint_url}/{repository_name}:{image_tag}'
    subprocess.run(['docker', 'tag', image_name, docker_image_uri])

    # Step 2e: Push the image to ECR
    subprocess.run(['docker', 'push', docker_image_uri])

# Step 3: Register ECS Task Definition
def register_task_definition():
    container_definition = {
        'name': container_name,
        'image': f'{ecr_client.meta.endpoint_url}/{repository_name}:{image_tag}',
        'memory': 512,
        'cpu': 256,
        'essential': True,
    }

    try:
        response = ecs_client.register_task_definition(
            family=task_definition_name,
            networkMode='awsvpc',
            containerDefinitions=[container_definition],
        )
        print(f"Registered task definition: {response['taskDefinition']['taskDefinitionArn']}")
    except Exception as e:
        print(f"Error registering task definition: {e}")

# Step 4: Create ECS Cluster
def create_ecs_cluster():
    try:
        response = ecs_client.create_cluster(
            clusterName=ecs_cluster_name
        )
        print(f"Created ECS cluster: {response['cluster']['clusterName']}")
    except ecs_client.exceptions.ClusterAlreadyExistsException:
        print(f"Cluster {ecs_cluster_name} already exists.")

# Step 5: Create ECS Service to Run Docker Container
def create_ecs_service():
    try:
        response = ecs_client.create_service(
            cluster=ecs_cluster_name,
            serviceName=service_name,
            taskDefinition=task_definition_name,
            desiredCount=1,
            launchType='FARGATE',  # You can change this to EC2 if you're using EC2 instances
            networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': ['subnet-12345678'],  # Update with your subnet ID
                    'assignPublicIp': 'ENABLED'
                }
            }
        )
        print(f"Created ECS service: {response['service']['serviceName']}")
    except Exception as e:
        print(f"Error creating ECS service: {e}")

# Main execution
if __name__ == '__main__':
    create_ecr_repository()  # Step 1
    build_and_push_docker_image()  # Step 2
    register_task_definition()  # Step 3
    create_ecs_cluster()  # Step 4
    create_ecs_service()  # Step 5
