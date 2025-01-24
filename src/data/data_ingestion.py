import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    url: str = 'https://raw.githubusercontent.com/connectaditya/House-price-prediction/refs/heads/master/USA_Housing.csv'

class DataIngestion:
    def __init__(self, config: DataIngestionConfig = None):
        self.data_config = config or DataIngestionConfig()