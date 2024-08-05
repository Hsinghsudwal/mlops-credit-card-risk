import joblib
import pandas as pd
import os
import sys
import mlflow
from mlflow import MlflowClient



MLFLOW_TRACKING_URI="http://127.0.0.1:5000"
EXPERIMENT_NAME="xgboost-mlflow"
MODEL_NAME = "best_result"

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
mlflow.set_experiment(EXPERIMENT_NAME)

client = MlflowClient()

# Get the latest versions of the registered model
latest_versions = client.get_latest_versions(MODEL_NAME, stages=["Production"])

# Print run_ids of all the latest versions
for version in latest_versions:
    RUN_ID = version.run_id

print(RUN_ID)

logged_model = f'runs:/{RUN_ID}/model'

# Load model as a PyFuncModel.
model = mlflow.pyfunc.load_model(logged_model)

joblib.dump(model,"xgboost.joblib")