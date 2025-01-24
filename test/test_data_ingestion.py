import pytest
def test_dummy():
    assert True
# Test generated using Keploy
from unittest.mock import MagicMock, patch
import os
import pandas as pd
from src.data.data_ingestion import DataIngestion
@patch("src.data.data_ingestion.pd.read_csv")
@patch("src.data.data_ingestion.os.makedirs")
@patch("src.data.data_ingestion.pd.DataFrame.to_csv")
def test_fetch_and_save_data_happy_path(mock_to_csv, mock_makedirs, mock_read_csv):
    # Mocking the data returned by pd.read_csv
    mock_data = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    mock_read_csv.return_value = mock_data
    # Instantiate the DataIngestion class
    ingestion = DataIngestion()
    # Call the method
    ingestion.fetch_and_save_data()
    # Assertions
    mock_read_csv.assert_called_once_with(ingestion.data_config.url)
    mock_makedirs.assert_called_once_with("artifacts", exist_ok=True)
    assert mock_to_csv.call_count == 3  # raw, train, and test data