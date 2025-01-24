def test_dummy():
    assert True
# Test generated using Keploy
import pytest
from unittest.mock import patch
from src.data.data_transformation import DataTransformation
from src.exception.exception import customexception
@patch("src.data.data_transformation.pd.read_csv")
def test_initialize_data_transformation_missing_train_file(mock_read_csv):
    # Mock read_csv to raise FileNotFoundError
    mock_read_csv.side_effect = [FileNotFoundError("Train file not found")]
    # Instantiate the class
    data_transformation = DataTransformation()
    # Call the method and assert exception
    with pytest.raises(customexception) as excinfo:
        data_transformation.initialize_data_transformation("missing_train.csv", "test.csv")
    assert "Train file not found" in str(excinfo.value)
# Test generated using Keploy
import pytest
import pandas as pd
from unittest.mock import patch
from src.data.data_transformation import DataTransformation
from src.exception.exception import customexception
@patch("src.data.data_transformation.pd.read_csv")
def test_initialize_data_transformation_missing_target_column(mock_read_csv):
    # Mock train and test data without the target column
    train_data = pd.DataFrame({
        "Feature1": [1.0, 2.0, 3.0],
        "Feature2": ["A", "B", "C"]
    })
    test_data = pd.DataFrame({
        "Feature1": [4.0, 5.0],
        "Feature2": ["D", "E"],
        "Price": [400, 500]
    })
    mock_read_csv.side_effect = [train_data, test_data]
    # Instantiate the class
    data_transformation = DataTransformation()
    # Call the method and assert exception
    with pytest.raises(customexception) as excinfo:
        data_transformation.initialize_data_transformation("train.csv", "test.csv")
    assert "Price" in str(excinfo.value), "Exception should indicate missing target column"