import mlflow
from sklearn.datasets import load_diabetes
logged_model = 'runs:/e2351cc9b3cc45f1bfccd4111e5e46a0/model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)
data = load_diabetes()
print(data.data[0])

# Predict on a Pandas DataFrame.
import pandas as pd
print(loaded_model.predict([data.data[0]]))