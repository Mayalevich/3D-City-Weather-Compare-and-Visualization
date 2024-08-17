import pytest
from unittest.mock import patch
from project import fetch_weather_data, extract_weather_data

# Mocked response for the API
mock_response = {
    "main": {"temp": 295.15, "humidity": 50},
    "wind": {"speed": 5.0}
}

# Test fetch_weather_data
@patch('project.requests.get')
def test_fetch_weather_data(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    result = fetch_weather_data("fake_api_key", "New York")
    assert result == mock_response

# Test extract_weather_data
def test_extract_weather_data():
    data = extract_weather_data(mock_response)
    assert data == (22.0, 50, 5.0)  # Temperature should be in Celsius

# Test handling of KeyError in extract_weather_data
def test_extract_weather_data_key_error():
    incomplete_response = {"main": {"humidity": 50}}
    data = extract_weather_data(incomplete_response)
    assert data is None
