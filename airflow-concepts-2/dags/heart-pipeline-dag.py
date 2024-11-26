from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),  # Optional retry delay
}

# Define the DAG
dag = DAG(
    'heart_pipeline',
    default_args=default_args,  # Default arguments
    description='Pipeline for training and deploying the best heart disease model',
    schedule_interval=None,  # Run manually (no schedule)
    start_date=datetime.now() - timedelta(minutes=1),  # Start immediately
    catchup=True,  # Do not backfill
)


# File paths
DATA_PATH = 'data/heart.csv'
MODEL_PATH = 'models/best_model.pkl'

# Task 1: Load and preprocess data
def load_and_preprocess_data():
    df = pd.read_csv(DATA_PATH)
    df = df.dropna()  # Drop missing values
    X = df.drop(columns=['target'])  # Features
    y = df['target']  # Target variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Save split data to temporary CSV files
    X_train.to_csv('/tmp/X_train.csv', index=False)
    X_test.to_csv('/tmp/X_test.csv', index=False)
    y_train.to_csv('/tmp/y_train.csv', index=False)
    y_test.to_csv('/tmp/y_test.csv', index=False)

# Task 2: Train Logistic Regression model
def train_logistic_regression():
    X_train = pd.read_csv('/tmp/X_train.csv')
    y_train = pd.read_csv('/tmp/y_train.csv').squeeze()
    model = LogisticRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, '/tmp/logistic_model.pkl')

# Task 3: Train Random Forest model
def train_random_forest():
    X_train = pd.read_csv('/tmp/X_train.csv')
    y_train = pd.read_csv('/tmp/y_train.csv').squeeze()
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    joblib.dump(model, '/tmp/random_forest_model.pkl')

# Task 4: Evaluate models
def evaluate_models():
    X_test = pd.read_csv('/tmp/X_test.csv')
    y_test = pd.read_csv('/tmp/y_test.csv').squeeze()
    logistic_model = joblib.load('/tmp/logistic_model.pkl')
    rf_model = joblib.load('/tmp/random_forest_model.pkl')

    # Evaluate Logistic Regression
    logistic_preds = logistic_model.predict(X_test)
    logistic_acc = accuracy_score(y_test, logistic_preds)

    # Evaluate Random Forest
    rf_preds = rf_model.predict(X_test)
    rf_acc = accuracy_score(y_test, rf_preds)

    # Select the best model
    if logistic_acc > rf_acc:
        best_model = logistic_model
    else:
        best_model = rf_model

    # Save the best model
    joblib.dump(best_model, MODEL_PATH)

# Task 5: Simulate Deployment
def deploy_model():
    print(f"Best model saved to {MODEL_PATH} and ready for deployment.")

# Define tasks
load_data_task = PythonOperator(
    task_id='load_and_preprocess_data',
    python_callable=load_and_preprocess_data,
    dag=dag,
)

train_lr_task = PythonOperator(
    task_id='train_logistic_regression',
    python_callable=train_logistic_regression,
    dag=dag,
)

train_rf_task = PythonOperator(
    task_id='train_random_forest',
    python_callable=train_random_forest,
    dag=dag,
)

evaluate_task = PythonOperator(
    task_id='evaluate_models',
    python_callable=evaluate_models,
    dag=dag,
)

deploy_task = PythonOperator(
    task_id='deploy_model',
    python_callable=deploy_model,
    dag=dag,
)

# Set task dependencies
load_data_task >> [train_lr_task, train_rf_task] >> evaluate_task >> deploy_task
