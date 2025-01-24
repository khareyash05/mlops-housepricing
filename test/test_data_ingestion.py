import pytest
from src.data.data_ingestion import DataIngestion
from unittest.mock import patch
import pytest
def test_dummy():
    assert True
# Test generated using Keploy
def test_fetch_and_save_data_invalid_url():
    """
    Test that fetch_and_save_data raises an exception when an invalid URL is provided.
    """
    with patch('pandas.read_csv', side_effect=Exception("Invalid URL")) as mocked_read_csv:
        ingestion = DataIngestion()
        ingestion.data_config.url = 'http://invalid-url.com'
        with pytest.raises(Exception) as exc_info:
            ingestion.fetch_and_save_data()
        assert "Invalid URL" in str(exc_info.value)
        mocked_read_csv.assert_called_once_with(ingestion.data_config.url)