import pandas as pd
import numpy as np
import argparse
import os
import joblib
from sklearn.ensemble import RandomForestRegressor

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max_depth", type=int, default=None)
    args = parser.parse_args()

    # Load training data
    train_data_path = os.path.join("/opt/ml/input/data/train/train.csv")
    data = pd.read_csv(train_data_path)

    # Split features and target
    X_train = data.drop("MedHouseVal", axis=1)
    y_train = data["MedHouseVal"]

    # Train model
    model = RandomForestRegressor(max_depth=args.max_depth, random_state=42)
    model.fit(X_train, y_train)

    # Save model
    model_dir = os.path.join("/opt/ml/model")
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(model, os.path.join(model_dir, "model.joblib"))
