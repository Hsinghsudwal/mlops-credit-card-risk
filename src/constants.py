# BASE:
PROJECT_NAME = "Credit Card"
AUTHOR = "Harinder Singh Sudwal"

# ARCHITECTURE
TARGET_COLUMN = "class"
TEST_SIZE = 0.2


# DATA_LOCATION_PATH
NOTEBOOK_DATA = (
    "https://raw.githubusercontent.com/Hsinghsudwal/Dataset-Files/main/creditcard.csv"
)
DATA_ARTIFACTS = "artifact"
RAW_FILE_NAME = "raw.csv"
PREPROCESS_NAME = "process_clean.csv"
TRAIN_NAME = "train.csv"
TEST_NAME = "test.csv"
MODEL_NAME = "xgboost.joblib"
