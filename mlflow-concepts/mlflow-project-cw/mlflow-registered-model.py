import mlflow.pyfunc
from sklearn.datasets import load_diabetes

# Load the model from the registry
model_name = "diabetes-model"
model_stage = "None" # None | Staging | Production | Archived
model_version = 1
alias = "champion"
model = mlflow.pyfunc.load_model(f"models:/{model_name}/{model_version}")
#champion_version = mlflow.pyfunc.load_model(f"models:/{model_name}@{alias}")

# Make predictions
import pandas as pd
data = load_diabetes()
print(data.data[0])
predictions = model.predict(data.data[0])
print(predictions)

