import os
import pickle

import pandas as pd
import yaml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

from src.constants import *


class Utility:
    def __init__(self) -> None:
        pass

    def create_folder(folder_name):
        try:
            # Creating a directory if it does not exist already
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)

        except Exception as e:
            raise e

    def read_csv_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise e

    def data_split_test(self, data):
        """split the data to independent and dependent
        -return variable
        """
        try:
            x = data.drop(columns=[TARGET_COLUMN], axis=1)
            y = data[TARGET_COLUMN]

            return x, y

        except Exception as e:
            raise e

    def apply_encoder(data, category):
        try:
            le = LabelEncoder()
            for i in category:
                data[i] = le.fit_transform(data[i])

            return data
        except Exception as e:
            raise e
