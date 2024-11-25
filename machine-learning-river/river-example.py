from river import datasets
from river import naive_bayes
from river import metrics
from river import preprocessing

# Load the Phishing dataset
dataset = datasets.Phishing()

# Initialize a model pipeline
model = preprocessing.StandardScaler() | naive_bayes.GaussianNB()

# Initialize an online accuracy metric
metric = metrics.Accuracy()

# Simulate stream-based learning
for i, (X, y) in enumerate(dataset):
    # Update the model with the incoming data point
    model.learn_one(X, y)
    
    # Evaluate the model on the same data point
    metric.update(y, model.predict_one(X))
    
    # Print accuracy every 100 iterations
    if i % 100 == 0:
        print(f"Iteration {i}, Accuracy: {metric}")

# Final accuracy after processing all data
print(f"Final Accuracy: {metric}")
