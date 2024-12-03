import kfp
from kfp import dsl
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import pickle

# Component 1: Load the dataset
def load_data():
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target, name='target')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    data = {
        'X_train': X_train,
        'X_test': X_test,
        'y_train': y_train,
        'y_test': y_test
    }
    with open('/data.pkl', 'wb') as f:
        pickle.dump(data, f)
    print("Data saved to /data.pkl")

# Component 2: Train the model
def train_model():
    with open('/data.pkl', 'rb') as f:
        data = pickle.load(f)
    X_train = data['X_train']
    y_train = data['y_train']
    
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    with open('/model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Model saved to /model.pkl")

# Component 3: Evaluate the model
def evaluate_model():
    with open('/data.pkl', 'rb') as f:
        data = pickle.load(f)
    X_test = data['X_test']
    y_test = data['y_test']
    
    with open('/model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    print(f"Accuracy: {accuracy}")
    print(f"Classification Report:\n{report}")

# Define the pipeline
@dsl.pipeline(
    name="Iris ML Pipeline",
    description="A simple ML pipeline for the Iris dataset"
)
def iris_pipeline():
    load_data_op = dsl.ContainerOp(
        name="Load Data",
        image="python:3.9",
        command=["python", "-c"],
        arguments=[
            f"""
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd

{load_data.__code__}
load_data()
            """
        ],
        file_outputs={"data": "/data.pkl"}
    )

    train_model_op = dsl.ContainerOp(
        name="Train Model",
        image="python:3.9",
        command=["python", "-c"],
        arguments=[
            f"""
import pickle
from sklearn.ensemble import RandomForestClassifier

{train_model.__code__}
train_model()
            """
        ],
        file_outputs={"model": "/model.pkl"}
    ).after(load_data_op)

    evaluate_model_op = dsl.ContainerOp(
        name="Evaluate Model",
        image="python:3.9",
        command=["python", "-c"],
        arguments=[
            f"""
import pickle
from sklearn.metrics import classification_report, accuracy_score

{evaluate_model.__code__}
evaluate_model()
            """
        ]
    ).after(train_model_op)

# Compile the pipeline
if __name__ == "__main__":
    kfp.compiler.Compiler().compile(iris_pipeline, "iris_pipeline.yaml")
