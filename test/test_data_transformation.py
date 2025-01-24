import pytest
from src.data.data_transformation import DataTransformation
from src.exception.exception import customexception
from unittest.mock import patch
import pytest
def test_dummy():
    assert True
# Test generated using Keploy
def test_initialize_data_transformation_invalid_file_path():
    """
    Test that initialize_data_transformation raises customexception when given invalid file paths.
    """
    with patch('pandas.read_csv', side_effect=FileNotFoundError("File not found")):
        transformer = DataTransformation()
        with pytest.raises(customexception) as exc_info:
            transformer.initialize_data_transformation('invalid_train.csv', 'invalid_test.csv')
        assert "File not found" in str(exc_info.value)