from river import naive_bayes
from river import preprocessing
from river import metrics

# Define your data as a stream
stream = [
    ({"feature1": 1.0, "feature2": 0.5}, "A"),
    ({"feature1": 0.7, "feature2": 1.2}, "B"),
    ({"feature1": 1.1, "feature2": 0.8}, "A"),
    # Add more data points as needed
]

# Initialize a model pipeline
model = preprocessing.StandardScaler() | naive_bayes.GaussianNB()

# Initialize an online accuracy metric
metric = metrics.Accuracy()

# Simulate stream-based learning
for i, (X, y) in enumerate(stream):
    model.learn_one(X, y)
    metric.update(y, model.predict_one(X))
    print(f"Iteration {i+1}, Accuracy: {metric}")

# Final accuracy after processing all data
print(f"Final Accuracy: {metric}")
