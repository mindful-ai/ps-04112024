import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
data = pd.read_csv('heart_disease.csv')

# Preprocess the data (e.g., handle missing values, feature selection, etc.)
X = data.drop('target', axis=1)
y = data['target']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Save the model to a file
joblib.dump(model, 'heart_disease_model.pkl')


'''
aws s3 cp heart_disease_model.pkl s3://your-bucket-name/heart_disease_model.pkl
aws s3 ls s3://your-bucket-name/


'''