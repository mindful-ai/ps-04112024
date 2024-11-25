import numpy as np
from creme import datasets
from creme import stream
from creme import metrics
from creme import classifiers

# Step 1: Load the Iris dataset from `creme`'s built-in datasets module
dataset = datasets.Iris()

# Step 2: Create a stream (wrap the dataset to simulate streaming data)
data_stream = stream.iter_pandas(dataset)

# Step 3: Initialize the model (we'll use Logistic Regression as an example)
model = classifiers.LogisticRegression()

# Step 4: Set up an evaluation metric (e.g., accuracy)
metric = metrics.Accuracy()

# Step 5: Iterate over the data stream
for i, (X, y) in enumerate(data_stream):
    # Update the model incrementally with the new data point
    model.fit_one(X, y)
    
    # Make a prediction
    y_pred = model.predict_one(X)
    
    # Update the accuracy metric
    metric.update(y, y_pred)
    
    # Output the current accuracy after every 10th sample
    if i % 10 == 0:
        print(f"Step {i}, Accuracy: {metric}")

# Final accuracy after processing the entire stream
print(f"Final Accuracy: {metric}")
