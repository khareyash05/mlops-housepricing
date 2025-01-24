import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception
from src.utils.utils import save_object
import os
import sys
from dataclasses import dataclass
from pathlib import Path

from sklearn.preprocessing import StandardScaler , OneHotEncoder
from sklearn.compose import ColumnTransformer

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
